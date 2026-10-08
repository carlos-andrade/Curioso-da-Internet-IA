#!/usr/bin/env python3
"""Validador determinístico da FASE 2 — Curioso da Internet IA.

Valida registros Markdown segundo ESTRUTURA/LAYOUT-VALIDACAO-FASE-2.md.
Não usa dependências externas.
"""
from __future__ import annotations
import json
import re
import sys
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCOPES = {
    "FONTE": ("FONTES", {"referencia"}),
    "EVIDÊNCIA": ("EVIDENCIAS", {"fonte_id", "afirmacao"}),
    "PESQUISA": ("PESQUISAS", {"evidencia_ids", "conflitos"}),
    "CONHECIMENTO": ("CONHECIMENTO", {"pesquisa_ids", "evidencia_ids"}),
    "ENTIDADE": ("ENTIDADES", {"nome"}),
    "CONEXÃO": ("CONEXOES", {"origem_id", "destino_id", "relacao"}),
    "HOOK": ("GANCHOS", {"categoria", "texto"}),
    "IDEIA": ("BANCO_DE_IDEIAS", {"premissa", "origens"}),
}
STATES = {
    "DESCOBERTA", "EM INVESTIGAÇÃO", "PARCIALMENTE VALIDADA", "VALIDADA",
    "CONHECIMENTO CONSOLIDADO", "PUBLICÁVEL", "PUBLICADO", "MONITORADO", "ATUALIZADO",
    "CONTESTADA", "NÃO CONFIRMADA", "SUPERADA", "CORRIGIDA", "ARQUIVADA",
}
PUBLICATION_STATES = {"PUBLICÁVEL", "PUBLICADO"}
EXCEPTION_STATES = {"CONTESTADA", "NÃO CONFIRMADA", "SUPERADA", "CORRIGIDA", "ARQUIVADA"}
ID_RE = re.compile(r"^(FONTE|EVID|PESQ|ENT|CONH|CONX|HOOK|IDEIA)-\d{8}-\d{4}$")

REFERENCE_FIELDS = (
    "fonte_id", "fonte_ids", "evidencia_ids", "pesquisa_ids",
    "entidade_ids", "conhecimento_ids", "origem_id", "destino_id", "origens",
)

def frontmatter(text: str):
    if not text.startswith("---\n"):
        return None, "frontmatter ausente"
    end = text.find("\n---\n", 4)
    if end < 0:
        return None, "frontmatter sem fechamento"
    data = {}
    for line in text[4:end].splitlines():
        if not line.strip() or ":" not in line:
            continue
        k, v = line.split(":", 1)
        data[k.strip()] = v.strip().strip('"')
    return data, None

def split_refs(value: str):
    return [x.strip() for x in re.split(r"[,;]", value or "") if x.strip()]

def valid_iso_date(value: str):
    try:
        datetime.fromisoformat(value.replace("Z", "+00:00"))
        return True
    except ValueError:
        return False

def validate(path: Path, known_ids=None):
    text = path.read_text(encoding="utf-8")
    data, err = frontmatter(text)
    errors, warnings = [], []
    if err:
        return [f"{path}: {err}"], []

    required = {"id", "tipo", "estado", "data_captura", "afirmacoes", "limitacoes"}
    missing = required - set(data)
    errors += [f"{path}: campo obrigatório ausente: {x}" for x in sorted(missing)]

    rid = data.get("id", "")
    if rid and not ID_RE.fullmatch(rid):
        errors.append(f"{path}: ID inválido: {rid}")

    state = data.get("estado")
    if state and state not in STATES:
        errors.append(f"{path}: estado inválido: {state}")

    tipo = data.get("tipo", "")
    if tipo not in SCOPES:
        errors.append(f"{path}: tipo não suportado: {tipo}")
    else:
        _, fields = SCOPES[tipo]
        for field in fields:
            if not data.get(field):
                errors.append(f"{path}: campo obrigatório para {tipo}: {field}")

    if data.get("data_captura") and not valid_iso_date(data["data_captura"]):
        errors.append(f"{path}: data_captura inválida: {data['data_captura']}")

    if state in PUBLICATION_STATES:
        for field in ("fonte_ids", "evidencia_ids"):
            if not data.get(field):
                errors.append(f"{path}: {state} exige {field}")
        if data.get("proveniencia_completa", "").lower() not in {"true", "sim"}:
            errors.append(f"{path}: {state} exige proveniencia_completa=true")

    if state == "VALIDADA" and not data.get("evidencia_ids"):
        errors.append(f"{path}: VALIDADA exige evidencia_ids")

    if state == "CONHECIMENTO CONSOLIDADO":
        if not data.get("evidencia_ids"):
            errors.append(f"{path}: CONHECIMENTO CONSOLIDADO exige evidencia_ids")
        if not data.get("pesquisa_ids"):
            errors.append(f"{path}: CONHECIMENTO CONSOLIDADO exige pesquisa_ids")

    if state in EXCEPTION_STATES:
        warnings.append(f"{path}: estado de exceção; promoção editorial bloqueada por regra")

    if known_ids is not None:
        for field in REFERENCE_FIELDS:
            for ref in split_refs(data.get(field, "")):
                if not ID_RE.fullmatch(ref):
                    errors.append(f"{path}: referência inválida em {field}: {ref}")
                elif ref not in known_ids:
                    errors.append(f"{path}: referência inexistente em {field}: {ref}")

    return errors, warnings

def discover_records():
    records = []
    for folder, _ in SCOPES.values():
        base = ROOT / folder
        if not base.exists():
            continue
        for path in sorted(base.rglob("*.md")):
            if path.name.upper() != "README.MD":
                records.append(path)
    return records

def main():
    errors, warnings = [], []
    records = discover_records()
    known_ids = set()

    for path in records:
        data, err = frontmatter(path.read_text(encoding="utf-8"))
        if err:
            errors.append(f"{path}: {err}")
            continue
        rid = (data or {}).get("id")
        if rid:
            if rid in known_ids:
                errors.append(f"{path}: ID duplicado: {rid}")
            known_ids.add(rid)

    for path in records:
        e, w = validate(path, known_ids)
        errors.extend(e)
        warnings.extend(w)

    result = "BLOCKED" if errors else ("CONDITIONAL" if warnings else "PASS")
    report = {
        "fase": "FASE-2",
        "resultado": result,
        "registros_verificados": len(records),
        "erros": sorted(errors),
        "avisos": sorted(warnings),
        "gerado_em": datetime.now().astimezone().isoformat(timespec="seconds"),
    }
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 1 if errors else 0

if __name__ == "__main__":
    raise SystemExit(main())

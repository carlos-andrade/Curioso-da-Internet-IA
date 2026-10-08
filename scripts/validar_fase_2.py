#!/usr/bin/env python3
"""Validador determinístico da FASE 2 — Curioso da Internet IA.

Sem dependências externas. Valida arquivos Markdown com frontmatter YAML simples
e campos serializados como listas por linhas iniciadas com '- '.
"""
from __future__ import annotations
import json, re, sys
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
        v = v.strip().strip('"')
        data[k.strip()] = v
    return data, None

def validate(path: Path):
    text = path.read_text(encoding="utf-8")
    data, err = frontmatter(text)
    errors, warnings = [], []
    if err:
        return [f"{path}: {err}"], []
    required = {"id", "tipo", "estado", "data_captura", "afirmacoes", "limitacoes"}
    missing = required - set(data)
    errors += [f"{path}: campo obrigatório ausente: {x}" for x in sorted(missing)]
    rid = data.get("id", "")
    if rid and not re.fullmatch(r"(FONTE|EVID|PESQ|ENT|CONH|CONX|HOOK|IDEIA)-\d{8}-\d{4}", rid):
        errors.append(f"{path}: ID inválido: {rid}")
    state = data.get("estado")
    if state and state not in STATES:
        errors.append(f"{path}: estado inválido: {state}")
    tipo = data.get("tipo", "")
    if tipo not in SCOPES:
        errors.append(f"{path}: tipo não suportado: {tipo}")
    else:
        _, fields = SCOPES[tipo]
        for f in fields:
            if not data.get(f):
                errors.append(f"{path}: campo obrigatório para {tipo}: {f}")
    if state in PUBLICATION_STATES:
        for f in ("fonte_ids", "evidencia_ids"):
            if not data.get(f):
                errors.append(f"{path}: {state} exige {f}")
        if data.get("proveniencia_completa", "").lower() not in {"true", "sim"}:
            errors.append(f"{path}: {state} exige proveniencia_completa=true")
    if state in {"VALIDADA", "CONHECIMENTO CONSOLIDADO"}:
        if not data.get("evidencia_ids"):
            errors.append(f"{path}: {state} exige evidencia_ids")
    if state in EXCEPTION_STATES:
        warnings.append(f"{path}: estado de exceção; promoção editorial bloqueada por regra")
    return errors, warnings

def main():
    errors, warnings, records = [], [], []
    for tipo, (folder, _) in SCOPES.items():
        base = ROOT / folder
        if not base.exists():
            continue
        for path in sorted(base.rglob("*.md")):
            if path.name.upper() == "README.MD":
                continue
            records.append(str(path.relative_to(ROOT)))
            e, w = validate(path)
            errors.extend(e); warnings.extend(w)
    result = "BLOCKED" if errors else ("CONDITIONAL" if warnings else "PASS")
    report = {
        "fase": "FASE-2",
        "resultado": result,
        "registros_verificados": len(records),
        "erros": errors,
        "avisos": warnings,
    }
    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 1 if errors else 0

if __name__ == "__main__":
    raise SystemExit(main())

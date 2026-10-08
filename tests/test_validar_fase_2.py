import importlib.util
import json
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("v", ROOT / "scripts" / "validar_fase_2.py")
v = importlib.util.module_from_spec(spec)
spec.loader.exec_module(v)

def run_case(name, text, expect_errors):
    with tempfile.TemporaryDirectory() as d:
        p = Path(d) / f"{name}.md"
        p.write_text(text, encoding="utf-8")
        errors, _ = v.validate(p)
        assert bool(errors) is expect_errors, (name, errors)

VALID = """---
id: "EVID-20261008-0001"
tipo: "EVIDÊNCIA"
estado: "VALIDADA"
data_captura: "2026-10-08"
afirmacoes: "A afirmação é sustentada pela evidência."
limitacoes: "Escopo limitado à fonte capturada."
fonte_id: "FONTE-20261008-0001"
afirmacao: "A afirmação é sustentada pela evidência."
evidencia_ids: "EVID-20261008-0001"
---
# Registro
"""

INVALID = """---
id: "EVID-20261008-0002"
tipo: "EVIDÊNCIA"
estado: "VALIDADA"
data_captura: "2026-10-08"
afirmacoes: "Sem evidência vinculada."
limitacoes: "Desconhecidas."
---
# Registro
"""

def test_valid():
    run_case("valid", VALID, False)

def test_invalid():
    run_case("invalid", INVALID, True)

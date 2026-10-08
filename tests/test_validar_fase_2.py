import importlib.util
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("v", ROOT / "scripts" / "validar_fase_2.py")
v = importlib.util.module_from_spec(spec)
spec.loader.exec_module(v)

class TestValidadorFase2(unittest.TestCase):
    def run_case(self, text, expect_errors, state="VALIDADA"):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / "registro.md"
            p.write_text(text, encoding="utf-8")
            errors, _ = v.validate(p, {"EVID-20261008-0001", "FONTE-20261008-0001"})
            self.assertEqual(bool(errors), expect_errors, errors)

    def test_valid_evidencia(self):
        self.run_case("""---
id: "EVID-20261008-0001"
tipo: "EVIDÊNCIA"
estado: "VALIDADA"
data_captura: "2026-10-08T12:00:00+00:00"
afirmacoes: "A afirmação é sustentada pela evidência."
limitacoes: "Escopo limitado à fonte capturada."
fonte_id: "FONTE-20261008-0001"
afirmacao: "A afirmação é sustentada pela evidência."
evidencia_ids: "EVID-20261008-0001"
---
# Registro
""", False)

    def test_missing_evidence(self):
        self.run_case("""---
id: "EVID-20261008-0002"
tipo: "EVIDÊNCIA"
estado: "VALIDADA"
data_captura: "2026-10-08T12:00:00+00:00"
afirmacoes: "Sem evidência vinculada."
limitacoes: "Desconhecidas."
fonte_id: "FONTE-20261008-0001"
afirmacao: "Sem evidência vinculada."
---
# Registro
""", True)

    def test_invalid_id(self):
        self.run_case("""---
id: "EVID-INVALIDO"
tipo: "EVIDÊNCIA"
estado: "VALIDADA"
data_captura: "2026-10-08T12:00:00+00:00"
afirmacoes: "Teste."
limitacoes: "Teste."
fonte_id: "FONTE-20261008-0001"
afirmacao: "Teste."
evidencia_ids: "EVID-20261008-0001"
---
""", True)

    def test_publication_requires_provenance(self):
        self.run_case("""---
id: "EVID-20261008-0003"
tipo: "EVIDÊNCIA"
estado: "PUBLICADO"
data_captura: "2026-10-08T12:00:00+00:00"
afirmacoes: "Teste."
limitacoes: "Teste."
fonte_id: "FONTE-20261008-0001"
afirmacao: "Teste."
---
""", True)

    def test_exception_is_warning_not_error(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / "registro.md"
            p.write_text("""---
id: "EVID-20261008-0004"
tipo: "EVIDÊNCIA"
estado: "CONTESTADA"
data_captura: "2026-10-08T12:00:00+00:00"
afirmacoes: "Há versões conflitantes."
limitacoes: "Conflito ainda não resolvido."
fonte_id: "FONTE-20261008-0001"
afirmacao: "Há versões conflitantes."
evidencia_ids: "EVID-20261008-0004"
---
""", encoding="utf-8")
            errors, warnings = v.validate(p, {"EVID-20261008-0004", "FONTE-20261008-0001"})
            self.assertFalse(errors)
            self.assertEqual(len(warnings), 1)

if __name__ == "__main__":
    unittest.main()

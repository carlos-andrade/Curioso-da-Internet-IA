---
projeto: "Curioso da Internet IA"
repositorio: "carlos-andrade/Curioso-da-Internet-IA"
tipo_documento: "LAYOUT ÚNICO"
fase: "FASE-3"
id_documento: "DOC-20261008-0062"
titulo: "LAYOUT DA PRODUÇÃO EDITORIAL"
status: "ATIVO"
versao: "1.0"
data_criacao: "2026-10-08"
data_atualizacao: "2026-10-08"
origem: "CARTA FASE 3 — PRODUÇÃO EDITORIAL"
autoridade_documental: "GOVERNANÇA"
cadeia_autoridade: "PROMPT → CARTA → LAYOUT ÚNICO → CÓDIGO"
---

# LAYOUT DA PRODUÇÃO EDITORIAL

## Registro mínimo

Todo produto editorial deve possuir:

- id
- tipo
- estado
- conhecimento_ids
- fonte_ids
- evidencia_ids
- data_criacao
- data_revisao
- objetivo_editorial
- limitacoes

## Tipos

| Tipo | Campos específicos |
|---|---|
| HISTÓRIA | premissa, narrativa |
| STORYTELLING | gancho, contexto, conflito, virada, consequência, significado, fechamento |
| ROTEIRO | cenas, duração, locução, texto_na_tela |
| DECUPAGEM | tomadas, visual, áudio, transição |
| PACOTE MULTIPLATAFORMA | plataformas, formatos, derivados |

## Rastreamento

Cada saída deve apontar para os IDs de conhecimento, fonte e evidência que sustentam a produção.

## Regra de equivalência

O layout é a referência editorial. Qualquer schema ou código futuro deve implementar este contrato sem redefini-lo.

## Regra de promoção

Um conteúdo só pode ser marcado como PUBLICADO quando sua origem, revisão e proveniência estiverem completas.

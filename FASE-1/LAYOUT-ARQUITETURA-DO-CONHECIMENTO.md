---
projeto: "Curioso da Internet IA"
repositorio: "carlos-andrade/Curioso-da-Internet-IA"
tipo_documento: "LAYOUT ÚNICO"
fase: "FASE-1"
id_documento: "DOC-20261008-0042"
titulo: "LAYOUT DA ARQUITETURA DO CONHECIMENTO"
status: "CONCLUÍDO"
versao: "1.0"
data_criacao: "2026-10-08"
data_atualizacao: "2026-10-08"
origem: "CARTA FASE 1 — ARQUITETURA DO CONHECIMENTO"
autoridade_documental: "GOVERNANÇA"
cadeia_autoridade: "PROMPT → CARTA → LAYOUT ÚNICO → CÓDIGO"
---

# LAYOUT DA ARQUITETURA DO CONHECIMENTO

## Objetivo

Definir a representação conceitual única dos registros nucleares do sistema editorial.

## Registro mínimo

Todo registro deve possuir, conforme o tipo:

- `id`
- `tipo`
- `estado`
- `data_captura`
- `afirmacoes`
- `limitacoes`

## Tipos e campos específicos

| Tipo | Campos específicos |
|---|---|
| FONTE | `referencia` |
| EVIDÊNCIA | `fonte_id`, `afirmacao` |
| PESQUISA | `evidencia_ids`, `conflitos` |
| CONHECIMENTO | `pesquisa_ids`, `evidencia_ids` |
| ENTIDADE | `nome` |
| CONEXÃO | `origem_id`, `destino_id`, `relacao` |
| HOOK | `categoria`, `texto` |
| IDEIA | `premissa`, `origens` |

## Identidade

O ID deve seguir:

`TIPO-AAAAMMDD-NNNN`

As referências entre registros devem utilizar IDs existentes no conjunto validado.

## Estado e publicação

- `VALIDADA` exige evidência.
- `CONHECIMENTO CONSOLIDADO` exige pesquisa e evidência.
- `PUBLICÁVEL` e `PUBLICADO` exigem proveniência completa.
- Estados de exceção não podem ser promovidos silenciosamente.

## Equivalência

A representação Markdown e qualquer representação estruturada devem ser semanticamente equivalentes. O layout é a referência editorial; schemas e código implementam o contrato sem redefini-lo.

## Regra de autoridade

Alterações neste layout devem preceder alterações de código e testes.

---
projeto: "Curioso da Internet IA"
repositorio: "carlos-andrade/Curioso-da-Internet-IA"
tipo_documento: "LAYOUT ÚNICO"
fase: "FASE-2"
id_documento: "DOC-20261008-0035"
titulo: "LAYOUT DE VALIDAÇÃO FASE 2"
status: "ATIVO"
versao: "1.1"
data_criacao: "2026-10-08"
data_atualizacao: "2026-10-08"
origem: "CARTA FASE 2 — VALIDAÇÃO"
autoridade_documental: "GOVERNANÇA"
cadeia_autoridade: "PROMPT → CARTA → LAYOUT ÚNICO → CÓDIGO"
---

# LAYOUT DE VALIDAÇÃO FASE 2

## Objetivo

Definir o contrato único da representação Markdown operacional que o código da FASE 2 deve validar.

> Este layout é o contrato operacional dos registros Markdown. Os schemas JSON continuam sendo o contrato da representação estruturada. As duas representações devem permanecer semanticamente equivalentes.

## Envelope obrigatório

Todo registro Markdown deve possuir:

- `id`
- `tipo`
- `estado`
- `data_captura`
- `afirmacoes`
- `limitacoes`

O campo `id` segue `TIPO-AAAAMMDD-NNNN`.

## Campos por tipo

- FONTE: `referencia`
- EVIDÊNCIA: `fonte_id`, `afirmacao`
- PESQUISA: `evidencia_ids`, `conflitos`
- CONHECIMENTO: `pesquisa_ids`, `evidencia_ids`
- ENTIDADE: `nome`
- CONEXÃO: `origem_id`, `destino_id`, `relacao`
- HOOK: `categoria`, `texto`
- IDEIA: `premissa`, `origens`

Listas de referências na representação Markdown devem ser serializadas como valores separados por vírgula, sem espaços obrigatórios.

## Estados

Estados de fluxo:

DESCOBERTA, EM INVESTIGAÇÃO, PARCIALMENTE VALIDADA, VALIDADA, CONHECIMENTO CONSOLIDADO, PUBLICÁVEL, PUBLICADO, MONITORADO, ATUALIZADO.

Estados de exceção:

CONTESTADA, NÃO CONFIRMADA, SUPERADA, CORRIGIDA, ARQUIVADA.

## Regras de promoção

- PUBLICÁVEL e PUBLICADO exigem `fonte_ids`, `evidencia_ids` e `proveniencia_completa=true`.
- VALIDADA exige `evidencia_ids`.
- CONHECIMENTO CONSOLIDADO exige `evidencia_ids` e `pesquisa_ids`.
- Estados de exceção não podem ser promovidos silenciosamente.
- BOATO e HIPÓTESE não podem ser convertidos em FATO sem nova evidência.
- Toda referência deve apontar para um ID existente no conjunto validado.
- Datas de captura devem ser ISO 8601; a data de captura não substitui a data do fato.

## Saída do validador

O validador deve emitir:

- PASS;
- BLOCKED;
- CONDITIONAL;
- lista determinística de erros;
- lista determinística de avisos;
- quantidade de registros verificados;
- lote/data da validação.

## Regra de autoridade

Este layout deriva da CARTA FASE 2 e é a referência direta do código de validação. Alterações no contrato devem atualizar primeiro este documento, depois o código e os testes.

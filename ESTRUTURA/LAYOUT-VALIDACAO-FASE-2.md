---
projeto: "Curioso da Internet IA"
repositorio: "carlos-andrade/Curioso-da-Internet-IA"
tipo_documento: "LAYOUT ÚNICO"
fase: "FASE-2"
id_documento: "DOC-20261008-0035"
titulo: "LAYOUT DE VALIDAÇÃO FASE 2"
status: "ATIVO"
versao: "1.0"
data_criacao: "2026-10-08"
data_atualizacao: "2026-10-08"
origem: "CARTA FASE 2 — VALIDAÇÃO"
autoridade_documental: "GOVERNANÇA"
cadeia_autoridade: "PROMPT → CARTA → LAYOUT ÚNICO → CÓDIGO"
---

# LAYOUT DE VALIDAÇÃO FASE 2

## Objetivo
Definir o contrato mínimo que o código deve validar.

## Contrato de registro validável
Campos obrigatórios:
- `id`
- `tipo`
- `estado`
- `data_captura`
- `afirmacoes`
- `limitacoes`

Campos obrigatórios conforme o tipo:
- FONTE: `referencia`
- EVIDÊNCIA: `fonte_id`, `afirmacao`
- PESQUISA: `evidencia_ids`, `conflitos`
- CONHECIMENTO: `pesquisa_ids`, `evidencia_ids`
- ENTIDADE: `nome`
- CONEXÃO: `origem_id`, `destino_id`, `relacao`
- HOOK: `categoria`, `texto`
- IDEIA: `premissa`, `origens`

## Estados
Estados de fluxo:
DESCOBERTA, EM INVESTIGAÇÃO, PARCIALMENTE VALIDADA, VALIDADA, CONHECIMENTO CONSOLIDADO, PUBLICÁVEL, PUBLICADO, MONITORADO, ATUALIZADO.

Estados de exceção:
CONTESTADA, NÃO CONFIRMADA, SUPERADA, CORRIGIDA, ARQUIVADA.

## Regras de promoção
- PUBLICÁVEL e PUBLICADO exigem proveniência completa.
- VALIDADA exige evidência identificável.
- CONHECIMENTO CONSOLIDADO exige pesquisa identificável.
- Estados de exceção não podem ser promovidos silenciosamente para estados de publicação.
- Uma afirmação marcada como BOATO ou HIPÓTESE não pode ser tratada como FATO sem nova evidência.

## Saída do validador
O validador deve emitir:
- PASS;
- BLOCKED;
- CONDITIONAL;
- lista determinística de erros;
- lista de avisos;
- registro do lote/data da validação.

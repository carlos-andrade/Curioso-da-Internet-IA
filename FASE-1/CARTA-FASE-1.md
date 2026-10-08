---
projeto: "Curioso da Internet IA"
repositorio: "carlos-andrade/Curioso-da-Internet-IA"
tipo_documento: "CARTA"
fase: "FASE-1"
id_documento: "DOC-20261008-0041"
titulo: "CARTA FASE 1 — ARQUITETURA DO CONHECIMENTO"
status: "CONCLUÍDA"
versao: "1.0"
data_criacao: "2026-10-08"
data_atualizacao: "2026-10-08"
origem: "DECISÃO ARQUITETURAL"
autoridade_documental: "GOVERNANÇA"
cadeia_autoridade: "PROMPT → CARTA → LAYOUT ÚNICO → CÓDIGO"
---

# CARTA FASE 1 — ARQUITETURA DO CONHECIMENTO

## Regra central

O Curioso da Internet IA deve operar como uma base de conhecimento editorial rastreável, e não como uma coleção de roteiros independentes.

## Regras obrigatórias

1. Separar FONTE de EVIDÊNCIA.
2. Vincular afirmações às evidências que as sustentam.
3. Separar pesquisa de conhecimento consolidado.
4. Registrar ENTIDADES de forma reutilizável.
5. Registrar CONEXÕES entre entidades e registros.
6. Manter estados editoriais explícitos.
7. Registrar conflitos, limitações e incertezas.
8. Não promover hipótese ou boato a fato sem nova evidência.
9. Preservar IDs estáveis e referências verificáveis.
10. Não produzir em escala quando o Gate de validação aplicável estiver bloqueado.

## Regra de mudança

Nenhum código deve criar ou alterar silenciosamente o significado dos registros. Mudanças semânticas devem passar pela cadeia:

PROMPT → CARTA → LAYOUT ÚNICO → CÓDIGO.

## Relação com a FASE 2

A FASE 2 é a implementação operacional destas regras por meio de contratos, validador determinístico, testes e evidências de execução.

## Critério de encerramento

Esta Carta entra em estado CONCLUÍDA. Qualquer mudança futura será tratada como nova versão, com impacto documentado.

---
projeto: "Curioso da Internet IA"
repositorio: "carlos-andrade/Curioso-da-Internet-IA"
tipo_documento: "CONTROLE DE FASE"
fase: "FASE-1"
id_documento: "DOC-20261008-0040"
titulo: "FASE 1 — ARQUITETURA DO CONHECIMENTO"
status: "CONCLUÍDA"
versao: "1.0"
data_criacao: "2026-10-08"
data_atualizacao: "2026-10-08"
origem: "ARQUITETURA DO CONHECIMENTO"
autoridade_documental: "GOVERNANÇA"
cadeia_autoridade: "PROMPT → CARTA → LAYOUT ÚNICO → CÓDIGO"
---

# FASE 1 — ARQUITETURA DO CONHECIMENTO

## Objetivo

Estabelecer o modelo mínimo e reutilizável para transformar fontes em evidências, pesquisas, conhecimento, entidades, conexões, ideias e ganchos, antes da produção editorial em escala.

## Decisão arquitetural

A unidade principal do projeto é o **conhecimento reutilizável**, e não o vídeo.

Uma mesma pesquisa pode alimentar múltiplos formatos e voltar a ser utilizada quando surgir novo contexto.

## Camadas

```text
FONTE
  ↓
EVIDÊNCIA
  ↓
PESQUISA
  ↓
CONHECIMENTO
  ↓
ENTIDADES ↔ CONEXÕES
  ↓
BANCO DE IDEIAS / GANCHOS
  ↓
HISTÓRIAS / ROTEIROS / DECUPAGEM
  ↓
CONTEÚDO / PUBLICAÇÃO
  ↓
MÉTRICAS / APRENDIZADO
  ↺
```

## Tipos nucleares

- FONTE
- EVIDÊNCIA
- PESQUISA
- CONHECIMENTO
- ENTIDADE
- CONEXÃO
- HOOK
- IDEIA

## Estados

Estados de fluxo:

DESCOBERTA, EM INVESTIGAÇÃO, PARCIALMENTE VALIDADA, VALIDADA, CONHECIMENTO CONSOLIDADO, PUBLICÁVEL, PUBLICADO, MONITORADO, ATUALIZADO.

Estados de exceção:

CONTESTADA, NÃO CONFIRMADA, SUPERADA, CORRIGIDA, ARQUIVADA.

## Princípios

1. Uma fonte não é automaticamente uma evidência.
2. Toda afirmação publicável deve possuir rastreabilidade até evidências.
3. Fato, interpretação, hipótese e boato devem permanecer semanticamente separados.
4. Entidades devem possuir identidade reutilizável.
5. Conexões devem apontar para registros identificáveis.
6. O estado editorial deve refletir o grau de sustentação disponível.
7. Lacunas e conflitos devem ser preservados, não apagados por conveniência narrativa.
8. Alterações de contrato seguem a cadeia de autoridade: PROMPT → CARTA → LAYOUT ÚNICO → CÓDIGO.

## Relação com a FASE 2

A FASE 2 operacionaliza a validação dos registros definidos nesta arquitetura. Portanto, esta documentação é uma formalização controlada da arquitetura que sustenta os contratos já utilizados pela validação.

## Critério de encerramento

A FASE 1 é considerada concluída porque seus tipos, estados, relações e princípios já possuem representação operacional na FASE 2.

A partir deste ponto, novas alterações arquiteturais devem ser tratadas como mudança de contrato, com impacto explícito sobre layout, schemas, código e testes.

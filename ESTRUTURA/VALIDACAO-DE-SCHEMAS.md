# CABEÇALHO HISTÓRICO

- **Projeto:** Curioso da Internet IA
- **Documento:** Validação Determinística dos Schemas
- **Tipo:** Controle técnico
- **Versão:** 1.0
- **Data:** 2026-10-08
- **Status:** ATIVO
- **Repositório:** carlos-andrade/Curioso-da-Internet-IA
- **Local:** /ESTRUTURA/

## Objetivo

Garantir que registros respeitem os contratos estruturais antes de serem considerados ingestíveis pela automação.

## Validações mínimas

- JSON válido.
- Schema válido.
- Campos obrigatórios presentes.
- Tipos corretos.
- Enums respeitados.
- IDs no padrão.
- Referências com prefixo compatível.
- Datas em ISO 8601.
- URLs válidas quando obrigatórias.
- Ausência de propriedades não permitidas.
- Relações não podem apontar para IDs inexistentes em uma validação de integridade.

## Limite

Validação estrutural não prova que o conteúdo é verdadeiro. A verdade factual depende de evidência, fonte, revisão e estado editorial.

## Critério de bloqueio

Falha estrutural = registro rejeitado.

Conflito factual = registro pode existir, mas deve carregar o estado de incerteza correspondente.

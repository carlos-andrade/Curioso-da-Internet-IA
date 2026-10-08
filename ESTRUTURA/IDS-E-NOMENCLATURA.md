# CABEÇALHO HISTÓRICO

- **Projeto:** Curioso da Internet IA
- **Documento:** IDs e Nomenclatura
- **Tipo:** Padrão estrutural
- **Versão:** 1.0
- **Data:** 2026-10-08
- **Status:** ATIVO
- **Repositório:** carlos-andrade/Curioso-da-Internet-IA
- **Local:** /ESTRUTURA/

## Padrão

Formato geral:

`TIPO-AAAAMMDD-NNNN`

O prefixo identifica a classe do registro; a data identifica o lote de criação; o sufixo é sequencial dentro do lote.

## Prefixos

| Registro | Prefixo |
|---|---|
| Fonte | FONTE |
| Evidência | EVID |
| Pesquisa | PESQ |
| Entidade | ENT |
| Conhecimento | CONH |
| Conexão | CONX |
| Gancho | HOOK |
| Ideia | IDEIA |

## Regras

1. IDs são imutáveis.
2. O título pode mudar; o ID não.
3. Um registro corrigido mantém seu ID e recebe histórico de alteração.
4. Não reutilizar IDs apagados.
5. Referências entre registros usam o ID, não o título.
6. Nomes de arquivos devem usar o ID quando o registro for materializado individualmente.

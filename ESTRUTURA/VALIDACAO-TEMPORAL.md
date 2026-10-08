---
projeto: "Curioso da Internet IA"
repositorio: "carlos-andrade/Curioso-da-Internet-IA"
tipo_documento: "PROTOCOLO DE VALIDAÇÃO"
fase: "FASE-2"
id_documento: "DOC-20261008-0032"
titulo: "VALIDAÇÃO TEMPORAL"
status: "PUBLICADO"
versao: "1.0"
data_criacao: "2026-10-08"
data_atualizacao: "2026-10-08"
origem: "FASE-1 — estados e rastreabilidade"
autoridade_documental: "GOVERNANÇA"
cadeia_autoridade: "PROMPT → CARTA → LAYOUT ÚNICO → CÓDIGO"
---

# VALIDAÇÃO TEMPORAL

## Objetivo

Impedir que informação temporalmente sensível seja tratada como atual sem uma verificação compatível com a sua natureza.

## Classificação

1. **ATEMPORAL** — não depende de mudança relevante ao longo do tempo.
2. **HISTÓRICA** — descreve um período passado e deve preservar a data/período do fato.
3. **TEMPORALMENTE SENSÍVEL** — pode mudar e exige data de captura e última verificação.
4. **ATUAL** — afirmação sobre o presente; deve possuir verificação recente adequada ao assunto.

## Campos mínimos

- data do fato ou período;
- data de publicação da fonte, quando disponível;
- data/hora da captura;
- última verificação;
- responsável pela verificação;
- estado da informação;
- fonte/evidência utilizada.

## Regras

- Não usar a data da captura como se fosse a data do fato.
- Não converter informação histórica em afirmação atual sem evidência.
- Informação atual sem última verificação deve permanecer não confirmada para fins de publicação.
- Quando duas fontes apresentarem datas incompatíveis, registrar o conflito.
- Correções devem preservar o histórico da versão anterior.

## Gate

Falha temporal não apaga o registro; bloqueia sua promoção para um estado que exija atualidade.

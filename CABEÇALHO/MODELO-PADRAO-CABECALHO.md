# CABEÇALHO PADRÃO — Curioso da Internet IA

> **Documento normativo — modelo canônico para arquivos Markdown (.md).**

Este modelo define o cabeçalho obrigatório e a estrutura mínima de rastreabilidade dos documentos oficiais do projeto.

---

## 1. MODELO MARKDOWN

Para documentos Markdown, o cabeçalho deve ser inserido **no início do arquivo**, antes do conteúdo principal.

### 1.1 Front Matter YAML

```yaml
---
projeto: "Curioso da Internet IA"
repositorio: "carlos-andrade/Curioso-da-Internet-IA"
tipo_documento: "[TIPO]"
fase: "[FASE]"
id_documento: "[ID-UNICO]"
titulo: "[TÍTULO]"
status: "[STATUS]"
versao: "[VERSÃO]"
data_criacao: "[AAAA-MM-DD]"
data_atualizacao: "[AAAA-MM-DD]"
origem: "[ORIGEM]"
autoridade_documental: "[FONTE | CARTA | LAYOUT | GOVERNANÇA]"
cadeia_autoridade: "PROMPT → CARTA → LAYOUT ÚNICO → CÓDIGO"
rastreabilidade: "[COMMIT | PR | EVIDÊNCIA | REFERÊNCIA]"
escopo: "[ESCOPO]"
objetivo: "[OBJETIVO]"
dependencias: "[DEPENDÊNCIAS | N/A]"
---
```

### 1.2 Cabeçalho documental visível

```markdown
# [TÍTULO]

> **Projeto:** Curioso da Internet IA  
> **Repositório:** carlos-andrade/Curioso-da-Internet-IA  
> **Tipo:** [TIPO]  
> **Fase:** [FASE]  
> **ID:** [ID-UNICO]  
> **Status:** [STATUS]  
> **Versão:** [VERSÃO]  
> **Criação:** [AAAA-MM-DD]  
> **Atualização:** [AAAA-MM-DD]  
> **Origem:** [ORIGEM]  
> **Autoridade:** [FONTE | CARTA | LAYOUT | GOVERNANÇA]  
> **Rastreabilidade:** [COMMIT | PR | EVIDÊNCIA | REFERÊNCIA]
```

### 1.3 Contexto histórico

```markdown
## Contexto Histórico

[Registrar por que este documento existe, de onde surgiu, qual problema, decisão ou acontecimento o originou e sua relação com o projeto.]
```

### 1.4 Estado e validação

```markdown
## Estado

[Registrar o estado atual do documento.]

## Evidências

[Relacionar as evidências que sustentam o conteúdo.]

## Validação

[Registrar como o conteúdo foi validado.]

## Resultado

[Registrar o resultado produzido.]

## Próxima Ação

[Registrar a próxima etapa autorizada.]
```

---

## 2. REGRAS DO CABEÇALHO MARKDOWN

1. O **Front Matter YAML** deve ser a primeira informação do arquivo.
2. O título Markdown deve aparecer imediatamente após o Front Matter.
3. Os campos do Front Matter devem permanecer com nomes estáveis para permitir automação.
4. Campos não aplicáveis devem receber `N/A`; não devem ser simplesmente removidos.
5. `id_documento` deve ser único dentro do projeto.
6. Alterações relevantes devem atualizar `versao`, `data_atualizacao` e `rastreabilidade`.
7. O cabeçalho deve preservar o contexto histórico do documento.
8. A origem deve identificar de onde o documento deriva.
9. Evidência e validação são conceitos diferentes e devem permanecer separados.
10. O cabeçalho não substitui o conteúdo do documento; ele identifica sua autoridade, contexto, estado e rastreabilidade.
11. Documentos derivados devem apontar para seus artefatos de origem.
12. A estrutura deve ser válida como Markdown e compatível com automação futura.

---

## 3. CADEIA DE AUTORIDADE

**PROMPT → CARTA → LAYOUT ÚNICO → CÓDIGO**

O código não deve criar regras que não estejam sustentadas pelo layout.
O layout deve derivar das cartas.
As cartas devem derivar das regras e prompts de autoridade.

---

## 4. ESTADOS CANÔNICOS

`PLANEJADO` → `EM_DESENVOLVIMENTO` → `IMPLEMENTADO` → `VALIDANDO` → `VALIDADO` → `PUBLICADO` → `MONITORADO`

### Estados excepcionais

`BLOQUEADO` · `CONTESTADO` · `NÃO_CONFIRMADO` · `SUPERADO` · `CORRIGIDO` · `ARQUIVADO`

---

## 5. CLASSIFICAÇÃO DA INFORMAÇÃO

Quando aplicável, o documento deve distinguir explicitamente:

- **FATO** — informação sustentada por evidência verificável.
- **INTERPRETAÇÃO** — leitura analítica derivada dos fatos.
- **HIPÓTESE** — explicação ainda não demonstrada.
- **NÃO CONFIRMADO** — informação sem evidência suficiente para validação.
- **BOATO** — alegação cuja origem ou veracidade não foi estabelecida.

---

## 6. CHECKLIST

- [ ] Front Matter YAML presente
- [ ] Título definido
- [ ] Projeto definido
- [ ] Repositório definido
- [ ] Tipo definido
- [ ] Fase definida
- [ ] ID único definido
- [ ] Status definido
- [ ] Versão definida
- [ ] Datas registradas
- [ ] Origem registrada
- [ ] Autoridade documental registrada
- [ ] Rastreabilidade registrada
- [ ] Contexto histórico registrado
- [ ] Evidências registradas
- [ ] Validação registrada
- [ ] Resultado registrado
- [ ] Próxima ação registrada
- [ ] Documento Markdown válido

---

## 7. REGRA CENTRAL

> **Todo documento oficial do Curioso da Internet IA deve ser identificável, rastreável, contextualizado e validável.**

O cabeçalho é parte da governança do documento e não deve ser tratado como texto opcional.
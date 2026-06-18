# A Rebeldia da Mecatrônica

Este repositório contém o código-fonte, capítulos e scripts de compilação do livro **A Rebeldia da Mecatrônica - Romance Instrutivo de Tecnologia e Sociedade**.

## Estrutura do Repositório

* `/capitulos/`: Arquivos Markdown de cada um dos 13 capítulos estruturados sob o Padrão Editorial.
* `compile_book.py`: Script Python para geração do livro em formato PDF A5 com fonte Verdana 12 e leading condensado.
* `compile_html.py`: Script Python para compilação em página única HTML responsiva Mobile-First.
* `foundation.md`: Documento de fundação com a bíblia de personagens e diretrizes originais.
* `padrao_editorial.md`: Guia de estilo, ritmo e estrutura de escrita adotada no livro.
* `romance_instrutivo.pdf`: Livro compilado pronto em formato PDF.
* `romance_instrutivo.html`: Livro compilado pronto em formato HTML responsivo.

## Requisitos de Compilação

Para compilar o livro localmente, instale o ReportLab:

```bash
pip install reportlab
```

E execute:

```bash
python compile_book.py
python compile_html.py
```

# Memória do Workspace: A Rebeldia da Mecatrônica

Este documento registra o estado atual do projeto, a arquitetura do compilador, decisões técnicas críticas e diretrizes editoriais para que as próximas inteligências artificiais consigam assumir o desenvolvimento e edições futuras do livro de forma contínua e sem perda de contexto.

---

## 📈 1. Resumo das Últimas Alterações Realizadas

### 🖼️ Ajuste de Escalonamento e Proporção de Imagens (PDF)
* **Problema:** As imagens quadradas (`1024x1024` px) da capa e dos capítulos estavam sendo deformadas/esticadas no PDF devido a proporções fixadas estaticamente no código (`2:3` na capa e `16:9` nos capítulos).
* **Solução:** O script [compile_book.py](file:///d:/onedrive/outros/workspace_book/compile_book.py) agora usa a biblioteca `Pillow` (`PIL.Image`) para carregar a imagem em tempo de execução, calcular seu aspect ratio real (`altura / largura`) e aplicar o escalonamento proporcional dentro de limites de segurança de largura e altura da página A5, evitando qualquer distorção visual.

### 🧭 Correção na Navegação do Menu Lateral (HTML)
* **Problema:** O menu do [index.html](file:///d:/onedrive/outros/workspace_book/docs/index.html) gerava links genéricos (`#cap1`, `#cap2`...) sequencialmente sem considerar se o arquivo era uma introdução, um capítulo numerado ou um apêndice. Isso desalinhava o menu com a numeração real interna do livro.
* **Solução:** O script [compile_html.py](file:///d:/onedrive/outros/workspace_book/compile_html.py) agora analisa dinamicamente os títulos. Ele mapeia slugs amigáveis (`#como-estudar`, `#prologo`), capítulos reais (`#cap1` a `#cap13`) e apêndices (`#apendice-a`, `#apendice-b`), alinhando o menu do drawer lateral com as imagens e os IDs dos elementos.

### 📄 Sumário Dinâmico e Alinhado (Compilação em Duas Passadas no PDF)
* **Problema:** O sumário do PDF tinha números de página estáticos (`page_numbers`). Alterações de texto ou de tamanho de imagem quebravam o sumário de forma silenciosa.
* **Solução:** Implementação de um sistema de duas passadas utilizando a classe de fluxo invisível `PageTracker` (derivada de `Flowable`). O script roda o `doc.build()` uma primeira vez para capturar a página real onde cada capítulo começa e, na segunda passada, constrói o sumário final 100% atualizado e alinhado com o rodapé.

### ✍️ Refinamento de Conteúdo nos Capítulos & Apêndices
* **Capítulo 5:** Melhorada a explicação conceitual de IRQ/NMI e inserido diagrama ASCII da Stack. A narrativa do alarme real foi expandida para espelhar a dinâmica do Program Counter ($PC$) sendo salvo na pilha.
* **Capítulo 6:** Inserido diagrama de colisão booleana ASCII na camada $Z=0$, explicação de Bin Packing/First Fit e enriquecida a tensão do prazo de 24h em Milão e a proximidade física do robô AMR 12.
* **Capítulo 13:** Escrito por completo. Resolve todos os arcos: o arco narrativo de Alex moderno e de Alex Senior (com a carta oculta final de dedicatória), o arco técnico (ligando o Z80A ao AMR 12 em uma linha evolutiva contínua), e o arco social (engenharia prática brasileira contra o rentismo de mercado).
* **Apêndice A (Glossário):** Transformado em "Manual de Campo", contendo ícones temáticos, tags de referência cruzada, equações, analogias e micro-diagramas lógicos (Stack, Ponte H, PWM, Matriz Booleana).
* **Apêndice B (Guia Mecatrônico):** Expandido com trilhas de estudo estruturadas (do básico ao ROS 2), laboratórios detalhados com códigos práticos em Python e C++ (PWM, Encoders, Colisão, etc.), conselhos emocionais de faculdade e dicas para montar portfólio de carreira.

---

## 🛠️ 2. Arquitetura e Estrutura do Projeto

* `/capitulos/`: Contém os arquivos fontes em Markdown (`.md`) ordenados alfabética e numericamente.
* `/imagens/`: Contém as ilustrações do livro (`capa.png` e `cap1.png` a `cap3.png`).
* `/docs/`: Destino de saída compilado. O GitHub Pages aponta para este diretório.
  * `/docs/index.html`: Versão de página única Mobile-First responsiva.
  * `/docs/romance_instrutivo.pdf`: Versão diagramada A5.
* [compile_book.py](file:///d:/onedrive/outros/workspace_book/compile_book.py): Compilador PDF baseado em Python e ReportLab.
* [compile_html.py](file:///d:/onedrive/outros/workspace_book/compile_html.py): Compilador HTML que converte Markdown em HTML responsivo.

---

## 🚀 3. Instruções de Desenvolvimento (Comandos)

### 🔌 Requisitos
Instale as dependências com:
```bash
pip install reportlab Pillow bs4
```

### ⚡ Compilar Livro
Para gerar a versão PDF e a versão HTML atualizadas:
```bash
python compile_book.py
python compile_html.py
```

### 📦 Sincronização Git
Após compilar e validar alterações:
```bash
git add .
git commit -m "Mensagem descritiva"
git push
```

---

## 📝 4. Diretrizes Editoriais e de Estilo para Futuras IAs

1. **Tom de Voz:** Conversacional, prático, motivador e instigante. A matemática e a computação de baixo nível devem ser tratadas como "ferramentas de controle do mundo real" para solucionar problemas práticos, nunca como decoreba acadêmica teórica.
2. **Uso de Imagens no PDF:** Nunca force dimensões estáticas esticadas nas imagens. Sempre use o cálculo dinâmico com Pillow para preservar a proporção de aspecto nativa.
3. **Cálculo de Páginas:** Sempre compile em duas passadas para garantir que o sumário dinâmico reflita a página real dos capítulos.
4. **Fiel ao Continuum Tecnológico:** Mantenha sempre a analogia que cruza as eras do Z80 (baixo nível físico/eletricidade) e dos robôs autônomos modernos controlados por ROS 2 e SLAM. A tecnologia deve ser explicada como o mesmo fenômeno em escalas diferentes.

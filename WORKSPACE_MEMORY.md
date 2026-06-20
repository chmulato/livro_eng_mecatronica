# Memória do Workspace: A Rebeldia da Mecatrônica

Este documento registra o estado atual do projeto, a arquitetura do compilador, decisões técnicas críticas e diretrizes editoriais para que as próximas inteligências artificiais consigam assumir o desenvolvimento e edições futuras do livro de forma contínua e sem perda de contexto.

---

## 📈 1. Resumo das Últimas Alterações Realizadas

### 🖼️ Geração e Inserção Completa de Ilustrações (HTML & PDF)
*   **Melhoria:** Criação de ilustrações para todos os capítulos restantes do livro (`cap4.png` a `cap13.png`), mantendo consistência absoluta com os prompts estipulados no guia visual (`prompts_ilustracoes.md`).
*   **Estilo Visual:** Design de arte conceitual Tech-Noir Industrial com tons frios de azul cobalto e poeira industrial contrastando com pontos de energia quentes em laranja e amarelo neon.

### 🌉 Ajuste de Transições e Fórmulas Matemáticas no HTML
*   **Melhoria:** Adaptação da lógica de renderização matemática baseada em LaTeX simples também no arquivo `compile_html.py` (antes restrita apenas ao PDF). As equações em bloco (`$$`) e termos matemáticos inline (`$`) agora são renderizados com tags HTML compatíveis, exibindo símbolos de forma adequada e limpa no navegador.
*   **Estilização Lousa Verde:** A folha de estilos CSS do HTML agora recria a estética de lousas verdes escolares com molduras de madeira de 5px, sombras projetadas e fontes de giz mono-espaçadas para equações e códigos.

### 📄 Regras de Formatação e Recuo de Parágrafos (Padrão Editorial)
*   **Melhoria:** Correção de incongruências gráficas na indentação de romances.
    *   **PDF:** Criação do estilo `NarrativeFirstStyle` (com recuo `0`) aplicado automaticamente ao primeiro parágrafo de cada capítulo ou seção após cabeçalhos (`h1`, `h2`, `h3`), imagens, lousas e listagens. Parágrafos subsequentes mantêm o recuo literário padrão de `12pt`.
    *   **HTML:** Implementação de seletores de CSS avançados de irmão adjacente (`h2 + .narrative-p`, `pre + .narrative-p`) para remover o recuo do primeiro parágrafo de texto e manter `text-indent: 18px` nos seguintes.

### ⏱️ Transições Suaves e Navegação Otimizada (HTML)
*   **Melhoria:** Adição de `scroll-behavior: smooth` e `scroll-padding-top: 80px` nas folhas de estilo globais do HTML compilado, permitindo navegação fluida pelos tópicos do menu lateral (Drawer) sem sobrepor títulos por baixo da barra fixa superior.

### 🎨 Inclusão do Apêndice C: Galeria de Arte e Prompts de IA
*   **Melhoria:** Criação do arquivo [16_galeria_arte.md](file:///d:/onedrive/outros/workspace_book/capitulos/16_galeria_arte.md) para atuar como o **Apêndice C**. Este documento atua de forma lúdica revelando as descrições em português e os prompts em inglês que originaram a identidade visual e ilustrações do livro, alinhado à filosofia didática de "abrir a caixa preta".

---

## 🛠️ 2. Arquitetura e Estrutura do Projeto

*   `/capitulos/`: Contém os arquivos fontes em Markdown (`.md`) ordenados alfabética e numericamente.
*   `/imagens/`: Contém as ilustrações do livro (`capa.png` e `cap1.png` a `cap13.png`).
*   `/docs/`: Destino de saída compilado. O GitHub Pages aponta para este diretório.
    *   `/docs/imagens/`: Cópia espelhada dos assets visuais para consumo do arquivo HTML.
    *   `/docs/index.html`: Versão de página única Mobile-First responsiva.
    *   `/docs/romance_instrutivo.pdf`: Versão diagramada A5.
*   [compile_book.py](file:///d:/onedrive/outros/workspace_book/compile_book.py): Compilador PDF baseado em Python e ReportLab.
*   [compile_html.py](file:///d:/onedrive/outros/workspace_book/compile_html.py): Compilador HTML que converte Markdown em HTML responsivo.

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

1.  **Tom de Voz:** Conversacional, prático, motivador e instigante. A matemática e a computação de baixo nível devem ser tratadas como "ferramentas de controle do mundo real" para solucionar problemas práticos, nunca como decoreba acadêmica teórica.
2.  **Uso de Imagens no PDF:** Nunca force dimensões estáticas esticadas nas imagens. Sempre use o cálculo dinâmico com Pillow para preservar a proporção de aspecto nativa.
3.  **Cálculo de Páginas:** Sempre compile em duas passadas para garantir que o sumário dinâmico reflita a página real dos capítulos.
4.  **Recuo de Romance:** Mantenha sempre a regra de recuo nulo para o parágrafo inicial que sucede qualquer cabeçalho ou caixa especial de código e recuo padrão para os subsequentes.
5.  **Fiel ao Continuum Tecnológico:** Mantenha sempre a analogia que cruza as eras do Z80 (baixo nível físico/eletricidade) e dos robôs autônomos modernos controlados por ROS 2 e SLAM. A tecnologia deve ser explicada como o mesmo fenômeno em escalas diferentes.

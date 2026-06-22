# Memória do Workspace: A Rebeldia da Mecatrônica

Este documento registra o estado atual do projeto, a arquitetura do compilador, decisões técnicas críticas e diretrizes editoriais para que as próximas inteligências artificiais consigam assumir o desenvolvimento e edições futuras do livro de forma contínua e sem perda de contexto.

---

## 📈 1. Resumo das Últimas Alterações Realizadas

### 🎓 Aprimoramento Didático e Narrativo dos Capítulos Finais (11, 12 e 13)
*   **Capítulo 11 ("A Elite do Atraso"):** Reescrevemos o capítulo focando na engenharia de fluxo cotidiano do jovem leitor (sistemas dinâmicos, *bus bunching*, gargalos na catraca e o Problema do Caixeiro Viajante - TSP). Adicionamos a caixa de destaque **💡 A Regra do Custo de Oportunidade** para ilustrar matematicamente a decisão econômica entre investimentos industriais reais (ROI da tecnologia) vs. rentismo passivo (taxa Selic).
*   **Capítulo 12 ("A Engenharia do Pix e do Bloco"):** Implementamos uma abertura narrativa tensa com o travamento físico de um robô AMR devido a um erro de *timeout* e consistência distribuída. Explicamos a criptografia assimétrica (chave pública/privada) como uma caixa de correio com fresta e cadeado, os blocos da Blockchain como paletes lacrados invioláveis por hash, e desenvolvemos um script Python prático que simula a integridade encadeada e o efeito avalanche do hash SHA-256. Adicionamos um desafio físico de medição de latência (`ping`).
*   **Capítulo 13 ("A Rebeldia da Mecatrônica"):** Concluímos o romance com uma cena reflexiva ao entardecer sob a névoa de Curitiba. Amarramos o *continuum tecnológico* unindo o antigo Z80 e o AMR moderno como o mesmo fenômeno em escalas diferentes. Preservamos na lousa verde do galpão o **Manifesto do Silício** (três regras fundamentais sobre soberania, recusa de caixas-pretas proprietárias e persistência teimosa na física). Inserimos o desafio final maker estimulando o leitor a abrir e mapear a engenharia de um dispositivo doméstico comum para iniciar seu próprio manual de campo.

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

### 🌐 Sincronização e Publicação
*   **Melhoria:** Compilação bem-sucedida das saídas finais (PDF e HTML) e envio das atualizações para o branch `master` no repositório remoto do GitHub.

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

---

## 🔮 5. Perspectivas e Diretrizes para Evoluções Didáticas Futuras

Para edições ou desdobramentos futuros, as seguintes melhorias didáticas são recomendadas para enriquecer a experiência de aprendizado do leitor:

1.  **Laboratórios Interativos Virtuais (Simulação Web):**
    *   *Objetivo:* Embutir simuladores ou pequenos compiladores interativos baseados em Javascript/WebAssembly (Wasm) diretamente na página web (`docs/index.html`).
    *   *Sugestão:* Permitir que o leitor manipule e teste portas lógicas básicas (Capítulo 3) ou escreva pequenos blocos de Z80 Assembly e veja o estado dos registradores mudando visualmente na própria lousa digital do livro.
2.  **Notas de Bordo com Mapeamento Conceitual Visual:**
    *   *Objetivo:* Facilitar a visualização da árvore de dependências conceituais.
    *   *Sugestão:* Adicionar pequenos diagramas de fluxos (ASCII ou SVG leve) que mapeiam visualmente os tópicos do Manual de Campo que estão ativos ou são fundamentais para o trecho da narrativa em leitura.
3.  **Exercícios de Engenharia Crítica e Geopolítica:**
    *   *Objetivo:* Estimular discussões extracurriculares sobre o papel social da engenharia técnica.
    *   *Sugestão:* Criar um apêndice extra com debates estruturados ou desafios sobre soberania tecnológica, investimento de capital em desenvolvimento nacional vs. rentismo financeiro (conectando as tensões dos Capítulos 11 e 13).


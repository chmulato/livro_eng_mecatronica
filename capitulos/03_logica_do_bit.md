# Capítulo 3: A Lógica do Bit

A chuva finalmente desabou sobre o telhado da escola técnica.
O barulho isolava a sala de aula do resto do mundo em 1986.
Alex Senior encarava o cursor piscante do TK90X na TV de tubo.

Ele queria criar um jogo de ação espacial com uma nave desviando de asteroides.
O problema era cruel: não existia internet ou tutoriais para consultar.
O único manual do computador era um livreto fino e traduzido de forma confusa.

Para ir além, ele precisava decifrar a linguagem nativa do chip Z80.
Ele tinha que entender como converter números em pixels coloridos na tela.
Precisava dominar a matemática invisível que governava os transistores.

Para se comunicar com o hardware sem perder a razão, ele anotou uma regra fundamental.

> “Para nós, humanos, contar de dez em dez é o natural,” escreveu Alex Senior.
> “Em contrapartida, o Z80 só enxerga eletricidade e tensão elétrica nos pinos.
> Ele só tem dois estados elétricos possíveis: ligado (1) ou desligado (0). É o sistema binário.”

> “Para não enlouquecer escrevendo zeros e uns, usamos o sistema hexadecimal.
> Agrupamos os números de dezesseis em dezesseis, de 0 a 9 e de A a F para 10 a 15.
> O número 255 (máximo de um byte) vira 11111111 em binário, ou simplesmente FF em hexa.”

A transição da teoria para a prática dependia apenas de um caderno quadriculado.

### [Desafio Prático] A Conversão do Sprite da Nave

Para criar o gráfico da nave espacial, Alex Senior abriu o caderno.
Com uma caneta preta, desenhou uma matriz quadriculada de 8 colunas por 8 linhas.
Pintou os quadradinhos centrais para dar forma física à fuselagem.

Cada quadrado em branco representava o bit zero (`0`).
Cada quadrado preenchido e pintado de preto representava o bit um (`1`).
Linha por linha, os blocos de interruptores criavam uma sequência numérica.

A primeira linha desenhada tinha o padrão binário `00011000`, equivalente ao decimal 24.
A segunda linha exibia `00111100`, que correspondia ao número decimal 60.
A terceira, com as asas da nave totalmente abertas, formava `11111111` (decimal 255).

Alex Senior traduziu o desenho em uma lista de oito números decimais de controle.
Aquele conjunto numérico era o código genético de sua nave na memória.
Ele usaria o comando `POKE` do BASIC para gravar esses valores diretamente no hardware.

---

### A Luz que Pisca: Do Caderno Quadriculado aos Encoders Industriais

A imagem pixelada daquela nave espacial desenhada na TV Colorado pareceu pulsar, até congelar sob o feixe verde do laser do LiDAR moderno de Curitiba em 2026.

Alex moderno levantou os olhos do diário no galpão silencioso de Curitiba.
Ele observou o motor de tração de um dos robôs AMRs parado na estação.
No eixo da roda traseira do robô, notou a carcaça de proteção do encoder óptico.

O princípio do sensor moderno era o mesmo grid quadriculado desenhado por seu mentor.
Dentro do encoder, um pequeno disco plástico transparente cheio de ranhuras pretas girava.
Um feixe de luz infravermelha atravessava o disco durante a rotação física.

A luz passando pela área transparente gerava corrente elétrica: bit um (`1`).
Quando a ranhura escura bloqueava a luz, a corrente elétrica cessava: bit zero (`0`).
O sensor gerava uma sequência de bits em alta velocidade para calcular a velocidade.

"Tanto poder de processamento em 2026," murmurou Alex, vendo o robô piscar em azul.
"E a segurança física de uma máquina cara ainda depende de a luz passar ou não pelo disco.
No fim das contas, tudo na engenharia se resume a zeros e uns."

Ele passou a mão sobre a folha amarelada do diário com respeito.
A primeira parte de sua jornada de descoberta física com o mentor estava concluída.
Ele agora precisava virar a página e viajar para as memórias industriais da Itália.

---

### 🧠 O que você aprendeu aqui
- **Bases Lógicas**: O binário reflete estados elétricos (0 e 1), e o hexadecimal serve como abreviação.
- **Estruturação de Dados**: Imagens bidimensionais em telas antigas eram mapeadas como matrizes de bits de memória.

### 🎮 Desafio prático
**O Desenho de Sprites Digitais**  
Desenhe uma grade de 8x8 em um papel quadriculado e crie o desenho de um invasor espacial. Escreva a sequência binária correspondente a cada linha e faça a conversão decimal equivalente.

### ✨ Conexão com o próximo capítulo
Com a lógica dos bits compreendida, Alex precisa encarar como esses dados são manipulados em grande escala. No próximo capítulo, cruzaremos o tempo até o inverno de 2001 na Itália para desvendar a temida "saudação de três dedos" e ver o que acontece quando a memória de um sistema real atinge seus limites físicos.

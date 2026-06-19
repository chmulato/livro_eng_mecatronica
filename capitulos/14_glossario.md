# Apêndice A: Glossário de Engenharia e Automação

Bem-vindo ao **Manual de Campo Mecatrônico**. Este glossário não é apenas uma lista alfabética de definições: é uma ferramenta prática de campo projetada para conectar o hardware clássico de 1986 à robótica moderna de 2026. 

---

### 🛠️ Como Usar Este Guia
Cada termo está estruturado em três níveis de profundidade:
1. **Definição Direta:** O conceito técnico traduzido de forma clara e sem rodeios.
2. **Metáfora & Analogia:** A ligação literária com as ilustrações e histórias do livro.
3. **Caso de Uso Prático:** Como e onde o conceito é aplicado no galpão de Curitiba ou na crise logística de Milão.

#### 🏷️ Símbolos de Identificação Rápida
* ⚙️ **Hardware / Eletrônica:** Peças, circuitos e chips físicos.
* 🧠 **Software / Fluxo:** Algoritmos, código e lógica de controle.
* 🤖 **Robótica Aplicada:** A fusão de lógica e movimento mecânico.
* 🧮 **Matemática do Espaço:** Fórmulas, matrizes e álgebra linear.

---

## 📂 Grupos Temáticos de Referência

* **[Sistemas e CPU]** Z80, Registrador, Program Counter, Stack, IRQ, NMI, Vetor de Reset.
* **[Controle e Atuadores]** Ponte H, PWM, Encoder Óptico.
* **[Navegação e Percepção]** LiDAR, Odometria, SLAM, Filtro de Kalman.
* **[Lógica e Otimização]** Matriz Booleana, 3D Bin Packing, ROS 2, Nós.

---

## 📖 Dicionário de Campo

### 1. Z80 (⚙️ Hardware)
* **Capítulos Relacionados:** Cap. 1, Cap. 2, Cap. 4
* **Definição:** Microprocessador de 8 bits lançado em 1976. Executa instruções lógicas sequenciais básicas.
* **Analogia:** O cérebro primitivo e obstinado do escriturário de olheiras profundas.
* **Exemplo Prático:** O processador principal que governou computadores antigos como o TK90X e o circuito de monitoramento mecânico de Milão.
* **Termos Relacionados:** Registrador, Program Counter.

---

### 2. Registrador / Register (⚙️ Hardware)
* **Capítulos Relacionados:** Cap. 2, Cap. 5
* **Definição:** Pequeno compartimento de armazenamento temporário ultrarrápido integrado diretamente no interior da CPU.
* **Analogia:** As gavetas de mesa do escriturário da CPU, que guardam apenas um número de cada vez.
* **Exemplo Prático:** O Acumulador (Reg A) que armazena dados de 8 bits (de 0 a 255) em tempo real durante operações lógicas.
* **Termos Relacionados:** Z80, Program Counter.
* **Micro-código:**
  ```assembly
  LD A, 10      ; Carrega o número decimal 10 no registrador Acumulador (Reg A)
  ```

---

### 3. Program Counter / PC (🧠 Software)
* **Capítulos Relacionados:** Cap. 2, Cap. 5
* **Definição:** Registrador especial da CPU que aponta para o endereço da próxima instrução a ser executada no fluxo de memória.
* **Analogia:** A setinha indicadora ou régua física que guia os olhos do escriturário no manual de instruções do chip.
* **Exemplo Prático:** Durante um RESET físico, o PC é forçado a pular instantaneamente de volta para o endereço inicial `0000h`.
* **Termos Relacionados:** Z80, Stack, Vetor de Reset.

---

### 4. Stack / Pilha de Memória (🧠 Software)
* **Capítulos Relacionados:** Cap. 5
* **Definição:** Região da RAM que armazena dados de forma sequencial utilizando a lógica LIFO (Last-In, First-Out).
* **Analogia:** Uma pilha de pratos onde você só adiciona (PUSH) ou remove (POP) o prato posicionado no topo.
* **Exemplo Prático:** Onde a CPU salva o Program Counter ($PC$) quando uma interrupção de hardware suspende a rotina de execução.
* **Termos Relacionados:** Program Counter, IRQ.
* **Micro-diagrama:**
  ```
  Inserir dado (PUSH) / Retirar dado (POP)
                 │   ▲
                 ▼   │
        Topo ──> [ PC Salvo (ex: 0x0042) ]
                 [ Registrador A antigo  ]
                 [ Endereço de Retorno   ]
  ```

---

### 5. Interrupção / IRQ (🧠 Software / ⚙️ Hardware)
* **Capítulos Relacionados:** Cap. 5
* **Definição:** Sinal elétrico enviado por um dispositivo de hardware externo que força a CPU a parar temporariamente sua execução.
* **Analogia:** O telefone vermelho tocando na mesa do escriturário de forma insistente, demandando atenção prioritária.
* **Exemplo Prático:** O sinal gerado pelo sensor de presença no teclado IBM que interrompe a CPU para ler a tecla pressionada.
* **Termos Relacionados:** Stack, NMI, Program Counter.

---

### 6. NMI / Interrupção Não-Mascarável (⚙️ Hardware)
* **Capítulos Relacionados:** Cap. 5
* **Definição:** Um tipo especial de interrupção física de hardware de prioridade absoluta que a CPU não pode ignorar ou desativar.
* **Analogia:** Um alarme físico de incêndio que obriga o escriturário a sair correndo imediatamente, sem chance de ignorar.
* **Exemplo Prático:** O sinal do botão de parada de emergência do galpão de Milão que interrompeu o transelevador em 2001.
* **Termos Relacionados:** Interrupção (IRQ).

---

### 7. Vetor de Reset (💡 Conceito)
* **Capítulos Relacionados:** Cap. 5
* **Definição:** O endereço de memória fixado no hardware para onde a CPU aponta logo após ser alimentada com energia ou reiniciada.
* **Analogia:** O endereço da primeira instrução do manual do escriturário toda vez que ele acorda ou liga.
* **Exemplo Prático:** O hexadecimal `0000h` no Z80 ou a linha de código em `FFFF:0000h` nos processadores modernos baseados em x86.
* **Termos Relacionados:** Program Counter.

---

### 8. Ponte H (🔌 Eletrônica / ⚙️ Hardware)
* **Capítulos Relacionados:** Cap. 8
* **Definição:** Circuito chaveado que permite a microcontroladores inverter a polaridade aplicada a motores de corrente contínua.
* **Analogia:** Um trilho ferroviário com desvios articulados que alteram o sentido em que o trem (a corrente) corre.
* **Exemplo Prático:** O circuito integrado responsável por comandar o sentido de rotação dos motores nos transelevadores de Milão.
* **Termos Relacionados:** PWM.
* **Micro-diagrama:**
  ```
          [ + Vcc (Alimentação) ]
            /                 \
       Chave 1               Chave 2
          ├───[ Motor CC ]────┤
       Chave 3               Chave 4
            \                 /
            [ Terra (GND) ]
  ```

---

### 9. PWM / Modulação por Largura de Pulso (🔌 Eletrônica)
* **Capítulos Relacionados:** Cap. 8
* **Definição:** Técnica que varia a potência de saída variando a proporção de tempo que um sinal elétrico digital passa ligado.
* **Analogia:** Acender e apagar o interruptor de luz tão rápido que a lâmpada parece estar no estado de "meia luz" estável.
* **Exemplo Prático:** O controle eletrônico preciso da velocidade das rodas motrizes do robô AMR no galpão de Curitiba.
* **Termos Relacionados:** Ponte H.
* **Micro-diagrama:**
  ```
  Duty Cycle 25%: [───]___________[───]___________ (Velocidade Baixa)
  Duty Cycle 75%: [─────────]_____[─────────]_____ (Velocidade Alta)
  ```

---

### 10. LiDAR (🤖 Robótica Aplicada)
* **Capítulos Relacionados:** Cap. 6, Cap. 7, Cap. 8
* **Definição:** Sensor óptico rotativo de distância baseado no tempo de ida e volta (Time of Flight) de feixes de laser infravermelho.
* **Analogia:** Uma lanterna laser ultrarrápida que calcula distâncias "gritando" pulsos de luz e cronometrando o eco do reflexo.
* **Exemplo Prático:** O scanner laser no topo do AMR 12 que faz a varredura do corredor B para detectar paletes estacionados.
* **Termos Relacionados:** SLAM.

---

### 11. Encoder Óptico (⚙️ Hardware)
* **Capítulos Relacionados:** Cap. 7, Cap. 8
* **Definição:** Sensor óptico acoplado ao eixo de motores que mede velocidade angular contando fendas físicas em um disco giratório.
* **Analogia:** Um disco quadriculado que gira sob um sensor de luz, contando os pequenos "passos de formiga" das rodas.
* **Exemplo Prático:** O sensor físico nas rodas do AMR que decide se ele avança com precisão milimétrica ou bate na prateleira.
* **Termos Relacionados:** Odometria.

---

### 12. Odometria (🧮 Matemática do Espaço / 🤖 Robótica)
* **Capítulos Relacionados:** Cap. 7, Cap. 8
* **Definição:** A estimativa da distância percorrida pelo veículo calculada integrando no tempo os giros medidos nas rodas.
* **Analogia:** O ato de estimar a distância caminhada contando passos com um pedômetro no pé do robô.
* **Exemplo Prático:** O cálculo de posicionamento do robô AMR que acumula pequenos erros causados por derrapagens no piso liso.
* **Termos Relacionados:** Encoder Óptico, Filtro de Kalman.

---

### 13. SLAM / Localização e Mapeamento Simultâneos (🤖 Robótica)
* **Capítulos Relacionados:** Cap. 7
* **Definição:** Algoritmo de mapeamento que constrói de forma dinâmica o mapa do ambiente enquanto estima a posição do veículo.
* **Analogia:** Andar de olhos vendados tateando as paredes e desenhando o mapa do quarto na mente à medida que caminha.
* **Exemplo Prático:** A inteligência do AMR que atualiza o mapa operacional das docas de Curitiba para evitar colisões.
* **Termos Relacionados:** LiDAR, Odometria.

---

### 14. Filtro de Kalman (🧮 Matemática do Espaço)
* **Capítulos Relacionados:** Cap. 7
* **Definição:** Algoritmo estatístico recursivo que funde medições dinâmicas de sensores ruidosos para estimar o estado ideal.
* **Analogia:** Um navegador prudente que combina uma bússola imprecisa e o número de passos do tripulante para calcular o rumo exato.
* **Exemplo Prático:** O software que integra os dados do LiDAR com a odometria ruidosa das rodas para manter o robô na rota.
* **Termos Relacionados:** Odometria, SLAM.

---

### 15. Matriz Booleana de Ocupação (🧮 Matemática do Espaço)
* **Capítulos Relacionados:** Cap. 6
* **Definição:** Grade de bits onde o valor 1 indica células tridimensionais ocupadas por objetos físicos e 0 representa espaço livre.
* **Analogia:** Um condomínio de caixas virtuais empilhadas onde cada apartamento pode estar ocupado por carga ou vazio.
* **Exemplo Prático:** O mapa tridimensional do Corredor B no tablet de Alex que previne sobreposição de caixas pesadas de baterias.
* **Termos Relacionados:** 3D Bin Packing.
* **Micro-diagrama:**
  ```
  Camada Z = 0 (Nível do Solo)
  [0][1][0][0]  <── 1 indica ocupado por outro palete
  [0][1][1][0]  <── Carga atual ocupando mais de uma célula
  ```

---

### 16. 3D Bin Packing (🧮 Matemática do Espaço)
* **Capítulos Relacionados:** Cap. 6
* **Definição:** Algoritmo combinatório focado em organizar de forma ótima caixas tridimensionais de tamanhos variados em contêineres.
* **Analogia:** A arte mecânica de empilhar perfeitamente malas e mochilas no porta-malas de um carro de viagem.
* **Exemplo Prático:** O algoritmo First Fit que resolveu o empilhamento das autopeças da Fiat na crise de estocagem de Milão.
* **Termos Relacionados:** Matriz Booleana de Ocupação.
* **Micro-código:**
  ```python
  # Heurística First Fit simples
  if verificar_colisao(pos_nova, dim_nova, pos_existentes, dim_existentes):
      procurar_proximo_nicho()
  ```

---

### 17. ROS 2 / Robot Operating System (🧠 Software)
* **Capítulos Relacionados:** Cap. 5, Cap. 8
* **Definição:** Middleware estruturado para gerenciar a troca distribuída de tópicos de comunicação e serviços em sistemas robóticos.
* **Analogia:** A rede de tubulações e rádios que liga os diferentes operadores de uma grande fábrica conectada.
* **Exemplo Prático:** O software central do robô AMR que recebe dados LiDAR e envia comandos de movimento para as rodas.
* **Termos Relacionados:** Nós (Nodes).

---

### 18. Nós / Nodes (🧠 Software)
* **Capítulos Relacionados:** Cap. 5, Cap. 8
* **Definição:** Processos independentes especializados que processam dados de sensores e comandam atuadores na rede ROS 2.
* **Analogia:** Diferentes operários especializados em uma equipe: um mede com laser, outro decide a rota, outro dirige as rodas.
* **Exemplo Prático:** O nó de navegação do AMR comunicando-se em milissegundos com o nó de controle de velocidade das rodas.
* **Termos Relacionados:** ROS 2.

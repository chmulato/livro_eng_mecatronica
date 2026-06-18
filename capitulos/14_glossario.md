# Apêndice A: Glossário de Engenharia e Automação

Para ajudar na navegação pelos conceitos apresentados no diário e no CD, aqui está um glossário com explicações visuais e analógicas dos principais termos mecatrônicos:

### 1. Hardware e Eletrônica Básica
* **Z80**: Microprocessador de 8 bits lançado em 1976. Ele executa instruções lógicas sequenciais básicas de leitura e escrita e governou computadores antigos como o TK90X e o MSX.
* **Registradores**: Pequenos compartimentos internos de armazenamento temporário ultrarrápido dentro do chip. No Z80, guardam números inteiros de 8 bits (de 0 a 255).
* **Ponte H**: Circuito eletrônico chaveado que permite a microcontroladores controlar o sentido de rotação e a velocidade de motores elétricos de corrente contínua (CC).
* **PWM (Modulação por Largura de Pulso)**: Técnica que simula tensões analógicas variando a largura de pulso de um sinal digital (ligado/desligado) em alta velocidade. Usada para alterar o brilho de LEDs e velocidades de motores.

### 2. Robótica Móvel e Algoritmos
* **LiDAR (Light Detection and Ranging)**: Sensor óptico de distância. Funciona disparando feixes de laser infravermelho e calculando o tempo necessário para a luz refletir e retornar (Time of Flight).
* **SLAM (Simultaneous Localization and Mapping)**: Algoritmo que permite a um veículo autônomo construir o mapa de um ambiente desconhecido e, ao mesmo tempo, estimar sua própria posição física dentro dele.
* **Filtro de Kalman**: Algoritmo recursivo que funde dados ruidosos de sensores (ex: LiDAR e odometria) para obter estimativas de posição com o menor erro estatístico possível.
* **Odometria**: Estimativa da distância percorrida pelo veículo calculada com base na rotação das rodas monitorada por sensores (encoders). Sujeita a desvios por derrapagem.

### 3. Sistemas e Redes
* **ROS 2 (Robot Operating System)**: Framework de software de código aberto (middleware) que gerencia a troca de mensagens em tópicos e serviços entre diferentes programas (Nós) de um robô.
* **Nós (Nodes)**: Processos de software independentes e cooperativos dentro do ROS 2. Exemplo: um nó lê o sensor do laser e outro decide a velocidade do motor.

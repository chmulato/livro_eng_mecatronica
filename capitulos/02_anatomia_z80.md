# Capítulo 2: A Anatomia do Z80

Sentado em um banco de madeira no posto de monitoramento, Alex abriu o diário técnico.
A caligrafia de Alex Senior começava abaixo de um título sublinhado duas vezes:
*"Como o Z80 pensa: O mistério dos 8 bits e das gavetas secretas"*.

Alex moderno deu um gole no café morno de sua garrafa térmica.
Acostumado a usar Python, onde uma única biblioteca oculta milhares de processos, ele sentiu curiosidade.
Decidiu ler a explicação de seu mentor para entender as raízes do hardware de baixo nível.

Para desmistificar a caixa de metal sob o teclado, as anotações do diário propunham um ponto de partida simples.

> “Se você quer controlar uma máquina, não pode tratá-la como um computador de ficção. O Z80 não sabe o que é uma imagem, som ou palavra. Ele só entende energia elétrica: passa corrente (1) ou não passa (0). Esse é o bit.”

> “Mas um bit sozinho é apenas um interruptor solitário na parede. Para fazer algo útil, nós os agrupamos de oito em oito. Oito bits formam um byte. Pense em uma palavra de oito letras onde cada letra só pode ser '0' ou '1'.”

Para explicar a manipulação desses bytes no processador, o diário trazia uma analogia visual simples.

### [Conceito Chave] A analogia das gavetas de dados

Imagine que o processador é um escriturário muito rápido, mas com séria perda de memória recente.
Ele só consegue trabalhar com o que está vendo exatamente neste instante em sua mesa.
Para ajudá-lo, o chip possui gavetas de armazenamento ultrarrápidas chamadas registradores.

No Z80, essas gavetas guardam apenas números de 8 bits.
O maior valor que cabe em cada gaveta é o correspondente a oito bits ligados em nível alto (11111111).
No nosso sistema decimal comum, esse valor limite é o número 255.

O diagrama feito à mão por Alex Senior mostrava a disposição interna dos registradores:
```
+-----------------------------------+
|      GAVETAS DO PROCESSADOR (REG) |
|  +---------+   +---------+        |
|  |  Reg A  |   |  Reg B  |        |
|  | (Acumul)|   | (Auxil) |        |
|  +---------+   +---------+        |
|  |  Reg C  |   |  Reg D  |        |
|  +---------+   +---------+        |
+-----------------------------------+
```

A gaveta **A** é a mais importante e chama-se **Acumulador**.
Se você quer somar dois números, deve colocar o primeiro em A e o segundo em B.
Ao comandar a soma, o resultado final substitui o valor anterior que estava na gaveta A.

Alex moderno sorriu, comparando aquela lógica física com seu código cotidiano em Python:
```python
acumulador = 10
auxiliar = 5
acumulador = acumulador + auxiliar
```

Por trás do código abstrato, a CPU moderna repete o mesmo ciclo elétrico elementar.
Ela move dados entre registradores físicos de hardware e acumula o resultado final no registrador principal.
A linguagem Assembly do Z80 simplesmente eliminava essas máscaras de software.

No diário, a instrução **LD** (Load/Carregar) era apresentada como a chave de tudo:
`LD A, 10` coloca o número 10 na gaveta A.
`LD B, A` copia o valor contido em A diretamente para a gaveta B.

---

### Os Portais para o Mundo Exterior: IN e OUT

O diário técnico avançava mostrando como o chip se conecta aos dispositivos externos.
Havia setas desenhadas da CPU até caixas escritas "Gravador", "Teclado" e "Alto-falante".
Alex Senior explicava como transpor a barreira do silício para interagir com o mundo físico.

> “O processador precisa agir sobre o exterior. No Z80, essa ponte física é feita por duas instruções mágicas: IN (Entrar) e OUT (Sair). Elas abrem portas físicas de comunicação elétrica.”

> “Se você quer emitir um som, usa OUT (254), A. Isso descarrega o byte do acumulador na porta física 254 conectada ao falante. Para ler o teclado, IN A, (254) traz o nível elétrico dos botões direto para o acumulador.”

Alex moderno olhou para o monitor, vendo a telemetria do robô autônomo AMR operando no corredor.
O script complexo calculava as distâncias usando o tempo de retorno da luz do laser do LiDAR.
No final da linha de processamento do robô moderno de 2026, a ação elétrica era idêntica à de 1986.

Para frear o robô diante de uma viga irregular, a placa executava uma operação de baixo nível.
Enviava bits na porta lógica correspondente ao driver dos motores, cortando a corrente de acionamento.
Toda a complexidade de ROS 2 e robótica repousava em cascata sobre instruções fundamentais de entrada e saída.

Para demonstrar a lógica, o diário apresentava este bloco curto em Assembly do Z80:
```assembly
; Loop simples para ler o teclado e alterar o som
LEITURA:
    IN A, (254)    ; Lê a porta de I/O 254 (teclado)
    LD B, A        ; Salva o estado lido na gaveta B
    OUT (254), A   ; Envia o mesmo valor para a porta de som
    JP LEITURA     ; Pula de volta para o início (Loop)
```

A poeira vermelha da estrada de Cascavel e os robôs de última geração dividiam os mesmos princípios básicos.
A leitura do caderno fornecia a base que faltava à engenharia puramente abstrata da faculdade.
Alex se ajeitou no posto de monitoramento, pronto para avançar para a lógica numérica dos bits.

---

### 🧠 O que você aprendeu aqui
- **Registradores**: São gavetas internas de memória ultrarrápida do processador. No Z80, operam com dados de 8 bits (números de 0 a 255).
- **Instruções de Controle**: `LD` carrega e move informações, enquanto `IN` e `OUT` fazem a interface física direta com os periféricos externos.

### 🎮 Desafio prático
**O Desenho do Fluxo dos Bits**  
Desenhe a gaveta do Acumulador A e a gaveta auxiliar B. Indique graficamente para onde o dado flui ao executar sequencialmente as instruções `LD A, 5` e `LD B, A`.

### ✨ Conexão com o próximo capítulo
Agora que conhecemos os compartimentos onde o Z80 manipula os bytes, precisamos desvendar como esses números se estruturam por dentro. No próximo capítulo, vamos decifrar a lógica binária e hexadecimal, aprendendo a ler e traduzir as combinações numéricas básicas que governam as decisões lógicas das máquinas.

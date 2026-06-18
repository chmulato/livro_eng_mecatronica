# Capítulo 9: A Pilha de Código Moderna

Com a chave Allen, Alex moderno apertou o último parafuso da tampa lateral do AMR 12.
O torque metálico indicou que o invólucro de proteção do robô estava lacrado.
Ele abriu a conexão ssh em seu tablet de diagnóstico para checar os processos internos.

Uma cascata de identificadores se desenrolou no console preto do Linux embutido.
O robô gerenciava simultaneamente tarefas escritas em linguagens diferentes.
Como o silício unificava esses mundos sem travar ou entrar em colapso técnico?

> “Na mecatrônica de alta performance, não existe uma única linguagem salvadora,” dizia o diário.
> “Nós dividimos o trabalho do robô seguindo a lógica do corpo humano.
> Separamos entre os músculos de ação reflexa rápida e a mente de planejamento lento.”

> “Para os reflexos e músculos da máquina, nós usamos C++.
> Ele roda direto no metal do chip, calculando o Filtro de Kalman em microssegundos.
> Se o LiDAR detectar um obstáculo próximo, o código em C++ freia as rodas na hora.”

Para a estratégia de rota e a inteligência de negócios, a equipe utilizava o Python.
Python é uma linguagem interpretada, mais lenta, mas excelente para regras complexas.
Ela conecta o robô à nuvem do armazém e gerencia a prioridade de entrega do palete.

---

### [Conceito Chave] O Maestro da Orquestra: ROS 2

Para fazer o sistema em C++ e a mente em Python cooperarem, usa-se o ROS 2.
O Robot Operating System funciona como um middleware de comunicação de dados.
Ele conecta programas independentes que rodam de forma concorrente, chamados Nós.

Imagine um canal de rádio corporativo operando em tópicos de publicação e assinatura.
O nó do sensor LiDAR publica as distâncias físicas em um canal chamado `/scan`.
O nó de processamento assina esse canal, trata o ruído e publica a posição real em `/odom`.

O nó estratégico assina `/odom` e decide os comandos de movimentação das rodas.
Os nós funcionam de maneira autônoma, trocando mensagens estruturadas pela rede local.
Abaixo, o modelo de código demonstra a criação desse nó em Python:

```python
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class PublicadorVelocidade(Node):
    def __init__(self):
        super().__init__('publicador_cmd_vel')
        self.publicador = self.create_publisher(Twist, 'cmd_vel', 10)
        self.timer = self.create_timer(0.5, self.enviar_comando)

    def enviar_comando(self):
        msg = Twist()
        msg.linear.x = 0.5  # Velocidade linear
        msg.angular.z = 0.1 # Rotação angular
        self.publicador.publish(msg)
```

E o receptor de reflexo rápido, compilado em C++, recebe os comandos e atua nos motores:

```cpp
#include "rclcpp/rclcpp.hpp"
#include "geometry_msgs/msg/twist.hpp"

class ReceptorVelocidade : public rclcpp::Node {
public:
    ReceptorVelocidade() : Node("receptor_cmd_vel") {
        assinatura_ = this->create_subscription<geometry_msgs::msg::Twist>(
            "cmd_vel", 10, std::bind(&ReceptorVelocidade::callback_velocidade, this, std::placeholders::_1));
    }
private:
    void callback_velocidade(const geometry_msgs::msg::Twist::SharedPtr msg) const {
        double vel = msg->linear.x;
        // Atuação física no driver do motor
    }
    rclcpp::Subscription<geometry_msgs::msg::Twist>::SharedPtr assinatura_;
};
```

Alex observou os logs provando a perfeita comunicação concorrente dos dois nós.
Ele aprendeu como a arquitetura do robô se organizava em processos paralelos.
Agora, precisava aplicar essa troca de dados para resolver o empilhamento das caixas.

---

### 🧠 O que você aprendeu aqui
- **Middleware (ROS 2)**: Um framework de software que gerencia a troca de mensagens em tópicos entre processos independentes chamados nós.
- **Divisão C++/Python**: C++ cuida de reflexos e controle de hardware rápido, enquanto Python planeja caminhos e lógicas complexas.

### 🎮 Desafio prático
**A Criação do Tópico**  
Desenhe o diagrama de fluxo de dados mostrando o caminho da mensagem desde o sensor LiDAR físico até a atuação na roda, indicando os nós e nomes dos tópicos intermediários.

### ✨ Conexão com o próximo capítulo
A comunicação de mensagens unifica a percepção e a atuação do robô no espaço físico. No próximo capítulo, utilizaremos essa infraestrutura de comunicação para aplicar a equação clássica de alocação de carga e otimizar a arrumação dos paletes no galpão.

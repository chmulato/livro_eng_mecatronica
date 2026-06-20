# Capítulo 10: A Equação do Almoxarifado

As caixas aguardavam a decisão de encaixe na doca de Curitiba. Alex moderno observou o robô AMR 12 desacelerar suavemente no Setor B. Em cima do compartimento de carga da máquina, repousavam três caixas de papelão de tamanhos diferentes contendo rolamentos, eixos e sensores.

O robô precisava decidir em quais nichos vazios colocaria cada volume.
A decisão devia ser tomada em frações de segundo para otimizar o espaço livre.
Para entender essa lógica de controle, Alex abriu o diário de seu mentor.

Para acelerar a triagem e evitar o travamento dos microprocessadores, o diário apresentava o limite combinatório.

Se você tentar calcular todas as combinações de empilhamento de caixas, a matemática explode.
O número de combinações possíveis cresce de forma fatorial com novos itens.
O computador mais potente do mundo levaria séculos processando o cálculo.
Chamamos isso de problema NP-difícil; o tempo de cálculo é o inimigo real.

Calcular todas as combinações era como tentar organizar um armário enquanto alguém jogava roupas infinitas pela porta.

> “Para resolver isso sem travar a CPU, nós usamos Heurísticas.
> Heurísticas são atalhos lógicos práticos baseados no bom senso matemático.
> Elas oferecem respostas excelentes em frações de microssegundo.”

A lógica do algoritmo baseia-se em uma analogia comum de arrumação de bagagem.

### [Conceito Chave] A Heurística First-Fit Decreasing (FFD)

Ao arrumar uma mala de viagem, você não joga itens aleatoriamente pelo espaço.
A regra clássica manda ordenar os volumes por tamanho, do maior para o menor.
Acomodamos as peças maiores primeiro no fundo para preencher o volume principal.

Os itens menores e flexíveis (como meias) ficam por último para ocupar as frestas.
O algoritmo do AMR ordenou as três caixas recebidas em sua malha lógica.
Colocou a maior de rolamentos no fundo e a menor de sensores no vão restante.

Ele calculou a eficiência volumétrica por álgebra linear em tempo real:
```python
# Algoritmo First-Fit Decreasing (FFD) Simplificado
def otimizar_alocacao(itens, capacidade_nicho=100):
    itens_ordenados = sorted(itens, reverse=True)
    nichos = [capacidade_nicho]
    alocacao = []

    for item in itens_ordenados:
        alocado = False
        for i in range(len(nichos)):
            if nichos[i] >= item:
                nichos[i] -= item
                alocacao.append((item, f"Nicho {i+1}"))
                alocado = True
                break
        if not alocado:
            nichos.append(capacidade_nicho - item)
            alocacao.append((item, f"Nicho {len(nichos)}"))
    return alocacao, nichos
```

O robô alocou os itens em milissegundos sem congelar em cálculos infinitos.
A engenharia mecatrônica física estava toda ali, rodando sob seus olhos.
Mas Alex começou a refletir sobre o impacto social daquela eficiência mecânica.

---

### A Riqueza Oculta sob as Prateleiras de Aço

Toda aquela matemática brilhante servia para enriquecer fundos de investimento.
Bianchi e os investidores da Faria Lima viam o galpão como vetor de juros.
Mas para os trabalhadores reais do local, a automação gerava apenas mais pressa.

Os entregadores de aplicativo corriam de moto sob a neblina e perigo constantes.
Havia um muro invisível de desigualdade que a mecatrônica não resolvia sozinha.
E era sobre essa fronteira social que a Parte IV do diário começaria a falar.

---

### 🧠 O que você aprendeu aqui
- **Problemas NP-Difíceis**: Questões cujo número de combinações cresce de forma fatorial, tornando inviável o cálculo perfeito em tempo real.
- **Heurística FFD**: Algoritmo de primeiro encaixe decrescente que ordena itens do maior para o menor para otimizar a alocação de espaço.

### 🎮 Desafio prático
**O Algoritmo de Encaixe**  
Escreva o teste manual do algoritmo FFD para acomodar caixas de tamanhos [50, 20, 30, 40, 10] em nichos com capacidade máxima de 60 unidades cada.

### ✨ Pergunta-gancho para o próximo capítulo
A otimização das caixas preenchia as prateleiras do galpão logístico de forma eficiente. Mas o que acontece quando a barreira para o avanço da tecnologia não é um limite de hardware, mas o custo financeiro imposto pela própria economia? Como a taxa básica de juros e a rentabilidade passiva afetam a mecatrônica real e travam os engenheiros nacionais? É esse o choque de realidade que Alex investigará a seguir.

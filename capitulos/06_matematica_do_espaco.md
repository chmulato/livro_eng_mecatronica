# Capítulo 6: A Matemática do Espaço

O aquecedor barulhento da sala de controle tentava combater o frio em Milão.
Ao lado do terminal antigo de fósforo verde, o café de Alex Senior esfriara.
Seus olhos estavam fixos na planta baixa industrial impressa sobre a mesa de fórmica.

O galpão de armazenamento estava saturado em 2001.
Noventa por cento da capacidade nominal física do galpão já havia sido ocupada.
A diretoria italiana exigia estocar mais dez por cento de carga sem ampliar o espaço físico.

A solução lógica do problema não estava no aço das prateleiras, mas no código.
Ele precisava programar o terminal para otimizar cada centímetro livre no local.
Era necessário converter os paletes físicos em representações lógicas na CPU.

Para estruturar a movimentação tridimensional, o diário trazia a formulação das matrizes espaciais.

> “O mundo físico parece contínuo e caótico,” registrava o diário técnico.
> “But para controlá-lo de forma digital, precisamos mapeá-lo como um tabuleiro tridimensional.
> As imensas prateleiras de aço não passam de uma grande Matriz Tridimensional de dados.”

> “Mapeamos cada nicho de armazenagem usando coordenadas espaciais ortogonais.
> Definimos os eixos de coluna (X), profundidade (Y) e altura (Z).
> Qualquer posição física é expressa por um vetor de posição $\vec{P} = [x, y, z]$.”

Para mover o transelevador mecânico, a máquina precisava ler essa álgebra linear.

### [Conceito Chave] A Matriz Booleana de Ocupação

O sistema gerenciava a ocupação das prateleiras usando matrizes de bits.
Se um bloco do espaço estivesse ocupado por carga, seu valor na matriz era um (`1`).
Se o espaço estivesse livre e desocupado, o valor binário correspondente era zero (`0`).

Para alocar um novo palete de dimensões $L \times C \times A$, o sistema validava o volume.
Multiplicava-se logicamente a submatriz tridimensional das coordenadas desejadas.
Se qualquer bit retornasse um (`1`), o movimento era abortado para evitar colisão física.

O grande desafio de Alex Senior era resolver o aproveitamento de volumes fracionados.
Empacotar caixas pequenas sem deixar vãos vazios exigia cálculos combinatórios complexos.
Volume geométrico bruto é diferente do volume utilizável pela cinemática da máquina.

---

### O Quebra-Cabeças de Três Eixos: O Bin Packing Problem em 2026

O frio cortante do inverno italiano de 2001 e o barulho de seus transelevadores de carga se dissiparam sob a névoa úmida, abrindo espaço para a claridade cinza do amanhecer de Curitiba em 2026.

Alex moderno abriu o terminal de testes em seu tablet de manutenção em Curitiba.
Ele observou os robôs AMRs movendo cargas pesadas de forma autônoma pelas docas.
Os robôs dependiam de um serviço em nuvem para resolver o *3D Bin Packing*.

Ele relembrou a equação fundamental que media a eficiência de alocação de itens:
$$Efe = \left( \frac{\sum_{i=1}^{n} V_{item\_i}}{V_{total}} \right) \times 100\%$$

Diferente da física escolar teórica, na mecatrônica as restrições geométricas são rígidas.
As caixas reais não se comportam como líquidos maleáveis que preenchem vazios.
Alex digitou uma função heurística em Python para demonstrar essa validação espacial:

```python
# Validação de posicionamento tridimensional (First Fit Heuristic)
def verificar_colisao(pos_nova, dim_nova, pos_existentes, dim_existentes):
    x_new, y_new, z_new = pos_nova
    w_new, l_new, h_new = dim_nova
    
    for (x, y, z), (w, l, h) in zip(pos_existentes, dim_existentes):
        # Verifica sobreposição nos três eixos ortogonais simultaneamente
        if (x_new < x + w and x_new + w_new > x and
            y_new < y + l and y_new + l_new > y and
            z_new < z + h and z_new + h_new > z):
            return True # Colisão detectada!
    return False # Espaço livre
```

A lógica mantinha os atuadores e sensores operando em perfeita harmonia mecânica.
O plantão da madrugada terminava ali, sob as primeiras luzes da manhã.
Ele recolheu o diário amarelado e guardou o chip Z80A de forma segura na mochila.

---

### 🧠 O que você aprendeu aqui
- **Vetores Espaciais**: Posições físicas tridimensionais são descritas por coordenadas lineares de eixos ortogonais $[x, y, z]$.
- **Algoritmo de Colisão**: A verificação geométrica impede a alocação de volumes coincidentes no mesmo espaço de hardware.

### 🎮 Desafio prático
**A Otimização de Caixas**  
Implemente o cálculo manual da eficiência volumétrica ($Efe$) para um palete de volume 1m³ contendo exatamente 4 caixas retangulares de dimensões 40x50x30 cm.

### ✨ Conexão com o próximo capítulo
Com a matemática do espaço consolidada na mente, Alex precisará lidar com robôs em movimento constante. No próximo capítulo, entraremos na Parte III do livro para compreender as "Formigas Elétricas": a dinâmica operacional do CD moderno de Curitiba em 2026 e o controle de robôs autônomos simultâneos.

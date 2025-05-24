"""
1- Área da circunferência
A fórmula para calcular a área de uma circunferência é: área = π ×raio2. 
Considerando para
este problema que π = 3.14159265:
• Efetue o cálculo da área, elevando o valor de raio ao 
quadrado e multiplicando por π.
**Entrada:** A entrada contém um valor de ponto flutuante
 (dupla precisão), no caso, a variávelraio.
**Saída:** Apresente a mensagem "A=" seguido pelo 
valor da variável area, conforme exemplo
abaixo, com 4 casas após o ponto decimal.
Utilize variáveis de dupla precisão (double). Como em todos os 
problemas, não esqueça de imprimir o fim de linha após o 
resultado, caso contrário, você receberá "Presentation Error"
"""

# Definir o valor de π
pi = 3.14159265

# Solicitar dados do usuário
raio = float(input("Insira o valor do raio: "))

# Calcular a área do circulo
area = pi * (raio ** 2)

# Exibir o resultado 
print(f"A= {area:.4f}")
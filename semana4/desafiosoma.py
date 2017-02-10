#desafio
#O desafio é o seguinte, dado número inteiro, deve calcular qual a soma os numeros adjacentes
#exemplo: input 12345 = 15
#exemplo: input 12234 = 12

entrada = int(input("Entre com um valor "))

total = 0
# valoranterior = 0
atual = 0
possui = True

while entrada > 0:
    atual = entrada % 10

    restodivisao = entrada % 10
    entrada = entrada // 10
    total += restodivisao
    print("entrada",entrada,"soma resto da divisao",restodivisao,"soma do resto",total)

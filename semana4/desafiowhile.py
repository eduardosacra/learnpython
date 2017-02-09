#desafio
#digitando um valor inteir realizar a soma dos numeros que compoem o numero digitando
#exemplo: input 432 então 4+3+2 = 9

entrada = int(input("Entre com um valor "))

restodivisao = 0
total = 0

while entrada > 0:
    restodivisao = entrada % 10
    entrada = entrada // 10
    total += restodivisao
    print("entrada",entrada,"soma resto da divisao",restodivisao,"soma do resto",total)

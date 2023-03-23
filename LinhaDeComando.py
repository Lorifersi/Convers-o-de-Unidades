from Calculos import converterStringParaFloat, bitParaByte, byteParaBit, byteParakiloByte, kilobyteParaByte, kilobyteParamegaByte, megabyteParakiloByte, megabyteParagigaByte, gigabyteParamegaByte, gigabyteParateraByte, terabyteParagigaByte, terabyteParapetaByte, petabyteParateraByte

print(' -Escreva 1 para bitParaByte \n -Escreva 2 para byteParaBit \n -Escreva 3 para byteParakiloByte \n -Escreva 4 para kilobyteParaByte \n -Escreva 5 para kilobyteParamegaByte \n -Escreva 6 para  megabyteParakiloByte \n -Escreva 7 para megabyteParagigaByte \n -Escreva 8 para gigabyteParamegaByte \n -Escreva 9 para gigabyteParateraByte \n -Escreva 10 para terabyteParagigaByte \n -Escreva 11 para terabyteParapetaByte \n -Escreva 12 para petabyteParateraByte')
funcEscolha = input()
if(funcEscolha == '1'):
    print('Você escolheu a opção 1')
    entradaDoTecladoValorASerConvertido = converterStringParaFloat(input())
    valorConvertido = bitParaByte (entradaDoTecladoValorASerConvertido)
    print(valorConvertido)

elif(funcEscolha == '2'):
    print('Você escolheu a opção 2')
    entradaDoTecladoValorASerConvertido = converterStringParaFloat (input())
    valorConvertido = byteParaBit (entradaDoTecladoValorASerConvertido)
    print(valorConvertido)

elif(funcEscolha == '3'):
    print('Você escolheu a opção 3')
    entradaDoTecladoValorASerConvertido = converterStringParaFloat (input())
    valorConvertido = byteParakiloByte (entradaDoTecladoValorASerConvertido)
    print(valorConvertido)

elif(funcEscolha == '4'):
    print('Você escolheu a opção 4')
    entradaDoTecladoValorASerConvertido = converterStringParaFloat (input())
    valorConvertido = kilobyteParaByte (entradaDoTecladoValorASerConvertido)
    print(valorConvertido)

elif(funcEscolha == '5'):
    print('Você escolheu a opção 5')
    entradaDoTecladoValorASerConvertido = converterStringParaFloat (input())
    valorConvertido = kilobyteParamegaByte (entradaDoTecladoValorASerConvertido)
    print(valorConvertido)

elif(funcEscolha == '6'):
    print('Você escolheu a opção 6')
    entradaDoTecladoValorASerConvertido = converterStringParaFloat (input())
    valorConvertido = megabyteParakiloByte (entradaDoTecladoValorASerConvertido)
    print(valorConvertido)

elif(funcEscolha == '7'):
    print('Você escolheu a opção 7')
    entradaDoTecladoValorASerConvertido = converterStringParaFloat (input())
    valorConvertido = megabyteParagigaByte (entradaDoTecladoValorASerConvertido)
    print(valorConvertido)

elif(funcEscolha == '8'):
    print('Você escolheu a opção 8')
    entradaDoTecladoValorASerConvertido = converterStringParaFloat (input())
    valorConvertido = gigabyteParamegaByte (entradaDoTecladoValorASerConvertido)
    print(valorConvertido)

elif(funcEscolha == '9'):
    print('Você escolheu a opção 9')
    entradaDoTecladoValorASerConvertido = converterStringParaFloat (input())
    valorConvertido = gigabyteParateraByte (entradaDoTecladoValorASerConvertido)
    print(valorConvertido)

elif(funcEscolha == '10'):
    print('Você escolheu a opção 10')
    entradaDoTecladoValorASerConvertido = converterStringParaFloat (input())
    valorConvertido = terabyteParagigaByte (entradaDoTecladoValorASerConvertido)
    print(valorConvertido)

elif(funcEscolha == '11'):
    print('Você escolheu a opção 11')
    entradaDoTecladoValorASerConvertido = converterStringParaFloat (input())
    valorConvertido = terabyteParapetaByte (entradaDoTecladoValorASerConvertido)
    print(valorConvertido)

elif(funcEscolha == '12'):
    print('Você escolheu a opção 12')
    entradaDoTecladoValorASerConvertido = converterStringParaFloat (input())
    valorConvertido = petabyteParateraByte (entradaDoTecladoValorASerConvertido)
    print(valorConvertido)
# O jogo consiste em resolver problemas matemáticos para ganhar.
print("Bem vindo! O jogo consiste em fazer cálculos matemáticos para sua sobrevivência, caso você erre uma questão, você perde, contudo, você poderá responder as outras questões caso o caminho que você tenha escolhido tenha mais de uma questão.")
jogador = str(input("Diga seu nickname\n")).strip()
print("Seja Bem Vindo {}".format(jogador))
print("Você está em um avião sobrevoando o Oceano Atlântico quando de repente os aparelhos de detecção do avião começam a falhar, você olha pelo radar e percebe que está em cima do Triangulo das Bermudas. Para que você sobreviva, você terá de fazer algumas tarefas de cálculo para estabilizar os aparelhos e o avião. Neste exato momento, você está no fundo do avião e precisa se salvar, a direita temos a primeira classe um caminho mais curto, porém mais difícil, a esquerda temos a executiva, um caminho intermediário, a frente tem a econômica, um caminho com desafios mais fáceis porém estes irão ficar mais difíceis com o tempo e atrás de você temos a porta do avião com um paraquedas, você pode saltar e se salvar, mas primeiramente irá responder a questão mais trabalhosa do jogo. Se você erra uma questão você perde mas poderá fazer as outras questões normalmente. Depois de escolher um caminho, não terá volta. Escolha com Sabedoria!.")
questaoInicial = str(input('Qual caminho você escolhe? Siga, Volte, Direita ou Esquerda?\n'))
siga = ("Siga")
volte = ("Volte") 
esquerda = ("Esquerda")
direita = ("Direita")
if questaoInicial == siga: #As 4 Questões do Siga
    questao1Siga = input(('Quanto é o Quintuplo de 3?\n'))
    resposta1Siga = ('15')
    if questao1Siga == resposta1Siga: #Questão 1
        print('Certo!')
    else:
        print('Você Errou!')
    questao2Siga = input(('Quanto é a raiz quadrada de 1024?\n'))
    resposta2Siga = ('32')
    if questao2Siga == resposta2Siga: #Questão 2
        print('Correto! Mais duas questões e você ganha o jogo')
    else:
        print('Você Errou!')
    questao3Siga = input('Qual a derivada de f(x) = x³ + 1000?\n')
    resposta3Siga = ('3x2')
    if questao3Siga == resposta3Siga: #Questão 3
        print('Correto!! Mais uma questão e você ganha')
    else:
        print('Você Errou!')
    questao4Siga = input('Em uma panificadora são produzidos 90 pães de 15 gramas cada um. Caso queira produzir pães de 10 gramas, quantos iremos obter?\n')
    resposta4Siga = ('135')
    if questao4Siga == resposta4Siga: #Questão 4
        print('Correto!')
    else:
        print("Você Errou!")
    if questao1Siga != resposta1Siga or questao2Siga != resposta2Siga or questao3Siga != resposta3Siga or questao4Siga != resposta4Siga:
        print('Como você errou uma das questões ou todas, você perdeu {}!'.format(jogador))
    if questao1Siga == resposta1Siga and questao2Siga == resposta2Siga and questao3Siga == resposta3Siga and questao4Siga == resposta4Siga:
        print('Parabéns, você acertou todas as questões e estabilizou o avião!')
        print('{} venceu o jogo'.format(jogador))
if questaoInicial == esquerda: #As 3 Questões da Esquerda
    questao1Esquerda = input('Se 6 impressoras iguais produzem 1000 panfletos em 40 minutos, em quanto tempo 3 dessas impressoras produziriam 2000 desses panfletos?\n')
    resposta1Esquerda = ('160')
    if questao1Esquerda == resposta1Esquerda: #Questão 1
        print('Certo!')
    else:
        print('Você Errou!')
    questao2Esquerda = input('Qual a derivada de f(x) = 3x-1?\n')
    resposta2Esquerda = ('3')
    if questao2Esquerda == resposta2Esquerda: #Questão 1
        print('Correto! Mais uma questão e você vence!')
    else:
        print('Você Errou!')
    questao3Esquerda = input('Uma indústria produz um tipo de máquina que demanda a ação de grupos de funcionários no preparo para o despacho ao cliente. Um grupo de 20 funcionários prepara o despacho de 150 máquinas em 45 dias. Para preparar o despacho de 275 máquinas, essa indústria designou 30 funcionários. O número de dias gastos por esses 30 funcionários para preparem essas 275 máquinas é igual a?\n')
    resposta3Esquerda = ('55')
    if questao3Esquerda == resposta3Esquerda: #Questão 3
        print('Correto!')
    else: 
        print('Você Errou!')
    if questao1Esquerda != resposta1Esquerda or questao2Esquerda != resposta2Esquerda or questao3Esquerda != resposta3Esquerda:
        print('Como você errou uma das questões ou todas, você perdeu {}!'.format(jogador))
    if questao1Esquerda == resposta1Esquerda and questao2Esquerda == resposta2Esquerda and questao3Esquerda == resposta3Esquerda:
        print('Parabéns, você acertou todas as questões e estabilizou o avião!')
        print('{} venceu o jogo!!!'.format(jogador))
if questaoInicial == direita: #As 2 Questões da Direita 
    questao1Direita = input('Uma empresa investiu 3,42 bilhões de reais na construção de uma rodovia. Perto do final da construção a empresa solicitou uma verba adicional de 7% do valor investido para terminar a obra. Sabe-se que três oitavos desse valor adicional estavam destinados ao pagamento de fornecedores e equivalem, em reais, a?\n')
    resposta1Direita = ('89775000')
    if questao1Direita == resposta1Direita: #Questão 1
        print('Certo!')
    else:
        print('Você Errou!')    
    questao2Direita = input('Numa área retangular com 60 metros de comprimento por 40 metros de largura, podem ser construídas quantas casas de 30 m2 ?\n')
    resposta2Direita = ('80')
    if questao2Direita == resposta2Direita: #Questão 2
        print('Correto!')
    else:
        print('Você Errou!')
    if questao1Direita != resposta1Direita or questao2Direita != resposta2Direita:
        print('Como você errou uma das questões ou todas, você perdeu {}!'.format(jogador))
    if questao1Direita == resposta1Direita and questao2Direita == resposta2Direita:
        print('Parabéns, você acertou todas as questões e estabilizou o avião!')
        print('{} venceu o jogo!!!'.format(jogador))
if questaoInicial == volte: #A Questão Volte
    questaoVolte = input(('Uma quantia foi aplicada a juros simples de 6% ao mês, durante 5 meses e, em seguida, o montante foi aplicado durante mais 5 meses, a juros simples de 4% ao mês. No final dos 10 meses, o novo montante foi de R$ 234,00. Qual o valor da quantia aplicada inicialmente? \n'))
    respostaVolte = ('12250')
    if questaoVolte == respostaVolte:
        print('Correto!!')
        print('Parabéns, você acertou a questão e pulou do avião com o paraquedas!')
        print('{} venceu o jogo!!!'.format(jogador))
    else:
        print('Você Errou!')
    if questaoVolte != respostaVolte:
        print('Você Perdeu {}!'.format(jogador))




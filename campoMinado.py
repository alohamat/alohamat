quant = int(input())
tabuleiro = [int(input()) for x in range(quant)]    # um array para representar o tabuleiro
minas = [0] * quant     # outro array do tamanho do primeiro

for x in range(quant):
    if x > 0:
        minas[x] += tabuleiro[x - 1] # testa a casa à esquerda
        
    minas[x] += tabuleiro[x] # testa a prórpia casa
    
    if x < quant - 1:
        minas[x] += tabuleiro[x + 1] # testa a casa à direita

for y in minas:
    print(y)
# A comparação NÃO é feita pelos 'if' e sim pelos operadores dos índices

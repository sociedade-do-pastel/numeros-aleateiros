
def leitura_arquivos():
    lista_senha = []
    contador = 1
    with open('Chaves de Criptografia 2022.S1.txt') as senhas:
        for line in senhas:
            line = line.strip().replace("'","")
            lista_senha.append(line)
            print(contador, end = "\r")
            contador +=1
    return lista_senha
    
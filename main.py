def parse_keys(keys):
    b = []
    for chave in keys:
        chave2 = chave.replace("'", "").replace("\n", "")
        if chave2 == "" or chave2 == "\n": continue
        b.append(chave2)

    c = []
    for chave in b:
        chave2 = bin(int(f'{chave}', 16))[2:]
        if len(chave2) == 19999: chave2 = '0'+chave2
        c.append(chave2)
    
    return c

def monobit_test(b):
    contador = 0

    for bit in b:
        if bit == '1': contador += 1

    if contador > 9654 and contador < 10346:
        return True

    return False

def poker_test(b):
    nibbles = [b[i:i+4] for i in range(0, len(b), 4)]
    contador = dict()

    for nibble in nibbles:
        if nibble in contador: contador[nibble] += 1
        else: contador[nibble] = 1

    somatoria = 0
    for i in contador.values():
        somatoria += i**2

    x = (16/5000) * (somatoria) - 5000

    if x > 1.03 and x < 57.4:
        return True
    
    return False

def runs_test(b):
    tabela = {
        1: {'inicio': 2267, 'fim': 2733},
        2: {'inicio': 1079, 'fim': 1421},
        3: {'inicio': 502, 'fim': 748},
        4: {'inicio': 223, 'fim': 402},
        5: {'inicio': 90, 'fim': 223},
        6: {'inicio': 90, 'fim': 223}
    }

    contador = {
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0
    }

    ult = chave[0]
    i = 1
    for bit in chave[1:]:
        if bit == ult:
            i += 1
        else:
            if i > 6: contador[6] += 1
            else: contador[i] += 1                
            i = 1
            ult = bit
    
    if i > 6: contador[6] += 1
    else: contador[i] += 1   
    
    for idx, val in contador.items():
        if val < tabela[idx]['inicio'] or val > tabela[idx]['fim']: return False
    
    return True

def long_run_test(b):
    ult = b[0]
    contador = 1
    for bit in b[1:]:
        if bit == ult: 
            contador += 1
            contador += 1
            if contador >= 34: return False
        else: 
            ult = bit
            contador = 1
    if contador >= 34: return False
    return True            

with open('Chaves de Criptografia 2022.S1.txt', 'r') as arquivo:
    seq_bits = parse_keys(arquivo.readlines())

    for idx, chave in enumerate(seq_bits):
        print(f'chave={idx+1}')
        print(f'monobit={monobit_test(chave)}')
        print(f'poker_test={poker_test(chave)}')
        print(f'runs={runs_test(chave)}')
        print(f'long_run={long_run_test(chave)}')
        print('-'*45)
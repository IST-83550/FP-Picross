# IST - FUNDAMENTOS PROGRAMACAO - 2015/2016
# GRUPO 6 - Afonso Feijao 83418 e Pedro Santos 83550
"""-----------------------------------------------------------------------------
                                TAD COORDENADA
                                
Representacao interna de coordenada: Tuplo                                
-----------------------------------------------------------------------------"""
def cria_coordenada(l,c):
    """CONSTRUTOR
    Esta funcao recebe dois argumentos inteiros e positivos e devolve o tuplo.
    O primeiro numero corresponde a linha e o segundo a coluna."""
    if isinstance(l, int) and l > 0 and isinstance(c, int) and c > 0:
        #verifica se os argumentos sao inteiros e positivos
        return (l,c)
    else:
        raise ValueError ("cria_coordenada: argumentos invalidos")
    
def e_coordenada(univ):
    """RECONHECEDOR
    Esta funcao recebe um argumento e devolve o valor logico True se for coordenada"""
    if isinstance(univ, tuple) and len(univ) == 2:
        if isinstance(univ[0], int) and univ[0] > 0 and \
           isinstance(univ[1], int) and univ[1] > 0:
            #verifica se o input e um tuplo, se apenas tem 2 elementos
            #se ambos os elementos sao inteiros e positivos
            return True
    return False
    
def coordenada_linha(coor):
    """SELETOR
    Esta funcao recebe um argumento do tipo coordenada e devolve a linha respetiva"""
    if e_coordenada(coor):
        return coor[0]
    
def coordenada_coluna(coor):
    """SELETOR
    Esta funcao recebe um argumento do tipo coordenada e devolve a coluna respetiva"""
    if e_coordenada(coor):
        return coor[1]
    
def coordenadas_iguais(c1, c2):
    """TESTE
    Esta funcao recebe dois argumentos do tipo coordenada e devolve True se 
    as coordenadas corresponderem a mesma celula do tabuleiro"""
    return e_coordenada(c1) and e_coordenada(c2) and \
       coordenada_linha(c1) == coordenada_linha(c2) and \
       coordenada_coluna(c1) == coordenada_coluna(c2)
    
def coordenada_para_cadeia(coor):
    """Esta funcao recebe um argumento do tipo coordenada e devolve uma cadeia
    de caracteres"""
    if not e_coordenada(coor):
        return False
    return "(" + str(coordenada_linha(coor)) + " : " + str(coordenada_coluna(coor)) + ")"

def cadeia_para_coordenada(cad):
    """Esta funcao recebe uma cadeia de caracteres e devolve um elemento do tipo
       coordenada"""
    coord = ["",""]
    indice = 0
    for car in cad:
        if car != "(" and car != " " and car != ")":
            if car == ":":
                indice = 1
            else:
                coord[indice] = coord[indice] + car
    return cria_coordenada(eval(coord[0]), eval(coord[1]))

"""-----------------------------------------------------------------------------
                                  TAD TABULEIRO
                     
Representacao interna de tabuleiro: Lista
-----------------------------------------------------------------------------"""
def cria_tabuleiro(t): 
    """CONSTRUTOR
    Esta funcao recebe um tuplo e devolve uma lista(representacao interna)"""
    if cria_tabuleiro_aux(t):
        num_linhas = len(t[0])
        num_colunas = len(t[1])
        tabuleiro = [list(t[0])] + [list(t[1])]
        row = []
        for i in range(num_linhas):
            row = row + [0]
        for i in range(num_colunas):
            tabuleiro = tabuleiro + [list(row)]    
        return tabuleiro
    
def cria_tabuleiro_aux(t):
    """FUNCAO AUXILIAR
        Esta funcao verifica a validade dos argumentos"""    
    if isinstance(t, tuple) and len(t) == 2 and\
       isinstance(t[0], tuple) and isinstance(t[1], tuple):
        #verifica se o input e um tuplo, se apenas tem 2 elementos
        #se os elementos sao tuplos
        comp_tup_l = len(t[0])
        comp_tup_c = len(t[1])
        for e in t[0]:
            if isinstance(e, tuple):
                soma = 0
                for a in e:
                    soma = soma + a
                    if isinstance(a, int) and soma <= comp_tup_c:
        #verifica se o que esta dentro do primeiro tuplo e tuplo e se o que esta dentro
        #desse tuplo e inteiro
        #verifica se a soma dos inteiros em cada tuplo e menor ou igual ao numero
        #de colunas
                        valido = True                        
                    else:
                        raise ValueError('cria_tabuleiro: argumentos invalidos')
            else:
                raise ValueError('cria_tabuleiro: argumentos invalidos')
        for e in t[1]:
            if isinstance(e, tuple):
                soma = 0
                comp_tup = len(e)
                for a in e:
                    soma = soma + a
                    if isinstance(a, int) and soma <= comp_tup_l:
        #verifica se o que esta dentro do segundo tuplo e tuplo e se o que esta dentro
        #desse tuplo e inteiro
        #verifica se a soma dos inteiros em cada tuplo e menor ou igual ao numero
        #de linhas        
                        valido = True                        
                    else:
                        raise ValueError('cria_tabuleiro: argumentos invalidos')        
    else:
        raise ValueError('cria_tabuleiro: argumentos invalidos')
    return valido
    
def tabuleiro_dimensoes(t):
    """SELETOR
    Esta funcao recebe uma lista (tabuleiro) e devolve um tuplo com dimennsao 
    da linha e da coluna respetivamente"""
    if e_tabuleiro(t):
        num_linhas = len(t[0])
        num_colunas = len(t[1])
        return (num_linhas, num_colunas)

def tabuleiro_especificacoes(t):
    """SELETOR
    Esta funcao recebe uma lista(tabuleiro) e devolve um tuplo de dois tuplos"""
    if e_tabuleiro(t):
        return (tuple(t[0]), tuple(t[1]))

def tabuleiro_celula(t, c):
    """SELETOR
    Esta funcao recebe uma lista (tabuleiro) e devolve um tuplo com a linha e
    a coluna respetivamente"""
    if e_tabuleiro(t) and e_coordenada(c) and\
       coordenada_linha(c) <= tabuleiro_dimensoes(t)[0] and\
       coordenada_coluna(c) <= tabuleiro_dimensoes(t)[1]:
        #verifica se os inputs sao um tabuleiro e uma coordenada, respetivamente
        #se a linha e a coluna da coordenada estao dentro das dimensoes do tabuleiro
        l, c = coordenada_linha(c), coordenada_coluna(c)
        return t[l+1][c-1]
    
    else:
        raise ValueError('tabuleiro_celula: argumentos invalidos')
        
def tabuleiro_preenche_celula(t, c, valor):
    """MODIFICADOR
    Esta funcao recebe uma lista (tabuleiro) e uma coordenada e modifica a
    a coordenada no tabuleiro"""
    if e_tabuleiro(t) and e_coordenada(c) and valor in [0, 1, 2] and\
       coordenada_linha(c) <= tabuleiro_dimensoes(t)[0] and\
       coordenada_coluna(c) <= tabuleiro_dimensoes(t)[1]:
        #verifica se os inputs sao um tabuleiro, uma coordenada, e um valor entre 0 e 2, respetivamente
        #se a linha e a coluna da coordenada estao dentro das dimensoes do tabuleiro        
        l, c = coordenada_linha(c), coordenada_coluna(c)
        t[l+1][c-1] = valor
        return t
    else:
        raise ValueError('tabuleiro_preenche_celula: argumentos invalidos')
    
def e_tabuleiro(arg):
    """RECONHECEDOR
    Esta funcao recebe uma lista (tabuleiro) e devolve True se o argumento for um tabuleiro"""    
    if isinstance(arg, list) and isinstance(arg[0], list) and isinstance(arg[1], list):
        num_linhas = len(arg[0])
        num_colunas = len(arg[1])
        if num_linhas == len(arg) - 2:
            for i in arg[2:]:
                if num_colunas != len(i):
    #verifica se o input e uma lista e se os dois primeiros indices dessa lista sao listas
    #se o comprimento dessas listas corresponde ao numero (para as linhas)
    #e comprimento (para as colunas) dos restantes indices da lista principal
                    return False
            return True
        else:
            return False
        return True
    else:
        return False

def tabuleiro_completo(t):
    """RECONHECEDOR
    Esta funcao recebe uma lista (tabuleiro) e devolve True se o tabuleiro estiver
    corretamente preenchido. False em caso contrario"""    
    return linha_completa(t) and coluna_completa(t)

def linha_completa(t):
    """FUNCAO AUXILIAR
    RECONHECEDOR
    Esta funcao recebe uma lista (tabuleiro) e devolve True se a linha estiver
    corretamente preenchida. False em caso contrario"""   
    for i in range(len(t[0])): # i percorre tuplos
        soma_esp = 0
        soma_dois = 0
        CONTADOR_GRUPOS_DOIS = 0
        FLAG = 0
        for e in range(len(t[0][i])):
            soma_esp += t[0][i][e]   
        for f in range(len(t[i+2])):
            # conta a soma total de celulas com valor 'dois'
            if t[i+2][f] == 2:
                soma_dois += 1
            elif t[i+2][f] == 0:
                return False
        if soma_esp != soma_dois:
            return False
        for f in range(len(t[i+2])):
            # conta os grupos de celulas seguidas com valor 'dois'
            if t[i+2][f] == 2 and FLAG == 0: 
                CONTADOR_GRUPOS_DOIS += 1
                FLAG =1
            elif t[i+2][f] == 1:
                FLAG =0
        if CONTADOR_GRUPOS_DOIS != len(t[0][i]):
            return False
    return True

def coluna_completa(tab):
    """FUNCAO AUXILIAR
    RECONHECEDOR
    Esta funcao recebe uma lista (tabuleiro) e devolve True se a coluna estiver
    corretamente preenchida. False em caso contrario"""      
    t = transposta_matriz_aux(tab)
    for i in range(len(t[1])): # i percorre tuplos
        soma_esp = 0
        soma_dois = 0
        CONTADOR_GRUPOS_DOIS = 0
        FLAG = 0
        for e in range(len(t[1][i])):
            soma_esp += t[1][i][e]
        for f in range(len(t[i+2])): # para contar soma total de 'dois'
            if t[i+2][f] == 2:
                soma_dois +=1
            elif t[i+2][f] == 0:
                return False
        if soma_esp != soma_dois:
            return False        
        for f in range(len(t[i+2])):
            if t[i+2][f] == 2 and FLAG == 0: # para contar os grupos de 'dois'
                CONTADOR_GRUPOS_DOIS += 1
                FLAG =1
            elif t[i+2][f] == 1:
                FLAG =0
        if CONTADOR_GRUPOS_DOIS != len(t[1][i]):
            return False   
    return True

def transposta_matriz_aux(t):
    """FUNCAO AUXILIAR
    Devolve a transposta da matriz"""      
    final=[]
    tab = t[2:]
    esp = t[:2]
    lst_col = [None]*len(tab[0])
    for t in range(len(tab)):
        lst_col[t] = [None]*len(tab)
        for tt in range(len(tab[t])):
            lst_col[t][tt] = tab[tt][t]
    final = esp + lst_col
    return final
            
def tabuleiros_iguais(t1,t2):
    """TESTE
    Esta funcao recebe duas listas(tabuleiros) e devolve o valor logico"""    
    return t1 == t2

def escreve_tabuleiro(t): 
    """Esta funcao recebe uma lista (tabuleiro) e devolve a representacao externa"""
    if e_tabuleiro(t):
        maior_nmr_instr_col, maior_nmr_instr_lin, lista_tab = 0, 0, []
        esp_lin, esp_col = tabuleiro_especificacoes(t)[0], tabuleiro_especificacoes(t)[1]
        dim_lin, dim_col = tabuleiro_dimensoes(t)[0], tabuleiro_dimensoes(t)[1]
        
        for i in range(dim_lin):
            lista_tab = lista_tab + [[]]
        for e in range(dim_col):
            lista_tab[e] = lista_tab[e] + [[]]
        #criacao do tabuleiro com as celulas
        
        for i in esp_lin:
            if len(i) > maior_nmr_instr_lin:
                maior_nmr_instr_lin = len(i)
        #averigua o maior numero de instrucoes na mesma linha        
        for i in esp_col:
            if len(i) > maior_nmr_instr_col:
                maior_nmr_instr_col = len(i)
        #averigua o maior numero de instrucoes na mesma coluna
        
        while maior_nmr_instr_col > 0:
            
            cc = '  '
            for i in esp_col:
                if len(i) >= maior_nmr_instr_col:
                    cc = cc + str(i[len(i) - maior_nmr_instr_col]) + '    '
                else:
                    cc = cc + '     '        
            print (cc) #escreve as instrucoes das colunas
            maior_nmr_instr_col = maior_nmr_instr_col - 1
            
        y = 0
        cc_ = ''
        num_lin = tabuleiro_dimensoes(t)[0]
        num_col = tabuleiro_dimensoes(t)[1]
        for i in range(1, num_lin + 1):
            z = 0
            for j in range(1, num_col + 1):
                if tabuleiro_celula(t, cria_coordenada(i, j)) == 0:
                    lista_tab[z] = '[ ? ]'
                    z = z + 1
                elif tabuleiro_celula(t, cria_coordenada(i, j)) == 1:
                    lista_tab[z] = '[ . ]'
                    z = z + 1
                else:
                    lista_tab[z] = '[ x ]'
                    z = z + 1
                    
            espec_linhas = list(tabuleiro_especificacoes(t)[0])
            comp_ = len(espec_linhas)
            for x in range(comp_):
                espec[x] = list(espec_linhas[x])
                comp__ = len(espec_linhas[x])
                for a in range(comp__):
                    espec[x][a] = str(espec_linhas[x][a])
                
            nmr_esp = maior_nmr_instr_lin - len(espec[y]) #calcula o numero de espacos
            cc_ = '  ' * nmr_esp #cadeia com os espacos em branco
            print ( ("". join(lista_tab)) + ' ' + " ". join(espec_linhas[y]) + cc_ + '|' )
            #escreve o tabuleiro e as instrucoes das linhas
            y = y + 1
        print()
    else:
        raise ValueError ("escreve_tabuleiro: argumento invalido")

def celulas_todas_preenchidas(t):
    if e_tabuleiro(t):
        num_lin = tabuleiro_dimensoes(t)[0]
        num_col = tabuleiro_dimensoes(t)[1]
        
        for i in range(1, num_lin + 1):
            for j in range(1, num_col + 1):
                if tabuleiro_celula(t, cria_coordenada(i, j)) == 0:
                    return False
        #verifica se existe alguma celula nao preenchida, ou seja, com valor 0
        return True

"""-----------------------------------------------------------------------------
                                    TAD JOGADA
                                     
Representacao interna: Dicionario    
-----------------------------------------------------------------------------"""
def cria_jogada(coor, val):
    """CONSTRUTOR
    Recebe uma coordenada e um inteiro 1 ou 2"""
    if e_coordenada(coor) and val in [1, 2]:
        #verifica se os inputs sao uma coordenada e um valor entre 1 e 2, respetivamente
        jogada = {'linha': coordenada_linha(coor), 'coluna': coordenada_coluna(coor), 'valor': val}
        return jogada
    else:
        raise ValueError ("cria_jogada: argumentos invalidos")
    
def jogada_coordenada(jog):
    """SELETOR
    Recebe um dicionario(jogada) e devolve a coordenada respetiva"""
    if e_jogada(jog):   
        return cria_coordenada(jog['linha'], jog['coluna'])  

def jogada_valor(jog):
    """SELETOR
    Recebe um dicionario(jogada) e devolve o valor respetivo"""
    return jog['valor']

def e_jogada(jog):
    """RECONHECEDOR
    Devolve True se for do tipo jogada"""
    return isinstance(jog, dict) and len(jog) == 3 and 'linha' in jog and\
           'coluna' in jog and 'valor' in jog and jog['valor'] in [1, 2]
    #verifica se o input e um dicionario, que tem apenas 3 chaves
    #se as chaves tem os nomes certos e se o valor e 1 ou 2

def jogadas_iguais(j1, j2):
    """TESTE
    Recebe dois dicionarios e devolve True se corresponderem a mesma jogada"""
    if e_jogada(j1) and e_jogada(j2):
        return j1 == j2

def jogada_para_cadeia(jog):
    """Recebe um dicionario(jogada) e devolve a cadeia correspondente a jogada"""
    return coordenada_para_cadeia(jogada_coordenada(jog)) + ' --> ' + str(jogada_valor(jog))

"""-----------------------------------------------------------------------------
      FUNCOES ADICIONAIS (le_tabuleiro, pede_jogada, jogo_picross --> MAIN)
-----------------------------------------------------------------------------"""
def le_tabuleiro(cadeia_tab):
    """Esta funcao recebe um ficheiro e devolve um tuplo de dois tuplos com as
    especificacoes de jogo"""
    fich = open(cadeia_tab, 'r')
    linha = fich.readline()
    fich.close()
    return eval(linha)
    
def pede_jogada(T):
    """Esta funcao recebe o tabuleiro de jogo e devolve a jogada que o utilizador
    pretende realizar"""
    print('Introduza a jogada')
    dim_lin = tabuleiro_dimensoes(T)[0]
    dim_col = tabuleiro_dimensoes(T)[1]
    coord = input('- coordenada entre (1 : 1) e ' + coordenada_para_cadeia(cria_coordenada\
            (dim_lin, dim_col)) + ' >> ')
    valor = eval (input('- valor >> '))
    if   e_coordenada(cadeia_para_coordenada(coord))and\
         coordenada_linha(cadeia_para_coordenada(coord))<= tabuleiro_dimensoes(T)[0] and\
         coordenada_coluna(cadeia_para_coordenada(coord))<= tabuleiro_dimensoes(T)[1]:
        return cria_jogada(cadeia_para_coordenada(coord), valor)
    else:
        return False

def jogo_picross(fich):
    """Esta e a funcao principal do jogo. Permite jogar o Picross. Recebe uma cadeia
    de caracteres com o nome do ficheiro com as espedificacoes de jogo, verifica
    se o tabuleiro esta completo e escreve a representacao externa do tabuleiro
    jogada apos jogada"""
    tab = cria_tabuleiro(le_tabuleiro(fich))
    print('JOGO PICROSS')
    escreve_tabuleiro(tab)
    while not celulas_todas_preenchidas(tab):
        jog = pede_jogada(tab)
        if not jog:
            print('Jogada invalida.')
        else:
            tabuleiro_preenche_celula (tab, jogada_coordenada(jog),jogada_valor(jog))
            escreve_tabuleiro(tab)        
    if tabuleiro_completo(tab):
        print('JOGO: Parabens, encontrou a solucao!')
        return True
    else:
        print('JOGO: O tabuleiro nao esta correto!')
        return False

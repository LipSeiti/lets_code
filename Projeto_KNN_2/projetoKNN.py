class ClassificadorKnn:
    '''
    Classe teste
    '''
    def __init__( self, data ):
        '''
        Método construtor;
        Ele recebe como parâmetro a base de dados utilizada para classificação;
        '''
        self.data = data

    def calculo_distancia( self, carteira, param ):
        '''
        Método para calcular a distância entre os elementos e a base de dados;
        Ele recebe como parâmetro as carteiras do elemento a ser classificado (carteira) e de um item da base de dados (param);
        Ele retorna o valor da distância entre os 2 elementos;
        '''
        distancia = 0
        for i in range(len(carteira)):
            distancia += (carteira[i] - param[i])**2

        return( distancia**(0.5) )
    
    def classificar_elemento( self, elemSelecionados ):
        '''
        Método que realiza a classificação do perfil a partir dos K números selecionados;
        Ele recebe como parâmetro os K elementos mais próximos do item a ser classificado (elemSelecionados);
        Ele retorna uma string com o perfil correspondente;
        '''
        countC = elemSelecionados.count( "Conservador" )
        countM = elemSelecionados.count( "Moderado" )
        countA = elemSelecionados.count( "Agressivo" )

        if( (countC > countM) and (countC > countA) ):
            return "Conservador"
        elif( (countM > countC) and (countM > countA) ):
            return "Moderado"
        else:
            return "Agressivo"

    def classificacao_perfil( self, listaInput, numK ):
        '''
        Método principal para a classificação de perfis;
        Ele recebe como parâmetro a lista a ser classificada (listaInput) e o número de K para ser utilizado (numK);
        Ele retorna um dicionário com os elementos classificados e seus respectivos CPFs;
        '''
        listaClassificada = {}
        listaDistProx     = []
        listaPerfProx     = []

        for i in listaInput:
            listaDistProx     = []
            listaPerfProx     = []
            for j in self.data:
                aux = self.calculo_distancia( i[2], j[2] )
                if( len(listaDistProx) < numK ):
                    listaDistProx.append(aux)
                    listaPerfProx.append(j[1])
                else:
                    if( max(listaDistProx) > aux ):
                        maiorDistancia = listaDistProx.index(max(listaDistProx))
                        listaDistProx[maiorDistancia] = aux
                        listaPerfProx[maiorDistancia] = j[1]

            listaClassificada[i[0]] = self.classificar_elemento( listaPerfProx )

        return listaClassificada
# implementacao do metodo smarter para MAD
def k_roc(size, order):
    k = [0 for x in range(size)]
    for i in range(size):
        sum = 0
        for j in range(size-i):
            sum = sum + 1/(size-(size-i-j)+1) 
        k[order[i]] = (1/size)*sum
    return k

def smarter(matriz_cons , order):
    if matriz_cons is None:
        return 0
    else:
        k_norm = k_roc(len(order),order)
        #print("k_roc",k_norm)
        score_alt = [[0 for x in range(2)] for y in range(len(matriz_cons))]
        for alt in range(len(matriz_cons)):
            for criteria in range(len(matriz_cons[alt])-1):
                if(criteria == 0):
                    score_alt[alt][0] = matriz_cons[alt][6]
                score_alt[alt][1] = score_alt[alt][1] + matriz_cons[alt][criteria]*k_norm[criteria]
                
        score_alt.sort(key=lambda row: (row[1]), reverse = True)
        #print("smarter",score_alt)
            
        return score_alt
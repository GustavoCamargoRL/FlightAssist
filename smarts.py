import variables

# implementacao do metodo smarts para MAD

def smarts(matriz_cons,k):
    if matriz_cons is None:
        return 0
    else:
        total_k = 0
        #print("smarts",k)
        k_norm = []
        score_alt = [[0 for x in range(2)] for y in range(len(matriz_cons))]
        for i in k:
            total_k = total_k + i
        for v in range(len(k)):
            k_norm.append(k[v]/total_k)
        for alt in range(len(matriz_cons)):
            for criteria in range(len(matriz_cons[alt])-1):
                if(criteria == 0):
                    score_alt[alt][0] = matriz_cons[alt][6]
                score_alt[alt][1] = score_alt[alt][1] + matriz_cons[alt][criteria]*k_norm[criteria]
                
        score_alt.sort(key=lambda row: (row[1]), reverse = True)
        variables.knorm_smarts = k_norm
        #print("smarts",k_norm, score_alt)
            
        return score_alt


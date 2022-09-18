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
        #print("smarts",k_norm, score_alt)
            
        return score_alt

#matriz = [[12.41, 2134, 20, 2,1,0],
#    [15.42,1833,8.4,1,3,1],
#    [31.27,3048,17.4,1,2,2],
#    [40.22,2083,82,2,3,3],
#    [65.72,2135,99,2,3,4],
#    [29.44,1996,439,1,2,5],
#    [48.17,655,921,1,1,6]]
#matriz_con = []
#for i in range(len(matriz)):
#    if (i%2 == 0):
#        matriz_con.append(matriz[i])
#max_vc = []
#min_vc = []

#for alt in range(len(matriz_con)):
#    for cri in range(len(matriz_con[0])-1):
#        if(alt == 0):
#            max_vc.append(matriz_con[alt][cri])
#            min_vc.append(matriz_con[alt][cri])
#        else:
#            if matriz_con[alt][cri] > max_vc[cri]:
#                max_vc[cri] = matriz_con[alt][cri]
#            if matriz_con[alt][cri] < min_vc[cri]:
#                min_vc[cri] = matriz_con[alt][cri]

#for alt in range(len(matriz_con)):
#    for cri in range(len(matriz_con[0])-1):
#        if(cri == 1):
#            matriz_con[alt][cri] = (matriz_con[alt][cri] - min_vc[cri])/(max_vc[cri]-min_vc[cri])
#        else: 
#            matriz_con[alt][cri] = (matriz_con[alt][cri] - max_vc[cri])/(min_vc[cri]-max_vc[cri])
    
#k = [100,90,50,20,60]

#print(smarts(matriz_con,k))

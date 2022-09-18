# implementation of the g-smart/smartest method

def split_vector(vector):
    if(len(vector)%2==0):
        half = len(vector)//2
        return vector[:half], vector[half:]
    else:
        half = len(vector)//2
        return vector[:half], vector[half+1:]

def intra_analysis(matriz_cons,k,s,c_type):
    if (len(matriz_cons) < 1):
        return k
    else:
        ck_vector = []
        for i in range(len(k)):    # each criteria analysis
            if(c_type[i] == 0):    # case for continuous values
                distance_vector = []
                for alt in range(len(matriz_cons)):   # alternatives exploration
                    for n_alt in range(len(matriz_cons)-alt):   # pair-pair comparison  
                        if(alt != n_alt+alt):
                            distance_vector.append(abs(matriz_cons[alt][i]-matriz_cons[n_alt+alt][i])) #sum of all distances
                d_total = sum(distance_vector)
                d_mean = d_total/len(matriz_cons)  #mean of distances
                if(s[i] > d_mean):
                    ck = d_mean/s[i]             # correction factor for K
                else:
                    ck = 1
                ck_vector.append(ck)
            elif(c_type[i] == 1):  # case for discrete values
                if(len(matriz_cons) == 2):  # only 2 alternatives available
                    if(abs(matriz_cons[0][i] - matriz_cons[1][i]) == 0):
                        ck_vector.append(0)
                elif(len(matriz_cons) == 3): # only 3 alternatives available
                    if(abs(matriz_cons[0][i] - matriz_cons[1][i]) <= 1 and abs(matriz_cons[0][i] - matriz_cons[2][i]) <= 1 and abs(matriz_cons[1][i] - matriz_cons[2][i]) <= 1):
                        ck_vector.append(0.5)
                elif(len(matriz_cons) > 3):                       # 4 or more alternatives available, boxplot analysis
                    values_c = []
                    minimum = 0
                    Q1 = 0
                    Q2 = 0
                    Q3 = 0
                    maximum = 0
                    for a in range(len(matriz_cons)):
                        values_c.append(matriz_cons[a][i])
                    values_c.sort()
                    minimum = min(values_c)
                    maximum = max(values_c)
                    if(len(values_c) % 2 == 0):
                        Q2 = (values_c[len(values_c)//2] + values_c[len(values_c)//2 + 1])/2
                    else:
                        Q2 = values_c[len(values_c)//2]

                    split_low, split_up = split_vector(values_c)
                    if(len(split_low) % 2 == 0):
                        Q1 = (split_low[len(split_low)//2 - 1] + split_low[len(split_low)//2])/2
                    else:
                        Q1 = split_low[len(split_low)//2]
                    if(len(split_up) % 2 == 0):
                        Q3 = (split_up[len(split_up)//2 - 1] + split_up[len(split_up)//2])/2
                    else:
                        Q3 = split_up[len(split_up)//2]
                    
                    boxplot = [minimum,Q1,Q2,Q3,maximum]

                    distance_vector = []
                    for alt in range(len(boxplot)):   # alternatives exploration
                        for n_alt in range(len(boxplot)-alt):   # pair-pair comparison  
                            if(alt != n_alt+alt):
                                distance_vector.append(abs(boxplot[alt]-boxplot[n_alt+alt])) #sum of all distances
                    d_total = sum(distance_vector)
                    d_mean = d_total/len(boxplot)  #mean of distances
                    if(s[i] > d_mean):
                        ck = d_mean/s[i]             # correction factor for K
                    else:
                        ck = 1
                    ck_vector.append(ck)
                else:
                    ck_vector.append(1)
            elif(c_type[i] == 2):    #case for binary criteria
                distance_vector = []
                for alt in range(len(matriz_cons)):   # alternatives exploration
                    for n_alt in range(len(matriz_cons)-alt):   # pair-pair comparison  
                        if(alt != n_alt+alt):
                            distance_vector.append(abs(matriz_cons[alt][i]-matriz_cons[n_alt+alt][i])) #sum of all distances
                d_total = sum(distance_vector)
                if(d_total == 0):
                    ck = 0             # correction factor for K
                else:
                    ck = 1
                ck_vector.append(ck)


        return ck_vector         

def gsmarts(matriz_cons,k,k_correction):
    k_gsmartest = [0 for x in range(len(k))]
    for i in range(len(k)):
        k_gsmartest[i] = k[i]
    if matriz_cons is None:
        return 0
    else:
        for i in range(len(k_correction)):
            k_gsmartest[i] = k[i]*k_correction[i]
        total_k = 0
        print("gsmarts",k_gsmartest)
        k_norm_smartes = []
        score_alt = [[0 for x in range(2)] for y in range(len(matriz_cons))]
        for i in k_gsmartest:
            total_k = total_k + i
        for v in range(len(k_gsmartest)):
            if(total_k != 0):
                k_norm_smartes.append(k_gsmartest[v]/total_k)
            else:
                k_norm_smartes.append(0)
        for alt in range(len(matriz_cons)):
            for criteria in range(len(matriz_cons[alt])-1):
                if(criteria == 0):
                    score_alt[alt][0] = matriz_cons[alt][6]
                score_alt[alt][1] = score_alt[alt][1] + matriz_cons[alt][criteria]*k_norm_smartes[criteria]
                
        score_alt.sort(key=lambda row: (row[1]), reverse = True)
        print("gsmarts",k_norm_smartes, score_alt)
            
        return score_alt

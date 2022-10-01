

def init():
    global activate
    global rank
    global elicit
    global elicitation_done
    global knorm_smartest
    global knorm_smarts
    global knorm_smarter
    global found_smarter
    global found_smartest
    global found_smarts
    global best_smartest
    global best_smarts
    global best_smarter
    global score_smartest
    global score_smarts
    global score_smarter
    global thread_method
    global weights_smarts
    global st_smartest


    activate = [0,0,0]  # 1- smarts 2- smarter 3- smartest
    rank = []  #rank of elicitation
    elicit = [0,0,0,0,0,0] #check elicit criteria 0 if not, 1 if ranked
    elicitation_done = False
    knorm_smartest = []
    knorm_smarts = []
    knorm_smarter = []
    found_smarts = False
    found_smarter = False
    found_smartest = False
    best_smartest = []
    best_smarts = []
    best_smarter = []
    score_smartest = 0
    score_smarts = 0
    score_smarter = 0
    thread_method = True
    weights_smarts = [0,0,0,0,0,0]
    st_smartest = [0,0,0,0,0,0]

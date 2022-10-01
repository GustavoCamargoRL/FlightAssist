import cv2 as cv
import numpy as np
import variables

srcOut = cv.imread("output_canva.png")

def report():
    while(True):
        font = cv.FONT_HERSHEY_SIMPLEX
        
        # fontScale
        fontScale = 0.5
        
        # Blue color in BGR
        color = (0, 0, 0)
        ksmartest = (float(f'{e:.4f}') for e in variables.knorm_smartest)
        ksmarts = (float(f'{e:.4f}') for e in variables.knorm_smarts)
        ksmarter = (float(f'{e:.4f}') for e in variables.knorm_smarter)
        # Line thickness of 1 px
        thickness = 1
        output = srcOut.copy()
        cv.namedWindow("Console feedback", cv.WINDOW_AUTOSIZE)
        # Using cv2.putText() method
        if(variables.found_smartest and variables.activate[2] == 1):
            output = cv.putText(output, 'SMARTEST(K): ', (10,100), font, fontScale, color, thickness, cv.LINE_AA)
            output = cv.putText(output, ' '.join(str(e) for e in ksmartest), (120,100), font, fontScale, color, thickness, cv.LINE_AA)
            output = cv.putText(output, 'Best choice: ', (520,100), font, fontScale+0.5, color, thickness, cv.LINE_AA)
            output = cv.putText(output, variables.best_smartest, (530,135), font, fontScale+0.5, color, thickness, cv.LINE_AA)
            output = cv.putText(output, 'Score: ', (520,170), font, fontScale+0.5, color, thickness, cv.LINE_AA)
            output = cv.putText(output, str(variables.score_smartest), (530,200), font, fontScale+0.5, color, thickness, cv.LINE_AA)
        elif(variables.activate[2] == 0):
            output = cv.putText(output, 'SMARTEST(K): ', (10,100), font, fontScale, color, thickness, cv.LINE_AA)
            output = cv.putText(output, 'Disabled', (120,100), font, fontScale, color, thickness, cv.LINE_AA)
            output = cv.putText(output, 'Best choice: ', (520,100), font, fontScale+0.5, color, thickness, cv.LINE_AA)
            output = cv.putText(output, 'Disabled', (530,135), font, fontScale+0.5, color, thickness, cv.LINE_AA)
            output = cv.putText(output, 'Score: ', (520,170), font, fontScale+0.5, color, thickness, cv.LINE_AA)
            output = cv.putText(output, 'Disabled', (530,200), font, fontScale+0.5, color, thickness, cv.LINE_AA)
        else:
            output = cv.putText(output, 'SMARTEST(K): ', (10,100), font, fontScale, color, thickness, cv.LINE_AA)
            output = cv.putText(output, ' '.join(str(e) for e in ksmartest), (120,100), font, fontScale, color, thickness, cv.LINE_AA)
            output = cv.putText(output, 'Best choice: ', (520,100), font, fontScale+0.5, color, thickness, cv.LINE_AA)
            output = cv.putText(output, 'Not found!', (530,135), font, fontScale+0.5, color, thickness, cv.LINE_AA)
            output = cv.putText(output, 'Score: ', (520,170), font, fontScale+0.5, color, thickness, cv.LINE_AA)
            output = cv.putText(output, 'Not found!', (530,200), font, fontScale+0.5, color, thickness, cv.LINE_AA)

        if(variables.found_smarts and variables.activate[0] == 1):
            output = cv.putText(output, 'SMARTS(K): ', (10,140), font, fontScale, color, thickness, cv.LINE_AA)
            output = cv.putText(output, ' '.join(str(e) for e in ksmarts), (120,140), font, fontScale, color, thickness, cv.LINE_AA)
            output = cv.putText(output, 'Best choice: ', (20,370), font, fontScale+0.5, color, thickness, cv.LINE_AA)
            output = cv.putText(output, variables.best_smarts, (30,405), font, fontScale+0.5, color, thickness, cv.LINE_AA)
            output = cv.putText(output, 'Score: ', (20,440), font, fontScale+0.5, color, thickness, cv.LINE_AA)
            output = cv.putText(output, str(variables.score_smarts), (30,470), font, fontScale+0.5, color, thickness, cv.LINE_AA)
        elif(variables.activate[0] == 0):
            output = cv.putText(output, 'SMARTS(K): ', (10,140), font, fontScale, color, thickness, cv.LINE_AA)
            output = cv.putText(output, 'Disabled', (120,140), font, fontScale, color, thickness, cv.LINE_AA)
            output = cv.putText(output, 'Best choice: ', (20,370), font, fontScale+0.5, color, thickness, cv.LINE_AA)
            output = cv.putText(output, 'Disabled', (30,405), font, fontScale+0.5, color, thickness, cv.LINE_AA)
            output = cv.putText(output, 'Score: ', (20,440), font, fontScale+0.5, color, thickness, cv.LINE_AA)
            output = cv.putText(output, 'Disabled', (30,470), font, fontScale+0.5, color, thickness, cv.LINE_AA)
        else:
            output = cv.putText(output, 'SMARTS(K): ', (10,140), font, fontScale, color, thickness, cv.LINE_AA)
            output = cv.putText(output, ' '.join(str(e) for e in ksmarts), (120,140), font, fontScale, color, thickness, cv.LINE_AA)
            output = cv.putText(output, 'Best choice: ', (20,370), font, fontScale+0.5, color, thickness, cv.LINE_AA)
            output = cv.putText(output, 'Not found!', (30,405), font, fontScale+0.5, color, thickness, cv.LINE_AA)
            output = cv.putText(output, 'Score: ', (20,440), font, fontScale+0.5, color, thickness, cv.LINE_AA)
            output = cv.putText(output, 'Not found!', (30,470), font, fontScale+0.5, color, thickness, cv.LINE_AA)
        if(variables.found_smarter and variables.activate[1] == 1):
            output = cv.putText(output, 'SMARTER(K): ', (10,180), font, fontScale, color, thickness, cv.LINE_AA)
            output = cv.putText(output, ' '.join(str(e) for e in ksmarter), (120,180), font, fontScale, color, thickness, cv.LINE_AA)
            output = cv.putText(output, 'Best choice: ', (520,370), font, fontScale+0.5, color, thickness, cv.LINE_AA)
            output = cv.putText(output, variables.best_smarter, (530,405), font, fontScale+0.5, color, thickness, cv.LINE_AA) 
            output = cv.putText(output, 'Score: ', (520,440), font, fontScale+0.5, color, thickness, cv.LINE_AA)
            output = cv.putText(output, str(variables.score_smarter), (530,470), font, fontScale+0.5, color, thickness, cv.LINE_AA)
        elif(variables.activate[1] == 0):
            output = cv.putText(output, 'SMARTER(K): ', (10,180), font, fontScale, color, thickness, cv.LINE_AA)
            output = cv.putText(output, 'Disabled', (120,180), font, fontScale, color, thickness, cv.LINE_AA)
            output = cv.putText(output, 'Best choice: ', (520,370), font, fontScale+0.5, color, thickness, cv.LINE_AA)
            output = cv.putText(output, 'Disabled', (530,405), font, fontScale+0.5, color, thickness, cv.LINE_AA) 
            output = cv.putText(output, 'Score: ', (520,440), font, fontScale+0.5, color, thickness, cv.LINE_AA)
            output = cv.putText(output, 'Disabled', (530,470), font, fontScale+0.5, color, thickness, cv.LINE_AA)
        else:
            output = cv.putText(output, 'SMARTER(K): ', (10,180), font, fontScale, color, thickness, cv.LINE_AA)
            output = cv.putText(output, ' '.join(str(e) for e in ksmarter), (120,180), font, fontScale, color, thickness, cv.LINE_AA)
            output = cv.putText(output, 'Best choice: ', (520,370), font, fontScale+0.5, color, thickness, cv.LINE_AA)
            output = cv.putText(output, 'Not found!', (530,405), font, fontScale+0.5, color, thickness, cv.LINE_AA) 
            output = cv.putText(output, 'Score: ', (520,440), font, fontScale+0.5, color, thickness, cv.LINE_AA)
            output = cv.putText(output, 'Not found!', (530,470), font, fontScale+0.5, color, thickness, cv.LINE_AA)
                

        
        # using cv2.imshow() to display the output
        cv.imshow('Console feedback', output)
            
        key = cv.waitKey(30)
        if key == ord('q') or key == 27:
            break
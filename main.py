"""


"""

#!/usr/bin/env python


def get_trigger(risk, score):

    #low-risk
    if (risk == 1):
        if (score<20):
            return ("No notification")
        elif (20<= score < 30):
            return ("Notification for the family")
        elif (30<= score < 40):
            return ("Notification for the family and for the doctor, in the Remotely Close portal")
        else:
            return ("Notification for the family and for the doctor, in the EHR portal")

    elif (risk == 2):
        if (score<15):
            return ("No notification")
        elif (15<= score < 20):
            return ("Notification for the family")
        elif (20<= score < 25):
            return ("Notification for the family and for the doctor, in the Remotely Close portal")
        else:
            return ("Notification for the family and for the doctor, in the EHR portal")

    else:
        if (score<13):
            return ("No notification")
        elif (13<= score < 17):
            return ("Notification for the family")
        elif (17<= score < 20):
            return ("Notification for the family and for the doctor, in the Remotely Close portal")
        else:
            return ("Notification for the family and for the doctor, in the EHR portal")



def get_exercise(minutes):

    exerc_score = 0
    for minute in minutes:

        if minute >= 30:
            exerc_score = exerc_score-1
        elif 15 < minute <= 30:
            exerc_score = exerc_score+0
        elif 7 < minute <= 15:
            exerc_score = exerc_score + 1
        else:
            exerc_score = exerc_score+8


    return (exerc_score)


def get_progress(grades):

    prog_score = 0
    for grade in grades:
        if grade >= 3:
            prog_score = prog_score-1
        elif grade <= (-3):
            prog_score = prog_score+1

    return (prog_score)

def get_comm(normal, minutes):

    comm_score = 0
    
    #if normal == 0:
     #  normal = 1

    for minute in minutes:

        if minute/normal > 1.5:
            comm_score = comm_score-1
        elif 1.5 >= minute/normal > 0.1:
            comm_score = comm_score+0
        else:
            comm_score = comm_score+1


    return (comm_score)


def get_med(importance, compliance):

    med_score = 0

    if importance == 0:
        for comp in compliance:
            if comp == 0:
                med_score = med_score + 3
    else:
        for comp in compliance:
            if comp == 0:
                med_score = med_score + 10


    return (med_score)







"""


"""

#!/usr/bin/env python


def get_trigger(risk, score):

    #low-touch
    if (risk == 1):
        if (score<20):
            return ("No notification")
        elif (20<= score < 30):
            return ("Notification for the family")
        elif (30<= score < 40):
            return ("Notification for the family and for the doctor, in the Remotely Close portal")
        else:
            return ("Notification for the family and for the doctor, in the EHR portal")
    
    #medium-touch
    elif (risk == 2):
        if (score<15):
            return ("No notification")
        elif (15<= score < 20):
            return ("Notification for the family")
        elif (20<= score < 25):
            return ("Notification for the family and for the doctor, in the Remotely Close portal")
        else:
            return ("Notification for the family and for the doctor, in the EHR portal")
    
    #high-risk
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
    
    """
    This function returns the score related to minutes of exercise. The higher the score, the higher the risk.
    
    Parameters:
    minutes: minutes of exercise, per day, sent by the Remotely Close platform
    
    Score matrix:
        exerc >= 30 : -1
        15 < exerc < 30 : 0
        7 < exerc =< 15 : +1
        0 < exerc =< 7 : +8
    """

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
    """
    This function returns the score of the perceived progress of recovery.
    The threshold of classes is based on the Global Rating of Change.
    
    Parameter:
        grades: list of grades of perceived progress by the patient, sent by the Remotely Close platform
    
    Score matrix:
        score >=3 : -1
        -3 < score < 3 : 0
        score <= -3 : +1
    """
    
    prog_score = 0
    for grade in grades:
        if grade >= 3:
            prog_score = prog_score-1
        elif grade <= (-3):
            prog_score = prog_score+1

    return (prog_score)

def get_comm(normal, minutes):
    
    """
    This function returns the score related to time spent with communication with the family, comparing with the average. The higher the score, the higher the risk.
    Parameters:
        normal - average minutes per day spent with communication
        minutes - minutes spent each day with communication

    Score matrix:
        ratio >= 1.5 : -1
        1.5 < ratio =< 0.1: 0
        0 < ratio < 0.1 : +1

     """

    comm_score = 0
   

    for minute in minutes:

        if minute/normal > 1.5:
            comm_score = comm_score-1
        elif 1.5 >= minute/normal > 0.1:
            comm_score = comm_score+0
        else:
            comm_score = comm_score+1


    return (comm_score)


def get_med(importance, compliance):
    """
    This module returns the score related to medication compliance. The higher the score, the higher the risk.
    Parameters:
        importance - 1 for drugs with high importance, 0 for drugs with low importance
        compliance - 1 for dose of medicine taken, 0 not taken

    Score matrix:

        High importance
        1 : 0
        0:  10

        Medium - low importance
        1 : 0
        0: 3
    """
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

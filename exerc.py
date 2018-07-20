"""
This module returns the score related to minutes of exercise. The higher the score, the higher the risk.

Score matrix:
exerc >= 30 : -1
15 < exerc < 30 : 0
7 < exerc =< 15 : +1
0 < exerc =< 7 : +3

"""

#!/usr/bin/env python

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




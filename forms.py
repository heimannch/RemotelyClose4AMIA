from django import forms

class NameForm(forms.Form):
	risk = forms.IntegerField(label='What is the risk group of the patient? (1 - Low, 3 - High)', min_value = 1, max_value = 3)


    exercise1 = forms.IntegerField(label='Minutes of Exercise - Day 1', min_value = 0)
    exercise2 = forms.IntegerField(label='Day 2', min_value = 0)
    exercise3 = forms.IntegerField(label='Day 3', min_value = 0)
    exercise4 = forms.IntegerField(label='Day 4', min_value = 0)
    exercise5 = forms.IntegerField(label='Day 5', min_value = 0)


    prog1 = forms.IntegerField(label='Perceived Progress - Day 1', min_value = -7, max_value = 7)
    prog2 = forms.IntegerField(label='Day 2', min_value = -3, max_value = 3)
    prog3 = forms.IntegerField(label='Day 3', min_value = -3, max_value = 3)
    prog4 = forms.IntegerField(label='Day 4', min_value = -3, max_value = 3)
    prog5 = forms.IntegerField(label='Day 5', min_value = -3, max_value = 3)


    com = forms.FloatField(label='Average minutes/day of communication with family', min_value = 0)
    
    com1 = forms.IntegerField(label='Minutes of communication with family - Day 1', min_value = 0)
    com2 = forms.IntegerField(label='Day 2', min_value = 0)
    com3 = forms.IntegerField(label='Day 3', min_value = 0)
    com4 = forms.IntegerField(label='Day 4', min_value = 0)
    com5 = forms.IntegerField(label='Day 5', min_value = 0)

    
    med_importance = forms.IntegerField(label='Importance of the medication', min_value = 0, max_value = 1, help_text = '0 - Low, 1 - High')

    med1 = forms.IntegerField(label='Compliance - Dose 1', min_value = 0, max_value = 1, help_text = '0 - compliant, 1 - non-compliant')
    med2 = forms.IntegerField(label='Compliance - Dose 2', min_value = 0, max_value = 1)
    med3 = forms.IntegerField(label='Compliance - Dose 3', min_value = 0, max_value = 1)
    med4 = forms.IntegerField(label='Compliance - Dose 4', min_value = 0, max_value = 1)
    med5 = forms.IntegerField(label='Compliance - Dose 5', min_value = 0, max_value = 1)
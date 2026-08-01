from django import forms

class PredictionForm(forms.Form):

    attendance = forms.FloatField(
        label="Attendance (%)",
        min_value=0,
        max_value=100,
        widget=forms.NumberInput(attrs={
            'class':'form-control',
            'placeholder':'Percentage of class attendance'
        })
    )

    study_hours = forms.FloatField(
        label="Study Hours (per day)",
        min_value=0,
        widget=forms.NumberInput(attrs={
            'class':'form-control',
            'placeholder':'Number of daily study hours'
        })
    )

    past_score = forms.FloatField(
        label="Past Score (%)",
        min_value=0,
        max_value=100,
        widget=forms.NumberInput(attrs={
            'class':'form-control',
            'placeholder':'Previous academic performance percentage'
        })
    )

    assignments = forms.IntegerField(
        label="Assignments Submitted",
        min_value=0,
        widget=forms.NumberInput(attrs={
            'class':'form-control',
            'placeholder':'Total count of submitted assignments'
        })
    )

    extracurricular = forms.IntegerField(
        label="Extracurricular (0/1)",
        min_value=0,
        max_value=1,
        widget=forms.NumberInput(attrs={
            'class':'form-control',
            'placeholder':'0 = No, 1 = Yes'
        })
    )
from django import forms

def Check_SId(v):
    if len(str(v))<2:
        raise forms.ValidationError("SId should be morethan 3")
def Check_Sage(a):
    if 12>a:
        raise forms.ValidationError("Give correct input")
    if 14<a:
        raise forms.ValidationError("Give Proper input")

class StudentForm(forms.Form):
    SId=forms.IntegerField(validators=[Check_SId])
    Sname=forms.CharField(max_length=100)
    Sage=forms.IntegerField(validators=[Check_Sage])
    Sjdate=forms.DateField()
    Semail=forms.EmailField()
    Surl=forms.URLField()
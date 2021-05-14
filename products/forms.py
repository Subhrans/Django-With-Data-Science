from django import forms

choice = (
    ('bar plot', 'bar plot'),
    ('line plot', 'line plot'),
    ('graph plot', 'graph plot'),
)


class DateInput(forms.DateInput):
    input_type = "date"


class DataForm(forms.Form):
    choose_chart_type = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control form-select'}),
                                          choices=choice)
    date_from = forms.DateField(widget=DateInput(attrs={'class': 'form-control'}), )
    date_to = forms.DateField(widget=DateInput(attrs={'class': 'form-control'}))

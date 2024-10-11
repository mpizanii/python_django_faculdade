from django import forms
from .models import Event
from django.utils import timezone
from django.forms.widgets import DateTimeInput

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'date', 'description']
        widgets = {
            'date': DateTimeInput(attrs={
                'type': 'datetime-local',  
            }),
        }

    def clean_date(self):
        date = self.cleaned_data.get('date')
        if date is None:
            raise forms.ValidationError("Este campo é obrigatório.")
        if date < timezone.now():
            raise forms.ValidationError("A data e hora do evento não podem estar no passado.")
        return date
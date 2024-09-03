from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date', 'completed'] 
        labels = {
            'title': 'Título da Tarefa',
            'description': 'Descrição da Tarefa',
            'due_date': 'Data de Vencimento',
            'completed': 'Status',
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'due_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'completed': forms.Select(attrs={'class': 'form-control'}),
        }


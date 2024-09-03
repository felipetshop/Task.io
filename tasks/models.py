from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    completed_options = (
        ('concluído', 'Concluído'),
        ('pendente', 'Pendente'),
    )
    
    title = models.CharField(max_length=40)
    description = models.TextField(max_length=400)
    completed = models.CharField(max_length=25, choices=completed_options, default='pendente')
    created_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta
# Create your models here.
class Tasks(models.Model):
    user=models.ForeignKey(User,related_name='user',on_delete=models.CASCADE)
    title=models.CharField(max_length=56,blank=False)
    description=models.TextField(max_length=256,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    due_at = models.DateTimeField(("end"), db_index=True, help_text=("The end time must be later than the start time."),blank=True,default=timezone.now()+timedelta(1))
    compleated=models.BooleanField(default=False)
    
    def __str__(self) :
        return self.title
    
    class Meta:
        ordering = ('compleated',)
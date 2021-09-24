from django.db import models
from django.contrib.auth.models import User
class Task(models.Model):
          user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
          title= models.CharField(max_length=200,null=True,blank=False)
          description=models.TextField(null=True,blank=True)
          complete=models.BooleanField(default=False)
          created=models.DateTimeField(auto_now_add=True)

          def __str__(self):
                    # if self.title==None:
                    #           return "NO task"

                    return self.title


          class Meta:
                    ordering=['complete']
          
            
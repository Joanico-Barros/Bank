from django.db import models
from django.contrib.auth.models import User


class Account(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=100) 
    amount = models.FloatField(default= 0)
    active = models.BooleanField(default = True)
        
    def __unicode__(self,):
           #import pdb
           #pdb.set_trace()
           return "{}'s: {} is $.{}".format(self.user, self.name, self.amount)
               
    def __init__(self, *args, **kwargs):
        super (Account, self).__init__(*args, **kwargs)
        if 'amount' in kwargs:
            self.amount = kwargs['amount'] 
         
    def add(self, value):
            self.amount = self.amount + value
            self.save()
            return self.amount
        
    def subtract(self, value):
            self.amount = self.amount - value
            self.save()
            return self.amount
            
    def interest(self, rate):
             self.amount = self.amount + (self.amount * rate * 0.01)
             self.save()
             return self.amount
             
    def compound_interest(self, rate, period):
             self.amount = self.amount * (1 + rate * 0.01)** period
             self.save()
             return self.amount
             
    def total_amount(self,):
             self.save()
             return " USD ${0:.2f}".format(self.amount)
        
    
        
    #def save(self, *args, **kwargs):
     #       super(Account, self).save(*args, **kwargs) # Call the "real" save() method.
    

        
        #return "{user}'s account value: ${amount}".format(amount= 5, user= 'Niko')
   

# Create your models here.








from django.db import models

# Create your models here.
class Customers(models.Model):
    Account_holder=models.CharField(max_length=225)
    Email_ID=models.CharField(max_length=225)
    Current_Balance=models.IntegerField()
    
class transaction_deatials(models.Model):
    Sender_Name=models.CharField(max_length=225)
    Sender_updated_Balance=models.IntegerField()
    Amount_Transfer=models.IntegerField()
    Reciver_Name=models.CharField(max_length=225)
    Receiver_updated_Balance=models.IntegerField(default=0)
    


    
    


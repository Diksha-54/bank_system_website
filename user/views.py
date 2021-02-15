from django.shortcuts import render
from django.http import HttpResponse
from django.conf.urls.static import *
from . models import Customers
from . models import transaction_deatials
from django.contrib import messages


# Create your views here.
def index(request):
    return render(request,"index.html")



def viewall(request):
    data=Customers.objects.all()
    return render(request,"viewall.html",{"data":data})

def transfer(request):
    if(request.method == "POST"):
        sender=Customers.objects.get(id=request.POST['s_id'])
        receiver=Customers.objects.get(id=request.POST['r_id'])
        transfer_amount=int(request.POST['Amount'])
        #print(sender.Current_Balance,receiver.Current_Balance,transfer_amount)
        if((transfer_amount != 0) and (sender.Current_Balance >= transfer_amount)):
            sender.Current_Balance= sender.Current_Balance - transfer_amount
            receiver.Current_Balance=receiver.Current_Balance + transfer_amount
            print(sender.Current_Balance,receiver.Current_Balance,transfer_amount)
            messages.success(request," Money Transfered Successfully")
            
            if(sender.Current_Balance >= transfer_amount):
                Sender=Customers.objects.get(id=sender.id)
                Sender.Current_Balance=sender.Current_Balance
                Sender.save()

                Receiver=Customers.objects.get(id=receiver.id)
                Receiver.Current_Balance=receiver.Current_Balance
                Receiver.save()
                obj=transaction_deatials()
                obj.Sender_Name=sender.Account_holder
                obj.Sender_updated_Balance =sender.Current_Balance
                obj.Amount_Transfer=transfer_amount
                obj.Reciver_Name=receiver.Account_holder
                obj.Receiver_updated_Balance =receiver.Current_Balance
                obj.save()

        else:
            messages.error(request," ERROR , Please try again")


    data=Customers.objects.all()
    return render(request,"transfer.html",{"data":data})


def transaction(request):
    history=transaction_deatials.objects.all()
    return render(request,"transaction.html",{"history":history})





        
 
   
    
        



    





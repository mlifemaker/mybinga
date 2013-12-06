# -*- encoding:utf-8 -*-
from django.shortcuts import render
from MyBinga.demo.forms import P2PExchangeForm

# Create your views here.

def howitworks(request):

        return render(request, 'howitworks.html')

def pricing(request):

        return render(request, 'pricing.html')

def security(request):

        return render(request, 'security.html')

def about(request):

        return render(request, 'about.html')

def team(request):

        return render(request, 'team.html')

def exchange(request):
        ReceivedAmount=0
        envoi=False
        fee=0

        FromCurrency=""
        ToCurrency=""
        if request.method == 'POST':
                form=P2PExchangeForm(request.POST)
                if form.is_valid():
                        if request.POST['SentAmount'].isdigit():
                                SentAmount=float(request.POST['SentAmount'])
                                FromCurrency=request.POST['FromCurrency']
                                ToCurrency=request.POST['ToCurrency']
                                fee=(SentAmount *1)/100
                                if FromCurrency =="MAD":
                                        if ToCurrency == "EUR":
                                                ReceivedAmount=(SentAmount / 11) - fee
                                                ReceivedAmount=round(ReceivedAmount,2)
                                                envoi=True
                                        else:
                                                ReceivedAmount=SentAmount
                                                envoi=False
                                if FromCurrency =="EUR":
                                        if ToCurrency == "MAD":
                                                ReceivedAmount=SentAmount*11 - fee
                                                ReceivedAmount=round(ReceivedAmount,2)
                                                envoi=True

                                        else:
                                                ReceivedAmount=SentAmount
                                                envoi=False
        else:
                form=P2PExchangeForm()

        return render(request, 'accueil.html',{'form':form, 'From': FromCurrency,'To':ToCurrency ,'ReceivedAmount':ReceivedAmount,'fee':fee, 'envoi':envoi})


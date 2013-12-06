#-*- coding:utf-8 -*-
from django.http import HttpResponse, HttpResponseRedirect
from django import forms
from django.contrib.auth.forms import UserCreationForm
from MyBinga.client.forms import RegisterForm
from MyBinga.client.forms import ConnexionForm
from django.shortcuts import render, redirect
from django.contrib import messages
from email.mime.text import MIMEText
from datetime import date
import smtplib
from django.contrib.auth import login, authenticate, logout
from django.core.urlresolvers import reverse
# Create your views here.

def home(request):

	text="""<h1>Bienvenue sur MyBinga !</h1>
		<p>Binga...Bingo... De loin, la solution la moins chère pour transférer votre argent du/vers le Maroc! </p>"""
	return HttpResponse(text)


def register(request):

	if request.method=="POST":
		form=RegisterForm(request.POST)
		if form.is_valid():
			new_user=form.save()
			subject="Welcome to MyBinga!"
			msg="Dear "+new_user.username+ ",Thanks for signing up and welcome to MyBinga community!"
			send_email(new_user.email, "ibnalkadi@gmail.com", subject, msg)
			messages.add_message(request, messages.INFO, u'Bonjour nouvel utilisateur !')
			#return HttpResponseRedirect('/')

	else:
		form=RegisterForm()
	return render(request, "registration/register.html",{'form':form})


SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SMTP_USERNAME = "ibnalkadi@gmail.com"
SMTP_PASSWORD = "mohamed1989"
DATE_FORMAT = "%d/%m/%Y"
EMAIL_SPACE = ", "

def send_email(EMAIL_TO, EMAIL_FROM, EMAIL_SUBJECT, DATA):
    msg = MIMEText(DATA)
    msg['Subject'] = EMAIL_SUBJECT + " %s" % (date.today().strftime(DATE_FORMAT))
    msg['To'] = EMAIL_SPACE.join(EMAIL_TO)
    msg['From'] = EMAIL_FROM
    mail = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    mail.starttls()
    mail.login(SMTP_USERNAME, SMTP_PASSWORD)
    mail.sendmail(EMAIL_FROM, EMAIL_TO, msg.as_string())
    mail.quit()


def connexion(request):
    error = False

    if request.method == "POST":
        form = ConnexionForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]  # Nous récupérons le nom d'utilisateur
            password = form.cleaned_data["password"]  # … et le mot de passe
            user = authenticate(username=username, password=password)  #Nous vérifions si les données sont correctes
            if user:  # Si l'objet renvoyé n'est pas None
                login(request, user)  # nous connectons l'utilisateur
            else: #sinon une erreur sera affichée
                error = True
    else:
        form = ConnexionForm()

    return render(request, 'connexion.html',locals())


def deconnexion(request):
    logout(request)
    return redirect(reverse(connexion))
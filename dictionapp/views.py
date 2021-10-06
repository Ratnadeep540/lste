from django.shortcuts import render
from . import dadata
import speech_recognition as sr
import pyttsx3
from time import sleep
from .models import GeeksModel
from .forms import GeeksForm
#from django.template import Template, Context
#from django.template.engine import Engine
#from django.conf import settings
#settings.congigure(DEBUG=False)
# Create your views here.

d = dadata.data
s = dadata.sum
counter = 0
save = [0]
temp = save[-1]
def addCounter():
    global counter
    global save
    if save[-1] >= len(d):
        counter = 0
        save = [0]
    del(save[0])
    counter += 1
    save.append(counter)
    return save[-1]-1

def subCounter():
    global counter
    global save
    if -(len(d)) >= save[-1]:
        counter = 0
        save = [0]
    del(save[0])
    counter -= 1
    save.append(counter)
    return save[-1]
def save_op():
    global save
    return save[-1]


def create_view(request):
	# dictionary for initial data with
	# field names as keys
	context ={}

	# add the dictionary during initialization
	form = GeeksForm(request.POST or None)
	if form.is_valid():
		form.save()
		
	context['form']= form
	return render(request, "diction.html", context)

def diction(request):
    #d = dadata.data
    global d
    nav = False
    context = {}
    #ddd = d_data(recive_diction_from_user())
    if request.method == 'POST' and 'btnform1' in request.POST:
        context = {}
        
        context['display_word'] = check_data()
        #context['display_word'] = "correct answer"
        #context['display_word'] = d[subCounter()]
        #context['time'] = sleep(3)
        
        return render(request,"diction.html", context)
   
    return render(request,"diction.html")
def check_data():
    if recive_diction_from_user().lower() in d:
        t = "you pronunciation word is correct"
        print("success")
        t_t_s(t)
    else:
        t = "come again i did not get you"
        print("com again i did not get you")
        t_t_s(t)
    return t
def recive_diction_from_user():
    output = ""
    text = "testing"
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Speak Anything :")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            print("You said : {}".format(text))
        except:
            print("Sorry could not recognize what you said")
    output = text
    return output
def t_t_s(text):
    pyobj = pyttsx3.init()
    pyobj.setProperty("rate", 150)
    pyobj.say(text)
    #pyobj.save_to_file(text,"sample.mp3")
    pyobj.runAndWait()
def d_data(t):
    a = list(t)
    #l = len(d)-1
    global d
    if t in d:
        return "you prounation is very good"
    else:
        return "come again i didnot get you"
    return 
def fdisplay(request):
    context = {
        "display_word" : d[save_op()],
        }
    return render(request,"diction.html", context)
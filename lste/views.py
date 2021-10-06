from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.http import HttpRequest
from django.http import HttpResponseRedirect
import pyttsx3
import speech_recognition as sr
from . import qadata
from django.template import Context, Template

d = qadata.data

request = HttpRequest

def index(request):
    return render(request,"index.html")
def hrt(request):
    #context={}
    t1 = "<h1>hello</h1>"
    t2 = """<h1>hello</h1>"""
    t3 = "<h1>hello oye</h1>"
    t4 = "<h1>hello unnava</h1>"
    dat = "hello babai"
    #context = {t1, t2,"oye",t3,t4}
    string1 = ""
    

    string1 = "Hello World"

    if request.method == 'POST' and 'btnform1' in request.POST:
        context = {}
       # context['display_word'] = check_data()
    context1 = {t1, t2,"oye",t3,t4}
    template = Template("My name is {{ my_name }}.")
    #check_data()
    diction = """
                <!DOCTYPE html>
{% load static %}
<html>
<head>
<meta charset="UTF-8">
  <meta name="description" content="Free Web tutorials">
  <meta name="keywords" content="HTML, CSS, JavaScript">
  <meta name="author" content="John Doe">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
<title></title>
{% block styles %}
<style type="text/css">
#logo_heading {
  width:100%;
  height:10%;

}
#logo {
  width:100px;
  height:100px;
}
#heading {
  color:red;
  text-align:center;
  margin-top:-60px;
  width:100%;
  height:100%;
}
#displaydiction {
  width:95%;
  margin-left:20px;
  height:90%;
  border:2px solid grey;
  background-color: DarkGreen;
}
#note {
  color:white;
  margin-left:10%;
}

/* Next & previous buttons */
.pbtn {
  
}
.nbtn {
  margin-bottom:30px;
}
#label_name 
{
  margin-left:5%;
}
.img-box {
  text-align:center;
}
.slider {
  width:100%;
  height:100%;
}
#imgname{
  color:white;
}
#output {
  width:400px;
  height:300px;
}
</style>
{% endblock %}

{% block scripts %}

<script src="https://www.gstatic.com/firebasejs/8.2.7/firebase-app.js"></script>

<script src="https://www.gstatic.com/firebasejs/8.2.7/firebase-database.js"></script>
<script src="https://www.gstatic.com/firebasejs/8.2.7/firebase-storage.js"></script>
<script>

const firebaseConfig = {
    apiKey: "AIzaSyBDPVFR4fpJbP655fi0gECiX3rB_DEk1fE",
    authDomain: "health-report-334d5.firebaseapp.com",
    projectId: "health-report-334d5",
    storageBucket: "health-report-334d5.appspot.com",
    messagingSenderId: "192843149376",
    appId: "1:192843149376:web:51df5b1c10bd7779be6fa5",
    measurementId: "G-L1GFZMT005"
      };
    
    // Initialize Firebase
    firebase.initializeApp(firebaseConfig);
    var database = firebase.database();
    var i = 0;


    function incNumber() {
      
        if (i < 5) {
            i++;
        } else if (i = 5) {
            i = 0;
        }
        //document.getElementById("display").innerHTML = dict[i-1];   
        return i;   
    }

    function decNumber() {
      
        if (i > 0) {
            --i;
        } else if (i = 0) {
            i = 5;
        }
        //document.getElementById("display").innerHTML = dict[i]; 
        return i;       
    }

function prev()
{
  ImgId = decNumber();

    var leadsRef = database.ref('Imagestext/').child(ImgId);
    leadsRef.on('child_added', function(snapshot) {
        
        document.getElementById("imgname").innerHTML = snapshot.val().ImageName;
        const flag = false;
        try
        {
            document.getElementById("output").src = snapshot.val().ImageURL;
           
        }
        catch(err)
        {
            console.log("error bro");
        }

    });
}
function next()
{
  ImgId = incNumber();

    var leadsRef = database.ref('Imagestext/').child(ImgId);
    leadsRef.on('child_added', function(snapshot) {
        
        document.getElementById("imgname").innerHTML = snapshot.val().ImageName;
        const flag = false;
        try
        {
            document.getElementById("output").src = snapshot.val().ImageURL;
           
        }
        catch(err)
        {
            console.log("error bro");
        }

    });
}
</script>
{% endblock %}
<head>
<body bgcolor="dark">
<div id="logo_heading">
    <div id="logodiv">
        <a id="aid" href="{% url 'index' %}">
        <img id="logo" src="{% static 'images/Sproud_Knowledge.png'%}" data-name="Sproud Knowledge"></img>
        </a>
        <h1 id="heading">Practise Diction</h1>
    </div>    
</div>
<br>
<div id="displaydiction">
<p id="note">note: click the button and read correct pronounce on display words</p>

    
		<div class="slider">
			<div class="img-box">
				<img id="output"></img>
        <h1 id="imgname">{{display_word}}</h1>
        <br> <br>
        <button class="pbtn" onclick="prev()">❮❮❮❮❮</button>

        <form class="probtn" action="" method="POST">
        {% csrf_token %}
        <button class="probtn" type="submit" name="btnform1">click and pronounce</button>
        </form>
        
			  <button class="nbtn" onclick="next()">❯❯❯❯❯</button>
			</div>

			
		</div>


 
</div>+
 

<div>

</body>
<html>

              """
    return HttpResponse(diction)


def test(request):
    context = {}
    template = Template("My name is {{ my_name }}.")
    #a1 = "hello am test1 hello am test1 hello am test1 how many times i want to say"
    a2 = "hello am test2"
    context["imgop"]= "https://firebasestorage.googleapis.com/v0/b/health-report-334d5.appspot.com/o/Images%2Fone.png?alt=media&token=25e2a26b-bcdc-4afb-a3e3-22368abdba13"
    #context["imgop"] = "C:/1 Routine use/1_html_css_js/00001SPROUD_KNOWLEDGElste/static/images/Sproud_Knowledge.png";
    #t_t_s(a1)
    if request.method == 'POST' and 'btntestform1' in request.POST:
        context["imgop"]= "https://firebasestorage.googleapis.com/v0/b/health-report-334d5.appspot.com/o/Images%2Fone.png?alt=media&token=25e2a26b-bcdc-4afb-a3e3-22368abdba13"
    
        return render(request,"test.html",context)
    
    return render(request,"test.html")


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
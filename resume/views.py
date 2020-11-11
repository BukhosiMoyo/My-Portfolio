from django.shortcuts import render, redirect
from .models import Person, Social, Skill, Education, Experience, Stat, ImagePortfolio, SliderPortfolio, YoutubeVideoPortfolio, LocalVideoPortfolio
from django.views.generic import UpdateView
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail, BadHeaderError
from .forms import ContactForm


""" 
Context ={} is being used as a context dictionary to make to code look a bit cleaner and easier to understand.


"""


#Home page Views 

def HomeView(request):
    persons = Person.objects.first()
    socials = Social.objects.all()

    context = {'persons':persons, 'socials': socials}
    return render(request, "resume/home.html", context)

#About page Fuction based View 

def AboutView(request):
    persons = Person.objects.first()
    skills = Skill.objects.all()
    experiences = Experience.objects.all()
    education = Education.objects.all()
    stat = Stat.objects.first()

    context = {'persons':persons,
                'skills':skills,
                'experiences':experiences,
                'education':education,
                'stat':stat,
    
        }
    return render(request, "resume/about.html", context)


#Portfolio page unction based view
def PortfolioView(request):
    image_portfolio = ImagePortfolio.objects.all()
    slider_portfolio = SliderPortfolio.objects.all()
    local_video_portfolio = LocalVideoPortfolio.objects.all()
    youtube_portfolio = YoutubeVideoPortfolio.objects.all()



    context = {'image_portfolio':image_portfolio,
                'slider_portfolio': slider_portfolio,
                'local_video_portfolio':local_video_portfolio,
                'youtube_portfolio':youtube_portfolio,
                }
    return render(request, "resume/portfolio.html", context)


#Contact me page Fuction based view 
def ContactView(request):
    persons = Person.objects.first()
    socials = Social.objects.all()
    form = ContactForm()

    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['bukhosi@symaxx.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('home')


    context={'persons': persons, 'socials':socials, 'form':form}
    return render(request, "resume/contact.html", context)

""" ######################## END FRONT VIEWS ############################ """

#These will all be dashboard view to make sure that we have easier way to edit and change our portfolio

class PortfolioEdit(UpdateView):
    model = Person
    template_name = "resume/portfolio-edit.html"
    fields = '__all__'
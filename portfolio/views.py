from django.shortcuts import render
from .forms import ContactForms
from .models import Networks,Author,Skills,Resume,Text

def index(request):
  author=Author.objects.all()[0]
  network=Networks.objects.all()
  skills=Skills.objects.all()
  resume=Resume.objects.all()
  txt=Text.objects.all()


  if request.method == 'POST':

    form=ContactForms(request.POST)

    if form.is_valid():
      form.save()

  form=ContactForms()
  return render(request, 'index.html',{'forms':form,"icon":network,"author":author,"skills":skills,"resume":resume,"txt":txt})

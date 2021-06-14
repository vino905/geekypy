from django.shortcuts import render, HttpResponse
from django.core.mail import send_mail
from django.views.generic import ListView , CreateView
from .models import Ebooks,Firstyear
from django.core.paginator import Paginator
from .models import Cs2Paper,Cs3Paper,Cs4Paper
from .models import It2Paper,It3Paper,It4Paper
from .models import Cve2Paper,Cve3Paper,Cve4Paper
from .models import Che2Paper,Che3Paper,Che4Paper
from .models import Ee2Paper,Ee3Paper,Ee4Paper
from .models import Ece2Paper,Ece3Paper,Ece4Paper
from .models import Me2Paper,Me3Paper,Me4Paper
from .models import Pythonproject,Cproject,Guiproject,Webdevlopment,Ethical
from .models import Ccodes


# from django.core.paginator import Paginator
class HomeView(ListView):
    model = Pythonproject
    template_name = 'pythonproject.html'
    context_object_name = "blog_entries"
    paginate_by = 3

# class HomeView(ListView):
#     model = Paper
#     template_name = 'cs.html'
#     context_object_name = "allPapers"
#     paginate_by = 3






class CreateEntryView(CreateView):
    model = Pythonproject
    template_name = 'create_entry.html'
    fields = ['Title', 'Text']

    def form_valid(self , form):
       
        return super().form_valid(form)   

# Create your views here.
def home(request):
    return render(request,'home.html')

def ccodes(request):
    page_obj= Ccodes.objects.all()
    context= {'page_obj': page_obj}
    paginator = Paginator(page_obj, 4) # Show 25 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'ccodes.html', {'page_obj': page_obj})
    

def c1codes(request):
    return render(request,'c1codes.html')     

def pythoncodes(request):
    return render(request,'pythoncodes.html')    

def javacodes(request):
    return render(request,'javacodes.html')        
    
def dsacodes(request):
    return render(request,'dsacodes.html')   


def cproject(request):
    page_obj= Cproject.objects.all()
    context= {'page_obj': page_obj}
    paginator = Paginator(page_obj, 4) # Show 25 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'cproject.html', {'page_obj': page_obj})

def ethicalhacking(request):
    page_obj= Ethical.objects.all()
    context= {'page_obj': page_obj}
    paginator = Paginator(page_obj, 4) # Show 25 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'ethicalhacking.html', {'page_obj': page_obj})          
      

def guiproject(request):
    page_obj= Guiproject.objects.all()
    context= {'page_obj': page_obj}
    paginator = Paginator(page_obj, 4) # Show 25 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'guiproject.html', {'page_obj': page_obj})
          
    

def pythonproject(request):
    page_obj= Pythonproject.objects.all()
    context= {'page_obj': page_obj}
    paginator = Paginator(page_obj, 4) # Show 25 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'pythonproject.html', {'page_obj': page_obj})
           

def webdevlopmentproject(request):
    page_obj= Webdevlopment.objects.all()
    context= {'page_obj': page_obj}
    paginator = Paginator(page_obj, 4) # Show 25 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'webdevlopmentproject.html', {'page_obj': page_obj})
          
          
    
def ebooks(request):
    page_obj= Ebooks.objects.all()
    context= {'page_obj': page_obj}
    paginator = Paginator(page_obj, 4) # Show 25 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'ebooks.html', {'page_obj': page_obj})
          

def contact (request):
    if request.method == "POST":
        name = request.POST ['name']
        email = request.POST ['email']
        college = request.POST ['college']
        city = request.POST ['city']
        issue = request.POST ['issue']

       #send an email 
        send_mail (
           name , #subject
           issue , #message
           email, #from email
          ['geekypy@gmail.com']  , #to email
        )
        return render (request , 'contact.html' , {'name': name})

    else : 
        return render (request , 'contact.html' , {})   

def firstyear(request):
    page_obj= Firstyear.objects.all()
    context= {'page_obj': page_obj}
    paginator = Paginator(page_obj, 6) # Show 25 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'firstyear.html', {'page_obj': page_obj})

         



def secondyear(request):
    return render(request,'secondyear.html')      

def thirdyear(request):
    return render(request,'thirdyear.html')      

def fourthyear(request):
    return render(request,'fourthyear.html')   

      

def it2(request):
    page_obj= It2Paper.objects.all()
    context= {'page_obj': page_obj}
    paginator = Paginator(page_obj, 6) # Show 25 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'it2.html', {'page_obj': page_obj})

   


def it3(request):
    page_obj= It3Paper.objects.all()
    context= {'page_obj': page_obj}
    paginator = Paginator(page_obj, 6) # Show 25 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'it3.html', {'page_obj': page_obj})




def it4(request):
    page_obj= It4Paper.objects.all()
    context= {'page_obj': page_obj}
    paginator = Paginator(page_obj, 6) # Show 25 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'it4.html', {'page_obj': page_obj})


    


def cs2(request):
    page_obj= Cs2Paper.objects.all()
    context= {'page_obj': page_obj}
    paginator = Paginator(page_obj, 6) # Show 25 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'cs2.html', {'page_obj': page_obj})

    # return render(request,'cs.html', context) 
    

def cs3(request):
    page_obj= Cs3Paper.objects.all()
    context= {'page_obj': page_obj}
    paginator = Paginator(page_obj, 6) # Show 25 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'cs3.html', {'page_obj': page_obj})
    



def cs4(request):
    page_obj= Cs4Paper.objects.all()
    context= {'page_obj': page_obj}
    paginator = Paginator(page_obj, 6) # Show 25 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'cs4.html', {'page_obj': page_obj})
         


def che2(request):
    page_obj= Che2Paper.objects.all()
    context= {'page_obj': page_obj}
    paginator = Paginator(page_obj, 6) # Show 25 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'che2.html', {'page_obj': page_obj})
         


def che3(request):
    page_obj= Che3Paper.objects.all()
    context= {'page_obj': page_obj}
    paginator = Paginator(page_obj, 6) # Show 25 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'che3.html', {'page_obj': page_obj})
    



def che4(request):
    page_obj= Che4Paper.objects.all()
    context= {'page_obj': page_obj}
    paginator = Paginator(page_obj, 6) # Show 25 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'che4.html', {'page_obj': page_obj})
    


def cve2(request):
    page_obj= Cve2Paper.objects.all()
    context= {'page_obj': page_obj}
    paginator = Paginator(page_obj, 6) # Show 25 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'cve2.html', {'page_obj': page_obj})
          


def cve3(request):
    page_obj= Cve3Paper.objects.all()
    context= {'page_obj': page_obj}
    paginator = Paginator(page_obj, 6) # Show 25 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'cve3.html', {'page_obj': page_obj})
    



def cve4(request):
    page_obj= Cve4Paper.objects.all()
    context= {'page_obj': page_obj}
    paginator = Paginator(page_obj, 6) # Show 25 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'cve4.html', {'page_obj': page_obj})
       

def ece2(request):
    page_obj= Ece2Paper.objects.all()
    context= {'page_obj': page_obj}
    paginator = Paginator(page_obj, 6) # Show 25 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'ece2.html', {'page_obj': page_obj})
        


def ece3(request):
    page_obj= Ece3Paper.objects.all()
    context= {'page_obj': page_obj}
    paginator = Paginator(page_obj, 6) # Show 25 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'ece3.html', {'page_obj': page_obj})
 


def ece4(request):
    page_obj= Ece4Paper.objects.all()
    context= {'page_obj': page_obj}
    paginator = Paginator(page_obj, 6) # Show 25 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'ece4.html', {'page_obj': page_obj})
   

def ee2(request):
    page_obj= Ee2Paper.objects.all()
    context= {'page_obj': page_obj}
    paginator = Paginator(page_obj, 6) # Show 25 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'ee2.html', {'page_obj': page_obj})
    


def ee3(request):
    page_obj= Ee3Paper.objects.all()
    context= {'page_obj': page_obj}
    paginator = Paginator(page_obj, 6) # Show 25 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'ee3.html', {'page_obj': page_obj})
  



def ee4(request):
    page_obj=Ee4Paper.objects.all()
    context= {'page_obj': page_obj}
    paginator = Paginator(page_obj, 6) # Show 25 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'ee4.html', {'page_obj': page_obj})
   

def me2(request):
    page_obj= Me2Paper.objects.all()
    context= {'page_obj': page_obj}
    paginator = Paginator(page_obj, 6) # Show 25 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'me2.html', {'page_obj': page_obj})
    


def me3(request):
    page_obj= Me3Paper.objects.all()
    context= {'page_obj': page_obj}
    paginator = Paginator(page_obj, 6) # Show 25 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'me3.html', {'page_obj': page_obj})
  



def me4(request):
    page_obj= Me4Paper.objects.all()
    context= {'page_obj': page_obj}
    paginator = Paginator(page_obj, 6) # Show 25 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'me4.html', {'page_obj': page_obj})
  





def dowmload(request,path):
    file_path=os.path.join(settings.MEDIA_ROOT,path)  
    if os.path.exists(file_path):
        with open(file_path,'rb')as fh:
            response=HttpResponse(fh.read(),content_type="application/fileupload")  
            response['content-Disposition']='inline;filename=' +os.path.basename(file_path)
            return response

    raise Http404        


def search(request):
    query=request.GET.get('query',False)
    # blog_entries=Entry.objects.all()
    blog_entries=Entry.objects.filter(Title__icontains=query)
    params={'blog_entries':blog_entries}
    return render(request,'search.html',params )  
   
def ebookssearch(request):
    query=request.GET.get('query',False)
    # blog_entries=Entry.objects.all()
    page_obj=Ebooks.objects.filter(title__icontains=query)
    params={'page_obj':page_obj}
    return render(request,'ebookssearch.html',params )  
       
    

# def free(request):
#     # allPapers= Paper.objects.all()
#     context= {'allPapers': Paper.objects.all()}

#     return render(request,'free.html', context)  

    


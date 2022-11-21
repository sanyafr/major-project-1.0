from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from main.models import Career

# Create your views here.
def homepage(request):
  return render(request, template_name='main/home.html')

def companiespage(request):
  return render(request, template_name='main/companies.html')

def studentspage(request):
  return render(request, template_name='main/students.html')

def dashboard(request):
  if request.method == 'GET':
    careers = Career.objects.exclude(applicant=request.user)
    return render(request, template_name='main/dashboard.html', context={'careers' : careers})
  if request.method == 'POST':
    applied_career = request.POST.get('applied-career')
    if applied_career:
      applied_career_object = Career.objects.get(name=applied_career)
      applied_career_object.applicant = request.user
      applied_career_object.save()
      messages.success(request,f'Congratulations! You have applied for {applied_career_object.name}')
    return redirect('dashboard')

def appliedcareers(request):
  if request.method == 'GET':
    careers = Career.objects.filter(applicant=request.user)
    return render(request, template_name='main/applied_careers.html', context={'careers' : careers})

def loginpage(request):
  if request.method == 'GET':
    return render(request, template_name='main/login.html')
  if request.method == 'POST':
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(username=username, password=password)
    if user is not None:
      login(request, user)
      messages.success(request,f'Logged in as {user.username}')
      return redirect('dashboard')
    else:
      messages.error(request,f'Account login was unsuccessful due to some errors')
      return redirect('login')

def registerpage(request):
  if request.method == 'GET':
    return render(request, template_name='main/register.html')
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      form.save()
      username = form.cleaned_data.get('username')
      password = form.cleaned_data.get('password1')
      user = authenticate(username=username, password=password)
      login(request,user)
      messages.success(request,f'You have registered your account successfully! Logged in as {user.username}')
      return redirect('home')
    else:
      messages.error(request,f'Account registration was unsuccessful due to some errors')
      return redirect('register')

def rulespage(request):
  return render(request, template_name='main/rules.html')

def preppage(request):
  return render(request, template_name='main/prep.html')

def testpage(request):
  return render(request, template_name='main/test.html')

def logoutpage(request):
  logout(request)
  messages.success(request,f'Logged Out Successfully!')
  return redirect('home')

from .functions import extract_text_from_pdf,extract_emails,extract_phone_number,extract_names
import PyPDF2

from mysite.forms import StudentForm,Form2
from django.core.files.storage import default_storage
def index(request):  
    if request.method == 'POST':  
        student = StudentForm(request.POST, request.FILES)  
        if student.is_valid(): 
            file = request.FILES['file']
            file_name = default_storage.save(file.name, file)

            #filename = request.FILES['file'].name
            pdfFileObj = open(file_name, 'rb')
            pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
            pageObj = pdfReader.getPage(0)
            text = (pageObj.extractText())
            
            pno = extract_phone_number(text)
            email = extract_emails(text)
            name = extract_names(text)
            return render(request,"form2.html",{'pno':pno,'email':email,'name':name})  
    else:  
        student = StudentForm()  
        return render(request,"index.html",{'form':student})  
   
from django.shortcuts import render, HttpResponse, redirect,HttpResponseRedirect
from Accounts.models import *
from Home.models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# Create your views here.
@login_required(login_url='/account/login-auth')
def home(request):
    
       
    user_obj = request.user.usersignup
    cat_obj = Category.objects.filter(cust=user_obj)
    phos = Photo.objects.filter(Category=cat_obj)
    category = request.GET.get('category')
    if category == None:
        photos = Photo.objects.filter(custphoto=user_obj)
    else:
        photos = Photo.objects.filter(Category__name=category) 
    context = {'cata': cat_obj, 'poths':photos}
    
    return render(request, 'home/home.html',context)

@login_required(login_url='/account/login-auth')
def addphotos(request):
    try:
        user_obj = request.user.usersignup
        cat_obj = Category.objects.filter(cust=user_obj)
        
        
        if request.method == 'POST':
            catery = request.POST.get('category')
            catery_new = request.POST.get('Category_new')
            image = request.FILES.getlist('image')

            if catery != 'none':
                category = Category.objects.get(id=cat_obj)
            elif catery_new  != '':
                category , create = Category.objects.get_or_create(name=catery_new,cust=user_obj)
            else:
                category = None
            for img in image:
                photo = Photo.objects.create(
                    custphoto=user_obj,
                    Category = category,
            
                    image = img,
                )
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        
        
    except Exception as e:
        print(e)
    
 
    return render(request, 'home/addphotos.html',{'cata': cat_obj})

@login_required(login_url='/account/login-auth')
def photov(request, pk):
    try:
        
        user_obj = request.user.usersignup
        cat_obj = Category.objects.filter(cust=user_obj)

        photo = Photo.objects.get(id=pk)
        if photo.Category.cust != request.user.usersignup:
            return HttpResponse ("you are not authorised to delete this item")

    

    
        context = {'photos':photo,'cata': cat_obj}
    except Exception as e:
        print(e)
    return render(request, 'home/photoview.html', context)

@login_required(login_url='/account/login-auth')
def deletev(request, pk):
    try:
      
    
        delete = Photo.objects.get(id=pk)
        if delete.Category.cust != request.user.usersignup:
            return HttpResponse ("you are not authorised to delete this item")
        delete.delete()
    except Exception as e:
        print(e)
    
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required(login_url='/account/login-auth')    
def deletecat(request, pk):
    try:
        delete = Category.objects.get(id=pk)
        if delete.cust != request.user.usersignup:
            return render(request,'home/errorpage.html')
        delete.delete()
  
   
    
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    except Exception as e:
        print(e)
    return render(request,'home/errorpage.html')

    


def error(request):
    return render(request,'home/errorpage.html')
from django.shortcuts import render
from django.db.models import Max
from .models import *
from django.contrib.auth import logout

from django.shortcuts import render, redirect
from django.utils import timezone
from django.shortcuts import render,redirect,get_object_or_404
from .models import Instructor, Slot
from django.http import HttpResponse,JsonResponse


def index(request):
    a = Instructor.objects.all()
    return render(request,'index.html',{"a":a})

def login(request):
    return render(request,'login.html')

from django.shortcuts import render, redirect
from .models import Student

def register(request):
    if request.method == 'POST':
        # Retrieve data from the form submission
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        phone_number = request.POST['phone_number']
        email = request.POST['email']
        address = request.POST['address']
        #  instructor_id = request.POST['instructor_id']
        birthcertif = request.FILES.get('birthcertif')
        adaar = request.FILES.get('adaar')
        sslc = request.FILES.get('sslc')
        image = request.FILES.get('image')
        password=request.POST['password']

        # Create a new student object
        student = Student(
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number,
            email=email,
            address=address,
            birthcertif=birthcertif,
            adaar=adaar,
            sslc=sslc,
            image=image,
            password=password
        )

        # Set the instructor based on the selected ID
        # if instructor_id:
        #     student.instructor_id = instructor_id

        # Save the student object to the database
        student.save()

        # Redirect to the student list page
        return redirect('/')

    # If the request method is GET, render the registration form
    instructors = Instructor.objects.all()
    context = {'instructors': instructors}
    return render(request, 'register.html', context)



# Create your views here.
from django.shortcuts import render, redirect
from .models import Instructor

def register_instructor(request):
    if request.method == 'POST':
        # Retrieve data from the form submission
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        area = request.POST['area']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        image = request.FILES.get('image')
        image2 = request.FILES.get('image2')
        image3 = request.FILES.get('image3')
        password=request.POST['password']

        # Create a new instructor object
        instructor = Instructor(
            first_name=first_name,
            last_name=last_name,
            phone_number= phone_number,
            email=email,
            image=image,
            password=password,
            image2=image2,
            image3=image3,
            area=area
        )

        # Save the instructor object to the database
        instructor.save()
        msg={'msg':'Account Creation Successful'}

        # Redirect to the instructor list page
        return render(request,'instructor.html',msg)

    # If the request method is GET, render the registration form
    return render(request, 'instructor.html')

def login(request):
    if request.method == "POST":

        email = request.POST.get('email')
        password = request.POST.get('password')
        obj1 = Instructor.objects.filter(email=email, password=password)
        obj2 = Student.objects.filter(email=email, password=password)
        if obj1.filter(email=email, password=password).exists():
            for i in obj1:
                id = i.id
                z = i.status
                
                request.session['email'] = email
                request.session['password'] = password
                request.session['id'] = id
                request.session['status'] = z
                
            # context ={'a': obj }
            if z == 'Verified':
                return redirect('/instructor_home')

            else:
                msg1='Your Account Verification Is Under Processing'
                return render(request,'login.html',{'msg1':msg1})
        elif obj2.filter(email=email, password=password).exists():
            for i in obj2:
                id = i.id
                
                
                request.session['email'] = email
                request.session['password'] = password
                request.session['id'] = id
                return redirect('/student_home')
        else:
            context = {'msg': 'Invalid Credentials'}
            return render(request,'login.html',context)
    return render(request, 'login.html')

def instructor_home(request):
    id=request.session['id']
    a=Instructor.objects.filter(id=id)
    b=Bookslot.objects.filter(instructor=id,status='Booked')
    all_data={'a':a,'b':b}
    return render(request,'instructor_home.html',all_data)

def logout_view(request):
    logout(request)
    return redirect('/')

def student_home(request):
    id=request.session['id']
    a=Student.objects.filter(id=id)
    b=Instructor.objects.all()
    all={
        'a':a,
        'b':b
    }
    return render(request,'student_home.html',all)


def add_slot(request):
    if request.method=='POST':
        instructor_id =request.session['id']
    # Retrieve the instructor based on the ID passed in the URL
        instructor = Instructor.objects.get(id=instructor_id)
        slottime=request.POST.get('slottime')
    # Create a new slot object and set the instructor and time
        new_slot = Slot(instructor=instructor, slottime=slottime)

    # Save the new slot object to the database
        new_slot.save()

    # Redirect to the instructor's detail page
        return redirect('/instructor_home')
    return render(request,'addslot.html')


def book_slot(request,id):
    if request.method == 'POST':
        # Get the selected slot ID from the form data
        slot_id = request.POST.get('slot')
        slot=Slot.objects.get(id=slot_id)

        # Get the student and instructor objects
        student_id=request.session['id']
        student = Student.objects.get(id=student_id)
        instructor = Instructor.objects.get(id=int(id))

        # Create a new Bookslot object with the selected slot, student, and instructor
        bookslot = Bookslot.objects.create(
            student=student,
            slot=slot,
            instructor=instructor,
            status='Booked'
        )

        # Update the status of the booked slot to "Booked"
        Slot.objects.filter(pk=slot_id).update(status='Booked')

        # Redirect the user to a success page
        return redirect('/student_home')

    else:
        # Get a list of all available slots
        slots = Slot.objects.filter(instructor=id,status='Not Booked')

        # Render the booking form template with the available slots
        return render(request, 'book_slot.html', {'slots': slots})
    


def profile(request):
    # u=request.session['email']
    # display=Student.objects.filter(email=u)
    # ss={'profile':display}
    return render(request,'editpage.html')

def updateprofile(request):
    return render(request,'updateprofile.html')
def editstudent(request):
    if request.method == 'POST':
        id = request.session['id']
        user = Student.objects.filter(id=id)
        up = Student.objects.get(id=id)
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        address = request.POST.get('address')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('email')

        if 'image' in request.FILES:
            image = request.FILES['image']
            up.image = image

        up.first_name = first_name
        up.last_name = last_name
        up.address = address
        up.phone_number = phone_number
        up.email = email

        up.save()
        ud = Student.objects.filter(email=request.session['email'])
        context = {'details': ud,
                   'user': user,
                   'msg': 'Profile Details Updated'}

        return render(request, 'editprofile-student.html', context)
    else:
        id = request.session['id']
        up = Student.objects.filter(id=id)
        user = Student.objects.filter(id=id)
        all_data = {
            'user': user,
            'details': up,
        }
        return render(request, 'editprofile-student.html', all_data)

    
def view_license(request, provider_id):
    provider = get_object_or_404(Instructor, pk=provider_id)
    with open(provider.image2.path, 'rb') as f:
        response = HttpResponse(f.read(), content_type='application/pdf')
        response['Content-Disposition'] = f'inline; filename={provider.first_name}_image2.pdf'
        return response
def search(request):
    area = request.GET.get('area')
    result = Instructor.objects.filter(area=area)
    all_data = {'result': result}
    return render(request,'search.html',all_data)


def changepassword_user(request):
    id = request.session['id']
    print(id)
    user = Student.objects.filter(id=id)
    all = {
        'user': user,
    }
    if request.method == 'POST':
        email = request.session['email']
        new_password = request.POST.get('new_password')
        current_password = request.POST.get('current_password')
        print('Email Is:' + email)
        print("Current_password" + str(current_password))
        try:

            ul = Student.objects.get(email=email, password=current_password)

            if ul is not None:
                ul.password = new_password  # change field
                ul.save()
                msg = 'Password Changed Successfully'
                all = {
                    'user': user,
                    'msg': msg
                }
                return render(request, 'change_password_user.html', all)
            else:
                context = 'Your Old Password is Wrong'
                all = {
                    'user': user,
                    'msg': context
                }
                return render(request, 'change_password_user.html', all)

        except Student.DoesNotExist:
            context = 'Your Old Password is Wrong'
            all = {
                'user': user,
                'msg': context
            }
            return render(request, 'change_password_user.html', all)
    else:
        return render(request, 'change_password_user.html', all)
def changepassword_instructor(request):
    id = request.session['id']
    print(id)
    user = Student.objects.filter(id=id)
    all = {
        'user': user,
    }
    if request.method == 'POST':
        email = request.session['email']
        new_password = request.POST.get('new_password')
        current_password = request.POST.get('current_password')
        print('Email Is:' + email)
        print("Current_password" + str(current_password))
        try:

            ul = Student.objects.get(email=email, password=current_password)

            if ul is not None:
                ul.password = new_password  # change field
                ul.save()
                msg = 'Password Changed Successfully'
                all = {
                    'user': user,
                    'msg': msg
                }
                return render(request, 'change_password_instructor.html', all)
            else:
                context = 'Your Old Password is Wrong'
                all = {
                    'user': user,
                    'msg': context
                }
                return render(request, 'change_password_instructor.html', all)

        except Student.DoesNotExist:
            context = 'Your Old Password is Wrong'
            all = {
                'user': user,
                'msg': context
            }
            return render(request, 'change_password_instructor.html', all)
    else:
        return render(request, 'change_password_instructor.html', all)


def editinstructor(request):
    if request.method == 'POST':
        id = request.session['id']
        user = Instructor.objects.filter(id=id)
        up = Instructor.objects.get(id=id)
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        area = request.POST.get('area')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('email')

        if 'image' in request.FILES:
            image = request.FILES['image']
            up.image = image

        up.first_name = first_name
        up.last_name = last_name
        up.area = area
        up.phone_number = phone_number
        up.email = email

        up.save()
        ud = Instructor.objects.filter(email=request.session['email'])
        context = {'details': ud,
                   'user': user,
                   'msg': 'Profile Details Updated'}

        return render(request, 'editprofile-instructor.html', context)
    else:
        id = request.session['id']
        up = Instructor.objects.filter(id=id)
        user = Instructor.objects.filter(id=id)
        all_data = {
            'user': user,
            'details': up,
        }
        return render(request, 'editprofile-instructor.html', all_data)

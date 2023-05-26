
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="drapp/index"),
    path('login',views.login,name="drapp/login"),
    path('register',views.register,name="drapp/register"),
    path('instructor',views.register_instructor),
    path('instructor_home',views.instructor_home),
    path('logoutt',views.logout_view),
    path('student_home',views.student_home),
    path('addslot',views.add_slot),
    path('book_slot/<int:id>',views.book_slot),
    path('editpage',views.profile,name="drapp/editpage"),
    path('updateprofile',views.editstudent),
    path('view_license/<int:provider_id>/', views.view_license, name='view_license'),
    path('search',views.search,name='search'),
    path('changes',views.changepassword_user),
    path('changei',views.changepassword_instructor),
    path('updateinstructor',views.editinstructor),


    

    

]
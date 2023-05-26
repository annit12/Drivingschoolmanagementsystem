from django.urls import reverse
from django.db import models

class Instructor(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20)
    image= models.ImageField(upload_to="media/instructors/",default="")
    email = models.EmailField()
    area=models.CharField(max_length=20,default='nothing')
    password=models.CharField(max_length=20,default='nothing')
    image2= models.ImageField(upload_to="media/instructors/",default="")
    image3= models.ImageField(upload_to="media/instructors/",default="")
    is_verified = models.BooleanField('Verification Status', default=False)
    status=models.CharField('Current Status',max_length=20,default='Not Verified')

    



    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('view_license/<int:provider_id>/', self.admin_site.admin_view(self.view_license), name='view_license'),
        ]
        return my_urls+urls

    class Meta:
        verbose_name = 'Verify Instructor'

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    # instructor = models.ForeignKey(Instructor, on_delete=models.SET_NULL, null=True, blank=True)
    address=models.CharField(max_length=70,null=True)
    image= models.ImageField(upload_to="drapp/static/img",default="")
    birthcertif=models.ImageField('Your Image in jpg/png Format',upload_to='certificates/',null=True)
    adaar=models.ImageField('Your Image in jpg/png Format',upload_to='aadar/',null=True)
    sslc=models.ImageField('Your Image in jpg/png Format',upload_to='sslc/',null=True)
    password=models.CharField(max_length=20,default='nothing')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = 'View Student Profile'


class Payment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student} - {self.amount}"
    

class Slot(models.Model):
    instructor=models.ForeignKey(Instructor,on_delete=models.CASCADE)
    slottime=models.TimeField()
    status=models.CharField(max_length=20,default='Not Booked')

    class Meta:
        verbose_name = 'View Slot Deatail'

class Bookslot(models.Model):
    student=models.ForeignKey(Student,on_delete=models.CASCADE)
    slot=models.ForeignKey(Slot,on_delete=models.CASCADE)
    instructor=models.ForeignKey(Instructor,on_delete=models.CASCADE,null=True,blank=True)
    status=models.CharField(max_length=20,default='Not Booked')

    class Meta:
        verbose_name = 'View Booking Detail'


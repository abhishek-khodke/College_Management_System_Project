from django.db import models

# Create your models here.

class ActivePersons(models.Manager): # Custom Model Manager
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True) # Model.objects.all()


class Person(models.Model): # Table # app1_person
    # default id
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    mobile_num = models.IntegerField()
    address = models.CharField(max_length=100)
    email = models.EmailField(null=True)
    date_joined = models.DateTimeField(auto_now=True, null=True)
    date_updated = models.DateTimeField(auto_now_add=True, null=True)
    is_active = models.BooleanField(default=True)
    activep = ActivePersons()
    objects = models.Manager()

    class Meta:
        db_table = "person"
    
    def __str__(self):
        return f"{self.name}  -- {self.address}"

    def show_details(self):
        print(f"""-----------------
Person Name:- {self.name}
Person Age:- {self.age}
Person Mobile:- {self.mobile_num}
Person Address:- {self.address}""")

    @classmethod
    def get_data_above_age(cls):
        return cls.objects.filter(age__gte = 25)   #gt, gte, lt, lts, startswith, endswiths


    @classmethod
    def get_avg_age(cls):
        '''average age of all person'''
        data = Person.objects.all().values("id", "name", "age")
        lst = list(map(lambda x : x['age'], list(data)))
        return sum(lst)//len(lst)

    @classmethod
    def get_active_data(cls):
        return cls.objects.filter(is_active=True)




class CommonClass(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class College(CommonClass):
    name = models.CharField(max_length=100)
    adr = models.CharField(max_length=500)
    est_date = models.DateField(auto_now=True)

    class Meta:
        db_table = "college" 

class Principal(CommonClass):
    exp = models.FloatField()
    qual = models.CharField(max_length=50)
    college = models.OneToOneField(College, on_delete=models.CASCADE, related_name="princi", null = True)

    
    class Meta:
        db_table = "principal" 


class Department(CommonClass):
    dept_str = models.IntegerField()
    college = models.ForeignKey(College, on_delete=models.CASCADE, related_name="depts")
    
    class Meta:
        db_table = "dept" 
        # unique_together = (("name", "college"),)


class Student(CommonClass):
    marks = models.IntegerField()
    age = models.IntegerField()
    dept = models.ForeignKey(Department, on_delete=models.CASCADE, related_name="studs", null = True) #  OneToManyField

    
    class Meta:
        db_table = "student" 


class Subjects(CommonClass):
    is_practical = models.BooleanField(default=False)
    student = models.ManyToManyField(Student, related_name="subjs")
    dept = models.ForeignKey(Department, on_delete=models.CASCADE, related_name="subjs")


    
    class Meta:
        db_table = "subject" 


# ------------------------------------------------------------------------
# from django.db import models


class FuelType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class CarModel(models.Model):
    name = models.CharField(max_length=255)
    fueltype = models.ManyToManyField(FuelType, related_name='carmodels')

    def __str__(self):
        return self.name
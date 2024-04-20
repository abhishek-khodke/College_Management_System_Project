# exec(open(r'C:\Python\Topic_Django\first_project\app2\db_shell.py').read())
from app2.models import *
from django.contrib.auth.models import User

# to get all data
# objs = Person.objects.all() #queryset - list
# print(objs.query)

# print(list(objs))

# for person in objs:
#     print(person.__dict__)

# to get first record
# first_record = Person.objects.first()
# print(first_record)

# to get record by id
# obj = Person.objects.get(id = 2) #single record
# print(obj)

# try:
#     obj = Person.objects.get(id = 4)
#     print(obj)
# except Person.DoesNotExist:
#     print("Record does not exist")

# to get multiple record by passing fieldname

# objs = Person.objects.filter(age = 25, address = "Pune" )
# print(objs.query)

# modify existing data

# p1 = Person.objects.get(id = 5)
# print(p1.__dict__)
# print(p1.mobile_num)
# p1.mobile_num = 9511693197
# print(p1.__dict__)
# p1.save()

# p1.delete()

# save - 1st way
# p1 = Person(name = "ABC", age = 29, mobile_num = 7387023091, address = "Nanded" )
# p1.save()

# 2nd way to save data
# Person.objects.create(name = "XYZ", age = 23, mobile_num = 7387838917, address = "Channai")

# print(dir(Person.objects))

# bulk_create
# p1 = Person(name = "P", age = 27, mobile_num = 7387838911, address = "Pune" )
# p2 = Person(name = "Q", age = 18, mobile_num = 7387838912, address = "Banglore" )
# p3 = Person(name = "R", age = 37, mobile_num = 7387838913, address = "Channai" )
# p4 = Person(name = "S", age = 45, mobile_num = 7387838914, address = "Mumbai" )

# Person.objects.bulk_create([p1, p2, p3, p4])

# count
# print(Person.objects.count())

# to delete all records 
# Person.objects.all().delete()

# to delete multiple records
# Person.objects.filter(age = 25).delete()

# startswith
# print(Person.objects.filter(name__startswith = "A"))

# endswith
# print(Person.objects.filter(name__endswith = "s"))

# exclude
# print(Person.objects.exclude(name__startswith = "P"))

# exists
# print(Person.objects.filter(id = 1).exists())
# print(Person.objects.filter(name = "XYZ").exists())

# order_by
# print(Person.objects.all().order_by("id"))
# print(Person.objects.all().order_by("-id"))
# print(Person.objects.all().order_by("name"))
# print(Person.objects.all().order_by("-name"))




# Person.objects.get(id = 1).show_details()

# for per_objs in Person.objects.all():
#     per_objs.show_details()

# print(Person.get_data_above_age())



# from django.contrib.auth import get_user_model
# User = get_user_model()
# or
# from django.contrib.auth import User
# print(User.objects.all())

# print(Person.objects.all())
# print(Person.objects.filter(name__contains = "k"))

# data = Person.objects.all().values("id", "name", "age")
# print(data)
# for i in data:
#     print(i, type(i))

# names_list = []
# for i in data:
#     names_list.append(i["name"])
# print(names_list)

# print(list(data))

# lst = list(map(lambda x : x['age'], list(data)))
# print(lst)
# print(sum(lst)//2)
# print(sum(lst)//len(lst))

# data = Person.objects.all().values_list()
# print(data)
# print(list(data))

# data = Person.objects.all().values_list("name")  #list of tuples containing values only
# print(list(data))


# database change to Mysql
# User.objects.create_user(username ="Abhi", password = "Abhishek21@")

# print(Person.objects.all())

# delete - soft delete, hard delete

# data = Person.objects.filter(id__in=[3, 5]).update(is_active=False)
# print(data)
# for i in data:
#     i.is_active = False
#     i.save()

# exec(open(r'C:\Python\Topic_Django\first_project\app2\db_shell.py').read())

# p1 = Person.objects.get(id=3)
# p1.is_active = False
# p1.save()

# print(Person.objects.filter(is_active=True))
# print(Person.objects.filter(is_active=False))

# print(Person.get_active_data()) 

# print(Person.activep.all())

# # object replaced by activep

# print(Person.objects.all())

# exec(open(r'C:\Python\Topic_Django\first_project\app2\db_shell.py').read())

# clgs = College.objects.all()
# prnc = Principal.objects.all()
# depts = Department.objects.all()
# studs = Student.objects.all()
# subjs = Subjects.objects.all()


# print(clgs)
# print(prnc)
# print(depts)
# print(studs)
# print(subjs)

# for dept in depts:
#     print(dept.__dict__)

# clg = clgs[0] # G S Moze
# print(clg)


# Abhishek_obj = Principal.objects.first()
# print(Abhishek_obj.college)

# print(clg.department_set.all()) 

# dept = Department.objects.first()# EE
# print(dept.college)

# dept = Department.objects.get(id=3)

# print(dept.student_set.all())

# get all studs dept wise

# all_depts = Department.objects.all()
# d = {}
# for dept in all_depts:
    # print(dept)
    # print(f"Department Name:- {dept.name}, Studs:- {list(dept.student_set.all())}")
#     d[dept.name] = list(dept.student_set.all())
# print(d)

# s1 = Student.objects.get(id=6)  
# print(s1.dept)

# s1 = Student.objects.get(id=9)  
# print(s1.dept)

# get dept from stud
# studs = Student.objects.all()
# print(studs)
# stud_dept_dict = {}
# for stud in studs:
#     stud_dept_dict[stud.name] = stud.dept.name

# print(stud_dept_dict)


# clg = College.objects.get(id=1)
# print(clg.princi)

# print(clg.depts.all())

# dept = Department.objects.get(id=3)
# print(dept)
# print(dept.subjs.all())

# depts = Department.objects.all()
# for dept in depts:
#     print(dept.subjs.all())
#     pass

# print([list(dept.subjs.all()) for dept in Department.objects.all()])

# clg = College.objects.get(id=1)
# print(clg)

# studs_list = []
# for dept in College.objects.get(id=1).depts.all():
    # studs_list.extend(dept.studs.all())
# print(studs_list)

# print(clg.depts.all()[2].studs.all()[0])

# s1 = Student.objects.get(id=5)
# print(s1.dept)
# print(s1.dept.college)
# print(s1.dept.college.est_date)


##   Addition

# College.objects.create(name="MIT", adr="Kothrud")

# c1 = College.objects.get(id=1)  # MIT

# p1 = Principal(name="ABC", exp=20, qual="PHD", college=c1) # as it is pass object of college
# p1 = Principal(name="ABC", exp=20, qual="PHD", college_id=3) # pass college id, college_id
# p1.save()


# Department.objects.create(name="Production", dept_str=80, college=c1)

# Department.objects.create(name="Petrechemical", dept_str=60, college=c1) # college instance(college) ya college id(college_id)


# Student.objects.create(name="A", marks=44, age=18) # dept_id ya dept(dept object)
# Student.objects.create(name="B", marks=97, age=17)
# Student.objects.create(name="C", marks=49, age=19)

# s1, s2, s3 = Student.objects.filter(id__gt=9)
# print(s1, s2, s3)

# prod_dept = Department.objects.get(id=4)
# prod_dept.studs.add(s1)
# prod_dept.studs.add(s2, s3)  # one to many -- add students in departments

# print(dir(prod_dept.studs))

# select_related

# studs = Student.objects.all()
# print(studs)

# studs = Student.objects.all()
# for stud in studs:
#     print(stud.dept)

# studs = Student.objects.select_related("dept")  # 
# for stud in studs:
#     print(stud.dept.name)

# Many to Many

# exec(open(r'C:\Python\Topic_Django\first_project\app2\db_shell.py').read())

# c180 = CarModel.objects.create(name="C180")
# c200 = CarModel.objects.create(name="C200")
# print(CarModel.objects.all())
# c180 = CarModel.objects.get(name="C180")
# c200 = CarModel.objects.get(name="C200")

# gas = FuelType.objects.create(name="Gas")
# diesel = FuelType.objects.create(name="Diesel")
# hybrid = FuelType.objects.create(name="Hybrid")
# print(FuelType.objects.all())

# gas = FuelType.objects.get(name="Gas")
# diesel = FuelType.objects.get(name="Diesel")
# hybrid = FuelType.objects.get(name="Hybrid")
# print(c180.fueltype.all())

# c180.fueltype.add(gas)
# c180.fueltype.add(diesel, hybrid) # 1
# c200.fueltype.add(gas, diesel, hybrid) # 3

# c200.fueltype.create(name="Bio Diesel") # FuelType creation, assign to CarModel
 
# print(c200.fueltype.all())
# print(c180.fueltype.all())

# print(gas.carmodel_set.all()) # 

# print(gas.carmodels.all())

# print(CarModel.objects.filter(fueltype__name__startswith="D"))

# print(FuelType.objects.filter(carmodels__name__startswith="C").distinct())

# c180.fueltype.clear()

# print(Student.objects.filter(dept__name= "IT"))
# print(Student.objects.filter(dept__name__startswith="E"))

# print(Student.objects.filter(dept__college__name__in=["MIT", "G S MOZE"]))


# Raw SQL Queries

# First Way

# from django.db import connection
# cursor = connection.cursor()
# cursor.execute('''SELECT * FROM student''') # raw sql
# # data = cursor.fetchall()
# # print(data)
# data = cursor.fetchmany(3)
# print(data)
# data = cursor.fetchmany(3)
# print(data)

# Second Way

# data = Student.objects.raw('SELECT * FROM student')
# for i in data:
#     print(i)

# Multiple Database
# MySQL, SQLite

SECOND_DATABASE = "second_db"
# data = Student.objects.using(SECOND_DATABASE).all()
# print(data)

# data = Student.objects.using(SECOND_DATABASE).create()

# c1 = College.objects.using(SECOND_DATABASE).create(name="COEP", adr="Pune")
# d1 = Department.objects.using(SECOND_DATABASE).create(name="ENTC", dept_str=60, college=c1)
# s1 = Student.objects.using(SECOND_DATABASE).create(name="XYZ", marks=89, age=25, dept=d1)
# s2 = Student.objects.using(SECOND_DATABASE).create(name="PQR", marks=95, age=26, dept=d1)
# d1 = Department.objects.using(SECOND_DATABASE).get(id=1)
# subj1 = Subjects.objects.using(SECOND_DATABASE).create(name="Data Signal", is_practical=True, dept=d1)


# studs = Student.objects.using(SECOND_DATABASE).all()
# print(studs)
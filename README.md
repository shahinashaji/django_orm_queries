# Django ORM Queries

### Create Django Project 

#### Command

```bash
    django-admin startproject project_name
```
#### Example
```commandline
    django-admin startproject django_orm
```

### Create App (Create multiple apps)
#### Command

```bash
    python manage.py startapp app_name
```
#### Example
```commandline
    python manage.py startapp dml_operations
```
### Open Shell
#### Command

```bash
    python manage.py shell
```

**NOTE**

1. We can create multiple app for a project as modules.
---
### Create Table 

#### Syntax (Student Table)

````
class Student(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField()
    address = models.TextField()
    phone_number = models.CharField(max_length=10)
````

**NOTE**

1. The models.py hold the database table and the class name be the Table Name
2. Migrate the table using the following commands:
    #### Create migration file
    ```commandline
        python manage.py makemigrations
    ```
    #### Migrate changes to database
    ```commandline
        python manage.py migrate
    ```
---

### DML Operation (Operations Are Performed Using Shell)

1. #### Insertion (In Multi-line)

````
    >>> from dml_operations.models import Student 
    >>> student_object = Student(first_name='Shahina',last_name='PS', age=25,phone_number='9897654867')
    >>> student_object.save()
````
   or

#### Insertion (In Single Line)

````
    >>> from dml_operations.models import Student 
    >>> Student.objects.create(first_name='Milu',last_name='Balan', age=25,phone_number='9897650867',address='ABC') 
````

#### Add an extra field or attribute (city) to Student table (After adding make migrations)
````
    city = models.CharField(max_length=20, default='abc')
````
#### Insertion (In Single Line)

````
    >>> from dml_operations.models import Student 
    >>> Student.objects.create(first_name='Reshma',last_name='N', age=25,phone_number='9897690867',address='ABC', city='kkk') 

````
#### Insertion (In Multi-line)

````
    >>> from dml_operations.models import Student 
    >>> student_object = Student(first_name='Aiswarya',last_name='Vikraman', age=25,phone_number='9897604867',address='xyz', city='kkk')
    >>> student_object.save()
````


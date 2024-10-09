# 💀 ⛓️ Goth Store ⚰️🦇

## 🔗[PWS APPLICATION](http://kezia-salsalina-gothstore.pbp.cs.ui.ac.id)

<details>
<Summary><b>ASSIGNMENT 2</b></summary>

### 1. Implementation of the Checklist: Step-by-Step 📝
#### ✔️Create a new Django project.
- Create a new directory with the name ```"goth-store"```
- Open the terminal and create a virtual environment inside the directory by running this command below
    ```
    python3 -m venv env
    ```
- And activate it by
    ```
    env\Scripts\activate
    ```
- Create a file named requirements.txt inside the directory and fill it with some dependencies below
    ```
    django
    gunicorn
    whitenoise
    psycopg2-binary
    requests
    urllib3
    ```
- then, install them by running this command
    ```
    pip install -r requirements.txt
    ```
- Finally, create a Django project named goth-store by running the following command
    ```
    django-admin startproject goth_store .
    ```
- In ```settings.py```, add this following line of code to allow local host
    ```
    ALLOWED_HOSTS = ["localhost", "127.0.0.1"]`
    ```
#### ✔️Create an application with the name main in the project.
- Create a new application called main within the goth_store project by running this command
    ```
    python3 manage.py startapp main
    ```
- To register the main app, open the ```settings.py``` file located inside the goth_store project directory. Add ```'main'``` to the ```INSTALLED_APPS``` list, as shown below.
    ```
    INSTALLED_APPS = [
    ...,
    'main'
    ]
    ```
#### ✔️Perform routing in the project so that the application main can run
- Open the ```urls.py``` file inside the ```goth_store``` project and fill it with the code below. 
    ```py
    from django.contrib import admin
    from django.urls import path, include

    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include('main.urls')),
    ]
    ```
#### ✔️Create a model in the application main with the name Product and have the mandatory attributes
- In ```main/models.py```, define the Product model with the attributes name, price, and description
    ```py
    from django.db import models

    class Product(models.Model):
        name = models.CharField(max_length=100)
        price = models.IntegerField()
        description = models.TextField()
        gothness = models.IntegerField()
    ```
- After creating the model, run migrations to apply the changes to the database:
    ```
    python manage.py makemigrations
    python manage.py migrate
    ```
#### ✔️Create a function in ```views.py```to return to an HTML template that displays the name of the application and your name and class
- In ```main/views.py```, create a function that returns an HTML template:
    ```py
    from django.shortcuts import render

    def show_main(request):
        context = {
            'app_name': 'goth-store',
            'name': 'Kezia Salsalina Agtyra Sebayang',
            'class': 'PBD KKI'
        }

        return render(request, 'main.html', context)
    ```
- Create a ```template``` directory inside the ```main``` application directory and add a new file called ```main.html```. Then fill it with the codes below
    ```html
    <h1>{{ app_name }} </h1>
    <h5>Name: </h5>
    <p>{{ name }}</p>
    <h5>Class: </h5>
    <p>{{ class }}</p>
    ```
#### ✔️Create a routing in ```urls.py``` for the application ```main ```to map the function created in ```views.py```.
- Create a ```urls.py``` file for the main app. Here's how my ```main/urls.py``` look:
    ```py
    from django.urls import path
    from main.views import show_main

    app_name = 'main'

    urlpatterns = [
        path('', show_main, name='show_main'),
    ]
    ```
#### ✔️Perform deployment to PWS for the application that has been created so that it can be accessed by others via the Internet.
- Before deploying, create a new public GitHub repository named goth-store. Then, initialize the local directory goth-store as a Git repository.
- After making sure local repository is connected to the GitHub, do a add, commit, and push
- For deployment, create a PWS project named gothstore. Then add ```kezia-salsalina-gothstore.pbp.cs.ui.ac.id``` to ```ALLOWED_HOSTS``` in ```settings.py```. 
    ```
    ALLOWED_HOSTS = ["localhost", "127.0.0.1", "kezia-salsalina-gothstore.pbp.cs.ui.ac.id"]
    ```
- Finally, use the ```push``` command to push it to the PWS repository for deployment.

### 2. A diagram that contains the request client to a Django-based web application and the response it gives.

![alt text](images/diagram.png)
- The diagram explains the relationships between Django components:
    - urls.py: Matches the incoming URL request and routes it to the appropriate view.
    - views.py: Handles the logic, interacting with the models.py for data, then passes the data to the HTML template for rendering.
    - models.py: Handles database interactions, passing data back to views.py.
    - The HTML template renders the final response which is sent back to the client.

### 3. Explain the use of git in software development!
- Git is a widely used version control system in software development that helps manage and track changes in code. It allows multiple developers to collaborate efficiently by enabling them to work on different features or bug fixes in parallel. With Git, developers can commit changes, create branches for separate tasks, and merge them back into the main project while keeping a history of all changes. This makes it easier to revert to previous versions if needed and resolve conflicts that arise during collaboration. Overall, Git ensures better code management, collaboration, and project organization.

### 4. Why is Django used as the starting point for learning software development?
- Django is often used as a starting point for learning software development because it offers a comprehensive, beginner-friendly structure for building web applications. It includes built-in features like authentication, routing, and database management, reducing the need for external tools and allowing learners to focus on core development concepts. 

### 5. Why is the Django model called an ORM?
- The Django model is called an ORM (Object-Relational Mapper) because it acts as a bridge between the database and the code by mapping database tables to Python objects. In Django, each model corresponds to a table in the database, and the fields in the model represent the columns of that table. The ORM allows developers to interact with the database using Python code instead of writing raw SQL queries. This abstraction makes database operations like creating, reading, updating, and deleting records easier and more intuitive, while also ensuring that the code remains database-agnostic, meaning it can work with different types of databases without needing modification.
</details>

 <details>
<Summary><b>ASSIGNMENT 3</b></summary>

###  1. Explain why we need data delivery in implementing a platform.
- Data delivery is crucial in platform implementation because it enables communication between different components, services, or systems. Whether it’s between the front end and the back end, or between various microservices in a distributed architecture, data needs to be exchanged seamlessly for the platform to function properly. For example, user actions on the front end often require data from the server or database, which is then processed and delivered back to be displayed to the user. Data delivery also ensures that external systems or APIs can integrate with the platform to enhance its functionality, such as with payment gateways or external authentication services. Without efficient data delivery, a platform would fail to provide a cohesive user experience and proper functionality.

### 2. In your opinion, which is better, XML or JSON? Why is JSON more popular than XML?
- In my opinion, JSON is generally better than XML, especially in modern web development, because it is simpler, more lightweight, and easier to parse. JSON (JavaScript Object Notation) is more human-readable and aligns naturally with JavaScript, which makes it more suitable for web-based platforms. XML, on the other hand, tends to be more verbose and harder to read due to its nested structure and use of closing tags. While XML has its use cases, such as in configuration files or when document formatting is important, JSON has gained popularity because of its simplicity and efficiency. 

### 3. Explain the functional usage of the ```is_valid()``` method in Django forms. Why do we need this method in forms?
- The ```is_valid()``` method in Django forms is used to check whether the data provided in the form meets the validation rules defined for each form field. When you call ```is_valid()```, Django automatically runs through the validation logic for each field, ensuring that all the required fields are filled, and the data provided is in the correct format (e.g., checking if an email is valid or if a date is properly formatted). This method is necessary because it allows developers to ensure that the data they are working with is clean and valid before saving it to the database or processing it further. Without this check, invalid data might be processed or stored, leading to potential errors and inconsistencies in the application.

### 4. Why do we need ```csrf_token``` when creating a form in Django? What could happen if we did not use ```csrf_token``` on a Django form? How could this be leveraged by an attacker?
- The ```csrf_token``` is needed in Django forms to prevent Cross-Site Request Forgery (CSRF) attacks, which occur when malicious sites attempt to execute unauthorized actions on behalf of authenticated users. When a form is submitted in Django, the ```csrf_token``` ensures that the request originated from the correct website and not from a third-party attacker. If we did not include the ```csrf_token``` in forms, attackers could craft requests that perform actions on the website (e.g., deleting user data, making purchases) without the user’s consent. Without this security measure, an attacker could use social engineering tactics to trick users into clicking links that perform unwanted actions on websites where they are logged in, making the platform vulnerable to attacks.

### 5. Explain how you implemented the checklist above step-by-step
#### ✔️Create a form input to add a model object to the previous app.
- Create a new file in the main directory with the name ```forms.py``` and added the following code. 
    ```py
    from django.forms import ModelForm
    from main.models import Product

    class GothEntryForm(ModelForm):
        class Meta:
            model = Product 
            fields = ["name", "price", "description", "gothness"]
    ```
- Add import ```redirect``` at the top of ```views.py``` file in the main directory then create a new function for adding the new product.
    ```py
    def create_product(request):
    form = GothEntryForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect('main:show_main')
    ```
- Then, change the ```show_main``` function to the following.
    ```py
    def show_main(request):
    goth_entries = Product.objects.all()
    context = {
        'app_name': 'goth-store',
        'name': 'Kezia Salsalina Agtyra Sebayang',
        'class': 'PBP KKI', 
        'product_entries' : goth_entries,
    }

    return render(request, 'main.html', context)
    ```
- Open the ```urls.py``` file in the main directory and import the ```create_product``` function and add the URL path to the urlpatterns variable.
    ```py
    from django.urls import path
    from main.views import show_main, create_product

    app_name = 'main'

    urlpatterns = [
        path('', show_main, name='show_main'),
        path('create-product', create_product, name='create_product'),
        ]
    ```
- Lastly, create a new HTML file called ```create_product.html``` and add the following code.
    ```html
    {% extends 'base.html' %} 
    {% block content %}
    <h1>Add New Product</h1>

    <form method="POST">
    {% csrf_token %}
    <table>
        {{ form.as_table }}
        <tr>
        <td></td>
        <td>
            <input type="submit" value="Add Product" />
        </td>
        </tr>
    </table>
    </form>

    {% endblock %}
    ```

#### ✔️Add 4 views to view the added objects in XML, JSON, XML by ID, and JSON by ID formats.
- Open the ```views.py``` file in the main directory and add these imports at the top.
    ```py
    from django.http import HttpResponse
    from django.core import serializers
    ```
- Open the ```views.py``` file in the main directory and create four new functions like the following. 
    ```py
    def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

    def show_json(request):
        data = Product.objects.all()
        return HttpResponse(serializers.serialize("json", data), content_type="application/json")

    def show_xml_by_id(request, id):
        data = Product.objects.filter(pk=id)
        return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

    def show_json_by_id(request, id):
        data = Product.objects.filter(pk=id)
        return HttpResponse(serializers.serialize("json", data), content_type="application/json")
    ```
#### ✔️Create URL routing for each of the views added in point 2.
- Open the ```urls.py``` file in the main directory and import the functions in this line.
    ```
    from main.views import show_main, create_product, show_xml, show_json, show_xml_by_id, show_json_by_id
    ```
- Add the URL path to the urlpatterns variable in the ```urls.py``` file.
    ```py
    urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-product', create_product, name='create_product'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
    ]   
    ```

### POSTMAN
#### XML
![alt text](images/xml.png)
#### JSON
![alt text](images/json.png)
#### XML BY ID
![alt text](images/xmlbyid.png)
#### JSON BY ID
![alt text](images/jsonbyid.png)
</details>

<details>
<Summary><b>ASSIGNMENT 4</b></summary>

### 1. What is the difference between HttpResponseRedirect() and redirect()?
- `HttpResponseRedirect()` is a basic way to redirect users to a new URL in Django, where you need to manually provide the full URL. On the other hand, `redirect()` is a simpler and more flexible option. It allows you to not only pass a URL but also the name of a view or even an object, and it will automatically figure out the correct URL for you.

### 2. Explain how the ProductEntry model is linked with User!
- The ProductEntry model is linked to the User model using a foreign key, which establishes a one-to-many relationship between users and product entries. This means that each ProductEntry belongs to a specific user, while one user can have multiple product entries. 

### 3. What is the difference between authentication and authorization, and what happens when a user logs in? Explain how Django implements these two concepts.
- Authentication is the process of verifying a user's identity, typically through a username and password. Once authenticated, the system knows who the user is. On the other hand, authorization determines what actions or resources the authenticated user is allowed to access. It controls permissions based on the user's role or status. In Django, authentication is handled through the built-in auth system, where users can log in by providing a username and password that are verified against the database. Once authenticated, Django creates a session for the user, storing it in a cookie, so they remain logged in across requests. Authorization is implemented using Django's permissions and groups system, where specific permissions are assigned to users or groups to control what they can access or modify in the application. Django checks these permissions when a user tries to perform an action or view specific content. When a user logs in, Django first authenticates their credentials and, once verified, uses authorization to determine their level of access within the system.

### 4. How does Django remember logged-in users? Explain other uses of cookies and whether all cookies are safe to use.
- Django remembers logged-in users through the use of session cookies. When a user logs in, Django creates a session ID and stores it in a cookie on the user's browser. This session ID allows Django to track the user across different pages without requiring them to log in again on each request. Besides session management, cookies can be used for storing preferences, tracking user behavior, and personalizing content. However, cookies can be vulnerable to attacks like cross-site scripting (XSS) or session hijacking if not properly secured.

### 5. Explain how did you implement the checklist step-by-step
#### ✔️Implement the register, login, and logout functions so that the user can access the application freely.
- First, I need to activate the virtual environment. Then I open my ```views.py``` in the main subdirectory and add these following imports.
    ```py
    from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
    from django.contrib import messages
    from django.contrib.auth import authenticate, login, logout
    ```
- Second, I add these following functions to my  ```views.py``` file.
    ```py
    def register(request):
        form = UserCreationForm()

        if request.method == "POST":
            form = UserCreationForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Your account has been successfully created!')
                return redirect('main:login')
        context = {'form':form}
        return render(request, 'register.html', context)

    def login_user(request):
        if request.method == 'POST':
            form = AuthenticationForm(data=request.POST)

            if form.is_valid():
                    user = form.get_user()
                    login(request, user)
                    return redirect('main:show_main')

        else:
            form = AuthenticationForm(request)
        context = {'form': form}
        return render(request, 'login.html', context)

    def logout_user(request):
        logout(request)
        return redirect('main:login')
    ```
- Then, I create a new HTML file named ```register.html``` in the main/templates directory and add this following code. 
    ```html
    {% extends 'base.html' %} {% block meta %}
    <title>Register</title>
    {% endblock meta %} {% block content %}

    <div class="login">
    <h1>Register</h1>

    <form method="POST">
        {% csrf_token %}
        <table>
        {{ form.as_table }}
        <tr>
            <td></td>
            <td><input type="submit" name="submit" value="Register" /></td>
        </tr>
        </table>
    </form>

    {% if messages %}
    <ul>
        {% for message in messages %}
        <li>{{ message }}</li>
        {% endfor %}
    </ul>
    {% endif %}
    </div>

    {% endblock content %}
    ```
- I also then create a new HTML file named ```login.html``` in the main/templates directory where I fill it with the following template:
    ```html
    {% extends 'base.html' %}

    {% block meta %}
    <title>Login</title>
    {% endblock meta %}

    {% block content %}
    <div class="login">
    <h1>Login</h1>

    <form method="POST" action="">
        {% csrf_token %}
        <table>
        {{ form.as_table }}
        <tr>
            <td></td>
            <td><input class="btn login_btn" type="submit" value="Login" /></td>
        </tr>
        </table>
    </form>

    {% if messages %}
    <ul>
        {% for message in messages %}
        <li>{{ message }}</li>
        {% endfor %}
    </ul>
    {% endif %} Don't have an account yet?
    <a href="{% url 'main:register' %}">Register Now</a>
    </div>

    {% endblock content %}
    ```
- Then, I open ```main.html``` file in the main/templates directory and add the following code.
    ```html
    <a href="{% url 'main:logout' %}">
    <button>Logout</button>
    </a>
    ```
- After that, I open ```urls.py``` in the main subdirectory and import these functions and add some URL paths to the ```urlpatterns```
    ```py
    from main.views import register, login_user, logout_user
    urlpatterns = [
        ...
        path('register/', register, name='register'),
        path('login/', login_user, name='login'),
        path('logout/', logout_user, name='logout'),
    ]
    ```
- Last, I need to import ```login_required``` and add this line of code inside ```views.py``` at the top of ```show_main``` function
    ```py
    from django.contrib.auth.decorators import login_required
    ...
    @login_required(login_url='/login')
    def show_main(request):
    ...
    ```
- After implementing all these steps, I have restricted access to the main page and implement the register, login, and logout functions

#### ✔️Make two user accounts with three dummy data each, using the model made in the application beforehand so that each data can be accessed by each account locally.
#### 1st account
![alt text](images/hayleym.png)
#### 2nd account
![alt text](images/elle.png)

#### ✔️Connect the models Product and User.
- First, I open ```models.py``` in the main subdirectory and add some imports and some lines of code
    ```py
    from django.contrib.auth.models import User
    class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ```
- Then, I reopen ```views.py``` in the main subdirectory and modify the code like this
    ```py
    def create_product(request):
    form = GothEntryForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        goth_entry = form.save(commit=False)
        goth_entry.user = request.user
        goth_entry.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_product.html", context)
    ```
- Then I change the value of ```goth_entries``` and ```context``` in the function ```show_main``` as follows
    ```py
    def show_main(request):
        mood_entries = Product.objects.filter(user=request.user)

        context = {
            'name': request.user.username,
            ...
        }
    ...
- Last, I need to run, apply the model migrations and ensure the project is ready for a production environtment. I do this by adding another import statement in ```settings.py``` and change the variable ```DEBUG```
    ```py
    import os
    PRODUCTION = os.getenv("PRODUCTION", False)
    DEBUG = not PRODUCTION
    ```
- These steps should make the project's Product model connected to the User model.

#### ✔️Display logged in user details such as username and apply cookies like last login to the application's main page.
- First, open ```views.py``` in the main subdirectory. Add some imports at the top.
    ```py
    import datetime
    from django.http import HttpResponseRedirect
    from django.urls import reverse
    ```
- In the ```login_user``` function, replace the code in the if ```form.is_valid()``` block
    ```py
    ...
    if form.is_valid():
        user = form.get_user()
        login(request, user)
        response = HttpResponseRedirect(reverse("main:show_main"))
        response.set_cookie('last_login', str(datetime.datetime.now()))
        return response
    ...
    ```
- In the ```show_main ```function, add the snippet to the ```context``` variable
    ````py 
    'last_login': request.COOKIES['last_login']
    ``` 
- Then, modify the ```logout_user``` function
    ```py
    def logout_user(request):
        logout(request)
        response = HttpResponseRedirect(reverse('main:login'))
        response.delete_cookie('last_login')
        return response
    ```
- I open the ```main.html``` file and add the following snippet after the logout button
    ```html
    ...
    <h5>Last login session: {{ last_login }}</h5>
    ...
    ```
- These steps should display logged in user details such as username and apply cookies.
</details>

<details>
<Summary><b>ASSIGNMENT 5</b></summary>

### 1. Priority Order of CSS Selectors
- When multiple CSS selectors apply to the same HTML element, the browser uses specificity to determine which styles to apply. Specificity is essentially a set of rules that helps the browser decide the weight or importance of each selector. The order of priority for CSS selectors is as follows: type selectors (e.g., `div`, `h1`) have the lowest specificity, followed by class selectors (e.g., `.my-class`) and pseudo-classes (e.g., `:hover`). ID selectors (e.g., `#my-id`) have higher specificity than classes and types. Inline styles, such as `<div style="color: red;">`, take precedence over all CSS selectors because they are directly applied to the element. Lastly, the `!important` rule overrides even inline styles and all other rules, making it the most powerful in terms of specificity. Understanding and properly managing specificity is key to ensuring that your CSS behaves as expected.

### 2. Importance of Responsive Design in Web Development
- Responsive design is crucial in modern web development because it ensures that websites function and display optimally across a wide variety of devices, including mobile phones, tablets, and desktops. In today’s digital age, users access websites from devices with vastly different screen sizes and resolutions. Without responsive design, websites can appear distorted or difficult to navigate on smaller screens, leading to a poor user experience. Responsive design allows for fluid grids, flexible images, and media queries that enable the website to adapt to different screen sizes and orientations automatically. This improves user engagement and accessibility while also enhancing SEO, as search engines like Google give higher rankings to mobile-friendly websites. Examples of applications with responsive designs include Twitter and YouTube, which seamlessly adjust their layouts across devices. In contrast, older sites or applications without responsive design may appear cluttered or unusable on mobile, leading to higher bounce rates and user frustration.

### 3. Differences Between Margin, Border, and Padding
- In CSS, margin, border, and padding are all part of the box model that controls the space around HTML elements, but they serve different purposes. Margin is the space outside an element, separating it from other elements on the page. It's used to create space between elements and can collapse between adjacent elements. Padding is the space between the content of an element and its border. It pushes the content inward, creating an internal buffer inside the element. Unlike margin, padding adds to the total size of the element. Border is the line that surrounds the padding and content, and it can have various styles, colors, and thicknesses. 

### 4. Flexbox and Grid Layout Concepts
- Both Flexbox and Grid Layout are modern CSS layout systems designed to help developers create flexible, responsive designs. Flexbox is a one-dimensional layout system, meaning it organizes items in a single direction (either row or column). It’s excellent for laying out elements in a line, centering items, or distributing space between them dynamically. Flexbox is often used for components like navigation bars, buttons, or aligning items vertically and horizontally. For instance, using `display: flex` on a parent element will align all child elements in a flexible container. Properties like `justify-content` and `align-items` allow easy control of how elements are distributed.
- On the other hand, CSS Grid is a two-dimensional layout system, allowing items to be arranged in both rows and columns. Grid is ideal for creating more complex layouts, like an entire webpage structure with header, sidebar, and content areas. By defining rows and columns, Grid provides finer control over both vertical and horizontal layout. Properties such as `grid-template-rows` and `grid-template-columns` let developers create structured grids with ease. For example, using `display: grid` with `grid-template-columns: 1fr 2fr;` will create a two-column layout with flexible widths. Flexbox and Grid are often used together, as they complement each other, allowing for both simple and complex designs to be created responsively.

### 5. Implementation of the checklist step by step
#### ✔️Implement functions to delete and edit products.
- First, I open my ```views.py``` file in the ```main``` folder and add these two functions.
    ```py
    def edit_product(request, id):
    product = Product.objects.get(pk = id)

    form = GothEntryForm(request.POST or None, instance=product)

    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "edit_product.html", context)

    def delete_product(request, id):
        product = Product.objects.get(pk = id)
        product.delete()
        return HttpResponseRedirect(reverse('main:show_main'))
    ```
- Then, at the same file I add these imports.
    ```py
    from django.shortcuts import .., reverse
    from django.http import .., HttpResponseRedirect
    ```

- Then , I create a new file called ```edit_product.html``` in ```main/templates``` subdirectory.

- Lastly, I open the ```urls.py``` in the ```main``` folder and import the functions I've created and added URL paths to ```urlpatterns```
    ```py
    from main.views import edit_product, delete_product
    ```
    ```py
    ...
    path('edit-product/<uuid:id>', edit_product, name='edit_product'),
    path('delete/<uuid:id>', delete_product, name='delete_product'),
    ...
    ```
#### ✔️Customize the design of the HTML templates that have been created in previous assignments using CSS or a CSS framework 
- I choose Tailwind as the CSS Framework that I'm going to use. To add it to my project, I open the ```base.html``` file that was previously created in the ```templates``` folder located in my project root and  add the Tailwind cdn script in the head section like the code below
    ```html
    <head>
    {% block meta %}
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1">
    {% endblock meta %}
    <script src="https://cdn.tailwindcss.com">
    </script>
    </head>
    ```
#### ✔️Customize the login, register, and add product pages to be as attractive as possible.
- So first, I create a ```global.css``` file in /static/css in the root directory so that I could add custom styling on the pages. 
- Then I customise the ```login.html```, ```register.html```, and ```create_product.html``` the way I wanted it to be.

#### ✔️Customize the product list page to be more attractive and responsive. If there are no products saved in the application, the product list page will display an image and a message that no products are registered.
- So first, I create ```images``` folder inside the ```static``` directory. I then imported ```bat.png``` inside it and open my ```main.html``` file. I then add some styling and added ```bat.png``` in it. Here is my final ```main.html``` code:
    ```html
    {% extends 'base.html' %}
    {% load static %}

    {% block meta %}
    <title>Product List | Goth Store</title>
    {% endblock meta %}

    {% block content %}
    {% include 'navbar.html' %}

    <!-- Main Section Wrapper -->
    <div class="overflow-x-hidden px-4 md:px-8 pb-8 pt-24 min-h-screen flex flex-col wallpaper">
    <div class="p-2 mb-6 relative">
        <div class="relative grid grid-cols-1 z-30 md:grid-cols-3 gap-8">
        {% include "card_info.html" with title='Name' value=name %}
        {% include "card_info.html" with title='Class' value=class %}
        </div>
        <div class="h-full w-full py-6  absolute top-0 left-0 z-20 md:hidden flex ">
        <div class="h-full min-w-4 bg-red-700 mx-auto">
        </div>
        </div>
    </div>



        <!-- Add New Product Button -->
        <div class="flex justify-end mb-8">
            <a href="{% url 'main:create_product' %}" class="text-center bg-red-700 hover:bg-red-800 text-gray-100 font-bold py-2 px-4 rounded-full transition duration-300 ease-in-out shadow-2xl logout-font gothic-font">
                Add New Product
            </a>
        </div>

        <!-- No Products Available Section -->
        {% if not product_entries %}
        <div class="flex flex-col items-center justify-center min-h-[24rem] p-6">
            <img src="{% static 'images/bat.png' %}" class="w-40 h-40 mb-6 opacity-70"/>
            <p class="text-center text-white gothic-readable text-lg tracking-wide">
                No products are available in the underworld yet...
            </p>
        </div>

        <!-- Product Cards Section -->
        {% else %}
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
            {% for product in product_entries %}  
                {% include 'product_card.html' with product=product %}
            {% endfor %}
        </div>
        {% endif %}

    </div>
    {% endblock content %}
    ```
#### ✔️If there are products saved, the product list page will display details of each product using cards. For each product card, create two buttons to edit and delete the product on that card!
- So first, I create ```product_card.html``` inside ```main/templates``` directory. I did some styling and added the edit and trash button in the end of the code. Here is my final code of the card:
    ```html
    <div class="relative bg-black border-b-8 border-red-800 rounded-none shadow-md p-6 mb-10 transform hover:scale-105 transition duration-300 ease-in-out">

        <!-- Floating Decorative Accent (Top Center) -->
        <div class="absolute -top-5 left-1/2 transform -translate-x-1/2 bg-white text-black px-4 py-2 shadow-lg rounded-full">
        <i class="fas fa-cross fa-2x"></i>
        </div>
    
        <!-- Product Name with Subtle Underline -->
        <div class="text-center mb-4 border-b-2 border-red-700 pb-2">
        <h2 class="text-3xl gothic-font tracking-widest text-white">
            {{ product.name }}
        </h2>
        </div>
    
        <!-- Centered Product Information Section -->
        <div class="grid grid-cols-1 gap-6 text-center">
        
        <!-- Description Section with Vertical Line -->
        <div class="relative">
            <p class="text-white gothic-readable italic text-lg px-6 relative z-10">
            "{{ product.description }}"
            </p>
        </div>
    
        <!-- Price Section with Blocky Borders -->
        <div class="border-2 border-black bg-gray-100 py-2 rounded-lg text-red-700 text-2xl gothic-font tracking-wider">
            Price: Rp{{ product.price }}
        </div>
        
        <!-- Gothness Meter with Minimalistic Style -->
        <div class="py-4">
            <p class="text-white gothic-font tracking-wide mb-2">Gothness Level</p>
            <div class="w-full h-3 bg-gray-200 border-2 border-red-500 rounded-full overflow-hidden">
            <div class="h-full bg-red-500" style="width: {% if product.gothness > 10 %}100%{% else %}{{ product.gothness }}0%{% endif %};"></div>
            </div>
        </div>
        </div>
    
        <!-- Floating Buttons with Circular Frames -->
        <div class="absolute bottom-0 left-1/2 transform -translate-x-1/2 flex space-x-4 -mb-6">
        <a href="{% url 'main:edit_product' product.pk %}" class="bg-white border-2 border-yellow-500 text-yellow-500 p-2 rounded-full hover:bg-yellow-500 hover:text-white transition duration-300 shadow-md">
            <i class="fas fa-edit"></i>
        </a>
        <a href="{% url 'main:delete_product' product.pk %}" class="bg-white border-2 border-red-500 text-red-500 p-2 rounded-full hover:bg-red-500 hover:text-white transition duration-300 shadow-md">
            <i class="fas fa-trash"></i>
        </a>
        </div>
    </div>
    ```
#### ✔️Create a navigation bar (navbar) for the features in the application that is responsive to different device sizes, especially mobile and desktop.
- So, for the last checklist, I created a ```navbar.html``` file and did some styling here and there. Here is my final styling:
    ```html
    <nav class="bg-black shadow-2xl fixed top-0 left-0 z-40 w-screen border-b-4 border-red-800 gothic-border">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="flex items-center justify-between h-16">
            <div class="flex items-center">
            <!-- Gothic-style Font for Brand Name -->
            <h1 class="text-3xl font-bold text-center text-white gothic-font tracking-widest">
                Goth Store
            </h1>
            
            </div>
    
            <!-- User Authentication Links -->
            <div class="hidden md:flex flex-row items-center space-x-4"> <!-- Horizontal alignment with space between -->
                {% if user.is_authenticated %}
                <div class="flex flex-col text-right"> <!-- Text in a vertical stack -->
                    <span class="text-white italic gothic-readable">Welcome, {{ user.username }}</span>
                    <span class="text-xs text-white italic gothic-readable">Last Login: {{last_login}}</span> <!-- Last Login Info -->
                </div>
                <!-- Logout Button -->
                <a href="{% url 'main:logout' %}" class="text-center bg-red-700 hover:bg-red-800 text-gray-100 font-bold py-2 px-4 rounded-full transition duration-300 ease-in-out shadow-2xl logout-font gothic-font">
                    Logout
                </a>
                {% else %}
                <a href="{% url 'main:login' %}" class="text-center bg-purple-700 hover:bg-purple-900 text-gray-100 font-bold py-2 px-4 rounded-full transition duration-300 ease-in-out shadow-2xl mr-2 gothic-font">
                    Login
                </a>
                <a href="{% url 'main:register' %}" class="text-center bg-gray-700 hover:bg-gray-900 text-gray-100 font-bold py-2 px-4 rounded-full transition duration-300 ease-in-out shadow-2xl gothic-font">
                    Register
                </a>
                {% endif %}
            </div>
            
    
            <!-- Mobile Menu Button -->
            <div class="md:hidden flex items-center">
            <button class="mobile-menu-button">
                <svg class="w-8 h-8 text-gray-200 hover:text-gray-100 transition duration-300 ease-in-out" fill="none" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" viewBox="0 0 24 24" stroke="currentColor">
                <path d="M4 6h16M4 12h16M4 18h16"></path>
                </svg>
            </button>
            </div>
        </div>
        </div>
    
        <!-- Mobile Menu -->
        <div class="mobile-menu hidden md:hidden bg-black text-gray-400 px-4 w-full shadow-lg border-t-2 border-red-700">
        <div class="pt-4 pb-6 space-y-2 mx-auto">
            {% if user.is_authenticated %}
            <span class="block text-gray-400 italic px-3 py-2 gothic-readable">Welcome, {{ user.username }}</span>
            <span class="block text-gray-400 italic px-3 py-2 gothic-readable">Last Login: {{ user.last_login }}</span> <!-- Last Login in Mobile -->
            <a href="{% url 'main:logout' %}" class="block text-center bg-red-800 hover:bg-red-900 text-gray-100 font-bold py-2 px-4 rounded-full transition duration-300 ease-in-out shadow-lg gothic-font">
                Logout
            </a>
            {% else %}
            <a href="{% url 'main:login' %}" class="block text-center bg-purple-700 hover:bg-purple-900 text-gray-100 font-bold py-2 px-4 rounded-full transition duration-300 ease-in-out shadow-lg mb-2 gothic-font">
                Login
            </a>
            <a href="{% url 'main:register' %}" class="block text-center bg-gray-700 hover:bg-gray-900 text-gray-100 font-bold py-2 px-4 rounded-full transition duration-300 ease-in-out shadow-lg gothic-font">
                Register
            </a>
            {% endif %}
        </div>
        </div>
    
        <!-- Toggle Mobile Menu Script -->
        <script>
        const btn = document.querySelector("button.mobile-menu-button");
        const menu = document.querySelector(".mobile-menu");
    
        btn.addEventListener("click", () => {
            menu.classList.toggle("hidden");
        });
        </script>
    </nav>
    ```
- This navbar is responsive and have a hamburger icon in the mobile version of the website.
  
</details>

<details>
<Summary><b>ASSIGNMENT 6</b></summary>

### 1. Explain the benefits of using JavaScript in developing web applications!
- JavaScript is great for making websites more interactive and responsive. It runs directly in the browser, so it can quickly respond to things like clicks, form submissions, and other user actions without needing to refresh the page or contact the server every time. This makes the website feel faster and smoother for users. Plus, JavaScript works on all modern browsers, so it’s easy to create cross-platform apps that work on any device.

- Another key benefit is how JavaScript helps create dynamic content. You can build things like interactive forms, animations, or real-time updates, making the web experience more engaging. This level of interactivity is hard to achieve without JavaScript, which is why it’s such a popular choice for web developers.

### 2. Explain why we need to use await when we call fetch()! What would happen if we don't use await?
- When we use fetch() in JavaScript, we’re making an HTTP request, but it doesn’t happen instantly. Instead, it returns a Promise, which means the request is still in progress. If you use await, it makes sure the code waits until the response is ready before moving on to the next line. This helps keep things in order, especially when you need to use the response data right away.

- If we don’t use await, the rest of the code will run without waiting for the request to finish. So, if you try to use the data that hasn’t arrived yet, you’ll likely get errors or unexpected behavior because the data simply isn’t ready.

### 3. Why do we need to use the csrf_exempt decorator on the view used for AJAX POST?
- Django, like many web frameworks, protects against something called CSRF (Cross-Site Request Forgery), which helps prevent attackers from making unwanted requests on behalf of users. When making a POST request through AJAX, Django expects a special CSRF token to be included to verify that the request is legitimate.

- However, sometimes it’s tricky to include this token in AJAX requests, so we use the csrf_exempt decorator to bypass this protection for that specific view. If we don’t use it (or include the token another way), Django will block the request, thinking it might be unsafe. Just be careful when using csrf_exempt, as disabling this protection can open up security risks if not managed properly.

### 4. Why can't the sanitization be done just in the front-end?
- Doing sanitization in the back-end ensures that no matter what users try to send to your server, it gets checked and cleaned up. This protects my app from serious security issues like SQL injection or cross-site scripting (XSS). In short, the front-end helps with usability, but the back-end is where the real protection happens.

### 5. Implementation of the checklist step-by-step
#### ✔️Modify the codes in data cards to able to use AJAX GET
- In ```main.html```, I added this async function to be able to get data using show_json.
    ```html
    ...
    <div id="product_cards"></div>
    ...
    <script>
    async function getProductEntries(){
        return fetch("{% url 'main:show_json' %}").then((res) => res.json())
    }
    </script>
    ```
#### ✔️Retrieve data using AJAX GET
- I modify my ```show_json``` in my ```views.py``` so that I could make sure that the data retrieved are only the data belonging to the logged-in user.
    ``` py
    def show_json(request):
        data = Product.objects.filter(user=request.user)
    ```
#### ✔️Create a button that open a modal with a form for adding a product entry.
- In the ```main.html``` file I set up the modal that contains a form for entering the product entry details
    ```js
    <!-- Modal for AJAX Entry -->
    <div id="crudModal" tabindex="-1" aria-hidden="true" class="hidden fixed inset-0 z-50 w-full flex items-center justify-center bg-gray-800 bg-opacity-50 overflow-x-hidden overflow-y-auto transition-opacity duration-300 ease-out">
        <div id="crudModalContent" class="relative bg-white rounded-lg shadow-lg w-5/6 sm:w-3/4 md:w-1/2 lg:w-1/3 mx-4 sm:mx-0 transform scale-95 opacity-0 transition-transform transition-opacity duration-300 ease-out">
        <!-- Modal header -->
        <div class="flex items-center justify-between p-4 border-b rounded-t bg-black">
            <h3 class="text-xl gothic-font text-white">
            Add New Product Entry
            </h3>
            <button type="button" class="text-gray-400 bg-transparent hover:bg-gray-200 hover:text-gray-900 rounded-lg text-sm p-1.5 ml-auto inline-flex items-center" id="closeModalBtn">
            <svg aria-hidden="true" class="w-5 h-5" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
                <path fill-rule="evenodd" d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z" clip-rule="evenodd"></path>
            </svg>
            <span class="sr-only">Close modal</span>
            </button>
        </div>
        <!-- Modal body -->
        <div class="px-6 py-4 space-y-6 form-style bg-black">
            <form id="GothEntryForm">
            <div class="mb-4">
                <label for="name" class="block text-sm font-medium text-white">Name</label>
                <input type="text" id="name" name="name" required>
            </div>
            <div class="mb-4">
                <label for="description" class="block text-sm font-medium text-white">Description</label>
                <textarea id="description" name="description" rows="3" class="text-white" required></textarea>
            </div>
            <div class="mb-4">
                <label for="price" class="block text-sm font-medium text-white">Price</label>
                <input type="number" id="price" name="price" min="1" step="0.01"  required>
            </div>
            <div class="mb-4">
                <label for="gothness" class="block text-sm font-medium text-white">Gothness</label>
                <input type="number" id="gothness" name="gothness" required>
            </div>
            </form>
        </div>
        <div class="flex flex-col space-y-2 md:flex-row md:space-y-0 md:space-x-2 p-6 border-t border-gray-200 rounded-b justify-center md:justify-end bg-black">
            <button type="button" class="bg-black hover:bg-gray-600 text-white font-bold py-2 px-4 rounded-lg" id="cancelButton">Cancel</button>
            <button type="submit" id="submitProductEntry" form="GothEntryForm">Save</button>
        </div>
        </div>
    </div>
    ```
- Then add the following Javascript Functions inside the ```<script>``` tag
    ```js
    const modal = document.getElementById('crudModal');
    const modalContent = document.getElementById('crudModalContent');

    function showModal() {
        const modal = document.getElementById('crudModal');
        const modalContent = document.getElementById('crudModalContent');

        modal.classList.remove('hidden'); 
        setTimeout(() => {
            modalContent.classList.remove('opacity-0', 'scale-95');
            modalContent.classList.add('opacity-100', 'scale-100');
        }, 50); 
    }

    function hideModal() {
        const modal = document.getElementById('crudModal');
        const modalContent = document.getElementById('crudModalContent');

        modalContent.classList.remove('opacity-100', 'scale-100');
        modalContent.classList.add('opacity-0', 'scale-95');

        setTimeout(() => {
            modal.classList.add('hidden');
        }, 150); 
    }

    document.getElementById("cancelButton").addEventListener("click", hideModal);
    document.getElementById("closeModalBtn").addEventListener("click", hideModal);
    document.getElementById("GothEntryForm").addEventListener("submit", (e) => {
        e.preventDefault();
        addProductEntry();
    })
    ```
- To create a button to trigger the modal, in the ```main.html``` I add this new button 
    ```html
    <button data-modal-target="crudModal" data-modal-toggle="crudModal" class="text-center bg-red-700 hover:bg-red-800 text-gray-100 font-bold py-2 px-4 rounded-full transition duration-300 ease-in-out shadow-2xl logout-font gothic-font" onclick="showModal();">
            Add New Product Entry by AJAX
            </button>
    ```

#### ✔️Create a new view function to add a new product to the database.
- In ```views.py```, I imported ```csrf_exempt``` and ```require_POST``` and implemented it on a new function. I also imported ```strip_tags``` to sanitize the entries.
    ```py
    @csrf_exempt
    @require_POST
    def add_product_ajax(request):
        name = strip_tags(request.POST.get("name"))
        price = request.POST.get("price")
        description = strip_tags(request.POST.get("description"))
        gothness = strip_tags(request.POST.get("gothness"))
        user = request.user

        new_product = Product(
            name=name, price=price,
            description=description, gothness=gothness,
            user=user
        )
        new_product.save()

        return HttpResponse(b"CREATED", status=201)
    ```
#### ✔️Create a /create-ajax/ path that routes to the new view function you created.
- In ```urls.py```, add this import and line of code.
    ```py
    from main.views import ..., add_product_ajax

    main/urls.py
    urlpatterns = [
        ...
        path('create-product-ajax', add_product_ajax, name='add_product_ajax'),
    ]
    ```

#### ✔️Connect the form you created inside the modal to the /create-ajax/ path
- To connect the form we create a new function in the block ```<script>``` such as the following:
    ```js
    function addProductEntry() {
        fetch("{% url 'main:add_product_ajax' %}", {
        method: "POST",
        body: new FormData(document.querySelector('#GothEntryForm')),
        })
        .then(response => {
        if (response.ok) {
            refreshProductEntries(); 
            document.getElementById("GothEntryForm").reset();  
            hideModal();  
        } else {
            console.error('Failed to save product via AJAX.');
        }
        })
        .catch(error => console.error('Error:', error));

        return false; 
    }
    ```
#### ✔️Perform asynchronous refresh on the main page to display the latest item list without reloading the entire main page.
- In main.hmtl, I created a new asynchronous function called refreshProductEntries.
    ```js
    async function refreshProductEntries() {
        document.getElementById("product_cards").innerHTML = "";
        document.getElementById("product_cards").className = "";
        const productEntries = await getProductEntries();
        let htmlString = "";
        let classNameString = "";

        if (productEntries.length === 0) {
        classNameString = "flex flex-col items-center justify-center min-h-[24rem] p-6";
        htmlString = `
            <div class="flex flex-col items-center justify-center min-h-[24rem] p-6">
            <img src="{% static 'images/bat.png' %}" class="w-40 h-40 mb-6 opacity-70"/>
            <p class="text-center text-white gothic-readable text-lg tracking-wide">
                No products are available in the underworld yet...
            </p>
            </div>
        `;
        } else {
        classNameString = "grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-8";
        productEntries.forEach((item) => {
            const name = DOMPurify.sanitize(item.fields.name);
            const description = DOMPurify.sanitize(item.fields.description);
            const gothness = DOMPurify.sanitize(item.fields.gothness);

            htmlString += `
            <div class="relative bg-black border-b-8 border-red-800 rounded-none shadow-md p-6 mb-10 transform hover:scale-105 transition duration-300 ease-in-out">

                <!-- Floating Decorative Accent (Top Center) -->
                <div class="absolute -top-5 left-1/2 transform -translate-x-1/2 bg-white text-black px-4 py-2 shadow-lg rounded-full">
                <i class="fas fa-cross fa-2x"></i>
                </div>
            
                <!-- Product Name with Subtle Underline -->
                <div class="text-center mb-4 border-b-2 border-red-700 pb-2">
                <h2 class="text-3xl gothic-font tracking-widest text-white">
                    ${name}
                </h2>
                </div>
            
                <!-- Centered Product Information Section -->
                <div class="grid grid-cols-1 gap-6 text-center">
                
                <!-- Description Section with Vertical Line -->
                <div class="relative">
                    <p class="text-white gothic-readable italic text-lg px-6 relative z-10">
                    ${description}
                    </p>
                </div>
            
                <!-- Price Section with Blocky Borders -->
                <div class="border-2 border-black bg-gray-100 py-2 rounded-lg text-red-700 text-2xl gothic-font tracking-wider">
                    Price: Rp${item.fields.price}
                </div>
                
                <!-- Gothness Meter with Minimalistic Style -->
                <div class="py-4">
                    <p class="text-white gothic-font tracking-wide mb-2">Gothness Level</p>
                    <div class="w-full h-3 bg-gray-200 border-2 border-red-500 rounded-full overflow-hidden">
                    <div class="h-full bg-red-500" style="width: ${gothness > 10 ? '100%' : gothness * 10 + '%'};"></div>
                    </div>
                </div>
                </div>
            
                
                <div class="absolute bottom-0 left-1/2 transform -translate-x-1/2 flex space-x-4 -mb-6">
                <a href="/edit-product/${item.pk}" class="bg-white border-2 border-yellow-500 text-yellow-500 p-2 rounded-full hover:bg-yellow-500 hover:text-white transition duration-300 shadow-md">
                    <i class="fas fa-edit"></i>
                </a>
                <a href="/delete/${item.pk}" class="bg-white border-2 border-red-500 text-red-500 p-2 rounded-full hover:bg-red-500 hover:text-white transition duration-300 shadow-md">
                    <i class="fas fa-trash"></i>
                </a>
                </div>
            </div>
    
            `;
        });
        }
        document.getElementById("product_cards").className = classNameString;
        document.getElementById("product_cards").innerHTML = htmlString;
    }

    refreshProductEntries();
    ```

</details>

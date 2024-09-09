## 💀 ⛓️ Goth Store ⚰️🦇
#### 🔗[CLICK HERE TO BE DIRECTED TO MY APP](http://kezia-salsalina-gothstore.pbp.cs.ui.ac.id)
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
- 
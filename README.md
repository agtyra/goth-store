# goth-store
link to my app:

## ASSIGNMENT 2

### 1. STEPS-BY-STEPS 
##### Checklist 1: Create a new Django project.
Create a new directory with the name "goth-store"
Open the terminal and create a virtual environment inside the directory by running this command below
    ```bash
    python3 -m venv env
    ```
    And activating it by:

    ```bash
    env\Scripts\activate
    ```
    '
Create a file named requirements.txt inside the directory and fill it with some dependencies below

    ```
    django
    gunicorn
    whitenoise
    psycopg2-binary
    requests
    urllib3
    ```
    then, install them by running this command
    ```bash
    pip install -r requirements.txt
    ```
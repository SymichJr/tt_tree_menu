# tt_tree_menu
Service to make trees URLs

### Install
Clone the project to the local machine, install the virtual environment and run it

Install all dependencies from a file ```requirements.txt```
```sh
pip install -r requirements.txt
```
### Admin
change dir to see ```manage.py``` file 
Create superuser
```sh
python manage.py createsuperuser
```
Now you can create trees /w its children in django Admin in ```http://127.0.0.1:8000/admin/```

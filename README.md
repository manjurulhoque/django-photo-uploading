### Photo Uploading App


##### To run the app

```bash
virtualenv <name of the env>
cd <name of the env>
git clone https://github.com/manjurulhoque/django-photo-uploading.git
cd django-photo-uploading
pip install -r requirments.txt
cd src
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

SECRET_KEY = 'q=8$i#3m)sdtpi$z$-63_52$t01wto90d330&ox6n%x&d#w_@^'
DEFAULT_AUTO_FIELD='django.db.models.AutoField'

DATABASES = {
   'default': {
       'ENGINE': 'django.db.backends.postgresql_psycopg2',
       'NAME': 'postgres',
       'USER': 'postgres',
       'PASSWORD': '1234',
       'HOST': 'localhost',
       'PORT': '5432',
   }
}

INSTALLED_APPS = ("app_dir",)
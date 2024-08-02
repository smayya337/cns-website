# ACM @ UVA Website

This is the source code for a brand-new ACM @ UVA website written using Django and Bootstrap.

## Deploy the Site

```bash
# clone repo
git clone https://github.com/smayya337/acm-website
# enter repo
cd acm-website
# create secret configuration settings file
cp acm_website/secret.py.example acm_website/secret.py
# edit secret configuration settings
nano acm_website/secret.py # substitute with your favorite editor
# create virtual environment
virtualenv .venv
# enter virtual environment
source .venv/bin/activate
# install dependencies
pip install -r requirements.txt
# apply database migrations
python ./manage.py migrate
# collect static files
python ./manage.py collectstatic
# create admin user
python ./manage.py createsuperuser
# start app
gunicorn acm_website.wsgi
```

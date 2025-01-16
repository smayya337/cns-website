# CNS @ UVA Website

This is the source code for a brand-new CNS @ UVA website written using Django and Bootstrap.

## Deploy the Site

```bash
# clone repo
git clone https://github.com/smayya337/cns-website
# enter repo
cd cns-website
# create secret configuration settings file
cp cns_website/secret.py.example cns_website/secret.py
# edit secret configuration settings
nano cns_website/secret.py # substitute with your favorite editor
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
gunicorn -b 0.0.0.0:8000 cns_website.wsgi
```

import os
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:////var/www/ctf.wncc-iitb.org/CTFd/ctfd.db'.format(os.path.dirname(os.path.abspath(__file__)))
print SQLALCHEMY_DATABASE_URI

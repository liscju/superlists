Creating virtual env:
$ pip3 install virtualenv
virtualenv --python=python3 ../virtualenv

Activate virtual env (Remember about it):
( git bash)
source ../virtualenv/bin/activate
( windows )
..\virtualenv\Scripts\activate.bat

Running server:

C:\Python34\python.exe manage.py runserver

Test:

C:\Python34\python.exe manage.py test -v 2

Functional Test:

C:\Python34\python.exe functional_test.py

Running specific test(example):
C:\Python34\python.exe manage.py test functional_tests.tests.NewVisitorTest.test_layout_and_styling

When something goes wrong in test - debug it with:
    @override_settings(DEBUG=True)
    def test_debug(self):
        ....

Update migration for models:

C:\Python34\python.exe manage.py makemigrations

Update tables in db:

C:\Python34\python.exe manage.py migrate

When sth goes wrong,you always can delete all tables
in db and runmigrations

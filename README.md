Uruchamianie:

C:\Python34\python.exe manage.py runserver

Testy:

C:\Python34\python.exe manage.py test -v 2

Functional Test:

C:\Python34\python.exe functional_test.py

Running specific test(example):
C:\Python34\python.exe manage.py test functional_tests.tests.NewVisitorTest.test_layout_and_styling

Aktualizacja migracji dla modeli:

C:\Python34\python.exe manage.py makemigrations

Aktualizacja tabeli w bazie:

C:\Python34\python.exe manage.py migrate

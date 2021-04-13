Pentru a putea crea o aplicatie PWA care sa se bazeze pe arhitectura REST vom folosi django,
pentru a initaliza un proiect folosind Django trebuie in primul rand sa initalizam un 'folder' pentru proiectul nostru.

Pentru initalizare vom folosi python virtual environment care sa encapsuleze proiectul nostru fata de restul sistemului astfel incat orice 
plugin instalat va fi relativ la nivelul PWA-ului si vom instala django.

1. Creeam un folder gol
	C:\Users\windowsuser>mkdir NumeProiect

2.Intram in folderul gol
	C:\Users\windowsuser>cd NumeProiect

3. Creean si activam environmentul virtual oferit de python
	C:\Users\windowsuser\NumeProiect>python -m venv env
	C:\Users\windowsuser\NumeProiect>env\Scripts\activate
4.Instalam django
	(env) C:\Users\windowsuser\NumeProiect>pip install django
	(env) C:\Users\windowsuser\NumeProiect>pip install djangorestframework
	(env) C:\Users\windowsuser\NumeProiect>pip install beautifulsoup4
	(env) C:\Users\windowsuser\NumeProiect>pip install requests



Dupa ce am facut pasii de initalizare si instalare trebuie sa activam proiectul folosind Django.

1. Folosind django-admin initalizam un proiect django cu numele dorit
	(env) C:\Users\windowsuser\NumeProiect>django-admin startproject ProiectNume
2. Dupa initalizarea proiectului navigam in folderul proiectului de django initalizat si creeam o aplicatie pentru proiectul nostru
	(env) C:\Users\windowsuser\NumeProiect>cd ProiectNume
	(env) C:\Users\windowsuser\NumeProiect\ProiectNume>ls                                                                       
		manage.py  stackproject
	(env) C:\Users\windowsuser\NumeProiect\ProiectNume>python manage.py startapp proiect
2.1 Pentru initalizarea bazei de date standard djangoo vom folosi 
	(env) C:\Users\windowsuser\NumeProiect\ProiectNume>python manage.py migrate

2.2 Pentru initalizarea contului de admin standard django vom folosi
	(env) C:\Users\windowsuser\NumeProiect\ProiectNume>python manage.py createsuperuser
        introducem nume, mail si parola necesare

3. In folderul proiectului de django trebuie sa editam fisierul 

	settings.py si sa cautam linia INSTALLED_APPS = ['django.etc'], 
	la finalul ei adaugam, urmarind sintaxa, numele proiectului nostru de Django,
	linia trebuie sa arate  INSTALLED_APPS = ['django.etc', 'ProiectNume'].
	

4. In folderul proiectului de django initalizat putem acum rula PWA-ul nostru folosind urmatoarea comanda
	(env) C:\Users\windowsuser\NumeProiect\ProiectNume>python manage.py runserver

	iar mai apoi vom astepta ca serverul sa porneasca si vom urmarii pana vedem unde a pornit serverul local.
       	
	Django version 3.2, using settings 'ProiectNume.settings'
	Starting development server at http://127.0.0.1:8000/

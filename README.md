Django Blog App (WIP)

A simple blog application built with Django. The project is still in progress core authentication exists, but most user facing features are under active development


Current State

Basic groundwork is in place:
	•	User registration (not yet exposed in UI)
	•	Login / logout functionality
	•	Project structure (apps, templates, static files)

No main blog interface yet — this is still being built.

Roadmap

Planned additions:
	•	Homepage with post feed
	•	Navigation (login/register from UI)
	•	User profiles
	•	Create / edit / delete blog posts
	•	Comments system
	•	Like / reaction feature

Tech Stack
	•	Python 3.11+
	•	Django
	•	SQLite (default, may change later)
	•	HTML / CSS (Django templates)

Setup Instructions
1. Clone the project
     git clone https://github.com/Faris07-cmd/blog-app.git
     cd blog-app
2.Create virtual environment (recommended)
    python -m venv env
    source env/bin/activate      # macOS / Linux
    env\Scripts\activate         # Windows
3. Install dependencies
  If you don’t have a requirements file yet, create one later with:
  pip install django
Or if you already add one:
  pip install -r requirements.txt
4. Apply migrations
   python manage.py migrate
5. Create superuser (for admin access)
   python manage.py createsuperuser
6. Run the development server
   python manage.py runserver
Then open:
 http://127.0.0.1:8000/
Notes
	•	Registration exists but is not linked yet — access is manual.
	•	UI is minimal; focus so far is backend structure.
	•	Expect breaking changes as features are added.
TODO (short-term)
	•	Connect auth pages to UI
	•	Build base layout (navbar, footer)
	•	Implement post model + views
	•	Add form handling for posts

License

 Not defined yet.

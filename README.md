##  Project Structure

# Social Booster Demo – Backend (REST APIs)

##  Overview
This is the **backend service** for the Social Booster demo task, built as part of the hiring process for the **Full Stack Developer role at Social Booster Media**.

The backend exposes REST APIs for managing campaigns, persists data in PostgreSQL (Supabase), and serves as the data source for the live frontend dashboard.

---

##  Live Links

- Live Backend API (Campaigns):  
  https://social-booster-backend.onrender.com/api/campaigns/

-  Live Frontend:  
  https://social-booster-frontend-mxw5rvq3v-sahil-vikas-thorats-projects.vercel.app

-  Frontend Repository:  
  https://github.com/sahil18z/social-booster-frontend

---

##  Tech Stack

- Framework: Django
- API Layer: Django REST Framework
- Language: Python
- Database: PostgreSQL (Supabase)
- Server: Gunicorn
- Deployment: Render

---

##  Features

### REST API (CRUD)
- Create campaigns
- Retrieve campaign list
- Update campaigns
- Delete campaigns
- Supported HTTP methods:
  - `GET`
  - `POST`
  - `PATCH`
  - `DELETE`

### Data Persistence
- Campaign data stored in PostgreSQL (Supabase)
- Fields include:
  - Name
  - Platform
  - Budget
  - Clicks
  - Impressions
  - Created timestamp

### Security Practices
- Environment variables used for secrets and credentials
- `.env` file excluded from GitHub
- Database credentials rotated after automated security alert

---

##  Project Structure

backend/
├─ config/
│ ├─ settings.py
│ ├─ urls.py
│ └─ wsgi.py
├─ campaigns/
│ ├─ models.py
│ ├─ serializers.py
│ ├─ views.py
│ ├─ urls.py
├─ manage.py
├─ requirements.txt
├─ .env



---

##  Environment Variables

Create a `.env` file in the backend root:

DATABASE_URL=postgresql://<supabase-session-pooler-url>
SECRET_KEY=your-django-secret-key
DEBUG=False
ALLOWED_HOSTS=*


> The `.env` file is intentionally not committed to GitHub.

---

##  Local Development

python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver



Backend runs at:http://127.0.0.1:8000



---

##  Deployment

### Render
- Deployed as a Python Web Service on Render
- Environment variables configured in Render dashboard

- Database migrations executed after deployment: python manage.py migrate


---

##  Testing

- APIs tested locally using Django REST Framework browsable API
- CRUD operations verified against deployed database
- Live API tested via deployed frontend

---

##  Demo Video
A 3–5 minute screen recording demonstrating:
- Live API responses
- CRUD operations via frontend
- Database persistence

---

## Submission Notes
This backend fulfills all backend requirements of the demo task:
- Full CRUD REST APIs
- PostgreSQL database integration
- Production deployment
- Publicly accessible API endpoints

---

##  Author
**Sahil Thorat**  
Full Stack Developer Candidate  
Social Booster Media



# Demo deployment

The project is now deployable as a small demo. It still runs locally with SQLite,
and accepts `DATABASE_URL` when a host provides PostgreSQL.

## Local verification

```powershell
pip install -r requirements.txt
python manage.py check
python manage.py migrate
python manage.py collectstatic --noinput
python manage.py runserver
```

## Render (recommended for a public demo)

1. Push `main` to GitHub.
2. Render dashboard → **New → Web Service** → connect `vivek11o1/puddle`.
3. Configure:
   - **Build command:** `pip install -r requirements.txt && python manage.py migrate --noinput && python manage.py collectstatic --noinput`
   - **Start command:** `gunicorn puddle.wsgi:application`
4. Create a Render **PostgreSQL** database and copy its **Internal Database URL**.
5. Add environment variables:

   ```txt
   SECRET_KEY=<a-new-long-random-key>
   DEBUG=False
   ALLOWED_HOSTS=<your-app>.onrender.com
   CSRF_TRUSTED_ORIGINS=https://<your-app>.onrender.com
   DATABASE_URL=<render-postgres-internal-url>
   ```

6. Deploy, then run `python manage.py createsuperuser` in Render Shell.
7. Open `https://<your-app>.onrender.com/admin/`.

## PythonAnywhere (simplest SQLite demo)

```bash
git clone https://github.com/vivek11o1/puddle.git
cd puddle
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py collectstatic --noinput
python manage.py createsuperuser
```

Then add a web app with **Manual configuration**, point it at `puddle/wsgi.py`,
activate the `.venv`, and map:

- `/static/` → `/home/<username>/puddle/staticfiles`
- `/media/` → `/home/<username>/puddle/media`

Set `DEBUG=False`, a fresh `SECRET_KEY`, and your hostname in the WSGI file.
Reload the web app.

## Notes

- `db.sqlite3`, `media/`, `.env`, and `staticfiles/` are ignored on purpose.
- Always set a fresh `SECRET_KEY`; never reuse the one that was committed earlier.
- On hosts with ephemeral disks, use PostgreSQL/`DATABASE_URL` and external media
  storage; uploaded files will not survive redeploys otherwise.

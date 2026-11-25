# Deploy the demo (minimal steps)

Everything in the repo is already prepared: SQLite fallback, static files,
media serving, demo images, and demo data. You only need to create the Render
web service.

## 1. Push

```powershell
git push origin main
```

## 2. Create a Render Web Service

Go to https://dashboard.render.com → **New → Web Service** → connect
`vivek11o1/puddle`.

Use:

- **Build command**
  ```bash
  pip install -r requirements.txt && python manage.py migrate --noinput && python manage.py collectstatic --noinput
  ```
- **Start command**
  ```bash
  gunicorn puddle.wsgi:application
  ```

## 3. Add environment variables

```txt
DEBUG=False
SECRET_KEY=<make-up-a-long-random-string>
ALLOWED_HOSTS=<your-app>.onrender.com
CSRF_TRUSTED_ORIGINS=https://<your-app>.onrender.com
```

Do **not** add `DATABASE_URL`. No PostgreSQL is needed.

Optional: set `DEMO_ADMIN_PASSWORD` to change the demo admin password.

## 4. Open the app

After deploy finishes, open:

```txt
https://<your-app>.onrender.com/
```

You will see demo items with images already displayed.

Admin panel:

```txt
https://<your-app>.onrender.com/admin/
```

Login:

```txt
username: admin
password: demo1234
```

Change that password immediately if you use a different
`DEMO_ADMIN_PASSWORD`.

## Notes

- The demo data and images are auto-created by migration `0005_seed_demo_data.py`.
- SQLite and uploaded media live on Render's temporary disk. They reset on
  every redeploy. That is expected for this demo.
- Serving media through Django is fine for a demo; don't use it for a real
  high-traffic site.

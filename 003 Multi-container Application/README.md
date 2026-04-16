Here's a complete, updated, and beginner-friendly guide to run **Project 3: Building a simple multi-container application** with **Flask + MySQL** using **Docker Compose** in **Visual Studio Code**.

This is a classic two-tier app: Flask (web frontend) talks to MySQL (database backend).

### 1. Create the Project in VS Code

1. Open VS Code.
2. **File → Open Folder** → Create and open a new folder named `flask-mysql-docker`.

### 2. Create the Project Files

Inside the folder, create these files:

#### A. `app.py` (Flask application)
Right-click → **New File** → `app.py`

Use this **improved and fixed version** (the original has issues with MySQL startup timing):

```python
from flask import Flask
import mysql.connector
import time
import os

app = Flask(__name__)

def get_db_connection(retries=5, delay=5):
    for attempt in range(retries):
        try:
            connection = mysql.connector.connect(
                host="db",                    # Service name from docker-compose.yml
                user="root",
                password=os.getenv("MYSQL_ROOT_PASSWORD", "example"),
                database=os.getenv("MYSQL_DATABASE", "test_db")
            )
            print("✅ Successfully connected to MySQL!")
            return connection
        except mysql.connector.Error as err:
            print(f"⏳ Database not ready yet (attempt {attempt+1}/{retries}): {err}")
            time.sleep(delay)
    raise Exception("❌ Could not connect to MySQL after multiple attempts.")

@app.route('/')
def hello_world():
    try:
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT 'Hello, Docker Compose! Flask + MySQL is working 🎉'")
        result = cursor.fetchone()
        connection.close()
        return f"<h1>{result[0]}</h1>"
    except Exception as e:
        return f"<h1 style='color:red'>Database Error: {str(e)}</h1>"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
```

#### B. `requirements.txt`
Right-click → **New File** → `requirements.txt`

```txt
Flask
mysql-connector-python
```

#### C. `Dockerfile` (for the Flask app)
Right-click → **New File** → `Dockerfile`

Use this updated version:

```dockerfile
FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]
```

#### D. `docker-compose.yml`
Right-click → **New File** → `docker-compose.yml`

Use this **improved and modern version**:

```yaml
version: '3.9'

services:
  db:
    image: mysql:8.0          # Updated from 5.7 (old and EOL)
    restart: always
    environment:
      MYSQL_ROOT_PASSWORD: example
      MYSQL_DATABASE: test_db
    ports:
      - "3306:3306"
    volumes:
      - db_data:/var/lib/mysql

  web:
    build: .
    restart: always
    ports:
      - "5000:5000"
    depends_on:
      db:
        condition: service_healthy   # Better than simple depends_on
    environment:
      FLASK_ENV: development
      MYSQL_ROOT_PASSWORD: example
      MYSQL_DATABASE: test_db
    volumes:
      - .:/app

volumes:
  db_data:
```

**Note**: The `healthcheck` is missing in the simple version above. For even better reliability, you can add a healthcheck to the `db` service later.

### 3. Run the Project in VS Code

#### Using the Integrated Terminal (Recommended)

1. Open Terminal: **Terminal → New Terminal** (Ctrl + `)

2. Make sure you're in the project folder.

3. Start everything with one command:

```bash
docker compose up --build
```

   - `--build` forces rebuilding the Flask image if you changed code.
   - Use `docker compose up --build -d` if you want it to run in the background.

4. Wait for output like:
   - MySQL starting...
   - Flask connecting (it will retry a few times — this is normal)
   - Flask running on http://0.0.0.0:5000

5. Open your browser and go to:  
   **http://localhost:5000**

You should see:  
!(image)[res.png]

### 4. Useful Commands

- Stop everything:  
  `Ctrl + C` (if running in foreground) or `docker compose down`

- Stop and remove volumes (reset database):  
  `docker compose down -v`

- Rebuild and restart:  
  `docker compose up --build`

- View logs:  
  `docker compose logs -f`  
  or `docker compose logs web` / `docker compose logs db`

- Using Docker Extension (GUI):  
  Click the Docker whale icon → right-click your compose project → Start / Stop / Restart.

### 5. Common Issues & Fixes

- **"Can't connect to MySQL"** or connection refused → Normal on first start. The retry logic in `app.py` handles it. Wait 10–20 seconds and refresh the browser.
- **Port already in use** → Change `5000:5000` to `5001:5000` in docker-compose.yml.
- **MySQL 8.0 authentication issues** → The code uses `mysql-connector-python`, which works fine with MySQL 8.0.
- **Changes not reflecting** → Because of the volume mount (`.:/app`), code changes should appear immediately (restart the web service if needed: `docker compose restart web`).

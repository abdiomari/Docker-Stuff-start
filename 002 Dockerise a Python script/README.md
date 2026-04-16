Here's a complete, beginner-friendly guide to run **Project 2: Dockerizing a Python script** entirely in **Visual Studio Code (VS Code)**.

### 1. Create the Project Folder in VS Code

1. Open VS Code.
2. Go to **File → Open Folder** → Create a new folder called `python-docker-script` and open it.

### 2. Create the Required Files

Inside your project folder, create these 4 files:

#### A. `data.csv` (sample data file)
Right-click → **New File** → name it `data.csv`

Paste this content:

```csv
Name,Age,Salary
Alice,28,75000
Bob,34,92000
Charlie,25,68000
Diana,41,115000
Eve,29,82000
```

#### B. `process_data.py` (the Python script)
Right-click → **New File** → name it `process_data.py`

Paste the script (slightly improved for better output):

```python
import pandas as pd

# Read the CSV file from the data folder
df = pd.read_csv('data/data.csv')

print("=== Data Preview ===")
print(df.head())

print("\n=== Statistical Summary ===")
print(df.describe())

print("\n=== Average Salary ===")
print(f"Average Salary: ${df['Salary'].mean():,.2f}")
```

#### C. `requirements.txt`
Right-click → **New File** → name it `requirements.txt`

Content:

```txt
pandas
```

#### D. `Dockerfile`
Right-click → **New File** → name it exactly `Dockerfile` (no extension)

Use this **improved version** (recommended over the original for 2026):

```dockerfile
# Use a lightweight Python base image
FROM python:3.12-slim

# Set working directory inside the container
WORKDIR /app

# Copy requirements first (for better Docker layer caching)
COPY requirements.txt .

# Install dependencies without caching pip packages (keeps image smaller)
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Default command to run when container starts
CMD ["python", "process_data.py"]
```

**Why this is better than the original:**
- Updated to `python:3.12-slim` (Python 3.9 is end-of-life).
- Better layer caching (`COPY requirements.txt` before `RUN pip install`).
- `--no-cache-dir` keeps the image size smaller.
- Clear comments for learning.

### 3. Build and Run the Project in VS Code

#### Method 1: Using Integrated Terminal (Recommended for learning)

1. Open Terminal in VS Code: **Terminal → New Terminal** (or Ctrl + ` )

2. Build the Docker image:

```bash
docker build -t python-script .
```

3. Run the container with volume mount (so it can read your `data.csv`):

**On macOS / Linux:**

```bash
docker run -v $(pwd)/data:/app/data python-script
```

**On Windows (PowerShell or Git Bash):**

```bash
docker run -v ${PWD}/data:/app/data python-script
```

Or simply (works in most cases):

```bash
docker run -v "%CD%/data":/app/data python-script
```

You should see output like:

![screenshot of Docker terminal](./res.png)

#### Method 2: Using Docker Extension (GUI)

1. Install the official **Docker** extension if not already installed.
2. Click the Docker icon on the left sidebar.
3. Right-click in the folder → **Docker: Build Image** (or build via terminal first).
4. Under **Images**, right-click your `python-script` image → **Run**.
5. When prompted for options, add the volume mount:  
   Host path: `data` (your local data folder)  
   Container path: `/app/data`

### 4. Common Issues & Fixes

- **"No such file or directory: 'data/data.csv'"**  
  → Make sure you created a `data` folder and put `data.csv` inside it.  
  → The volume mount must map correctly.

- **Permission or path issues on Windows**  
  → Use PowerShell and `${PWD}` or try Docker Desktop settings → Shared Drives.

- **pandas not found**  
  → You probably forgot to run `docker build` or the build failed.

- **Want to see the output again without rebuilding?**  
  Just run the container again.

### 5. Quick Tips & Next Improvements

- Create a `data/` subfolder in your project and keep `data.csv` inside it.
- After running once, try editing `data.csv` and run the container again — changes will reflect immediately thanks to the volume mount.
- To stop a running container: Use Docker sidebar → right-click → Stop.

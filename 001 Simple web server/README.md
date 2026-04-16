
### 1. Prerequisites

1. **Install Docker Desktop**  
   - Download and install from the official site: [docker.com](https://www.docker.com/products/docker-desktop/)  
   - After installation, open Docker Desktop and make sure it's running (the whale icon should be visible and healthy).  
   - On Windows: Switch to **Linux containers** mode if prompted.

2. **Install VS Code** (if you don't have it)  
   - Download from [code.visualstudio.com](https://code.visualstudio.com/)

3. **Install the Docker Extension in VS Code** (highly recommended)  
   - Open VS Code.  
   - Go to the **Extensions** view (Ctrl+Shift+X or Cmd+Shift+X on Mac).  
   - Search for "**Docker**" (the official one by Microsoft).  
   - Click **Install**.  
   - Once installed, you'll see a **Docker whale icon** on the left sidebar. This makes managing containers, images, and builds much easier with a GUI.

### 2. Create the Project in VS Code

1. Open VS Code.

2. Create a new folder for the project:  
   - Go to **File → Open Folder** → Click **New Folder** and name it something like `nginx-docker-project`.  
   - Open that folder in VS Code.

3. Create the `index.html` file inside the folder:  
   - Right-click in the Explorer sidebar → **New File** → name it `index.html`.  
   - Paste some simple content, for example:

```html
<!DOCTYPE html>
<html>
<head>
    <title>My Nginx Docker App</title>
</head>
<body>
    <h1>Hello from Nginx running in Docker!</h1>
    <p>This page is served from a Docker container.</p>
</body>
</html>
```

4. Create the **Dockerfile** (no file extension):  
   - Right-click in Explorer → **New File** → name it exactly `Dockerfile`.  
   - Paste the content from the project:

```dockerfile
FROM nginx:alpine
COPY ./index.html /usr/share/nginx/html
EXPOSE 80
```

### 3. Build and Run the Container

You have two easy ways to do this in VS Code:

#### Option A: Using the Integrated Terminal (Simplest for beginners)

1. Open the integrated terminal in VS Code:  
   - Go to **Terminal → New Terminal** (or Ctrl+` ).

2. Make sure you're in the project folder (the terminal prompt should show the folder name).

3. Build the image:

```bash
docker build -t my-nginx-app .
```

   (The dot `.` at the end is important — it means "use the current directory".)

4. Run the container:

```bash
docker run -d -p 8080:80 my-nginx-app
```

   - `-d` = detached (runs in background)  
   - `-p 8080:80` = maps port 8080 on your computer to port 80 inside the container

5. Open your browser and go to:  
   **http://localhost:8080**

You should see your "Hello from Docker" page!

#### Option B: Using the Docker Extension (GUI way — very convenient)

1. Click the **Docker whale icon** on the left sidebar or from your pc.

2. Under **Images**, you should see your image after building (or build it via terminal first).

3. To build using the extension:  
   - Right-click your folder in Explorer → **Docker: Build Image** (or use Command Palette).

4. To run:  
   - Go to **Images** section → right-click your `my-nginx-app` image → **Run**.  
   - In the prompt, set the port mapping: `-p 8080:80` (or use the interactive options).

5. Under **Containers**, you can see your running container, view logs, stop it, or restart it with a click.

### 4. Useful Tips While Working in VS Code

- **Stop the container** when done:  
  In the Docker sidebar → Containers → right-click your container → **Stop** or **Remove**.

- **Rebuild after changes**: If you edit `index.html`, run the build command again (or use Docker extension).

- **Command Palette shortcuts** (very useful):  
  Press `Ctrl+Shift+P` (or `Cmd+Shift+P` on Mac) and type:  
  - "Docker: Build Image"  
  - "Docker: Run"  
  - "Docker: Stop Container"

- **View logs easily**: In Docker sidebar → right-click running container → **Show Logs**.

- **Make changes and test quickly**: Edit `index.html` → rebuild → refresh browser.

### 5. Common Issues & Fixes

- **"docker: command not found"** → Docker Desktop is not installed or not running.
- **Port already in use** → Change the host port, e.g., `-p 8081:80` and open `http://localhost:8081`.
- **Permission issues on Linux** → Add your user to the docker group.
- **Nothing shows in browser** → Check the container is running (green in Docker sidebar) and the port mapping is correct.


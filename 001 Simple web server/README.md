README.md for Project 1
Markdown# Project 1: Simple Nginx Web Server with Docker

This project introduces the basics of Docker by creating and running a lightweight Nginx web server inside a container.

### Goal
Learn how to build a Docker image, expose ports, and access a containerized web application from your browser.

---

## Technologies Used
- Docker
- Nginx (Alpine)

---

## Project Structure
nginx-docker-project/
├── index.html
├── Dockerfile
└── README.md
text---

## How to Run

### 1. Build the Image
```bash
docker build -t my-nginx-app .

2. Run the Container
Bashdocker run -d -p 8080:80 my-nginx-app
3. Access the Application
Open your browser and visit:
http://localhost:8080
You should see the content of your index.html page.

Key Commands
Bashdocker ps                    # List running containers
docker logs <container-id>   # View container logs
docker stop <container-id>   # Stop the container

Key Learnings

Using official base images (FROM nginx:alpine)
Copying files into the container (COPY)
Exposing ports (EXPOSE)
Port mapping between host and container (-p)
Running containers in detached mode (-d)
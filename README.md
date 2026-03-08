# Docker-Stuff-start — Building Dockerized Applications from Scratch

## Overview
This project serves as a starting point for learning Docker and containerization. It demonstrates a simple web application that interacts with a MongoDB database, showcasing the power of Dockerized development. The goal is to provide a foundation for building scalable and portable applications.

## Tech Stack
* Primary language: HTML
* Frameworks:
	+ Express.js for the web application
	+ MongoDB for the database
* Libraries:
	+ Body-Parser for handling HTTP requests
	+ MongoDB Node.js Driver for interacting with the database
* Databases: MongoDB

## Features
* A simple web application that serves an HTML index page
* A RESTful API for updating and retrieving user profiles
* Integration with a MongoDB database for storing user data
* Support for serving profile pictures from the application
* Dockerization of the application and database for easy deployment

## Screenshots
> 📸 Screenshots coming soon. Run the project locally to see it in action.

## Setup & Installation
1. Clone the repository using Git:
```bash
git clone https://github.com/abdiomari/Docker-Stuff-start.git
```
2. Navigate to the project directory:
```bash
cd Docker-Stuff-start
```
3. Install the dependencies using npm:
```bash
npm install
```
4. Create a `.env` file to store environment variables:
```bash
touch .env
```
5. Add the following environment variables to the `.env` file:
```makefile
MONGO_URL=mongodb://admin:password@mongodb
```
6. Build the Docker image:
```bash
docker build -t docker-stuff-start .
```
7. Run the Docker container:
```bash
docker run -p 3000:3000 -d docker-stuff-start
```
8. Access the application by navigating to `http://localhost:3000` in your web browser.
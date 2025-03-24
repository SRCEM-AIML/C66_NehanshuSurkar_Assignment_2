# C66_NehanshuSurkar_Assignment_2

This project is a multi-app Django web application, deployed with Docker and automated using a Jenkins CI/CD pipeline.

The pipeline:

1) Pulls the code from GitHub
2) Builds a Docker image
3) Runs the container locally
4) Pushes the image to Docker Hub

Way to run project :

1) Clone GitHub repository
git clone (https://github.com/SRCEM-AIML/C66_NehanshuSurkar_Assignment_2.git)
cd StudentProject


2) Build and run with Docker
docker build -t studentproject .
docker run -d -p 8000:8000 --name studentproject studentproject

  
3) Running with Jenkins Pipeline
The Jenkins pipeline will:
       Clone the repository
       Build the Docker image
       Push the image to Docker Hub
    
4) Pull Docker Hub Image
docker pull nehanshusurkar20/studentproject:latest
 

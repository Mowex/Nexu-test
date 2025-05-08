# 🚀 FastAPI Project Initialization (Dockerized)

This project uses **Python 3.10.6** and [FastAPI](https://fastapi.tiangolo.com/) to build a fast and robust API. It is fully containerized using **Docker** for easier deployment.

## ✅ Prerequisites

To run this project, you need to have [Docker](https://www.docker.com/products/docker-desktop/) and [Docker Compose](https://docs.docker.com/compose/install/) installed on your system.

## ▶️ How to Run

Clone the repository and navigate into the project directory. Then, run the following command to build and start the application:

`docker-compose up --build`

This will start the FastAPI application, and it will be accessible at [http://localhost:8000](http://localhost:8000). You can visit the interactive API documentation at [http://localhost:8000/docs](http://localhost:8000/docs) or the alternative documentation at [http://localhost:8000/redoc](http://localhost:8000/redoc).

If you make changes to the source code and want them to reflect in the running app, stop the container with `CTRL+C` and re-run the command:

`docker-compose up --build`

To stop and remove the container, use:

`docker-compose down`

## 🧪 Running Tests (Optional)

If you'd like to run the tests outside of Docker, create a virtual environment with `python -m venv venv`, activate it (`.\venv\Scripts\activate` on Windows or `source venv/bin/activate` on macOS/Linux), install dependencies with `pip install -r requirements.txt`, and run the tests using `pytest`.

## 👨‍💻 Personal Comment

Project created with the goal of obtaining a full-stack developer position at **Nexu**! Completing this test in two hours was a real challenge because, despite knowing the technology, there are always small errors that need to be resolved — and that takes time. The initial setup took more time than expected (normal, I think, since we don’t bootstrap new projects every day). I obviously took more than two hours to complete the project, but I preferred submitting something finished rather than incomplete. You have the final say… **Thanks a lot for considering me!**

# Anime Girl Image Server

This project is a simple Flask web server that serves random anime girl images from a local image database.

## Features

- Serves a random image from the `IMG_DB` folder at the `/Anime-girl` endpoint.
- Health check endpoint at `/` returns "Alive".
- Ready for deployment with Docker and Gunicorn.

## Getting Started

### Prerequisites

- Python 3.9+
- pip
- Docker (optional, for containerized deployment)

### Installation

1. Clone this repository and navigate to the project directory.
2. Install dependencies:
   ```sh
   pip install flask gunicorn
   ```
3. Place your images (`.jpg`, `.jpeg`, `.png`, `.gif`) in the `IMG_DB` folder.

### Running Locally

```sh
python app.py
```


### Running with Docker

1. Build the Docker image:
   ```sh
   docker build -t anime-girl-server .
   ```
2. Run the container:
   ```sh
   docker run -p 5000:5000 anime-girl-server
   ```

## Endpoints

- `/` - Health check, returns "Alive".
- `/Anime-girl` - Returns a random image from `IMG_DB`.



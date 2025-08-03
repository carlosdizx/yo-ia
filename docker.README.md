# 📦 Streamlit App with Docker

This project runs a **Streamlit** application using **Docker**.

---

## 🚀 Requirements

- [Docker](https://www.docker.com/) must be installed on your system.

---

## 🛠️ Build the Docker Image

Run the following command from the root directory (where the `Dockerfile` is located):

```bash
docker build -t ai-me .
```

## ▶️ Run the App Locally
To run the container and expose the app on your local machine:

```bash
docker run -p 8501:8501 ai-me
```
### !!️ Note: Make sure to replace `8501` with the desired port number before running the command.
### PD: Add your environment variables to the `.streamlit/secrets.toml` file
### Example:
```toml
[GEMINI]
API_KEY = "...."
MODEL = "gemini-2.5-flash"
```
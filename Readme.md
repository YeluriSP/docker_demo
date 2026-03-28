# Simple Chatbot (Docker + Valkey + OpenAI)

## 🚀 Setup

### 1. Clone repo

```bash
git clone <your-repo>
cd docker_demo
```

### 2. Create env file

```bash
cp .env.example .env
```

Add your OpenAI API key inside `.env`.

---

### 3. Start Docker

Make sure Docker Desktop is running.

---

### 4. Run app

```bash
docker compose -f chatbot.yaml up --build
```

---

### 5. Open browser

```
http://localhost:8082
```

---

## 🧱 Tech Stack

* Streamlit
* OpenAI API
* Valkey (Redis)
* Docker + Docker Compose

---

## 📌 Notes

* Chat history is stored in Valkey
* Data persists via Docker volume (`chatbot_vol`)

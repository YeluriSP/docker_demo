FROM python:3.11-slim

WORKDIR /app

# Copy files
COPY app/ /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose Streamlit port
EXPOSE 8082

# Run app
CMD ["streamlit", "run", "app.py", "--server.port=8082", "--server.address=0.0.0.0"]
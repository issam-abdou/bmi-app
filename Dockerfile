# 1. Start with a "Base Image" (A tiny version of Linux with Python)
FROM python:3.10-slim

# 2. Set the working directory inside the container
WORKDIR /app

# 3. Copy your list of requirements
COPY requirements.txt .

# 4. Install the requirements inside the container
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy your main.py code into the container
COPY . .

# 6. The command to run your app
# We use 0.0.0.0 to make it accessible outside the container
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "3000"]
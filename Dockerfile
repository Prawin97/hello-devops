# Step 1: Use an official Python image
FROM python:3.13-slim

# Step 2: Create a working directory
WORKDIR /app

# Step 3: Copy dependency file
COPY requirements.txt .

# Step 4: Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Step 5: Copy application code
COPY . .

# Step 6: Tell Docker which port the app uses
EXPOSE 8000

# Step 7: Start the application
CMD ["python", "app.py"]
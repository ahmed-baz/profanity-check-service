# Step 1: Use an official Python runtime as the base image
FROM python:3.9-slim

# Step 2: Set the working directory in the container
WORKDIR /src

# Step 3: Copy the current directory contents into the container
COPY . /src

# Step 4: Install the required Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Step 5: Expose the port the app runs on
EXPOSE 5000

# Step 6: Define environment variable for Flask (optional)
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Step 7: Run the Flask app when the container starts
CMD ["flask", "run"]

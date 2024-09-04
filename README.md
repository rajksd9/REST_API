# Running the Application

Follow these steps to get the application up and running:

1. **Download or Clone the Repository**
   - Clone the repository using `git clone <repository-url>` or download the zip file and extract it.

2. **Install Required Packages**
   - Navigate to the project directory and install the necessary packages:
     ```bash
     pip install flask
     pip install flask-sqlalchemy
     pip install pytest
     pip install flask-swagger-ui
     ```

3. **Set Up the Flask Environment**
   - Open PowerShell and navigate to the current directory (code folder).
   - Set the Flask environment variable:
     ```powershell
     $env:FLASK_APP = "src/app.py"
     ```

4. **Set Up PostgreSQL**
   - Ensure that PostgreSQL is set up and running. You can use either a local PostgreSQL server or a Docker image with the database data from the `database` folder.
   - Update the PostgreSQL URL in `app.py` to match your setup.

5. **Run the Flask Application**
   - Start the Flask application:
     ```bash
     flask run
     ```

6. **Access Documentation**
   - Open your web browser and go to [http://localhost:5000/swagger](http://localhost:5000/swagger) for detailed documentation.

---

Feel free to reach out if you encounter any issues or need further assistance!

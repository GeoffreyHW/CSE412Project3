1. Download files

2. Install postgres
   Create movies database:
   psql -U postgres

   In the new interface type in:
   'create database movies'

   Type in \q to quit the interface

   Import database:
   psql -U postgres movies < inputfile.pgsql
   Now you have the database set up!

3. Download python

4. Configure config.py
   postgresql://USERNAME:YOURPASSWORD@localhost/movies

5. Set environment variable for pip

6. Navigate to downloaded folder in console

7. pip install -r requirements.txt 

8. Type 'set FLASK_APP=movie.py'

9. Type 'flask run'

10. Go to 127.0.0.1:5000 on your browser


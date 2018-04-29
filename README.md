1. Download files
2. Install postgres
   Create movies database:
   psql -U postgres
   In the new interface type in:
   create database movies
   Type in \q to quit 

   Import database:
   psql -U postgres movies < inputfile.pgsql
   Now you have the database set up!
3. Download python
4. Set environment variable
5. pip install -r requirements.txt
6. Configure config.py
   postgresql://USERNAME:YOURPASSWORD@localhost/movies
7. Go to 127.0.0.1:5000 on your browser


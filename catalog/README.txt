# Source code for Music Catalog Project
This project will display a website, listing music genres, artists that fall under each genre and biography for each genre.  
If the user is not logged in, the home page will show the currently entered music genres.  When a genre is selected, one will see artists that are associated with the genre.  When an artist name is selected, one will see the biography of an artist or a band.  
If the user authenticates via google login, one will have an option of adding a new music genre, as well as new artists for the music genre.  User will also have an ability to edit or delete either genre or artist info that was added by them.  User is not allowed to modify any information that wasn't created by them.
JSON version of the response is available via following links:
http://localhost:8000/genre/JSON
http://localhost:8000/genre/2/artist/JSON  - where '2' is an example of genre_id

# Instructions
1. Create a database and applicable tables by running 'python database_setup.py' in command prompt 
2. Populate intial entries in a database by running 'python loadMusic.py'
3. Start application by running 'python application.py'
4. Open the following url http://localhost:8000/ in Chrome

Authentication code has been based off of udactiy lessons

## License
N/A

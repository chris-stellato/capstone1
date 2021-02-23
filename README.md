# Chris Stellato - Capstone 1 project


## Proposal 2: 
### Spotify Million Playlist Dataset
https://www.aicrowd.com/challenges/spotify-million-playlist-dataset-challenge

#### Dataset
This dataset contains records of 1M spotify playlists, allowing Data Scientists to draw connections between songs within playlists and make helpful recommendations to users. Some interesting fields include: 
* playlist identifier
* playlist tracklist and track ids
* timestamp last edit
* count of number of edits to the playlist
* playlist length

#### Possible Visualizations
* distribution of playlist length (maybe asking what is the "perfect length mixtape"?) 
* histogram of genres most added to playlists
* scatterplot mapping genre spread in playlists (asking how diverse is each playlist?)

#### Possible Hypotheses to test: 
* "95% of playlists have between X and Y tracks in them"
* "Playlists usually stick to one genre and rarely deviate"

Monday update: 
- Dowloaded data
- launched spark docker instance, created jupyter notebook
- read in json file and explored data
- worked to move nested data into workable dataframes
- still in data wrangling mode. 

# Chris Stellato - Capstone 1 proposals


## Proposal 1: 
### Colorado Avalanche Information Center Data
https://docs.google.com/spreadsheets/d/1j4-5IKizg1dZ7N1honszrvymsNvKPPOAX8ltxLaXK58/edit?usp=sharing

#### Dataset
This dataset contains records of avalanche-related fatalities from 1951 through 2020. It contains several interesting data points for each incident, including: 
* location
* date of occurrance
* mode of travel (skis, snowshoes, snowmobile, etc)
* number of fatalities per incident
* magnitude of burial and incident details (only for more recent years. 
* NOTE: falls shy of the recommended data size @ only 914 rows

#### Possible Visualizations
* Heat map of avalanche fatalities by location
* histogram of fatalities by method of travel or by location
* probability of fatality incident by month, showing months with highest probability for fatal incidents

#### Possible Hypotheses to test: 
* "Traveling by X method is the most dangerous method when considering avalanche fatalities"
* "Choosing to recreate during X month increases the probability of an avalanche fatality incident by Y% vs. Z month
* "Due to regional snowpack characteristics and local demographics, X state is the most dangerous state to be a backcountry traveler" 


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


## Proposal 2: 
### Ski Resort Snowfall
https://www.kaggle.com/mrmarjo/resort-daily-snowfall-20092017

#### Dataset
This dataset contains information about daily snowfall for four major ski resorts in North America. This could allow some insight into which are the "best weeks" during the winter to visit a resort if you're hoping to score powder (or avoid it!). Fields include : 
* daily snowfall by date
* cumulative season-to-date snowfall
* base depth measurement by date

#### Possible Visualizations
* plotted lines showing base depth progression throughout the season
* histogram showing number of "powder days" (parameters can be defined) by resort and by month or week
* scatter plot showing snow events using dot size to represent snow impact to each area.

#### Possible Hypotheses to test: 
* "If you were to randomly pick a day out of the season, you'd have the best chance of powder at X resort"
* "If you were to go skiing during New Years week, you'd have the best chance of powder at X resort" 
* "When there is a snowfall event, X resort typically gets the deepest 24 hour snowfall (even if another resort has more snow events total)"

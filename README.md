# Chris Stellato - Capstone 1 project
#### Spotify Million Playlist Dataset

### Presentation
The final project presentation includes visual aids, results of hypothesis testing, and a summary of insights and takeaways.
View the final project presentation:
https://github.com/chris-stellato/capstone_1/blob/master/capstone_1_presentation.pdf



#

#
#### Original Proposal: 
Spotify Million Playlist Dataset
https://www.aicrowd.com/challenges/spotify-million-playlist-dataset-challenge

##### Dataset
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





## Daily project updates:
#### Monday update: 
- Dowloaded data
- launched spark docker instance, created jupyter notebook
- read in json file and explored data
- worked to move nested data into workable dataframes
- still in data wrangling mode. 

#### Tuesday update: 
- continued EDA
- cleaned dataframes & added diversity_ratio column
- started seeing if columns of interest were normally distributed
- started thinking about possible hypothesis and how to test them
- mucked around with unsuccessful distributions, sampling, graphs that didn't bear fruit

#### Wednesday update: 
- combined multiple JSON files into a single dataframe with 20k playlist records
- checked again that diversity_ratio and num_followers are NOT normally distributed
- set up bootstrapping to generate list of sample sets and the means of each sample set
- plotted those bootstrapped distributions to find normal distributions
- defined confidence intervals and ran hypothesis test, rejected null hypothesis 
- discussed maybe bootstrap isn't the best approach, should look at beta distributions and bayes

#### Thursday update: 
- adjusted bootstrappping method
- clarified hypothesis test
- cleaned up visuals
- began creating presentation

### Friday update:
- finishing presentation
- review with instructors and make adjustments
- add py files with helper functions to repo
- add presentation to repo
- clean up repo and prepare for presentation

# Spotify2019-Dashboard
https://newsroom.spotify.com/2019-12-03/the-top-songs-artists-playlists-and-podcasts-of-2019-and-the-last-decade/

Overview: 
--
On December 3, 2019, Spotify announced the top male and female artist of the decade. 
Males: Drake, Ed Sheeran, Post Malone, The Weeknd, Eminmen
Females: Sia, Beyonce, Taylor Swift, Ariana Grande, and Rihanna. 

Objective:
-- 
- Extract data from the Spotify API and conduct a cluster analysis to created 4 playlist based on the audio features from each track. 

Tableau Visualization: 
--
https://public.tableau.com/profile/drucila#!/vizhome/TopStreamedArtistsoftheDecadePlaylist_Inworks/introduction

Audio Features
---
Audio Features Source: https://developer.spotify.com/documentation/web-api/reference/tracks/get-audio-features/

- Acousticness: 	A confidence measure from 0.0 to 1.0 of whether the track is acoustic. 1.0 represents high confidence the track is acoustic. 

- Danceability: Danceability describes how suitable a track is for dancing based on a combination of musical elements including tempo, rhythm stability, beat strength, and overall regularity.

- Instrumentalness:	Predicts whether a track contains no vocals. 

- Energy: A measure from 0.0 to 1.0 and represents a perceptual measure of intensity and activity. Typically, energetic tracks feel fast, loud, and noisy. For example, death metal has high energy, while a Bach prelude scores low on the scale.

- Speechiness: detects the presence of spoken words in a track. The more exclusively speech-like the recording (e.g. talk show, audio book, poetry), the closer to 1.0 the attribute value. Values above 0.66 describe tracks that are probably made entirely of spoken words.

Clustering
--
- Standarized the range of the data which will enable the audio features have a an impact on the results.

Elbow Method 
--
- Detemine the number of clusters. 
- Using the Elbow Method, the Sum of the Squared Distances(SSD) decrease as the k value increase. 
- Decision: Choose a k value (5) that will result in the SSD decrease a bit lower.

Principal Component Analysis 
--
From the scree plot, 4 components were extracted. 

T-Distributed Stochastic Neighbor Embedding
--
- Use this method to visualize all five clusters. 
- Cluster 3 contains most of the songs

Cluster Profiling & Sample
-- 
Cluster 1: Roadtrip Playlist: High in danceability, energy, and speechiness (lyrical)

https://open.spotify.com/playlist/0iFXC0s8nqMKvBGXCsLpR5?si=VahgckKKSymo2sWLEqSYmA

Cluster 2: Time to Relax: high in acousticness, danceabillity, and energy

https://open.spotify.com/playlist/472Rwu3iNXCN41yUTi9efG?si=X4t-mSCFSkGFnOISbL7JHA

Cluster 3: Let's Party: High in both danceability and energy

https://open.spotify.com/playlist/3Uq0IGWpDSO5YLtYEvDVk2?si=cE48dKZFTvqfi4noUJhn2g

Cluster 4: Energy Booster: Highest in energy

https://open.spotify.com/playlist/170hEWj2iCX8PdCSUXlez3?si=LZCAQp5oTjidUi0wcuJeag

Cluster 5: GoodMorning: Great songs to wake up and get you motivated (High instrumentalness and energy)

https://open.spotify.com/playlist/0bLwx8AshIUjm0ysyk7MRo?si=5LvKpJZRR1CqvVgPM-eq7Q








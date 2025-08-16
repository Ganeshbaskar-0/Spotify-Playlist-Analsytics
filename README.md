# Spotify-Playlist-Analsytics
This project fetches Spotify playlist data via API, cleans and stores it in MySQL, and exports it to CSV. It includes popularity visualizations using Matplotlib, with error handling and duplicate checks. A complete data pipeline showcasing Python, SQL, and data visualization skills.

## Project Overview
This repository fetches data from a Spotify playlist using the **Spotify Web API**, performs data cleaning, stores track details in a MySQL database, exports the data to CSV, and generates a popularity visualization using Matplotlib.

---

## Feature Highlights
- Extract playlist tracks along with metadata (track name, artist, album, genre, popularity, duration).
- Clean track and album names to remove extraneous details.
- Insert data into a MySQL table with duplicate tracking.
- Export cleaned data to a CSV file.
- Render a bar chart of track popularity and save as `popularity_chart.png`.

---

## Required Spotify API Credentials
You must create a Spotify app on the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/applications) to obtain:

- **Client ID**  
- **Client Secret**  

Use these credentials securely (e.g. via a `.env` file) to authenticate using the *Client Credentials* flow for backend access.

---

## Setup Instructions

### 1. Clone the Project
```bash
git clone https://github.com/Ganeshbaskar-0/Spotify-Playlist-Analsytics.git
cd Spotify-Playlist-Analsytics
```

2. Install Dependencies
```bash
pip install spotipy pandas matplotlib mysql-connector-python python-dotenv
```

4. Configure Environment
Create a .env file with:
```bash
CLIENT_ID=your_spotify_client_id
CLIENT_SECRET=your_spotify_client_secret
```

4. Prepare MySQL Database
```bash
CREATE DATABASE spotify_db;
USE spotify_db;

CREATE TABLE spotify_tracks (
  id INT AUTO_INCREMENT PRIMARY KEY,
  Track VARCHAR(255) NOT NULL,
  Artist VARCHAR(255) NOT NULL,
  Genre VARCHAR(255),
  Album VARCHAR(255),
  Popularity INT,
  Duration_minutes FLOAT,
  UNIQUE (Track, Album)
);
```

5. Run the Script
```bash
python main.py
```

What You’ll Get:
    *A MySQL table (spotify_tracks) populated with cleaned track data.
    *A CSV file (playlist_tracks_list.csv) with the full dataset.
    *A visual bar chart (popularity_chart.png) showing track popularity.

Future Enhancements:
    *Pull and merge data from multiple playlists.
    *Add visualizations such as genre distribution or artist analysis.
    *Deploy an interactive dashboard using Flask or Streamlit.

Author:
```bash
    Ganesh Baskar
    Aspiring Data Analyst • GitHub: Ganeshbaskar-0
```



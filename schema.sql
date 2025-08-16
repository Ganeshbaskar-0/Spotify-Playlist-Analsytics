-- Create the database
CREATE DATABASE IF NOT EXISTS spotify_db;
USE spotify_db;

-- Create the table to store playlist tracks
CREATE TABLE IF NOT EXISTS spotify_tracks (
  id INT AUTO_INCREMENT PRIMARY KEY,
  Track VARCHAR(255) NOT NULL,
  Artist VARCHAR(255) NOT NULL,
  Genre VARCHAR(255),
  Album VARCHAR(255),
  Popularity INT,
  Duration_minutes FLOAT,
  UNIQUE (Track, Album)  -- Prevent duplicate tracks in same album
);

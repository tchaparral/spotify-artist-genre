# Spotify Artist Genre Finder

A simple web application built with Python and Streamlit that retrieves the genres of artists using the Spotify API.

---

## Description

This application allows users to input an artist's name and retrieves the associated genres from Spotify. It uses the Spotify API to fetch the data and displays it in a user-friendly interface.

---

## Features

- **Artist Search**: Enter the name of an artist to retrieve their genres.
- **Spotify API Integration**: Uses the Spotify API to fetch accurate genre data.
- **Environment Variables**: Securely manages API credentials using `.env` files.

---

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/tchaparral/spotify-artist-genre.git
   cd spotify-artist-genre
2. **Set up a Virtual Environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
3. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
4. **Set Up Environment Variables**:
    <li>Rename the .env_example file to .env
    ```bash    
    mv .env_example .env
    <li>Open the .env file and replace the placeholders with your Spotify API credentials:
    ```bash
    CLIENT_ID = 'your_client_id_here'
    CLIENT_SECRET = 'your_client_secret_here'
5. **Run the Application**:
    ```bash
    streamlit run app.py
## Usage

- Open the application in your browser (usually at http://localhost:8501).
- Enter the name of an artist in the input field.
- Click the "Search Genres" button to see the artist's genres.

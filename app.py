'''Streamlit application module'''

import streamlit as st
from spotify_functions import get_artist_genre

# App Title
st.title("Find Artist Genres on Spotify")

# User Input
artist_name = st.text_input("Enter the artist name:")

# Search Button
if st.button("Search Genres"):
    if artist_name:
        genres = get_artist_genre(artist_name)
        if genres:
            st.success(f"Genres for {artist_name}: {', '.join(genres)}")
        else:
            st.error("No genres found for this artist.")
    else:
        st.warning("Please enter an artist name.")

# End-of-file (EOF)

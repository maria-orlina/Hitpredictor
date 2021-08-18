import streamlit as st
from PIL import Image
import pickle

# load the saved model
model = pickle.load(open('billboard.pkl','rb'))


def run():
    img1 = Image.open('billboard-hot100.jpeg')
    img1 = img1.resize((200, 145))
    st.image(img1, use_column_width=False)
    st.title("BillBoard Hit Prediction using Machine Learning")
    st.text("Done by Maria Orlina")


    songname = st.text_input("song name")

    instrumentalness = st.number_input("instrumentalness")

    acousticness= st.number_input("acousticness")

    duration_ms = st.number_input("duration_ms")

    energy = st.number_input("energy")

    loudness = st.number_input("loudness")

    liveness = st.number_input("liveness")

    valence = st.number_input("valence")

    danceability = st.number_input("danceability")

    Key = st.number_input("Key")

    speechiness = st.number_input("speechiness")

    tempo = st.number_input("tempo")

    mode = st.number_input("mode")

    if st.button("Submit"):

        features = ([[danceability, energy, loudness, speechiness, acousticness, instrumentalness, liveness,
                      valence, tempo, Key, mode, duration_ms]])

        print(features)
        prediction = model.predict(features)
        lc = [str(i) for i in prediction]
        ans = int("".join(lc))

        if ans == 0:
          st.error("It's not a Hit")
        else:
          st.success("It's a Hit")
run()

import requests
import streamlit as st
import pickle

movies = pickle.load(open("movie_list.pkl", "rb"))
similarity = pickle.load(open("similarity.pkl", "rb"))


def recommend(movie):
    movie_index = movies[movies["title"] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[
        1:6
    ]
    recommended_movies = []
    for i in movies_list:
        # print(i)
        movie_id = movies.iloc[i[0]].movie_id
        url = "https://api.themoviedb.org/3/movie/{}?api_key=9db0eb5fb37b0b3ffdf2571dbdbf1618&language=en-US".format(
            movie_id
        )
        poster = requests.get(url)
        data = poster.json()
        recommended_movies.append(
            {
                "movie_title": movies.iloc[i[0]].title,
                "poster_path": "https://image.tmdb.org/t/p/w500" + data["poster_path"],
            }
        )
    return recommended_movies


st.title("Movie Recommendation System")
st.write("Welcome to the Movie Recommendation System")
st.write("This system will recommend you the best movies based on your preferences")
selected_movies = st.selectbox("Select a movie", movies["title"].values)
# if selected_movies:
# st.write("You have selected: ",selected_movies)
# st.button('Recommend')
if st.button("Recommend"):
    recommend_movies = recommend(selected_movies)
    st.write("You may like the following movies:")
    # for movies in recommend_movies:
    # Show in 5 columns
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommend_movies[0]["movie_title"])
        st.image(recommend_movies[0]["poster_path"])
    with col2:
        st.text(recommend_movies[1]["movie_title"])
        st.image(recommend_movies[1]["poster_path"])
    with col3:
        st.text(recommend_movies[2]["movie_title"])
        st.image(recommend_movies[2]["poster_path"])
    with col4:
        st.text(recommend_movies[3]["movie_title"])
        st.image(recommend_movies[3]["poster_path"])
    with col5:
        st.text(recommend_movies[4]["movie_title"])
        st.image(recommend_movies[4]["poster_path"])


# st.write('You have selected:', st.selectbox('Select a movie', movies['title'].values))

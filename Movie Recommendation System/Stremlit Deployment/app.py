import streamlit as st
import pickle
import pandas as pd
import requests

movies_dict = pickle.load(open('movies_dict.pkl','rb'))
movies =pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl','rb'))

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]  # similarity matrix of the particular index

    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies=[]
    recommended_movies_poster=[]
    for i in movies_list:
        movie_id=movies.iloc[i[0]].movie_id


        recommended_movies.append(movies.iloc[i[0]].title)
        # fetching posters from api
        recommended_movies_poster.append(fetch_poster(movie_id))

    return recommended_movies,recommended_movies_poster

def fetch_poster(movie_id):
    response= requests.get('https://api.themoviedb.org/3/movie/{}?api_key=95d78c73dcc1f1c126a46c0d808960bd&language=en-US'.format(movie_id))
    data= response.json()
    #print(data)
    return "https://image.tmdb.org/t/p/w500/"+data['poster_path']

st.title('Movie Recommendation System Based on TMDb')

selected_movie_name = st.selectbox( 'Write the name of your movie...', movies['title'].values)

if st.button('Recommend'):
    names,posters = recommend(selected_movie_name)

    col1,col2,col3,col4,col5= st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])

    # for i in recommendations:
    #     st.write(i)
import {defineStore} from 'pinia';
import {ref} from 'vue';

export const useMoviesStore = defineStore('movies', () => {
    const movieSearch = ref('');
    const movies = ref([]);
    const selectedMovie = ref({});
    const movieReviews = ref([]);
    const searchErrorMessage = ref('');

    

    
    async function searchMovies() {
        
        try{
            const response = await fetch(`api/movie?q=${movieSearch.value}`);
            const data = await response.json();
            if (!response.ok) {
                searchErrorMessage.value = data.error;
                movies.value = [];
            }
            else{
                movies.value = data;
                searchErrorMessage.value = '';                
            }
        }
        catch (error) {
            console.error('Error fetching movies:', error);
            searchErrorMessage.value = 'An error occurred while fetching movies.';
        }       
        
    }   

    function clearSearch() {
        movieSearch.value = '';
        movies.value = [];
        movieReviews.value = [];
        selectedMovie.value = '';
        searchErrorMessage.value = '';
    }

    async function fetchMovieReviews(movie) {
        try {
            const response = await fetch(`api/reviews`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ 'url': movie.url })
            });
            const data = await response.json();
            if (!response.ok) {                
                movieReviews.value = [];
            } else {
                selectedMovie.value = movie;
                movieReviews.value = data;
            }
        } catch (error) {
            console.error('Error fetching movie reviews:', error);
            movieReviews.value = [];
        }
    }

    return {
        movieSearch,
        movies,
        selectedMovie,
        movieReviews,
        searchErrorMessage,        
        searchMovies,
        clearSearch,
        fetchMovieReviews
        
    };

})
<template>
  <v-card
    v-if="store.movies.length > 0"
    class="search-card"
    dark
    outlined
  >
    <v-card-title>
      <h1>Search Results</h1>
    </v-card-title>
    <v-card-text>
      <v-list>
        <v-list-item-group>
          <v-list-item
            v-for="movie in store.movies"
            :key="movie.title"
            class="search-card-item"
            :class="{ 'search-card-item-selected': store.selectedMovie === movie }"
            @click="store.fetchMovieReviews(movie)"            
          >
            <v-list-item-content>
              <v-card>
                <template #title>
                  {{ movie.title }} ({{ movie.year }})
                </template>
                <template #subtitle>
                  Staring: {{ movie.cast }}
                </template>
                <template #text>
                  <v-list v-if="store.movieReviews.length > 0 && store.selectedMovie === movie">
                    <v-list-item-group>
                      <v-list-item
                        v-for="review in store.movieReviews"
                        :key="review.id"
                      >
                        <v-list-item-content>
                          <v-card outlined>
                            <v-card-text>
                              {{ review.content }}
                            </v-card-text>
                          </v-card>
                        </v-list-item-content>
                      </v-list-item>
                    </v-list-item-group>
                  </v-list>
                </template>
              </v-card>
            </v-list-item-content>
          </v-list-item>
        </v-list-item-group>
      </v-list>
    </v-card-text>
  </v-card>
</template>
<script setup>
    import { useMoviesStore } from "@/stores/moviesStore";

    const store = useMoviesStore();
</script>

<style scoped lang="scss">
    .search-card {
        margin: 20px;
        padding: 20px;
        color: #ecf0f1;
    }
    
    .search-card-item {
        cursor: pointer;
        transition: background-color 0.3s ease;
        margin: 1rem;
        padding: 3rem;        
        border-bottom:  1px solid #34495e;
    }
    
    // .search-card-item:hover {
    //     background-color: primary;
    // }
    
    .search-card-item-selected {
        background-color: #2980b9 !important;
        color: #ecf0f1 !important;
    }
</style>
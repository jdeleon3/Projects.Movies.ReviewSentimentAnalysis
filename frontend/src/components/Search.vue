<template>
  <v-card
    class="search-card"
    dark
    outlined
  >
    <v-card-title>
      <h1>Search Movies</h1>
    </v-card-title>
    <v-card-text>
      <v-text-field
        v-model="store.movieSearch"
        label="Search for a movie"
        @keyup.enter="store.searchMovies"
      />
      <v-btn
        color="primary"
        @click="store.searchMovies"
      >
        Search
      </v-btn>
      <v-btn
        color="primary"
        style="margin-left: 8px;"
        @click="store.clearSearch"
      >
        Clear
      </v-btn>
    </v-card-text>
  </v-card>
</template>

<script setup>
    import { useMoviesStore } from "@/stores/moviesStore";

    const store = useMoviesStore();
</script>
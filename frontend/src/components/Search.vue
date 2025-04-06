<template>
  <div class="flex flex-col">
    <h1 class="text-3xl font-bold pt-4 pb-4 text-slate-300">Search Movies</h1>
    <div class="flex flex-col items-center justify-center w-full mx-auto">
      <input
        v-model="store.movieSearch"
        type="text"
        placeholder="Search for a movie"
        @keyup.enter="store.searchMovies"
        class="block mb-2 p-2 border border-slate-300 rounded w-full border-b-4 bg-slate-200"
        
      >
      </div>
      <div class="mt-1 mb-4">
      <button @click="store.searchMovies">
        Search
      </button>
      <button
        style="margin-left: 8px;"
        @click="store.clearSearch"
      >
        Clear
      </button>
      
    </div>
  </div>
  <!-- <v-card
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
  </v-card> -->
</template>

<script setup>
    import { useMoviesStore } from "@/stores/moviesStore";

    const store = useMoviesStore();
</script>
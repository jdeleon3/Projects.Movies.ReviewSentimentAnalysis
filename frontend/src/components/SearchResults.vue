<template>
  <div
    v-if="store.movies.length > 0"
    class="text-slate-300"
  >
    <h1>Search Results</h1>
    <div class="mt-2 mb-2 border-b-2 border-slate-800 p-2">      
      <div
        v-for="movie in store.movies"
        :key="movie.title"      
        class="hover:bg-slate-700 hover:cursor-pointer"
        @click="store.fetchMovieReviews(movie)"
      >
        <div class="flex flex-col items-start justify-start p-2 border-b-2 border-slate-800">
          <div class="flex flex-row justify-between w-full">
            <div>{{ movie.title }} ({{ movie.year }})</div>
            <div
              class="expand-collapse-icon"
              :class="{collapsed: store.selectedMovie === movie}"
            />
          </div>
          <div>{{ movie.cast }}</div>
        </div>
        <div
          v-if="store.movieReviews.length > 0 && store.selectedMovie === movie"
          class="mt-2 mb-2 border-2 border-slate-800 p-2 bg-slate-900"
        >
          <div
            v-for="review in store.movieReviews"
            :key="review.id"
            class="mt-2 mb-2 border-b-2 border-slate-800 p-2"
          >
            <p>{{ review.content }}</p>
          </div>
        </div>    
        <div
          v-if="store.movieReviews.length === 0 && store.selectedMovie == movie"
          class="mt-2 mb-2 p-2 text-red-500"
        >
          <p>No reviews found for this movie.</p>
        </div>
      </div>
    </div>
  </div>
</template>
<script setup>
    import { useMoviesStore } from "@/stores/moviesStore";

    const store = useMoviesStore();
</script>

<style scoped lang="scss">
.expand-collapse-icon {
  //font-size: 200px;  
  width: 1em;
  height: 1em;
  position: relative;
  display: inline-block;
}

.expand-collapse-icon::before, .expand-collapse-icon::after {
  content: "";
  position: absolute;
  width: 1em;
  height: .16em;
  top: calc( (1em / 2 ) - .08em );
  background-color: gray;
  transition: 0.3s ease-in-out all;
  border-radius: 0.03em;
}

.expand-collapse-icon::after {
  transform: rotate(90deg);
}

.collapsed.expand-collapse-icon::after {
  transform: rotate(180deg);
}


.collapsed.expand-collapse-icon::before {
  transform: rotate(90deg) scale(0);
}    
</style>
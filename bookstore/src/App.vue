<script setup>
import BookListComponent from './components/BookListComponent.vue';
import CreateNewBook from './components/CreateNewBook.vue';
import SearchBar from './components/SearchBar.vue';
import {ref} from 'vue'

const books = ref([])
</script>

<template>
  <div class="bg-black min-h-screen  flex flex-col justify-center items-center">
    
    <SearchBar class="mt-2 mb-5"/>
    <CreateNewBook/>
    <BookListComponent class="mt-3"/>
  </div>
</template>

<style scoped>
.logo {
  height: 6em;
  padding: 1.5em;
  will-change: filter;
  transition: filter 300ms;
}
.logo:hover {
  filter: drop-shadow(0 0 2em #646cffaa);
}
.logo.vue:hover {
  filter: drop-shadow(0 0 2em #42b883aa);
}
</style>

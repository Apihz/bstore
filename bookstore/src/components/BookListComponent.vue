<script setup>
import { onMounted, ref } from "vue";

const books = ref([])
const isShown = ref('true')


const getBooks = async () => {
    const res = await fetch('http://localhost:5000/books',
        {
            method: 'GET'
        }
    )
    books.value = await res.json()
}
onMounted(async () =>{
  await getBooks()
})

const hideForm = () => {
    if(isShown.value){
        isShown.value = false;
        return
    }
    isShown.value = true;
return
}
</script>

<template>
    <div class="flex flex-col max-w-3xl justify-center items-center">
        <button @click="hideForm" class=" text-white bg-zinc-700 border border-gray-700 rounded-md p-3">Show books list</button>
        <div v-if="isShown" class="grid grid-cols-5 gap-5 mt-2">
            <div class="bg-zinc-600 border border-zinc-600 py-2 px-2 rounded-md text-white mt-2" v-for="book in books">
                <h1>{{ book.title }}</h1>
                <p>{{ book.author }}</p>
                <p>{{ book.publisher }}</p>
            </div>
        </div>


    </div>
</template>
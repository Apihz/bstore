<script setup>
import {ref} from "vue";

const title = ref('')
const author = ref('')
const publisher = ref('')
const picURL = ref('')
const isShown = ref('true')
function createBook(){
    fetch('http://localhost:5000/books',{
        method: 'POST',
        headers:{
            'Content-Type':'application/json'
        },

        body:JSON.stringify({
            title:title.value,
            author:author.value,
            publisher:publisher.value,
        })
    }).then(res => window.alert("TEST"))
}
function changePic(e){
    const file = e.target.files[0]
    const reader = new FileReader()
    reader.readAsDataURL(file)
    reader.onload = e => {
        picURL.value = e.target.result
    }
}
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
    <div  class="text-white bg-gray-700 border border-gray-700 rounded-md flex flex-col justify-center p-5">
        <button @click="hideForm" class="bg-gray-500 border border-gray-500 rounded-md my-3 transition hover:bg-zinc-500 hover:text-black p-2 text-center">Hide</button>
        <h1 class="text-center ">ADD BOOK TO THE LIST</h1>
        <div v-if="isShown" class="h-fit ">
            
           <form @submit.prevent="createBook" class="text-white flex flex-col">
            <label >Title:</label>
            <input v-model="title" class="text-black p-1  rounded transition hover:bg-zinc-300 hover:text-black " type="text">
            <label >Author:</label>
            <input  v-model="author" class="text-black p-1 rounded transition hover:bg-zinc-300 hover:text-black " type="text">
            <label >Publisher:</label>
            <input  v-model="publisher" class="text-black p-1 rounded transition hover:bg-zinc-300 hover:text-black " type="text" >
            <div class="bg-gray-500 border border-gray-500 rounded-md my-3 transition hover:bg-zinc-500 hover:text-black p-2 text-center">           
                <input type="submit" value="Submit">
            </div>
           </form>
        </div>
        <div>
            <form>
                <input @change="changePic" class="text-white" type="file">
                <img class="object-contain h-70 w-70 p-2 " :src="picURL">
            </form>
        </div>
        <div>

        </div>
    </div>
</template>
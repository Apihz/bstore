<script setup> 
import { ref } from 'vue'

const users = ref([])
function getBook(){
    fetch('https://api.github.com/users',{
        method: 'GET',


    }).then(res => res.json()).then(data => 
        users.value = data
    
    )
}
</script>

<template> 
    <div>
        <button @click="getBook"></button>
        <ul>
            <li v-for="user in users" :key ="user.id">
                {{user.login}}
            </li>
        </ul>
    </div>
</template>

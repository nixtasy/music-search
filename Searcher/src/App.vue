<template>
    <Header text= "center" title="Lyrics Searcher" />
    <SearchSong @return-query="returnQuery" v-if="!formSubmitted"/>
    <Songs :hit-songs="songs" v-if="formSubmitted"/>
</template>

<script>
 import {
    MDBNavbar,
    MDBNavbarToggler,
    MDBNavbarNav,
    MDBNavbarItem,
    MDBBtn,
    MDBCollapse,
  } from 'mdb-vue-ui-kit';
  import { ref } from 'vue';
  const collapse2 = ref(false);
import Header from './components/Header.vue'
import Songs from './components/Songs.vue'
import SearchSong from './components/SearchSong.vue'
import { MDBContainer } from 'mdb-vue-ui-kit';

export default {
  name: 'App',
  components: {
    Header,
    Songs,
    SearchSong,
    MDBContainer
  },
  data() {
    return {
      songs: [],
      formSubmitted: false
    }
  },
  methods: {
    returnQuery(text){
      this.formSubmitted = !this.formSubmitted
      try {
            // fetch("https://search-backend.fly.dev/search_lyrics/" + text)
            fetch("http://localhost:8000/search_lyrics/" + text)
            .then((response) => {
                return response.json();
            })
            .then((data) => {
                // console.log(data);
                this.songs = data['result']
                for (const song of this.songs) {
                  song.readActivated = false
                }
            });
        } catch (error) {
            console.log(error);
        }
    }
  }
}
</script>

<style>
#app {
  font-family: Roboto, Helvetica, Arial, sans-serif;
}
</style>

<template>
  <MDBContainer>
    <Header title="Lyrics Searcher" />
    <SearchSong @return-query="returnQuery" v-if="!formSubmitted"/>
    <Songs v-if="formSubmitted" :songs="songs"/>
    <!-- <p>{{ temp[0]["SName"] }}</p> -->
  </MDBContainer>
</template>

<script>
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
            fetch("127.0.0.1:8000/search_lyrics/" + text)
            .then((response) => {
                return response.json();
            })
            .then((data) => {
                // console.log(data);
                this.songs = data['result']
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

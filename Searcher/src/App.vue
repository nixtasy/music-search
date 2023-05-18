<template>
    <div v-if="!formSubmitted">
      <header><h1>Search for your fav tunes with lyrics</h1></header>
      <SearchSong style="margin-top: 10%;" @return-query="returnQuery"/>
      <Footer style="margin-top: 40%;" />
    </div>
    <Songs @search-similiar="searchSimiliar" :hit-songs="songs" v-if="formSubmitted && dataReceived"/>
    <div v-if="formSubmitted && !dataReceived">
        <h2>Searching for the most similiar musics for you...</h2>
    </div>
</template>

<script>
import Songs from './components/Songs.vue'
import SearchSong from './components/SearchSong.vue'
import Footer from './components/Footer.vue'

export default {
  name: 'App',
  components: {
    Songs,
    SearchSong,
    Footer
  },
  data() {
    return {
      songs: [],
      offset: "",
      formSubmitted: false,
      dataReceived: false,
    }
  },
  methods: {
    returnQuery({text, artist}){
      this.formSubmitted = !this.formSubmitted
      artist?(this.offset = "&filter="+artist):(this.offset="")
      try {
            fetch("https://search-backend.fly.dev/search_lyrics/?prompt=" + text+this.offset)
            // fetch("http://localhost:8000/search_lyrics/?prompt=" +text+this.offset)
            .then((response) => {
                return response.json();
            })
            .then((data) => {
                this.songs = data['result']
                this.dataReceived = !this.dataReceived
                if (this.songs.length == 0) {
                    alert("Sorry! Nothing found ... Click OK to start a new search!");
                    window.location.reload();
                } else {
                  for (const song of this.songs) {
                    song.readActivated = false
                  }
                }
            });
        } catch (error) {
            console.log(error);
        }
    },
    searchSimiliar(text){
      // this.formSubmitted = !this.formSubmitted
      // artist?(this.offset = "&filter="+artist):(this.offset="")
      this.dataReceived = !this.dataReceived
      try {
        fetch("https://search-backend.fly.dev/search_lyrics/?prompt=" + text+this.offset)
            // fetch("http://localhost:8000/search_lyrics/?prompt=" +text)
            .then((response) => {
                return response.json();
            })
            .then((data) => {
                this.songs = data['result']
                this.dataReceived = !this.dataReceived
                if (this.songs.length == 0) {
                    alert("Sorry! Nothing found ... Click OK to start a new search!");
                    window.location.reload();
                } else {
                  for (const song of this.songs) {
                    song.readActivated = false
                  }
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

<template>
  <MDBRow>
    <MDBCol v-for="hitSong in hitSongs">
      <MDBCard  text="white" class="bg-success p-2 text-white bg-opacity-75">
      <!-- <MDBCard  
      text="white" 
      class="bg-image">        -->
        <MDBCardBody>
            <MDBCardTitle>{{ hitSong.SName }}</MDBCardTitle>
            <MDBCardTitle subtitle class="mb-2 text-muted">{{ hitSong.Artist }}</MDBCardTitle>
            <!-- <MDBCardText class="pre-formatted">
                {{ hitSong.Lyric }}
            </MDBCardText> -->
            <MDBCardText class="pre-formatted" v-if="!hitSong.readActivated">
              {{hitSong.Lyric.slice(0,100)}}
              <span class="read" v-if="!readActivated" @click="hitSong.readActivated = !hitSong.readActivated">
                ..read more
              </span>
            </MDBCardText>
            <MDBCardText class="pre-formatted" v-if="hitSong.readActivated">
              {{hitSong.Lyric}}
            </MDBCardText> 
            <MDBCardFooter>
              <MDBBtn tag="a" href="#!" color="primary">Search similar</MDBBtn>
            </MDBCardFooter>
        </MDBCardBody>
    </MDBCard>
    </MDBCol>
  </MDBRow>
</template>

<script>
    // import Song from './Song.vue'
    import { MDBCol, MDBRow, MDBCardGroup, MDBCard, MDBCardBody, MDBCardTitle, MDBCardText, MDBCardImg,MDBListGroup, MDBListGroupItem, MDBBtn  } from 'mdb-vue-ui-kit';
    export default {
        name: 'Songs',
        props: {
            hitSongs: Array
        },
        components:{
            // Song,
            MDBCol, 
            MDBRow, 
            MDBCardGroup, MDBCard, MDBCardBody, MDBCardTitle, MDBCardText, MDBCardImg,
            MDBListGroup, MDBListGroupItem, MDBBtn
        }

    }
</script>

<style>
.pre-formatted {
  white-space: pre-wrap; /* 👈 this is the important part */
  /* border: 1px dotted; */
  padding: 1rem;
}

/* .bg-image{
  background-image: url('https://mdbcdn.b-cdn.net/img/new/slides/003.webp')
} */
</style>
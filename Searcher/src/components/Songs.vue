<template>
  <MDBRow>
    <MDBCol v-for="(hitSong, index) in hitSongs" :key="index">
      <MDBCard  border="primary" text="black" class="bg-primary p-2 bg-opacity-25">
      <!-- <MDBCard  
      text="white" 
      class="bg-image">        -->
        <MDBCardBody>
          <MDBCardHeader border="success"><i class="fas fa-record-vinyl"></i> &nbsp;No. {{index+1}} Result</MDBCardHeader>
            <MDBCardTitle>{{ hitSong.SName }}</MDBCardTitle>
            <MDBCardTitle subtitle class="mb-2 text-muted">{{ hitSong.Artist }}</MDBCardTitle>
            <!-- <MDBCardText class="pre-formatted">
                {{ hitSong.Lyric }}
            </MDBCardText> -->
            <MDBCardText class="pre-formatted" v-if="!hitSong.readActivated">
              {{hitSong.Lyric.slice(0,200)}}
              <span class="read" v-if="!readActivated" @click="hitSong.readActivated = !hitSong.readActivated">
                <u><strong>..read more</strong></u>
              </span>
            </MDBCardText>

            <MDBCardText class="pre-formatted" v-if="hitSong.readActivated">
              {{hitSong.Lyric}}
            </MDBCardText> 
            <MDBCardFooter @click="$emit('searchSimiliar', hitSong.Lyric)">
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
        },
        methods: {
        onSubmit(e) {
            this.formSubmitted = true;
            this.$emit("return-query", {text:this.text, artist:this.artist});
            this.text = "";
            this.artist = "";
        },
    }
    }
</script>

<style>
.pre-formatted {
  white-space: pre-wrap; /* 👈 this is the important part */
  /* border: 1px dotted; */
  padding: 1rem;
}
</style>
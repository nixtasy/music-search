<template>
    <!-- <MDBCardGroup>
        <MDBCard>
      <MDBCardImg src="https://mdbootstrap.com/img/new/standard/city/042.webp" top alt="..."/>
      <MDBCardBody>
        <MDBCardTitle>"$parent.song[0].SName"</MDBCardTitle>
        <MDBCardText>
          This card has supporting text below as a natural lead-in to
          additional content.
        </MDBCardText>
        <MDBCardText>
          <small class="text-muted">Last updated 3 mins ago</small>
        </MDBCardText>
      </MDBCardBody>
    </MDBCard>
    <MDBCard>
      <MDBCardImg src="https://mdbootstrap.com/img/new/standard/city/042.webp" top alt="..."/>
      <MDBCardBody>
        <MDBCardTitle>Card title</MDBCardTitle>
        <MDBCardText>
          This card has supporting text below as a natural lead-in to
          additional content.
        </MDBCardText>
        <MDBCardText>
          <small class="text-muted">Last updated 3 mins ago</small>
        </MDBCardText>
      </MDBCardBody>
    </MDBCard>
    <MDBCard>
      <MDBCardImg src="https://mdbootstrap.com/img/new/standard/city/043.webp" top alt="..."/>
      <MDBCardBody>
        <MDBCardTitle>Card title</MDBCardTitle>
        <MDBCardText>
          This is a wider card with supporting text below as a natural
          lead-in to additional content. This card has even longer
          content than the first to show that equal height action.
        </MDBCardText>
        <MDBCardText>
          <small class="text-muted">Last updated 3 mins ago</small>
        </MDBCardText>
      </MDBCardBody>
    </MDBCard>
  </MDBCardGroup> -->
    
    <MDBCardGroup v-for="song in songs">
        <!-- <Song :song="song" /> -->
        <MDBCard>
            <MDBCardImg src="https://mdbootstrap.com/img/new/standard/city/043.webp" top alt="..."/>
            <MDBCardBody>
                <MDBCardTitle>{{song.SName}}</MDBCardTitle>
                <MDBCardText>
                This is a wider card with supporting text below as a natural
                lead-in to additional content. This card has even longer
                content than the first to show that equal height action.
                </MDBCardText>
                <MDBCardText>
                    <small class="text-muted">Last updated 3 mins ago</small>
                </MDBCardText>
            </MDBCardBody>
        </MDBCard>
    </MDBCardGroup>
</template>

<script>
    // import Song from './Song.vue'
    import { MDBCol, MDBRow, MDBCardGroup, MDBCard, MDBCardBody, MDBCardTitle, MDBCardText, MDBCardImg  } from 'mdb-vue-ui-kit';
    export default {
        name: 'Songs',
        props: {
            songs: Array
        },
        components:{
            // Song,
            MDBCol, 
            MDBRow, 
            MDBCardGroup, MDBCard, MDBCardBody, MDBCardTitle, MDBCardText, MDBCardImg
        }

    }
</script>

<style>
.pre-formatted {
  white-space: pre-wrap; /* 👈 this is the important part */
  border: 1px dotted;
  padding: 1rem;
}
</style>
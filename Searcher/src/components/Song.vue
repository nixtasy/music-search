<template>
    <MDBCard class = "song" text="center">
        <MDBCardBody>
            <MDBCardTitle>{{ song.SName }}</MDBCardTitle>
            <MDBCardTitle subtitle class="mb-2 text-muted">{{ song.Artist }}</MDBCardTitle>
            <MDBCardText class="pre-formatted">
                {{ song.Lyric }}
            </MDBCardText>
            <MDBBtn tag="a" href="#!" color="primary">Search similar</MDBBtn>
        </MDBCardBody>
    </MDBCard>
    <MDBCard class = "song">
      <MDBCardImg src="https://mdbootstrap.com/img/new/standard/city/041.webp" top alt="..."/>
      <MDBCardBody>
        <MDBCardTitle>Card title</MDBCardTitle>
        <!-- <MDBCardText class="pre-formatted">
                {{ song.Lyric }}
            </MDBCardText>
        <MDBCardText> -->
        <MDBCardText>
                xxxx
            </MDBCardText>
        <MDBCardText>
          <small class="text-muted">Last updated 3 mins ago</small>
        </MDBCardText>
      </MDBCardBody>
    </MDBCard>
</template>

<script>
    import {
        MDBCard,
        MDBCardBody,
        MDBCardHeader,
        MDBCardTitle,
        MDBCardText,
        MDBCardLink,
        MDBCardImg,
        MDBCardFooter,
        MDBCardGroup,
        MDBBtn
    } from 'mdb-vue-ui-kit';

    export default {
        name: 'Song',
        props: {
            song: Object,
        },
        components: {
            MDBCard,
            MDBCardBody,
            MDBCardHeader,
            MDBCardTitle,
            MDBCardText,
            MDBCardLink,
            MDBCardImg,
            MDBCardFooter,
            MDBCardGroup,
            MDBBtn
        }
    };


</script>

<style>
.pre-formatted {
  white-space: pre-wrap; /* 👈 this is the important part */
  border: 1px dotted;
  padding: 1rem;
}
/* .card{
    max-width: 40%;
} */
</style>
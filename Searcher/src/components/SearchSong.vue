<template>
  <MDBContainer>
  <form @submit="onSubmit">
    <MDBInput
      type="text"
      id="form4Textarea"
      placeholder="Lyrics or whatever in your mind (Hint: try 'rainy days', 'fly me to the moon')"
      v-model="text"
      wrapperClass="mb-4"
    />
    <!-- Password input -->
    <MDBInput
      type="text"
      label="Artist (optional)"
      id="form5Name"
      placeholder=" Artist name"
      v-model="artist"
      wrapperClass="mb-4"
    />
    <!-- Submit button -->
    <MDBBtn type="submit" color="primary" block> Search </MDBBtn>
</form>
</MDBContainer>
</template>

<script>
import {MDBInput, MDBBtn, MDBContainer} from 'mdb-vue-ui-kit';
import { ref } from 'vue';
const form4Textarea = ref('');
const form5Name = ref("");
export default {
    name: "SearchSong",
    data() {
        return {
            text: "",
            artist: "",
            songs: [],
            formSubmitted: false
        };
    },
    methods: {
        onSubmit(e) {
            e.preventDefault();
            if (!this.text) {
                alert("Forget to write down the lyrics?");
                return;
            }
            this.formSubmitted = true;
            this.$emit("return-query", {text:this.text, artist:this.artist});
            this.text = "";
            this.artist = "";
        },
    },
    components: { MDBContainer,MDBInput, MDBBtn }
}
</script>

<style scoped>

</style>
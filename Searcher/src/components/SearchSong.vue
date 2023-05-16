<template>
  <!-- <MDBInput
    @submit="onSubmit"
    v-model="search3"
    inputGroup
    :formOutline="false"
    wrapperClass="mb-3"
    placeholder="Lyrics or whatever text in your mind now"
    aria-label="Search"
    aria-describedby="button-addon2"
  >
    <MDBBtn type="submit" outline="primary">Search</MDBBtn>
  </MDBInput> -->

    <form @submit="onSubmit" class="add-form">
      <div class="form-control">
        <input type="text" v-model="text" name="text" placeholder="Lyrics or whatever text in your mind now" />
      </div>
      <input type="submit" value="Search" class="btn btn-block" />
    </form>
  </template>

<script>
import { MDBInput, MDBBtn, MDBIcon } from 'mdb-vue-ui-kit';
import { ref } from 'vue';
const search3 = ref('');
export default {
    name: 'SearchSong',
    data() {
        return {
            text: '',
            songs: [],
            formSubmitted: false
            };
    },
  methods: {
    onSubmit(e) {
        e.preventDefault()
        if (!this.text) {
        alert('Forget to write down the lyrics?')
        return
        }
        this.formSubmitted = true;
        this.$emit('return-query', this.text)
        this.text = ''
    },
    },
}
</script>

<style scoped>
.add-form {
  margin-bottom: 40px;
}
.form-control {
  margin: 20px 0;
}
.form-control label {
  display: block;
}
.form-control input {
  width: 100%;
  height: 40px;
  margin: 5px;
  padding: 3px 7px;
  font-size: 17px;
}
.form-control-check {
  display: flex;
  align-items: center;
  justify-content: space-between;
}
.form-control-check label {
  flex: 1;
}
.form-control-check input {
  flex: 2;
  height: 20px;
}
</style>
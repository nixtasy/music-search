<template>
    <MDBNavbar light bg="light" container>
      <MDBNavbarBrand href="#">Navbar</MDBNavbarBrand>
      <form class="d-flex input-group w-auto">
        <input
          type="search"
          class="form-control"
          placeholder="Type query"
          aria-label="Search"
        />
        <MDBBtn outline="primary"> Search </MDBBtn>
      </form>
    </MDBNavbar>
  </template>

<script>
import { MDBBtn, MDBNavbar, MDBNavbarBrand } from 'mdb-vue-ui-kit';
export default{
    components: { MDBContainer,MDBInput, MDBBtn }
  }
  
</script>
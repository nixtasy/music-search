<template>
    <!-- Footer -->
    <MDBFooter :text="['center', 'lg-start', 'muted']">
      <div class="text-center p-4" style="background-color: rgba(0, 0, 0, 0.05)">
        This project is powered by  Qdrant vector search engine
      </div>
      <!-- Copyright -->
    </MDBFooter>
    <!-- Footer -->
</template>

<script>
  import {
    MDBFooter,
    MDBContainer,
    MDBRow,
    MDBCol,
    MDBIcon
  } from 'mdb-vue-ui-kit';

  export default {
    components: {
      MDBFooter,
      MDBContainer,
      MDBRow,
      MDBCol,
      MDBIcon
    },
  };
</script>

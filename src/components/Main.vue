<template>
  <section class="section">
    <div class="container">
      <h1 class="title has-text-centered has-text-info">
        LA Forum 2020
      </h1>
      <div class="box" @click="$router.push({ name: 'RegistrantList' })">
        <h1 class="title is-size-4">
          Registrants
        </h1>
      </div>
      <div class="box" @click="$router.push({ name: 'QRScanner' })">
        <h1 class="title is-size-4">
          QR Code Scanner
        </h1>
      </div>
      <div class="box" @click="$router.push({ name: 'OpeningCount' })">
        <h1 class="title is-size-4">
          Opening Ceremony
        </h1>
      </div>
      <div class="box" @click="$router.push({ name: 'RegistrantTable' })">
        <h1 class="title is-size-4">
          Registrants Management
        </h1>
      </div>
      <div class="box" @click="$router.push({ name: 'RegisterAdd' })">
        <h1 class="title is-size-4">
          Register Add
        </h1>
      </div>
      <div class="box" @click="$router.push({ name: 'Program' })">
        <h1 class="title is-size-4">
          Program Management
        </h1>
      </div>
    </div>
    <div class="box" @click="$router.push({ name: 'Gallery' })">
      <h1 class="title is-size-4">
        Gallery
      </h1>
    </div>
  </section>
</template>

<script>
export default {
name: "Main"
}
</script>

<style scoped>

</style>
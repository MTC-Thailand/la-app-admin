<template>
  <section class="section">
    <div class="container">
      <h1 class="title has-text-centered has-text-info">
        LA Forum 2022
      </h1>
      <h1 class="subtitle has-text-centered is-size-4">
        Admin Panel
      </h1>
      <p class="has-text-centered has-text-white notification is-danger">หากท่านไม่ทราบรหัสผ่านกรุณาติดต่อทีมประชาสัมพันธ์</p>
      <div class="box" @click="$router.push({ name: 'QRScanner' })">
        <h1 class="title is-size-4">
          QR Code Scanner
        </h1>
      </div>
      <div class="box" @click="$router.push({ name: 'RegistrantTable' })">
        <h1 class="title is-size-4">
          การจัดการผู้เข้าร่วมงาน
        </h1>
      </div>
      <div class="box" @click="$router.push({ name: 'RegisterAdd' })">
        <h1 class="title is-size-4">
          เพิ่มผู้ลงทะเบียน
        </h1>
      </div>
      <div class="box" @click="$router.push({ name: 'Program' })">
        <h1 class="title is-size-4">
          จัดการข้อมูลโปรแกรมการบรรยาย
        </h1>
      </div>
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
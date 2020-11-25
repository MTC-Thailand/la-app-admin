<template>
  <section class="section">
    <div class="container">
      <h1 class="title has-text-centered has-text-info">Register New</h1>
      <b-field label="Title/คำนำหน้า">
        <b-input v-model="user.title"></b-input>
      </b-field>
      <b-field label="Firstname/ชื่อ">
        <b-input v-model="user.firstname"></b-input>
      </b-field>
      <b-field label="Lastname/นามสกุล">
        <b-input v-model="user.lastname"></b-input>
      </b-field>
      <b-field label="License Id/เลขใบประกอบวิชาชีพ">
        <b-input v-model="user.licenseId"></b-input>
      </b-field>
      <b-field label="Passcode/รหัสผ่าน">
        <b-input v-model="user.passcode"></b-input>
      </b-field>
      <b-field label="Number/หมายเลขลงทะเบียน">
        <b-input v-model="user.number"></b-input>
      </b-field>
      <div class="buttons is-centered">
        <button class="button is-ligth" @click="$router.push({ name: 'Main'})">Back</button>
        <button class="button is-success" @click="save">Save</button>
      </div>
    </div>
  </section>
</template>

<script>
import {users} from '@/firebase'

export default {
  name: "RegisterAdd",
  data() {
  return {
      user: {
        title: '',
        number: null,
        firstname: '',
        lastname: '',
        licenseId: '',
        passcode: null,
      }
    }
  },
  methods: {
    save: function() {
      const self = this
      users.add(this.user).then(()=>{
        self.$buefy.toast.open({ message: "Save successfully", type: 'is-success'})
      })
    }
  },
  mounted() {
    const self = this
    this.$buefy.dialog.prompt({
      message: `Please enter the passcode:`,
      inputAttrs: {
        maxlength: 4
      },
      canCancel: false,
      trapFocus: true,
      onConfirm: (value)=>{
        if (value != '5625') {
          this.$buefy.toast.open({ message: 'Access denied', type: 'is-danger', position: 'is-bottom'})
          this.$router.push({ name: "Main"})
        } else {
          this.users = []
          users.get().then(snapshot=>{
            snapshot.docs.forEach(d=>{
              self.users.push(d.data())
            })
          })
          this.isLoading = false
        }
      }
    })
  }
}
</script>

<style scoped>

</style>
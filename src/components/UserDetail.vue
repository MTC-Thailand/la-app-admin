<template>
  <section class="section">
    <h1 class="title has-text-info">
      User Detail
    </h1>
    <table class="table is-fullwidth">
      <tr>
        <td>Number</td>
        <td>{{ user.number }}</td>
      </tr>
      <tr>
        <td>Name</td>
        <td>{{ user.title }}{{ user.firstname }} {{user.lastname}}</td>
      </tr>
      <tr>
        <td>Office</td>
        <td>{{ user.office }} {{ user.province }}</td>
      </tr>
      <tr>
        <td>License ID</td>
        <td>{{ user.licenseId }}</td>
      </tr>
      <tr>
        <td>Admin</td>
        <td><b-switch v-model="user.admin"></b-switch></td>
      </tr>
    </table>
    <div class="buttons is-centered">
      <button class="button is-light is-rounded" @click="$router.push({ name: 'RegistrantTable'})">Back</button>
      <button class="button is-light is-rounded is-success" @click="save">Save</button>
    </div>
    <h1 class="title has-text-info">
      Check In Records
    </h1>
    <table class="table is-narrow is-fullwidth" v-for="c in checkins" :key="c.checkedAt.toDate().toLocaleString()">
      <tr>
        <td>{{ c.checkedAt.toDate().toLocaleString() }}</td>
      </tr>
    </table>
    <div class="buttons is-centered">
      <button class="button is-light is-rounded" @click="$router.push({ name: 'RegistrantTable'})">Back</button>
      <button class="button is-light is-success is-rounded" @click="checkin">Check In</button>
    </div>
  </section>
</template>

<script>
import {users, checkins} from "@/firebase";

export default {
  name: "UserDetail",
  data() {
    return {
      user: {},
      userId: '',
      checkins: []
    }
  },
  methods: {
    save: function() {
      const self = this
      users.doc(self.userId).update(self.user).then(()=> {
        self.$buefy.toast.open({message: 'บันทึกข้อมูลเรียบร้อย', type: 'is-success'})
      })
    },
    checkin: function() {
      const self = this
      let record = {'checkedAt': new Date(), 'number': self.user.number}
      checkins.add(record).then(()=>{
        self.checkins = []
        checkins.where('lineId', '==', self.user.lineId).get().then(snapshot=>{
          snapshot.docs.forEach(d=>{
            self.checkins.push(d.data())
          })
        })
        self.$buefy.toast.open({message: 'บันทึกข้อมูลเรียบร้อย', type: 'is-success'})
      })
    }
  },
  mounted() {
    const self = this
      if (this.$route.params.userNumber) {
        users.where('number', '==', parseInt(this.$route.params.userNumber)).get().then(snapshot => {
          self.user = snapshot.docs[0].data()
          self.userId = snapshot.docs[0].id
          if (self.user.lineId) {
            checkins.where('number', '==', self.user.number).get().then(snapshot=>{
              snapshot.docs.forEach(d=>{
                self.checkins.push(d.data())
              })
            })
          }
        })
      }
    }
}
</script>

<style scoped>

</style>
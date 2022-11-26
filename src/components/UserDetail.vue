<template>
  <section class="section">
    <h1 class="title has-text-info">
      User Detail
    </h1>
    <table class="table is-fullwidth">
      <tr>
        <td><strong>Number</strong></td>
        <td>{{ user.number }}</td>
      </tr>
      <tr>
        <td><strong>Passcode</strong></td>
        <td>{{ user.passcode }}</td>
      </tr>
      <tr>
        <td><strong>Name</strong></td>
        <td>{{ user.title }}{{ user.firstname }} {{user.lastname}}</td>
      </tr>
      <tr>
        <td><strong>Office</strong></td>
        <td>{{ user.office }} {{ user.province }}</td>
      </tr>
      <tr>
        <td><strong>License ID</strong></td>
        <td>{{ user.licenseId }}</td>
      </tr>
    </table>
    <div class="buttons is-centered">
      <button class="button is-success" @click="save">Save</button>
    </div>
    <h1 class="title has-text-info">
      Check In Records
    </h1>
    <table class="table is-narrow is-fullwidth">
      <thead>
      <th>Method</th>
      <th>Date & Time</th>
      </thead>
      <tr v-for="c in checkins" :key="c.checkedAt.toDate().toLocaleString()">
        <td>{{ c.method }}</td>
        <td>{{ c.checkedAt.toDate().toLocaleString() }}</td>
      </tr>
    </table>
    <div class="buttons is-centered">
      <button class="button is-light" @click="$router.push({ name: 'RegistrantTable'})">Back</button>
      <button class="button is-info" @click="checkin">Check In</button>
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
      let record = {'checkedAt': new Date(), 'number': self.user.number, method: 'manual'}
      checkins.add(record).then(()=>{
        self.checkins = []
        checkins.where('number', '==', self.user.number).get().then(snapshot=>{
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
          checkins.where('number', '==', self.user.number).get().then(snapshot=>{
            snapshot.docs.forEach(d=>{
              self.checkins.push(d.data())
            })
          })
        })
      }
    }
}
</script>

<style scoped>

</style>
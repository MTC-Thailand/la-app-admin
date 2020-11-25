<template>
  <section class="section">
    <div class="container">
      <h1 class="title has-text-centered">Registrants</h1>
      <b-field label="Name">
        <b-input v-model="query" placeholder="First name or license ID" icon="search" icon-pack="fas"></b-input>
      </b-field>
      <div class="buttons is-centered">
        <button class="button is-success" @click="search">Search</button>
      </div>
    </div>
    <br>
    <div class="columns">
      <div class="column is-one-third is-offset-4">
        <div class="box" v-for="user in users" :key="user.number">
          <table class="table">
            <tr>
              <td><strong>Registration Number</strong></td>
              <td><span class="title is-size-5">{{ user.number }}</span></td>
            </tr>
            <tr>
              <td><strong>Passcode</strong></td>
              <td><span class="has-text-danger title is-size-5">{{ user.passcode }}</span></td>
            </tr>
            <tr>
              <td><strong>Name</strong></td>
              <td>{{ user.title }}{{ user.firstname }} {{ user.lastname }}</td>
            </tr>
            <tr>
              <td><strong>License ID</strong></td>
              <td>{{ user.licenseId }}</td>
            </tr>
          </table>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import { users } from '../firebase'

export default {
  name: "RegistrantList",
  data() {
    return {
      query: '',
      users: [],
    }
  },
  methods: {
    search: function() {
      const self = this
      this.users = []
      users.where('firstname', '==', this.query).get().then(snapshot=>{
        if (snapshot.docs.length > 0) {
          snapshot.docs.forEach(d=>{
            self.users.push(d.data())
          })
        } else {
          users.where('licenseId', '==', this.query.toString()).get().then(snapshot => {
            if (snapshot.docs.length > 0) {
              snapshot.docs.forEach(d => {
                self.users.push(d.data())
              })
            } else {
              self.$buefy.toast.open({message: 'Not Found', type: 'is-warning'})
            }
          })
        }
      })
    }
  }
}
</script>

<style scoped>

</style>
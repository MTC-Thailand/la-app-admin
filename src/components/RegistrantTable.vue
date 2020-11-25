<template>
  <section class="section">
    <div class="container">
    <b-field label="Search by first name">
      <b-input v-model="query"></b-input>
    </b-field>
    <b-table :data="fltUsers" :paginated="true" per-page="20" :loading="isLoading">
      <b-table-column field="number" label="Number" sortable numeric v-slot="props">
        {{ props.row.number }}
      </b-table-column>
      <b-table-column field="title" label="Title" v-slot="props">
        {{ props.row.title }}
      </b-table-column>
      <b-table-column field="firstname" label="First Name" sortable v-slot="props">
        {{ props.row.firstname }}
      </b-table-column>
      <b-table-column field="lastname" label="Last Name" sortable v-slot="props">
        {{ props.row.lastname }}
      </b-table-column>
      <b-table-column field="action" label="Action" sortable v-slot="props">
        <button @click="$router.push({ name: 'UserDetail', params: {userNumber: props.row.number }})">
          detail
        </button>
      </b-table-column>
    </b-table>
    <div class="buttons is-centered">
      <button class="button is-light" @click="$router.push({ name: 'Main'})">Main</button>
    </div>
    </div>
  </section>
</template>

<script>
import {users} from '@/firebase'
export default {
  name: "RegistrantTable",
  data() {
    return {
      users: [],
      query: "",
      isLoading: true
    }
  },
  computed: {
    fltUsers: function() {
      if (this.query) {
        return this.users.filter(u=>{
          return u.firstname == this.query
        })
      } else {
        return this.users
      }
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
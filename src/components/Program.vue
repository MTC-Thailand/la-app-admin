<template>
<section class="section">
  <div class="has-text-centered">
    <img src="../assets/LA-logo-small.png" width="100">
  </div>
  <h1 class="title has-text-info has-text-centered">
    Programs
  </h1>
  <table class="table is-fullwidth box is-striped" v-for="pg in progs" :key="pg.title">
    <col width="50%">
    <tr>
    <tr>
    <td colspan="2">
      <h1 class="title is-size-4 has-text-centered has-text-primary">{{ pg.sessionTitle }}</h1>
      <h1 class="subtitle is-size-5 has-text-centered">{{ pg.title }}</h1>
    </td>
    </tr>
    <tr>
      <td><strong>เริ่ม</strong></td>
      <td>{{ pg.start.calendar() }}-{{ pg.end.format('H:mm') }} น.</td>
    </tr>
    <tr>
      <td><strong>วิทยากร</strong></td>
      <td>{{ pg.speaker }}</td>
    </tr>
    <tr>
      <td><strong>สังกัด</strong></td>
      <td>{{ pg.affil }}</td>
    </tr>
    <tr>
      <td><strong>สถานที่</strong></td>
      <td>{{ pg.location }}</td>
    </tr>
    <tr>
      <td><strong>เอกสารประกอบ</strong></td>
      <td><a :href="pg.materialUrl">{{ pg.materialUrl }}</a></td>
    </tr>
    <tr>
      <td colspan="2"><button class="button is-rounded is-light is-danger" @click="$router.push({ name: 'ProgramAdminEdit', params: { programId: pg.id }})">Edit</button></td>
    </tr>
  </table>
  <div class="buttons is-centered">
    <button class="button is-light is-success is-rounded"
            @click="$router.push({ name: 'ProgramAdmin' })">Add</button>
    <button class="button is-info is-rounded" @click="$router.push({ name: 'Main' })">
      <span class="icon">
        <i class="fas fa-home"></i>
      </span>
      <span>Main</span>
    </button>
  </div>
</section>
</template>

<script>
import { programs } from '../firebase'
import moment from "moment";

moment.locale('th')

export default {
  name: "Program",
  data() {
    return {
      progs: [],
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
        }
      }
    })
    programs.get().then((snapshot)=>{
      snapshot.docs.forEach((doc)=>{
        let prog = doc.data()
        prog.id = doc.id
        prog.order = parseInt(doc.data().order)
        prog.start = moment(new Date(doc.data().startDateTime.toDate()))
        prog.end = moment(new Date(doc.data().endDateTime.toDate()))
        self.progs.push(prog)
      })
      self.progs.sort(function(a, b) {
        return a.order - b.order
      })
    })
  }
}
</script>

<style scoped>

</style>
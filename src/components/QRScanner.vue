<template>
  <section class="section">
    <div class="container">
      <h1 class="title has-text-info has-text-centered">
        QR Scanner
      </h1>
      <div class="columns">
        <div class="column is-half is-offset-3">
          <qrcode-stream @decode="onDecode"></qrcode-stream>
          <div class="has-text-centered is-size-4 has-text-success" v-if="record">
            {{ user.title }}{{ user.firstname }} {{ user.lastname }}
            ลงทะเบียนสำเร็จเมื่อ {{ record.toLocaleString() }}
          </div>
          <div class="has-text-centered is-size-4 has-text-danger" v-else>
            ไม่สามารถบันทึกการแสกนของท่านได้ กรุณาลองอีกครั้งหรือติดต่อเจ้าหน้าที่
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script>
import { users, checkins } from '../firebase'

export default {
  name: "QRScanner",
  data() {
    return {
      record: '',
      user: {}
    }
  },
  mounted() {
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
  },
  methods: {
    onDecode: function(decodedString) {
      console.log(decodedString)
      this.record = ''
      this.user = {}
      const self = this
      checkins.where('lineId', '==', decodedString).get().then(snapshot=>{
        if (snapshot.docs.length >= 0) {
          let checkedAt = new Date()
          users.where('lineId', '==', decodedString).get().then(snapshot=>{
            if(snapshot.docs.length > 0) {
              self.user = snapshot.docs[0].data()
              checkins.add({ lineId: decodedString, checkedAt: checkedAt, number: self.user.number, method: 'QRCode'}).then(()=>{
                self.record = checkedAt
                self.$buefy.toast.open({ message: 'แสกนเรียบร้อยแล้ว', type: 'is-success'})
              })
            }
          })
        } else {
          self.$buefy.toast.open({ message: 'ไม่สามารถแสกนซ้ำได้', type: 'is-warning'})
        }
      })
    }
  }
}
</script>

<style scoped>

</style>
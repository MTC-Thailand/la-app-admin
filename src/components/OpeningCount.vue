<template>
  <div>
  <section class="section" :style="myStyle" v-if="!countingStop">
    <div class="has-text-centered">
      <h1 class="title is-size-1">Opening Ceremony</h1>
      <h1 class="title is-size-1">{{ counter }}</h1>
    </div>
  </section>
  <section class="section has-text-centered">
    <div class="notification" v-if="countingStop">
      <h1 class="title is-size-1">Lucky Numbers!</h1>
      <div class="is-size-2" v-for="p in prizes" :key="p.number">
        <span class="has-text-success">
          {{ p.number }}
        </span>
      </div>
      <div class="buttons is-centered">
        <button class="button is-info" @click="showPrize">Show</button>
        <button class="button is-light" @click="$router.push({name : 'Main'})">Back</button>
      </div>
    </div>
  </section>
  </div>
</template>

<script>
import { draws } from '../firebase'

export default {
  name: "OpeningCount",
  data() {
    return {
      counter: 0,
      prizes: [],
      countingStop: false,
      myStyle: {
        backgroundColor: 'white'
      },
    }
  },
  methods: {
    showPrize: function() {
      const self = this
      draws.where('win', '==', true).get().then(snapshot=>{
        snapshot.docs.forEach(d=>{
          self.prizes.push(d.data())
        })
      })
    }
  },
  mounted() {
    setInterval(()=>{
      if (this.counter <= 900) {
        let val = Math.random() * 50
        this.counter += parseInt(val.toFixed(0))
        if (this.counter > 200) {
          this.myStyle = {
            backgroundColor: 'yellow'
          }
        }
        if (this.counter > 400) {
          this.myStyle = {
            backgroundColor: 'orange'
          }
        }
        if (this.counter > 600) {
          this.myStyle = {
            backgroundColor: 'red'
          }
        }
      } else {
        this.countingStop = true
      }
    }, 500)
  }
}
</script>

<style scoped>

</style>
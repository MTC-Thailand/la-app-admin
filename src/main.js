import Vue from 'vue'
import App from './App.vue'
import router from './router'
import Buefy from 'buefy'
import 'buefy/dist/buefy.css'
import '@fortawesome/fontawesome-free/css/all.css'
import VueQrcodeReader from 'vue-qrcode-reader'

Vue.config.productionTip = false
Vue.use(Buefy)
Vue.use(VueQrcodeReader)

new Vue({
  router,
  render: h => h(App),
}).$mount('#app')

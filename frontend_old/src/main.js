import Vue from 'vue'

// BootstrapVue
import BootstrapVue from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

import App from './App.vue'
import router from './router'
import store from './store'
import Vuetify from 'vuetify'

Vue.config.productionTip = process.env.NODE_ENV === 'production'

Vue.use(BootstrapVue)
Vue.use(Vuetify)

new Vue({
  router,
  store,
  render: h => h(App),
}).$mount('#app')

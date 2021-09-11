<template>
  <div class="home">
    <template v-if="$store.state.isAuthenticated">
      <form>
        <div>
          <button type="button" @click="logout()">ログアウト</button>
        </div>
      </form>
    </template>
    <template v-else>
      <form>
        <div>
          <label for="email">メールアドレス</label>
          <input type="email" v-model="email">
        </div>
        <div>
          <label for="password">パスワード</label>
          <input type="password" v-model="password">
        </div>
        <div>
          <button type="button" @click="login()">ログイン</button>
        </div>
      </form>
    </template>
  </div>
</template>

<script>
import axios from 'axios'
export default {
    data() {
        return {
            email: "",
            password: ""
        }
    },
    methods: {
        login() {
            axios.post(
                '/api/v1/login/',
                {
                    email: this.email,
                    password: this.password
                }
            ).then((response) => {
                const token = response.data.access_token
                this.$store.commit('setToken', token)
                axios.defaults.headers.common["Authorization"] = "Token " + token
                localStorage.setItem("token", token)
                this.$router.push('/')
            });
            this.email = "";
            this.password = "";
        },
        logout() {
            axios.post(
                '/api/v1/logout/',
            ).then((response) => {
                axios.defaults.headers.common["Authorization"] = ""
                localStorage.removeItem("token")
                this.$store.commit('removeToken')
                this.$router.push('/')
            })
        }
    }
}
</script>




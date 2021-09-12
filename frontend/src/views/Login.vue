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

        <div class="notification is-danger" v-if="errors.length">
          <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
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
            password: "",
            errors: []
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
            }).catch(error => {
                this.errors.push("メールアドレスまたはパスワードが間違っています。")
            })
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




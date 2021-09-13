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

  <section class="hero is-fullheight has-text-centered">
    <div class="hero-body">

      <div class="container has-text-centered">
        <div class="column is-4 is-offset-4">      
          
          <div class="box">            
          <form>
            <div class="field">
              <div class="control">
                <label class="label">メールアドレス</label>
                <input class="input is-midium" placeholder="Email" autofocus="" type="email" v-model="email">
              </div>
            </div>
            <div class="field">
              <div class="control">
                <label class="label">パスワード</label>
                <input class="input is-midium" placeholder="Password" type="password" v-model="password">
              </div>
            </div>
            <div class="is-danger" v-if="errors.length">
              <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
            </div>
            
            <div class="is-block">
              <button class="button is-link is-midium is-fullwidth" type="button" @click="login()">ログイン</button>
            </div>

            <div class="is-block">
              <router-link to="/" class="is-success is-fullwidth">パスワードを忘れた方</router-link>
            </div>

            <hr class="login-hr">
            
            <div class="is-block">
              <div class="has-account">
                アカウントをお持ちでない方
              </div>
              <router-link to="/signup" class="button is-success is-fullwidth"><strong>無料で始める</strong></router-link>
            </div>            
                        
          </form>
          </div>
          
        </div>
      </div>
      
    </div>
  </section>
      
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

<style lang="scss" scoped>
  .hero-body {
  background-image: url(../assets/top.jpg);
  background-size: cover;
  
  width: 100%;
  height: 100%;
  }
  .label {
  text-align: left;
  }
  .is-block {
  margin-top: 30px;
  }
  .is-danger {
  color: #ff0000;
  }
  .has-account {
  margin-bottom: 5px;
  }
  .login-hr {
  background-color: #dddddd;
  }
</style>


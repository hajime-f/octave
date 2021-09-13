<template>

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
                <input class="input is-midium" placeholder="Password" type="password" v-model="password1">
              </div>
            </div>

            <div class="field">
              <div class="control">
                <label class="label">パスワード（確認）</label>
                <input class="input is-midium" placeholder="Password" type="password" v-model="password2">
              </div>
            </div>
            <div class="is-danger" v-if="error">
              <p v-bind:key="error">{{ error }}</p>
            </div>
            
            <div class="is-block">
              <button class="button is-success is-midium is-fullwidth" type="button" @click="signup">ユーザ仮登録</button>
            </div>

            <hr class="login-hr">
            
            <div class="is-block">
              <div class="has-account">
                アカウントをお持ちの方
              </div>
              <router-link to="/login" class="button is-link is-fullwidth"><strong>ログイン</strong></router-link>
            </div>            
                        
          </form>
          </div>
          
        </div>
      </div>
      
    </div>
  </section>


</template>

<script>
  import axios from 'axios'
  export default {
      data() {
          return {
              email: "",
              password1: "",
              password2: "",
              error: ""
          }
      },
      methods: {
          signup() {
              axios.post(
                  '/api/v1/',
                  {
                      email: this.email,
                      password1: this.password1,
                      password2: this.password2
                  }
              ).then((response) => {
                  const token = response.data.access_token
                  this.$store.commit('setToken', token)
                  axios.defaults.headers.common["Authorization"] = "Token " + token
                  localStorage.setItem("token", token)
                  this.$router.push('/')
              }).catch(error => {
                  console.log(response)
                  this.error = '正しく入力してください。'
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

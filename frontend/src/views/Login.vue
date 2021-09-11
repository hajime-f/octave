<template>
  <div class="home">
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
                console.log(response);
            });
            this.email = "";
            this.password = "";
        }
    }
}
</script>




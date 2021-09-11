<template>
  <div id="wrapper">

    <!-- ヘッダーナビゲーション -->
    <nav class="navbar">
      
      <div class="container">

        <!-- 左上のロゴ表示 -->
        <div class="navbar-brand">
          <router-link to="/" class="navbar-item">
            <img src="./assets/octave.png">
          </router-link>
        </div>
        
        <div class="navbar-menu">
          <div class="navbar-end">
            
            <div class="navbar-item has-dropdown is-hoverable">
              <a class="navbar-link">
                Octave からのメッセージ
              </a>

              <div class="navbar-dropdown">
                <a class="navbar-item is-size-6">
                  楽団管理者の方へ<br>
                  吹奏楽部顧問の先生方へ
                  <!-- <div class="navbar-item is-size-7"> -->
                  <!--   楽団・吹奏楽部の管理がもっと簡単になり、<br> -->
                  <!--   練習だけに集中できるようになります。 -->
                  <!--   <span class="has-text-danger">&#8811; もっと詳しく</span> -->
                  <!-- </div> -->
                </a>
                <hr class="navbar-divider">
                
                <a class="navbar-item is-size-6">
                  楽器メーカー・楽譜出版社の方へ<br>
                  プロ演奏家の方へ
                  <!-- <div class="navbar-item is-size-7"> -->
                  <!--   音楽が大好きな Octave のユーザーに、<br> -->
                  <!--   効果的にマーケティングできます。 -->
                  <!--   <span class="has-text-primary">&#8811; もっと詳しく</span> -->
                  <!-- </div> -->
                </a>
                <hr class="navbar-divider">
                
                <a class="navbar-item is-size-6">
                  吹奏楽連盟の方へ
                  <!-- <div class="navbar-item is-size-7"> -->
                  <!--   連盟所属の楽団との情報共有が簡単になり、<br> -->
                  <!--   運営コストを下げられます。 -->
                  <!--   <span class="has-text-success">&#8811; もっと詳しく</span> -->
                  <!-- </div> -->
                </a>
              </div>
            </div>            
            
            <!-- ログイン認証されている場合の表示 -->
            <template v-if="$store.state.isAuthenticated">
              
            </template>

            <!-- ログイン認証されていない場合の表示 -->
            <template v-else>
              <div class="navbar-item">
                <div class="buttons">
                  <router-link to="/signup" class="button is-success"><strong>無料で始める</strong></router-link>
                  <router-link to="/login" class="button">ログイン</router-link>
                </div>
              </div> 
            </template>
            
          </div>
        </div>
        
      </div>
      
    </nav>
  </div>
  
    <router-link to="/">Home</router-link> |
    <router-link to="/about">About</router-link> |
    <router-link to="/login">Login</router-link>  <!-- 追記 -->  
  
  <router-view/>
</template>

<script>
  import axios from 'axios'

  export default {
    name: 'App',
    beforeCreate() {
      this.$store.commit('initializeStore')

      const token = this.$store.state.token

      if (token) {
        axios.defaults.headers.common['Authorization'] = "Token " + token
      } else {
        axios.defaults.headers.common['Authorization'] = ""
      }
    }
  }
</script>

<style lang="scss">
  @import '../node_modules/bulma';
</style>

<template>
  <header id="wrapper">

    <!-- ヘッダーナビゲーション -->
    <nav class="navbar">
      
        <!-- 左上のロゴ表示 -->
        <div class="navbar-brand">
          <router-link to="/" class="navbar-item">
            <img src="./assets/octave.png">
          </router-link>
          <a class="navbar-burger" aria-label="menu" aria-expanded="false" data-target="navbar-menu" @click="showMobileMenu = !showMobileMenu">
            <span aria-hidden="true"></span>
            <span aria-hidden="true"></span>
            <span aria-hidden="true"></span>
          </a>
        </div>
        
        <div class="navbar-menu" id="navbar-menu" v-bind:class="{'is-active': showMobileMenu}">
          <div class="navbar-end">
            
            <div class="navbar-item has-dropdown is-hoverable">
              <a class="navbar-link">
                Octave からのメッセージ
              </a>

              <div class="navbar-dropdown">
                <a class="navbar-item is-size-6">
                  楽団管理者の方へ<br>
                  吹奏楽部顧問の先生方へ
                </a>
                <hr class="navbar-divider">
                
                <a class="navbar-item is-size-6">
                  楽器メーカー・楽譜出版社の方へ<br>
                  プロ演奏家の方へ
                </a>
                <hr class="navbar-divider">
                
                <a class="navbar-item is-size-6">
                  吹奏楽連盟の方へ
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
        
    </nav>
  </header>
  
<router-view/>

<footer class="footer">
  <p class="has-text-centered">Copyright (c) 2021</p>
</footer>

</template>

<script>
import axios from 'axios'

export default {
    name: 'App',
    data() {
        return {
            showMobileMenu: false
        }
    },
    beforeCreate() {
        this.$store.commit('initializeStore')
        
        const token = this.$store.state.token
        
        if (token) {
            axios.defaults.headers.common['Authorization'] = "Token " + token
        } else {
            axios.defaults.headers.common['Authorization'] = ""
        }
    },
    mounted() {
        document.title = 'Octave - 楽団の管理をもっと簡単に'
        document.querySelector("meta[name='description']").setAttribute('content', "Octave - 楽団の管理をもっと簡単に")
    }
}

</script>

<style lang="scss">
  @import '../node_modules/bulma';
</style>

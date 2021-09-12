<template>

  <section class="hero is-fullheight has-text-centered">
    <div class="hero-body">
      <div class="container">
        <h1 class="title">楽団の管理をもっと簡単に</h1>
        <h2 class="subtitle">楽団・部活動の運営に必要な管理を簡単にして、<br>練習に集中できる環境を手に入れましょう。</h2>
        <div class="buttons are-medium">
          <div class="centering">
            <router-link to="/signup" class="button is-success"><strong>無料で始める</strong></router-link>
            <router-link to="/login" class="button">ログイン</router-link>
          </div>
        </div>
      </div>      
    </div>
  </section>
</template>

<script>
export default {
    mounted: function() {
        document.title = 'Octave | 楽団の管理をもっと簡単に'
        document.querySelector("meta[name='description']").setAttribute('content', "Octave | 楽団の管理をもっと簡単に")
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
  .title {
  color: #ffffff;
  font-size: 45px;
  margin-bottom: 40px;
  }
  .subtitle {
  color: #ffffff;
  font-size: 23px;
  line-height: 140%;
  margin-bottom: 30px;
  }
  .centering {
  margin: 0 auto;
  }
</style>

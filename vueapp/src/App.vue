<template>
  <div
    v-if="authenticated"
    id="app"
    key="main-app"
  >
    <NavItem/>
    <HeaderItem/>
    <MainItem/>
  </div>
  
  <div v-else id="login">
    <LoadSpinner v-if="!loaded"/>
    <MainItem v-if="loaded"/>
  </div>
</template>

<script>
import Vue from 'vue'

import BaseButton from './components/BaseButton.vue'
import HeaderItem from './components/HeaderItem.vue'
import LoadSpinner from './components/LoadSpinner.vue'
import MainItem from './components/MainItem.vue'
import NavItem from './components/NavItem.vue'

export default {
  name: 'app',
  components: {
    BaseButton,
    HeaderItem,
    LoadSpinner,
    MainItem,
    NavItem,
  },
  data() {
    return {
      authenticated: false,
      loaded: false,
      url: {
        clientId: '',
        redirectUri: '',
        state: '',
      },
    }
  },
  watch: {
    $route(to, from) {
      this.setTitle(to.meta.title);
      this.$store.commit('navOff')
    }
  },
  created() {
    this.$http.get('/api/is_authenticated')
      .then(response => {
        if (response.data.authenticated) {
          this.setTitle(this.$route.meta.title);
          this.authenticated = true;
        } else {
          this.$router.push(
            'login',
            () => this.loaded = true,
            () => this.loaded = true,
          );
        }
      })
      .catch(error => console.error(error))
  },
  methods: {
    setTitle(title) {
      document.title = `${title} | Twitch Colours`
    },
  },
}
</script>

<style scoped lang="stylus">
$max-flex
  display flex
  min-height 100vh

  >>> > *
    margin auto

#app
  @extend $max-flex
  padding 87px 25px 25px 275px

  @media (max-width: 768px)
    padding: 67px 20px 15px

#login
  @extend $max-flex
  padding 25px

.fade-slide-up-enter-active
.fade-slide-up-leave-active 
  transition all .15s

.fade-slide-up-enter
.fade-slide-up-leave-to
  opacity 0
  transform translateY(5px)
</style>

<style lang="stylus">
font = Lato, Helvetica, Arial, sans-serif

*
  box-sizing border-box

body
  background #f2f3f8
  color black
  margin 0
  text-align center

body
input
button
  font-family font
</style>
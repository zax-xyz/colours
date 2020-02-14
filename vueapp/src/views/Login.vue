<template lang="pug">
  .container
    .left
      img.logo(
        src="../assets/rainbow-twitch.png"
        height="135"
        width="auto"
      )

    .right
      LoadSpinner(v-if="loading")
      
      BaseButton.login(
        v-else
        @click.native="login"
      ) Login with Twitch

      .info You need to sign in with your Twitch account for us to be able to activate and control the script for you
</template>

<script>
import BaseButton from '@/components/BaseButton.vue'
import LoadSpinner from '@/components/LoadSpinner.vue'

export default {
  name: 'Login',
  components: {
    BaseButton,
    LoadSpinner,
  },
  data() {
    return {
      loading: true,
      url: {
        clientId: '',
        redirectUri: '',
        state: '',
      },
    }
  },
  created() {
    this.$http.get('/api/get_login_url')
      .then(response => {
        this.url = response.data;
        this.loading = false;
      })
      .catch(error => console.error(error))
  },
  methods: {
    login() {
      window.location.href = `https://id.twitch.tv/oauth2/authorize?client_id=${this.url.clientId}&redirect_uri=${this.url.redirectUri}&response_type=code&scope=chat:edit+chat:read&state=${this.url.state}`
    },
  },
}
</script>

<style scoped lang="stylus">
.container
  display flex
  align-items center

.left
  @extend .container
  flex 1
  padding 25px

.right
  @extend .container
  flex 2
  flex-direction column
  padding 25px

.load-spinner
  margin auto

.logo
  @extend .load-spinner
  filter drop-shadow(-3px 3px 5px rgba(0, 0, 0, 0.2))

.login
  background hsl(260, 70%, 60%)
  border-color @background
  box-shadow 0 1px 5px hsla(260, 70%, 60%, .5)
  color hsl(260, 70%, 98%)
  margin 0
  max-width 600px
  width 100%

  &:hover
    background hsl(260, 70%, 55%)
    border-color @background

p
  margin-bottom 0
</style>

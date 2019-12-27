<template lang="pug">
  nav(:class="cls")
    h3.title
      | Twitch 
      span.rainbow-text Colours

    ul
      router-link(
        v-for="tab in tabs"
        :to="tab.path"
        :key="tab.path"
        @click.native="updateViewKey"
      )
        li {{ tab.name }}

      a(href="/api/logout")
        li Logout
</template>

<script>
export default {
  name: 'NavItem',
  data() {
    return {
      tabs: [
        {
          path: '/home',
          name: 'Home',
        },
        {
          path: '/channels',
          name: 'Channel List',
        },
        {
          path: '/colours',
          name: 'Colour List',
        },
        {
          path: '/logs',
          name: 'Logs',
        },
        {
          path: '/libraries',
          name: 'Libraries',
        },
      ],
    }
  },
  computed: {
    navActive() {
      return this.$store.state.navActive
    },
    cls() {
      return {
        nav: true,
        active: this.navActive,
      }
    },
  },
  methods: {
    updateViewKey(e) {
      if (e.currentTarget.classList.contains('router-link-active')) {
        this.$store.commit('addViewKey');
      }
    },
  },
}
</script>

<style scoped lang="stylus">
.nav
  background hsl(210, 15%, 20%)
  bottom 0
  color white
  left 0
  overflow-y auto
  position fixed
  text-align left
  top 0
  transition transform .3s
  width 250px
  z-index 2

  @media (max-width 768px)
    box-shadow 0 0 10px 2px rgba(0, 0, 0, .25)
    padding-top 50px
    max-width 500px
    transform translateX(-100%) translateX(-5px)
    width 80%

    &.active
      transform none

ul
  list-style-type none
  margin 0
  padding 0

.title
  -webkit-user-select none
  border-left 0
  color inherit
  margin 0
  user-select none
  padding 25px 25px 15px 25px

a
  color hsl(210, 5%, 70%)
  display block
  font-style normal
  outline 0
  text-decoration none
  transition all .2s

  &:hover
    color #e4e6e7
    border-left 3px solid

  &.router-link-active
    @extend a:hover
    background hsl(210, 15%, 15%)
    border-color #54aff8
    font-weight bold
    padding-left 2px

li
  padding 10px 30px 10px 40px

.rainbow-text
  background-image repeating-linear-gradient(45deg, green, yellow, orange, red, violet)
  -webkit-background-clip text
  -webkit-text-fill-color transparent
  animation rainbow 4s ease infinite
  background-size 800% 800%

@keyframes rainbow
  0% 
    background-position 0% 50%

  50%
    background-position 100% 25%

  100%
    background-position: 0% 50%
</style>
<template lang="pug">
  transition(
    name="fade-slide-up"
    mode="out-in"
    appear
  )
    router-view#main(
      :key="viewKey"
    )
</template>

<script>
export default {
  name: 'MainItem',
  computed: {
    viewKey() {
      return this.$store.state.viewKey;
    },
  },
}
</script>

<style scoped lang="stylus">
#main
  background white
  border-radius 4px
  box-shadow 0 2px 5px rgba(0, 0, 0, .2)
  max-width 800px
  padding 30px 40px
  width 100%

>>> a
  border-bottom 1px solid transparent
  color #0073aa
  font-style italic
  text-decoration none
  transition border-bottom-color .2s, color .2s

  &:hover
    border-bottom-color #005177
    color #005177

>>> .info
  color #242424
  font-weight lighter

  strong 
    color black
    font-weight bolder

>>> .shadow
  box-shadow 0 0 5px rgba(0, 0, 0, .25)

{selector('>>>', 'h1, h2, h3, h4, h5, h6')}
  color #3e3e3e

.fade-slide-up-enter-active
.fade-slide-up-leave-active
  transition opacity .1s, transform .1s

.fade-slide-up-enter
.fade-slide-up-leave-to
  opacity 0
  transform translateY(5px)
</style>
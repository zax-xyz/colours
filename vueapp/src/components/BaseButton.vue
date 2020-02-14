<template lang="pug">
  button.btn
    slot
</template>

<script>
export default {
  name: 'BaseButton',
}
</script>

<style scoped lang="stylus">
btn-color(background, color = @color)
  background background
  border-color background
  color color

.btn
  border 2px solid
  btn-color hsl(210, 70%, 60%), hsl(210, 100%, 98%)
  border-radius 5px
  box-shadow 0 1px 5px hsla(210, 70%, 60%, .5)
  cursor pointer
  display inline-block
  font-size 1em
  font-weight bold
  margin 5px
  padding 8px 18px
  transition background .2s, border-color .2s, color .2s, transform .2s

  &:hover
    btn-color hsl(210, 70%, 55%)
    transform translateY(-1px)

  &.inactive
    background white
    color hsl(210, 30%, 40%)

    &:hover
      background hsl(210, 70%, 96%)

  &.success
    btn-color hsl(100, 70%, 50%) hsl(106, 100%, 98%)

    &:hover
      btn-color hsl(100, 70%, 45%)

  &.error
    btn-color hsl(0, 70%, 60%) hsl(0, 100%, 98%)

    &:hover
      btn-color hsl(0, 70%, 55%)
</style>

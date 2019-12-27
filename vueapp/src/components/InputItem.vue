<template lang="pug">
  transition(
    name="fade-height"
    mode="in-out"
    appear
  )
    input.input(
      v-if="isNotNull"
      v-model.trim="items[index]"
      :style="styles"
      :name="name"
      :placeholder="titleName"
      @focusout="checkDelete"
      autocomplete="off"
      spellcheck="false"
    )
</template>

<script>
export default {
  name: 'InputItem',
  props: {
    items: {
      type: Array,
      required: true,
    },
    styles: {
      type: Object,
      required: false,
    },
    index: {
      type: Number,
      required: true,
    },
    name: {
      type: String,
      required: true,
    },
  },
  data() {
    return {
      visible: true
    }
  },
  methods: {
    checkDelete(e) {
      const el = this.$el;
      if (!el.value && el.nextElementSibling !== null) {
        this.$set(this.items, this.index, null)
      }
    },
  },
  computed: {
    isNotNull() {
      return this.items[this.index] !== null
    },
    titleName() {
      return this.name[0].toUpperCase() + this.name.slice(1)
    },
  },
}
</script>

<style scoped lang="stylus">
.input
  border 0
  border-top 1px solid #d6d9db
  color black
  height 36px
  font-size 1em
  padding 8px
  transition box-shadow .2s

  &:first-child
    border-radius 3px 3px 0 0
    border-top-width 0

  &:last-child
    border-radius 0 0 3px 3px

  &:focus
    box-shadow 0 0 5px 1px lightblue
    z-index 1

.fade-height-enter-active
.fade-height-leave-active
  transition: height .2s, opacity .2s, padding .2s

.fade-height-enter
.fade-height-leave-to
  height 0
  opacity 0
  padding 0 8px
</style>
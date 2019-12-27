<template lang="pug">
  BaseButton(
    :class="classes"
    @click.native="get"
  )
    slot
</template>

<script>
import BaseButton from './BaseButton.vue'

export default {
  name: 'ButtonGet',
  components: {
    BaseButton
  },
  props: {
    url: {
      type: String,
      required: true,
    },
    inactive: {
      type: Boolean,
      default: false,
    },
  },
  data() {
    return {
      cls: '',
    }
  },
  computed: {
    classes() {
      return [
        { inactive: this.inactive },
        this.cls,
      ]
    },
  },
  methods: {
    tempClass(cls) {
      this.cls = cls;
      setTimeout(() => {
        this.cls = ''
      }, 1000)
    },
    get() {
      this.$http.get(this.url)
        .then(response => {
          if (response.data.result === 'success') {
            this.tempClass('success')
          } else {
            this.tempClass('error')
          }
          this.$emit('get-status')
        })
        .catch(error => {
          console.error(error);
          this.tempClass('error')
        })
    },
  },
}
</script>
<template>
  <svg
    class="load-spinner"
    :width="size"
    :height="size"
    viewBox="0 0 66 66"
  >
    <circle
      class="circle"
      fill="none"
      stroke-width="6"
      stroke-linecap="round"
      cx="33"
      cy="33"
      r="30"
    />
  </svg>
</template>

<script>
export default {
  name: 'LoadSpinner',
  props: {
    size: {
      type: Number,
      default: 36,
    },
  },
}
</script>

<style scoped lang="stylus">
.load-spinner
  animation rotator 1.4s linear infinite

@keyframes rotator
  0%
    transform rotate(0deg)
  100%
    transform rotate(270deg)

.circle
  stroke #4285f4
  stroke-dasharray 187
  stroke-dashoffset 0
  transform-origin center
  animation dash 1.4s ease-in-out infinite

@keyframes dash
  0%
    stroke-dashoffset 187
  50%
    stroke-dashoffset 46.75
    transform rotate(135deg)
  100%
    stroke-dashoffset 187
    transform rotate(450deg)
</style>
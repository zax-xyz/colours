<template lang="pug">
  div
    h1 Colours

    .info
      p Set which colours for the script to use here.
      p.
        The script will cycle through these colours every message,
        looping back to the beginning when it reaches the end.
      p.
        You can use the preset colours Twitch allows for all users (used by default),
        or hex colours like #5299e0 if you have Twitch Prime/Turbo.
      p You may set up to 100 colours.

    LoadSpinner(v-if="loading")

    FormItem(
      v-else
      :items="colours"
      :styles="styles"
      :pre="toHex"
      name="colour"
      save-name="Colours"
      url="/api/set_colours"
    )
</template>

<script>
import Color from 'color'

import FormItem from '@/components/FormItem.vue'
import LoadSpinner from '@/components/LoadSpinner.vue'

export default {
  name: 'Colours',
  data() {
    return {
      loading: true,
      colours: [],
    }
  },
  components: {
    FormItem,
    LoadSpinner,
  },
  created() {
    this.getColours();
  },
  methods: {
    getColours() {
      this.$http.get('/api/get_colours')
        .then(response => this.colours = response.data.data)
        .catch(error => console.error(error))
        .finally(() => this.loading = false)
    },
    styles(item) {
      return { color: item }
    },
    toHex(colour) {
      if (colour[0] == '#') {
        // Already a hex
        return colour;
      }

      // First element of each array is a regex string to match against
      // The second element is the method to call on the matches
      const toMatch = [
        [ String.raw`hsl\(\s*(\d+)\s*,\s*(\d+)%\s*,\s*(\d+)%\s*\)`, Color.hsl ],
        [ String.raw`rgb\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*\)`, Color.rgb ],
      ]

      for (const arr of toMatch) {
        const matches = colour.match(arr[0]);
        if (matches !== null) {
          // Get the color object from the matching groups, and return the
          // hex string
          return arr[1](
            matches.slice(1).map(n => Number(n))
          ).hex();
        }
      }

      // No matches, probably a colour name like 'red'
      return colour;
    },
  },
}
</script>

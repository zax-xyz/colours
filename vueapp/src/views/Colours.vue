<template>
  <div>
    <h1>Colours</h1>

    <p class="info">
      Set which colours for the script to use here.
      <br>
      The script will cycle through these colours every message, looping back to the beginning when it reaches the end.
      <br>
      You can use the preset colours Twitch allows for all users (used by default), or hex colours like #5299e0 if you have Twitch Prime/Turbo.
      <br>
      You may set up to 100 colours.
    </p>

    <LoadSpinner v-if="loading"/>

    <FormItem
      v-else
      :items="colours"
      name="colour"
      save-name="Colours"
      url="/api/set_colours"
    />
  </div>
</template>

<script>
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
  },
}
</script>
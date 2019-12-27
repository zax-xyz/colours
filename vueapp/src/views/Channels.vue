<template lang="pug">
  div
    h1 Channels

    p.info.
      Set which channels for the script to run in here.
      <br>
      The script needs a set of channels to run in as it has to listen for messages to know when to change colour.
      <br>
      You may set up to 100 channels.

    LoadSpinner(v-if="loading")

    FormItem(
      v-else
      :items="channels"
      name="channel"
      save-name="Channels"
      url="/api/set_channels"
    )
</template>

<script>
import FormItem from '@/components/FormItem.vue'
import LoadSpinner from '@/components/LoadSpinner.vue'

export default {
  name: 'Channels',
  data() {
    return {
      loading: true,
      channels: [],
    }
  },
  components: {
    LoadSpinner,
    FormItem,
  },
  created() {
    this.getChannels();
  },
  methods: {
    getChannels() {
      this.$http.get('/api/get_channels')
        .then(response => this.channels = response.data.data)
        .catch(error => console.error(error))
        .finally(() => this.loading = false)
    },
  },
}
</script>

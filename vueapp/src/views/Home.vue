<template lang="pug">
  div
    p
      | Set your 
      router-link(to="/channels") channels 
      | before starting the script!

    ButtonGet(
      :inactive="startInactive"
      @get-status="getStatus"
      url="/api/start"
    ) Start Script
    ButtonGet(
      :inactive="stopInactive"
      @get-status="getStatus"
      url="/api/stop"
    ) Stop Script

    p
      | Status: 
      LoadSpinner(
        v-if="loading"
        :size="16"
      )
      span(v-else) {{ status }}

    p.info
      | Please note that after running the script, 
      strong it will take 3 messages for you to notice an effect. 
      | Your colour will be changed from the second message (as it only changes colour after every captured message) and 
      strong
        em the colour changes on your screen are delayed by one message (everyone else sees it one colour ahead) 
      | due to Twitch caching the previous message metadata to re-use in subsequent messages.
</template>

<script>
import ButtonGet from '@/components/ButtonGet.vue'
import LoadSpinner from '@/components/LoadSpinner.vue'

export default {
  name: 'Home',
  components: {
    LoadSpinner,
    ButtonGet,
  },
  data() {
    return {
      loading: true,
      running: undefined,
    }
  },
  computed: {
    status() {
      if (this.running === undefined) {
        return ''
      }
      if (this.running) {
        return 'Running'
      }
      return 'Not Running'
    },
    startInactive() {
      return this.running === true
    },
    stopInactive() {
      return this.running === false
    },
  },
  created() {
    this.getStatus();
  },
  methods: {
    getStatus() {
      this.$http.get('/api/get_status')
        .then(response => this.running = response.data.running)
        .catch(error => console.error(error))
        .finally(() => this.loading = false)
    },
  },
}
</script>
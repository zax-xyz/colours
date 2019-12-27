<template>
  <div>
    <h1>Logs</h1>
    
    <LoadSpinner v-if="loading"/>

    <div
      v-else
      style="overflow-x:auto"
      class="shadow"
    >
      <table>
        <tr>
          <th>Channel</th>
          <th>Message</th>
          <th>Time</th>
        </tr>

        <tr v-for="row in logs" :key="row.pk">
          <td>{{ row.fields.channel }}</td>
          
          <td>
            /color
            <span :style="{color: color(row)}">
              {{ color(row) }}
            </span>
          </td>

          <td>{{ formatTime(row.fields.time) }}</td>
        </tr>
      </table>
    </div>
  </div>
</template>

<script>
import moment from 'moment'

import LoadSpinner from '@/components/LoadSpinner.vue'

export default {
  name: 'Logs',
  components: {
    LoadSpinner
  },
  data() {
    return {
      loading: true,
      logs: [],
    }
  },
  created() {
    this.getLogs();
  },
  methods: {
    getLogs() {
      this.$http.get('/api/get_logs')
        .then(response => this.logs = response.data.data)
        .catch(error => console.error(error))
        .finally(() => this.loading = false)
    },
    color(row) {
      const parts = row.fields.content.split(' ');
      return parts[1]
    },
    formatTime(time) {
      const format = 'D MMM H:mm:ss';
      return moment.utc(time, format).local().format(format)
    },
  },
}
</script>

<style lang="stylus">
table
  border-collapse collapse
  border-style hidden
  text-align center
  width 100%

td
  border 1px solid lightgrey
  padding 7px

th
  @extend td
  background #eff5fb
</style>
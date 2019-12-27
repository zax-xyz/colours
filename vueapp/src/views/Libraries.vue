<template lang="pug">
  div
    h1 Open Source Libraries
    p.info This website relies the following open source libraries, and their respective dependencies

    div(v-for="library in libraries")
      h3 {{ library.description }}
      p
        a(:href="library.url") {{ library.name }}
</template>

<script>
export default {
  name: 'Libraries',
  data() {
    return {
      libraries: [
        {
          name: 'Vue',
          description: 'Frontend JavaScript Framework',
          url: 'https://vuejs.org/',
        },
        {
          name: 'Vuex',
          description: 'Centralised State Management',
          url: 'https://vuex.vuejs.org',
        },
        {
          name: 'Vue Router',
          description: 'Frontend Router for Single Page Applications',
          url: 'https://router.vuejs.org/',
        },
        {
          name: 'Axios',
          description: 'JS HTTP Client',
          url: 'https://github.com/axios/axios',
        },
        {
          name: 'Moment.js',
          description: 'JS Date/Time Parse',
          url: 'https://momentjs.com/',
        },
        {
          name: 'Django',
          description: 'Backend Web Framework',
          url: 'https://www.djangoproject.com/',
        },
        {
          name: 'SQLite',
          description: 'Relational Database Management System',
          url: 'https://www.sqlite.org/index.html',
        },
        {
          name: 'Celery',
          description: 'Asynchronous Task Queue',
          url: 'http://www.celeryproject.org/',
        },
        {
          name: 'Redis',
          description: 'In-Memory Data Structure Store/Database',
          url: 'https://redis.io/',
        },
        {
          name: 'Requests',
          description: 'HTTP Library',
          url: 'https://github.com/psf/requests',
        },
        {
          name: 'TwitchIO',
          description: 'Async Twitch IRC Wrapper',
          url: 'https://github.com/TwitchIO/TwitchIO',
        },
      ]
    }
  },
}
</script>

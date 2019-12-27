import Vue from 'vue'
import VueRouter from 'vue-router'

const Home = () => import('@/views/Home.vue')
const Channels = () => import('@/views/Channels.vue')
const Colours = () => import('@/views/Colours.vue')
const Logs = () => import('@/views/Logs.vue')
const Libraries = () => import('@/views/Libraries.vue')
const Login = () => import('@/views/Login.vue')

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    redirect: '/home',
  },
  {
    path: '/home',
    component: Home,
    meta: { title: 'Home' },
  },
  {
    path: '/channels',
    component: Channels,
    meta: { title: 'Channels' },
  },
  {
    path: '/colours',
    component: Colours,
    alias: '/colors',
    meta: { title: 'Colours' },
  },
  {
    path: '/logs',
    component: Logs,
    meta: { title: 'Logs' },
  },
  {
    path: '/libraries',
    component: Libraries,
    meta: { title: 'Libraries' },
  },
  {
    path: '/login',
    component: Login,
    meta: { title: 'Login' },
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
})

export default router

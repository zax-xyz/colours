import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

const store = new Vuex.Store({
  state: {
    navActive: false,
    viewKey: 1,
  },
  mutations: {
    toggleNav: state => state.navActive = !state.navActive,
    navOff: state => { if (state.navActive) { state.navActive = false } },
    addViewKey: state => state.viewKey++,
  },
})

export default store
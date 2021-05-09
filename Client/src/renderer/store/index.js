import Vue from 'vue'
import Vuex from 'vuex'

import { createPersistedState, createSharedMutations } from 'vuex-electron'

import modules from './modules'

Vue.use(Vuex)

export default new Vuex.Store({
  modules,

  state:{
    result:''
  },
  getters:{
    getRes(state){
      return state.result;
    }
  },
  mutations:{
    setRes(state,payload){
      state.result = payload;
    }
  },
  plugins: [
    createPersistedState(),
    createSharedMutations()
  ],
  strict: process.env.NODE_ENV !== 'production'
})

import Vue from 'vue'
import Router from 'vue-router'
import Home from '../components/home'
import Predict from '../components/predict.vue'
import Result from '../components/result.vue'


Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '*',
      redirect: '/'
    },
	{
	  path: '/predict',
	  name: 'predict',
	  component: Predict
	},
	{
	  path: '/result',
	  name: 'result',
	  component: Result
	}
  ]
})

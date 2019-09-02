import Vue from 'vue';
import Router from 'vue-router';
import Delete from './components/Delete.vue';
import Chart from './components/Chart.vue';
import Entry from './components/Entry.vue';

Vue.use(Router);

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/delete',
      name: 'Delete',
      component: Delete,
    },
    {
      path: '/entry',
      name: 'Entry',
      component: Entry,
    },
    {
      path: '/chart',
      name: 'Chart',
      component: Chart,
    },
  ],
});

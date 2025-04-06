
/**
 * router/index.ts
 *
 * Automatic routes for `./src/pages/*.vue`
 */

// Composables
import { createRouter, createWebHistory } from 'vue-router'
import Index from '@/pages/index.vue'
import Admin from '@/pages/admin.vue'

const routes = [
  {path: '/', component: Index},
  {path: '/admin', component: Admin},
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router

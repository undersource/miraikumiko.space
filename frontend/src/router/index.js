import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import ArticleListView from '../views/ArticleListView.vue'
import TagListView from '../views/TagListView.vue'
import BusinessView from '../views/BusinessView.vue'
import TagView from '../views/TagView.vue'
import ArticleView from '../views/ArticleView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/articles',
      name: 'articles',
      component: ArticleListView
    },
    {
      path: '/tags',
      name: 'tags',
      component: TagListView
    },
    {
      path: '/business',
      name: 'business',
      component: BusinessView
    },
    {
      path: '/article/:slug',
      name: 'article',
      component: ArticleView
    },
    {
      path: '/tag/:name',
      name: 'tag',
      component: TagView
    }
  ]
})

export default router

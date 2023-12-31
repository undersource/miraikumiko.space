<template>
  <main>
    <div class="articles">
      <ul>
        <li v-for="article, index in articles" :key="index" class="article">
          <router-link :to="`/article/${article.slug}`">{{ article.title }}</router-link>
        </li>
      </ul>
    </div>
  </main>
</template>

<style scoped>
main {
  display: flex;
  justify-content: center;
}

.article {
  font-size: 25px;
  list-style-type: none;
  margin: 20px 0px;
}

.article a {
  color: inherit;
}
</style>

<script>
import axios from 'axios'
import { API_URL } from '../config'

export default {
  data() {
    return {
      endpoint: API_URL + "/articles",
      articles: []
    }
  },
  created() {
    this.$watch(
      () => this.$route.params,
      () => {
        this.fetchData()
      },
      { immediate: true }
    )
  },
  methods: {
    fetchData() {
      axios.get(this.endpoint)
        .then(res => {
          this.articles = res.data;
        })
        .catch(error => {
          console.log(error);
        })
    }
  }
}
</script>

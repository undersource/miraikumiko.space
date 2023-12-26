<template>
  <main>
    <div class="articles">
      <ul v-for="article, index in articles" :key="index">
        <li class="article">
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
      articles: [],
      endpoint: API_URL + "/tag/" + this.$route.params.name + "/articles"
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
          console.log('-------error-------');
          console.log(error);
        })
    }
  }
}
</script>

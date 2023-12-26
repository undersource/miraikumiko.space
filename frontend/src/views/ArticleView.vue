<template>
  <main>
    <h1>{{ article.title }}</h1>
    <i>{{ article.date }}</i>
    <article v-html="article.text"></article>
    <ul v-for="tag, index in tags" :key="index" class="tags">
      <li>
        <router-link :to="{ path: '/tag/' + tag.name }" class="tag">#{{ tag.name }}</router-link>
      </li>
    </ul>
  </main>
</template>

<script>
import axios from 'axios'
import { API_URL } from '../config'

export default {
  data() {
    return {
      article: null,
      article_endpoint: API_URL + "/article/" + this.$route.params.slug,
      tags: []
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
      axios.get(this.article_endpoint)
        .then(res => {
          this.article = res.data;

          axios.get(API_URL + "/article/" + res.data.id + "/tags")
            .then(res => {
              this.tags = res.data;
            })
            .catch(error => {
              console.log('-------error-------');
              console.log(error);
            })
        })
        .catch(error => {
          console.log('-------error-------');
          console.log(error);
        })
    }
  }
}
</script>

<template>
  <main>
    <h1>{{ article.title }}</h1>
    <i>{{ article_date }}</i>
    <article v-html="article.text"></article>
    <ul class="tags">
      <li v-for="tag, index in tags" :key="index">
        <router-link :to="{ path: '/tag/' + tag.name }" class="tag">#{{ tag.name }}</router-link>
      </li>
    </ul>
  </main>
</template>

<script>
import axios from 'axios'
import moment from 'moment';
import { API_URL } from '../config'

export default {
  data() {
    return {
      article: null,
      article_date: null,
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
          this.article_date = moment(res.data.date).format('DD MMM YYYY');

          axios.get(API_URL + "/article/" + res.data.id + "/tags")
            .then(res => {
              this.tags = res.data;
            })
            .catch(error => {
              console.log(error);
            })
        })
        .catch(error => {
          console.log(error);
        })
    }
  }
}
</script>

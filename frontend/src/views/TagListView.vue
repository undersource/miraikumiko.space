<template>
  <main>
    <div v-for="tag, index in tags" :key="index">
      <router-link :to="`/tag/${tag.name}`" class="tag">#{{ tag.name }}</router-link>
    </div>
  </main>
</template>

<style scoped>
main {
  display: flex;
  justify-content: center;
}

.tag {
  color: inherit;
  font-size: 20px;
  padding-right: 10px;
}
</style>

<script>
import axios from 'axios'
import { API_URL } from '../config'

export default {
  data() {
    return {
      endpoint: API_URL + "/tags",
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
      axios.get(this.endpoint)
        .then(res => {
          this.tags = res.data;
        })
        .catch(error => {
          console.log(error);
        })
    }
  }
}
</script>

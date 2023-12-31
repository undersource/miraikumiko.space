<template>
  <main>
    <h1>Add Article</h1>
    <div class="editor">
      <p v-if="status" class="status">{{ status }}</p>
      <p v-if="error" class="error">{{ error }}</p>
      <input type="text" placeholder="Title" id="title" v-model="title">
      <br>
      <input type="text" placeholder="Slug" id="slug" v-model="slug">
      <textarea placeholder="Text" id="text" v-model="text"></textarea>
      <input type="text" placeholder="Tags separated by comma" id="tags" v-model="tags">
      <br>
      <button @click="sendData">Submit</button>
    </div>
  </main>
</template>

<style scoped>
.editor * {
  margin: 5px;
}

textarea {
  height: 300px;
  width: 100%;
}

.status {
  color: green;
}

.error {
  color: red;
}
</style>

<script>
import axios from 'axios'
import { API_URL } from '../config'
import { cookies } from '../misc/cookies'

export default {
  data() {
    return {
      token: cookies.get("AuthToken"),
      endpoint: API_URL + "/auth",
      post_article_endpoint: API_URL + "/article/post",
      title: null,
      slug: null,
      text: null,
      tags: null,
      status: null,
      error: null
    }
  },
  created() {
    this.$watch(
      () => this.$route.params,
      () => {
        this.auth()
      },
      { immediate: true }
    )
  },
  methods: {
    auth() {
      if (this.token == null) {
        return;
      }

      const headers = {
        'Authorization': 'Basic ' + this.token
      };

      axios.get(this.endpoint, { headers: headers });
    },
    sendData() {
      const headers = {
        'Authorization': 'Basic ' + this.token
      };

      axios.post(this.post_article_endpoint, {
          title: this.title,
          slug: this.slug,
          text: this.text,
          tags: this.tags.split(',')
        },
        {
          headers: headers 
        })
        .then(() => {
          this.$router.push('/articles');
          this.status = "Article has been published"
          this.title = ''
          this.slug = ''
          this.text = ''
          this.tags = ''
        })
        .catch(error => {
          this.error = "Failed to post data"
          console.error(error);
        });
    }
  }
}
</script>

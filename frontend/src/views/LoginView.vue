<template>
  <main>
    <h1>Login</h1>
    <div class="login">
      <p v-if="error" class="error">Invalid login or password</p>
      <input type="name" placeholder="Username" autocomplete="on" id="username" v-model="username">
      <input type="password" placeholder="Password" id="password" v-model="password">
      <button @click="sendData">Submit</button>
    </div>
  </main>
</template>

<style scoped>
main {
  text-align: center;
}

.login {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.login input {
  width: 250px;
  padding: 10px;
  margin: 2px;
}

.login button {
  width: 274px;
  padding: 10px;
  margin: 2px;
}

.error {
  background-color: tomato;
  width: 252px;
  padding: 10px;
  margin: 2px;
  border: 1px solid #555;
  border-radius: 2px;
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
      username: null,
      password: null,
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

      axios.get(this.endpoint, { headers: headers })
        .then(() => {
          this.$router.push('/dashboard');
        });
    },
    sendData() {
      const headers = {
        'Authorization': 'Basic ' + btoa(this.username + ':' + this.password)
      };

      axios.get(this.endpoint, { headers: headers })
        .then(response => {
          cookies.set("AuthToken", response.data.token);
          this.$router.push('/dashboard');
        })
        .catch(error => {
          this.error = error
          console.error(error);
        });
    }
  }
}
</script>

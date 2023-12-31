<template>
  <main>
    <h1>Вы здесь</h1>
    <h3>Почему</h3>
    <p>А это философский вопрос.</p>
    <hr>
    <h3>Зачем</h3>
    <p>Развеять скуку - самую страшную вещь на свете.</p>
    <hr>
    <h3>Мир</h3>
    <p>Субъективное ощущение, он лишь в голове.</p>
    <p>
      Смысл это не физическая величина, нет такой молекулы из которой бы он
      состоял, только человек наделяет им вещи, которые есть сами по себе, без
      смысла.
    </p>
    <p>
      В нём нет одинаковых вещей, но все люди одинаковы по своей сути, чем дольше
      живёшь, тем в большем количестве людей видишь себя, но увидеть себя можно
      в каждом человеке.
    </p>
    <hr>
    <h3>Мнение</h3>
    <p>Хочет обладать каждый, но позволить иметь своё не может никто.</p>
    <hr>
    <h3>Технологии</h3>
    <p>Создают больше проблем чем решают.</p>
    <hr>
    <h3>Речь</h3>
    <p>
      Говорить нужно лаконично (производно от Лаконии - регион Эллады в котором
      находился город Спарта), чётко и по делу.
    </p>
    <hr>
    <h3>Список <a href="https://liberapay.com/underground">донатеров</a>:</h3>
    <table class="donators">
      <tr v-for="donator, index in donators" :key="index">
        <td><a href="{{ donator.url }}">{{ donator.name }}</a></td>
        <td><i>${{ donator.amount }}</i></td>
      </tr>
    </table>
    <hr>
    <h3>Кто я</h3>
    <p>Mirai Kumiko - псевдоним, созвучный с моим именем.</p>
    <h4>Софт которым пользуюсь:</h4>
    <div class="soft">
      <a href="https://archlinux.org">Arch Linux</a>
      <br>
      <a href="https://swaywm.org">Sway</a>
      <br>
      <a href="https://codeberg.org/dnkl/foot">Foot</a>
      <br>
      <a href="https://www.vim.org">Vim</a>
      <br>
      <a href="https://github.com/ungoogled-software/ungoogled-chromium">Ungoogled Chromium</a>
      <br>
      <a href="https://github.com/baresip/baresip">Baresip</a>
      <br>
      <a href="https://www.mutt.org">Mutt</a>
      <br>
      <a href="https://syncplay.pl">Syncplay</a>
      <br>
      <a href="https://framatalk.org">Jitsi Meet</a>
    </div>
  </main>
  <footer>
    <hr>
    <ul class="contacts">
      <li>
        <a href="mailto:underground@macaw.me">Email</a>
      </li>
      <li>
        <a href="xmpp:underground@macaw.me">XMPP</a>
      </li>
      <li>
        <a href="https://mastodon.social/@miraikumiko">Mastodon</a>
      </li>
      <li>
        <a href="https://pixtagram.social/miraikumiko">Pixelfed</a>
      </li>
    </ul>
  </footer>
</template>

<style scoped>
main a {
  color: maroon;
}

.donators td, th {
  border: 0px;
}
</style>

<script>
import axios from 'axios'
import { API_URL } from '../config'

export default {
  data() {
    return {
      endpoint: API_URL + "/donators",
      donators: []
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
          this.donators = res.data;
        })
        .catch(error => {
          console.log(error);
        })
    }
  }
}
</script>

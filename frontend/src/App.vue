<template>
  <header>
    <router-link to="/" class="logo"><span style="color: maroon;">MIRAI</span> | KUMIKO</router-link>
    <nav>
      <ul class="menu">
        <li v-for="link, index in ['articles', 'tags', 'business']" :key="index" >
          <router-link :to="`/${link}`">{{ link }}</router-link>
        </li>
      </ul>
    </nav>
  </header>
  <router-view></router-view>
</template>

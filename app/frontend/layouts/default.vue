<template>
  <v-app id="app">
    <v-container>
      <header/>
      <nuxt/>
    </v-container>
    <auth/>
  </v-app>
</template>

<script>
export default {
  data() {
    return {}
  }
}
</script>

<style>
#app {
  background: url("../static/back.png") no-repeat fixed;
  background-size: cover;
}
</style>

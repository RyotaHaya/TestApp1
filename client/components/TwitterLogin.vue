<template>
  <img
    class="twitter-login"
    src="~/assets/tmp-login-button.png"
    @click="TwitterLogin"
  />
</template>
<script>
export default {
  data() {
    return {
      name: 'Nuxt.js',
    }
  },
  methods: {
    TwitterLogin() {
      this.$axios
        .get(this.$config.apiURL + '/api/twitter/requestToken')
        .then((res) => {
          // .get('/twitter/requestToken')
          //リクエスト成功時
          alert('request success')
          //this.$config.apiURL
          window.location.href = res.data.url
        })
        .catch((err) => {
          //リクエスト失敗時
          alert('request falied')
        })

      alert(`Hello `)
    },
  },
}
</script>
<style>
.TwitterLogin {
  background-color: #00a656;
  border-radius: 1em;
  box-shadow: 0 0.2em 0.5em rgba(0, 0, 0, 0.2);
  padding: 1em 2em;
  color: #ffffff;
  font-weight: bold;
  text-decoration: none;
}
</style>

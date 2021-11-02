<template>
  <v-card color="white" width="200" height="240" class="ma-2">

    <a href="http://pbs.twimg.com/media/E1DeiydVEAIK8sf.jpg"
      ><img
        src="http://pbs.twimg.com/media/E1DeiydVEAIK8sf.jpg?format=jpg&name=thumb"
    /></a>

    <v-card-actions>
      <v-btn icon>A</v-btn>
      <v-btn icon>B</v-btn>
    </v-card-actions>
  </v-card>
</template>
<script>
export default {
  data() {
    return {
      name: 'Nuxt.js',
    }
  },
  methods: {
    SampleEvent() {
      alert(`Hello `)
    },
  },
}
</script>
<style>
.SampleEvent {
  background-color: #00a656;
  border-radius: 1em;
  box-shadow: 0 0.2em 0.5em rgba(0, 0, 0, 0.2);
  padding: 1em 2em;
  color: #ffffff;
  font-weight: bold;
  text-decoration: none;
}
</style>

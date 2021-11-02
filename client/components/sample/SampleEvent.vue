<template>
  <button @click="SampleEvent">alertMessage</button>
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

<template>
  <div>
    <button @click="changMessage">ボタン</button>
    <input type="text" v-model="message" />
    <p>{{ $store.state.message }}</p>
    <p>{{ $store.state.count }}</p>

    <button @click="counter">ボタン</button>
    <p>{{ count }}</p>
  </div>
</template>

<script>
export default {
  data() {
    return {
      message: "Changed"
    };
  },
  methods: {
    counter() {
      this.$store.commit("increment");
    },
    changMessage() {
      this.$store.commit("changMessage", this.message);
    }
  },
  computed: {
    count() {
      return this.$store.getters["count"];
    }
  }
};
</script>

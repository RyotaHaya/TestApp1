<template>
  <div>
    xxx
    <p>{{ jsonData }}</p>
  </div>
</template>

<script>
import { mapState, mapGetters, mapMutations, mapActions } from "vuex";

export default {
  data: function() {
    return {
      ss: {}
    };
  },
  created() {
    this.$store.dispatch("nuxtServerInit");
  },

  methods: {
    ...mapActions({ jsonData: "getItems" })
  },
  computed: {
    ...mapGetters({
      jsonData: "getItems"
    })
  }
};
</script>

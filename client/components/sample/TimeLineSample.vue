<!-- pages/posts.vue -->

<template>
  <!-- <v-main>
    <v-container>
      <v-row>
        <v-list>
          <v-list-item v-for="(tweet, i) in this.tweetList" :key="i">
            <v-list-item-content>
              <p>tweetId:{{ tweet.Id }}</p>
              <v-list-item-title>{{ article.title }}</v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </v-list>
      </v-row>
    </v-container>
  </v-main> -->
</template>

<script>
import { mapActions, mapState } from 'vuex'

export default {
  name: 'tweet',
  data() {
    return {}
  },
  methods: {
    ...mapActions({
      getList: 'getListTweet',
    }),
  },
  mounted: async function () {
    //this.getList(this.categories)
  },
  computed: {
    ...mapState({
      //tweetList: (state) => state.posts.tweetList,
    }),
  },
}
</script>

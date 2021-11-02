<template>
  <div>
    <div id="lifehack">{{ counter >= 10 ? '10以上' : '10未満です' }}</div>
    <div id="counter">Counter:{{ counter }}</div>
    <div id="bind-attribute">
      ddd
      <input v-bind:type="type" />
    </div>
    <div v-if="disp">
      <button v-on:click="increaseCouter">increaseCouter</button>
      <button @click="increaseCouter">increaseCouter</button>
    </div>

    <div>
      <p v-html="html"></p>
    </div>
    <div><a v-bind:href="myTwitterUrl">link</a></div>
    <div><a v-bind:[attributeName]="myTwitterUrl">link2</a></div>

    <dir>
      <button v-on:[attributeName]="alertMessage">ddd</button>
      <p v-once>{{ message }}</p>
    </dir>

    <dir>
      <input v-model="message" type="text" placeholder="入力してください" />
      <p>{{ message }}</p>
    </dir>
    <dir>{{ filterOneMediaTweet }}</dir>
  </div>
</template>
<script>
import Button from './Button.vue'
export default {
  components: { Button },
  data() {
    return {
      counter: 0,
      type: 'text',
      message: 'nervchange',
      html: '<p>HtmlVon</p>',
      disp: true,
      myTwitterUrl: 'https://twitter.com/watorin72',
      attributeName: 'click',
      eventName: 'alertMessage',
      jsonData: {
        UserId: '',
        TotalCount: 2,
        ImageTweetList: [
          {
            ID: 1434900252004290564,
            DateTime: '2021-09-06 15:24:13',
            MediaUrls: ['http://pbs.twimg.com/media/E-nKI5KVgAgTa0c.jpg'],
          },
          {
            ID: 1434899781403308033,
            DateTime: '2021-09-06 15:22:21',
            MediaUrls: [
              'http://pbs.twimg.com/media/E-nJuVrVgAEKv8c.jpg',
              'http://pbs.twimg.com/media/E-nJuVrVEAoyus-.jpg',
            ],
          },
        ],
      },
    }
  },
  beforeCreate() {
    console.log('beforeCreate')
    console.log('counter is: ' + this.counter)
    //console.log('DOM counter is ' + Document.getElementById('lifehack'))
  },
  created() {
    console.log('created')
    console.log('counter is: ' + this.counter)
    //console.log('DOM counter is ' + Document.getElementById('lifehack'))
  },
  beforeMount() {
    console.log('beforeMount')
    //const dom = Document.getElementById('lifehack')
  },
  // マウント(要素が置き換わる)後に実行される
  mounted() {
    console.log('mounted')
    //alert('counter is ' + this.counter)
    // vueでは直接DOMを参照できない
    //const dom = Document.getElementById('lifehack')
  },
  methods: {
    increaseCouter() {
      this.counter++
    },
    alertMessage() {
      alert('hello')
    },
  },
  computed: {
    filterOneMediaTweet() {
      return this.jsonData.ImageTweetList.length > 10 ? 'HasTweet' : 'NoTweet'
    },
  },
}
</script>

<template>
  <div>
    <ul width="1300" height="1000">
      <button @click="fetchUserTimeLine">fetchUserTimeLine</button>

      <ul class="category-list">
        <ul v-for="tweet in tweets" :key="tweet.ID">
          <ul v-for="mediaUrl of tweet.MediaUrls" key="index">
            <a v-bind:href="mediaUrl">
              <img :src="mediaUrl + '?format=jpg&name=thumb'" alt=""
            /></a>
          </ul>
        </ul>
      </ul>
    </ul>
  </div>
</template>
<script>
export default {
  data() {
    return {
      tweets: [],
      thumbnails: [
        { id: 1, src: "https://placehold.jp/300x300.png" },
        {
          id: 2,
          src: "https://placehold.jp/3d4070/fffff/300x300.png"
        },
        {
          id: 3,
          src: "https://placehold.jp/placehold.jp/b32020/fffff/300x300.png"
        }
      ]
    };
  },
  methods: {
    async fetchUserTimeLine() {
      // this.$config.apiURL + '/api/GetListTimeLineImages'
      // /GetListTimeLineImages
      await this.$axios
        .get(this.$config.apiURL + "/api/GetListTimeLineImages", {
          params: {
            // ここにクエリパラメータを指定する
            listId: "1304418413037498368",
            maxCount: 30,
            include_rts: true
          }
        })
        .then(response => {
          this.tweets = response.data["ImageTweetList"];
          //console.log(response.data)

          response.data.ImageTweetList.forEach(element => {
            //console.log(element.ID)
            const id = element.ID;
            const imagesEl = element.Url;
            const imagesArray = [];

            for (let i = 0; i < imagesEl.length; i++) {
              console.log(imagesEl[i]);
              imagesArray.push({
                id: String(i) + "_" + id,
                src: imagesEl[i]
              });
            }

            // this.tweets.push({
            //   userId: element.UseID,
            //   id: element.ID,
            //   urls: imagesEl,
            //   DateTime: element.DateTime,
            // })
          });
        })
        .catch(err => {
          //リクエスト失敗時
          //alert('request ffe')
        });
    }
  },
  beforeCreate: function() {
    //alert('request aa')
    console.log("before request success");
    this.fetchUserTimeLine();
  }
};
</script>
<style></style>

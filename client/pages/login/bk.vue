<template>
  <div>
    <header class="aaaa">
      <!-- <TimeLine /> -->
      <TwitterLogin />
      <TimeLineSample />
      <div class="header-base">
        <h1>
          <a
            class="
              text-white text-sm
              font-bold
              leading-relaxed
              inline-block
              mr-4
              py-2
              whitespace-no-wrap
            "
            href="/"
          >
            <Logo />
          </a>
          <div style="display: inline">
            <HeaderSearch />
          </div>
        </h1>
      </div>
      <SampleEvent />
    </header>

    <body>
      <div id="app">
        <!-- 
        <div class="selectable-box active" v-for="(imageUrl,index) in imageUrls">
            <img :src="imageUrl">
        </div>
      </div> -->
      </div>
      <Button />
      <ul class="images">
        <ImageCard />
        <ImageCard />
        <ImageCard />
        <ImageCard />
        <ImageCard />
        <ImageCard />
        <ImageCard />
        <ImageCard />
      </ul>
    </body>

    <footer class="bg-black pb-10 pt-10">
      <p
        class="
          text-center text-white text-sm
          font-bold
          leading-relaxed
          whitespace-no-wrap
          uppercase
        "
      >
        Copyright © 2021 NUXT PictCafe DEMO
      </p>
    </footer>
  </div>
</template>

<script>
// nuxtはcompnentsから自動で探しに行くため記載不要
// import Logo from '../components/Logo.vue'

// export default {
//   components: { Logo },}

export default {
  head() {
    // このページ向けにメタタグを設定します
  },
  data: function() {
    return {
      object: {
        name: "aaaa"
      }
    };
  },
  methods: {
    fetch: function() {
      getJson();
    }
  }
};

function getJson() {
  alert("aaaa");
}
</script>

<style>
.container {
  margin: 0 auto;
  min-height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  text-align: center;
}

.header-base {
  display: inline;
}

.title {
  font-family: "Quicksand", "Source Sans Pro", -apple-system, BlinkMacSystemFont,
    "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
  display: block;
  font-weight: 300;
  font-size: 100px;
  color: #35495e;
  letter-spacing: 1px;
}

.subtitle {
  font-weight: 300;
  font-size: 42px;
  color: #526488;
  word-spacing: 5px;
  padding-bottom: 15px;
}

.links {
  padding-top: 15px;
}

ul {
  display: flex;
  flex-wrap: wrap;
  list-style: none;
  margin: 0;
  padding: 0;
}
li {
  width: 21%;
  margin: 2%;
  height: 180px;
  line-height: 180px;
  background: #efe3e3;
  text-align: center;
}
</style>

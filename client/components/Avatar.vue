<template>
  <a v-bind:href="profile.twitterUrl">
    <v-avatar class="hidden-sm-and-down,mt-n12 mx-auto" color="white" size="48">
      <img
        v-bind:src="profile.iconUrl"
        alt="avatarImage"
        class="avatar-image"/></v-avatar
  ></a>
</template>

<script>
export default {
  data() {
    return {
      profile: {
        twitterUrl: "https://twitter.com/watorin72",
        iconUrl:
          "https://pbs.twimg.com/profile_images/1385570746680762372/APGtAaMN.jpg",
        defalutIcon: "~/assets/twitter-logo-icon"
      }
    };
  }
};
</script>

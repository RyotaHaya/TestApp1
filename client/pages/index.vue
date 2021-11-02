<template>
  <v-app id="inspire">
    {{ currentTabId }}
    <v-main class="pt-2 pt-md-0">
      <div>
        <Header />
      </div>
      <v-main class="pt-2 pt-md-0" app>
        <!-- v-content要素の中のコンテンツはサイドメニューの動作に連動します -->
        <v-tabs v-model="tab" flex color="grey darken-1">
          <v-tabs-slider color="blue"></v-tabs-slider>
          <v-tab
            v-for="list in userList"
            :key="list.id"
            @click="changeTab(list.name)"
          >
            {{ list.name }}
          </v-tab>

          <v-tab-item v-for="listId in listIdArray" :key="listId">
            <v-container>
              <div class="pt-2 pt-md-8">
                <ImageList v-bind:dispListId="listId" />
              </div>
            </v-container>
          </v-tab-item>
        </v-tabs>
      </v-main>
      <v-container>
        <!-- <div class="pt-2 pt-md-8"><ImageList /></div> -->
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
export default {
  data() {
    return {
      currentTabId: "aaa",
      tab: null,
      title: "Vuetify.js",
      text:
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.",
      links: ["home", "list1"],
      listIdArray: ["1280477992594993153", "1304418413037498368"],
      sampleArry: [{ id: "dddd", name: "dfdfdfdf" }],
      userList: []
    };
  },
  methods: {
    changeTab: function(tabId) {
      this.currentTabId = tabId;
    }
  },
  created: function() {
    console.log(this.sampleArry[0].name);
    this.listIdArray.forEach(element => {
      const listId = element;
      const listName = "MyList1";
      const item = { id: listId, name: listName };
      this.userList.push(item);
    });
  }
};
</script>

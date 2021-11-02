// // import axios from "axios";

// // export const state = () => ({
// //   counter: 0,
// //   cnt: 1000,
// //   items: []
// // });

// // export const mutations = {
// //   increment(state) {
// //     state.counter++;
// //   },
// //   setItems(state, items) {
// //     state.items = items;
// //   }
// // };

// // export const actions = {
// //   async nuxtServerInit({ commit }) {
// //     console.log("nuxtServerInit is called.");

// //     const { data } = axios.get(
// //       "http://localhost:5042/api/GetListTimeLineImages",
// //       {
// //         params: {
// //           listId: "1304418413037498368",
// //           maxCount: 3
// //         },
// //         withCredentials: false
// //       }
// //     );
// //     commit("setItems", data);

// //     state.cnt = 10;
// //     console.log("nuxtServerInit is called.");
// //     // if (req.user) {
// //     //   commit('user', req.session.user)
// //     // }
// //   }
// // };

// // export const getters = {
// //   getItems: state => state.items
// // };

// import Vue from "vue";
// import Vuex from "vuex";
// import createPersistedState from "vuex-persistedstate";

// export default new Vuex.Store({
//   state: {},
//   mutations: {},
//   actions: {},
//   getters: {},
//   plugins: [createPersistedState(
//       { // ストレージのキーを指定
//         key: 'appName',
//         // ストレージの種類を指定
//         storage: window.sessionStorage
//       }
//   )]

const initialState = {
  username: "",
  loggedIn: false
};

export const state = () => ({
  state: initialState,
  message: "   ",
  count: 0,
  tweets: []
});

export const mutations = {
  increment(state) {
    state.count += 2;
  },
  changMessage(state, message) {
    state.message = message;
  },
  storeTweets(state, tweets) {
    state.tweets = tweets;
  }
};

export const getters = {
  count: state => {
    return state.count;
  },
  tweets: state => {
    //const aa = sessionStorage.getItem("my-key");
    return state.tweets;
  }
};

// // export default new Vuex.Store({
// //   // ストアをモジュールに分けている場合。vuexのモジュールを指定
// //   // modules: {
// //   //   auth,
// //   //   master
// //   // },

// //   // `createPersistedState()`でインスタンス作成。引数に設定を書く
// //   plugins: [
// //     createPersistedState({
// //       // ストレージのキーを指定。デフォルトではvuex
// //       //key: "anyGreatApp",
// //       // 管理対象のステートを指定。pathsを書かない時は`modules`に書いたモジュールに含まれるステート全て。`[]`の時はどれも保存されない
// //       //paths: [""],
// //       // ストレージの種類を指定する。デフォルトではローカルストレージ
// //       //storage: window.sessionStorage
// //     })
// //   ]

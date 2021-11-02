import createPersistedState from "vuex-persistedstate";

export default ({ store }) => {
  window.onNuxtReady(() => {
    createPersistedState({
      key: "my-key",
      paths: ["message", "count", "tweets"],
      storage: window.sessionStorage
    })(store);
  });
};

import colors from "vuetify/es5/util/colors";

export default {
  publicRuntimeConfig: {
    baseURL: process.env.BASE_URL || "http://locahost:3000",
    apiURL: process.env.API_URL || "http://localhost:5042"
    // 本番環境用
    //baseURL: process.env.BASE_URL || 'http://locahost:3000',
    //apiURL: process.env.API_URL || 'http://localhost:5042',
  },
  privateRuntimeConfig: {
    secret: process.env.SECRET_KEY
  },
  server: {
    host: "0.0.0.0"
  },

  // Global page headers: https://go.nuxtjs.dev/config-head
  head: {
    titleTemplate: "%s",
    title: "PictCafe",
    htmlAttrs: {
      lang: "en"
    },
    meta: [
      { charset: "utf-8" },
      { name: "viewport", content: "width=device-width, initial-scale=1" },
      { hid: "description", name: "description", content: "" },
      { name: "format-detection", content: "telephone=no" }
    ],
    link: [{ rel: "icon", type: "image/x-icon", href: "/favicon.ico" }]
  },

  // Global CSS: https://go.nuxtjs.dev/config-css
  css: [],

  // Plugins to run before rendering page: https://go.nuxtjs.dev/config-plugins
  plugins: [
    { src: "~/plugins/infiniteloading", ssr: false },
    { src: "~/plugins/vuex-persist", ssr: false }
  ],

  // Auto import components: https://go.nuxtjs.dev/config-components
  components: true,

  // Modules for dev and build (recommended): https://go.nuxtjs.dev/config-modules
  buildModules: [
    // https://go.nuxtjs.dev/vuetify
    "@nuxtjs/vuetify"
  ],

  // Modules: https://go.nuxtjs.dev/config-modules
  modules: [
    "@nuxtjs/axios",
    "@nuxtjs/proxy",
    "@nuxtjs/component-cache",
    ["@nuxtjs/component-cache", { maxAge: 1000 * 60 * 60 }]
    // {
    //   max: 10000,
    //   maxAge: 1000 * 60 * 60
    // }
  ],

  // Vuetify module configuration: https://go.nuxtjs.dev/config-vuetify
  vuetify: {
    customVariables: ["~/assets/variables.scss"],
    theme: {
      dark: false,
      themes: {
        dark: {
          primary: colors.blue.darken2,
          accent: colors.grey.darken3,
          secondary: colors.amber.darken3,
          info: colors.teal.lighten1,
          warning: colors.amber.base,
          error: colors.deepOrange.accent4,
          success: colors.green.accent3
        },
        /*以下追加*/
        light: {
          primary: colors.blue.darken2,
          accent: colors.grey.darken3,
          secondary: colors.amber.darken3,
          info: colors.teal.lighten1,
          warning: colors.amber.base,
          error: colors.deepOrange.accent4,
          success: colors.green.accent3
        }
      }
    }
  },

  // Build Configuration: https://go.nuxtjs.dev/config-build
  build: {
    extend(config, ctx) {
      // Run ESLint on save
      if (ctx.isDev && ctx.isClient) {
        config.devtool = "inline-cheap-module-source-map";
      }
    }
  },
  proxy: {
    "/api/": {
      //target: 'http://localhost:5042/api/',
      //本番環境用
      target: "http://api:5042",
      changeOrigin: true,
      secure: false
    }
  },
  axios: {
    proxy: true,
    prefix: "/api"
  }
};

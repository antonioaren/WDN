// https://nuxt.com/docs/api/configuration/nuxt-config

import path from "path";

export default defineNuxtConfig({
    ssr: true,
    devtools: { enabled: true },
    alias: {
        "@": path.resolve(__dirname),
        "~": path.resolve(__dirname),
        assets: path.resolve(__dirname, "assets"),
        public: path.resolve(__dirname, "public"),
    },
    vite: {
        css: {
            preprocessorOptions: {
                scss: {
                    additionalData: `
                            @import "@/assets/styles/settings/colors.scss";
                            @import "@/assets/styles/settings/global.scss";
                            @import "@/assets/styles/settings/fonts.scss";
                            @import "@/assets/styles/breakpoints.scss";
                        `,
                },
            },
        },
    },
    app: {
        head: {
            title: "WDN-templates",
            htmlAttrs: {
                lang: "en",
            },
            meta: [
                { charset: "utf-8" },
                {
                    name: "viewport",
                    content: "width=device-width,initial-scale=1",
                },
                { hid: "description", name: "description", content: "" },
                { name: "format-detection", content: "telephone=no" },
            ],
            link: [{ rel: "icon", type: "image/x-icon", href: "/favicon.ico" }],
        },
    },
});
<template>
  <h1>{{ title }}</h1>
  <div v-html="content"></div>
  <div v-if="blocks.length">
    <div v-for="block in blocks">
      <Blocks :block="block"/>
    </div>
  </div>
</template>

<script lang="ts">
import Blocks from "~/components/reusable/Blocks.vue";

export default {

  data() {
    return {
      title: "Holi",
      content: null,
      blocks: []
    }
  },
  components: {
    Blocks
  },
  setup() {

  },
  beforeMount() {
    // TODO: Needs to be on server side otherwise it will load on the client.
    fetch('http://localhost:8000/api/v2/pages/?type=website.HomePage&fields=title,body,blocks')
        .then(async (res) => {
          if (res.ok) {
            const response = await res.json();
            const {title, body, blocks} = response.items[0]
            this.title = title;
            this.content = body;
            this.blocks = blocks;
          }
        })
        .catch((error) => {
          throw new Error(`Error conexion server: ${error}`)
        })
  }
}

</script>
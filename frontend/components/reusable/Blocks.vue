<template>
  <div v-if="block.value.type=BlocksEnum.BANNER">
    <Banner :block="block.value"/>
  </div>
</template>

<script lang="ts">
import { BlocksEnum } from "~/Enums/blocks.enum";
import Banner from "~/components/blocks/Banner.vue";

export default {
  name: "Blocks",
  components: {
    Banner
  },
  computed: {
    BlocksEnum() {
      return BlocksEnum
    }
  },
  props: {
    "block": {
      require: true
    }
  },
  mounted() {
    console.log(this.block)
  }
}
</script>
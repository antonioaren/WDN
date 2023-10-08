<template>
  <h2>{{ block.title }}</h2>
  <div v-html="block.description"></div>
  <CTAButton
      :link="block.cta.link"
      :text="block.cta.text"
      :isExternalLink=block.cta.isExternalLink
  />
</template>

<script lang="ts">
import CTAButton from "~/components/reusable/CTAButton.vue";

export default {
  name: "Banner",
  components: {
    CTAButton
  },
  props: {
    "block": {
      required: true
    }
  }
}
</script>
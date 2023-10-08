<template>
  <div class="br-cta-component">
    <a class="br-cta-component-link" :href="link">
      <div class="br-cta-component-text">
          {{ text }}
      </div>
    </a>
  </div>
</template>

<script lang="ts">
export default {
  props: {
    "link": {
      type: String,
      required: false
    },
    "text": {
      type: String,
      required: false,
    },
    "isExternalLink": {
      type: Boolean,
      required: false,
    }
  },

}

</script>

<style lang="scss" scoped>

.br-cta-component {
  max-width: 120px;
  width: 100%;
  border-radius: 50px;
  border: 1px solid black;
  text-align: center;
  background-color: white;
  transition: all .5s ease-out;

  &:hover {
    background-color: black;
    .br-cta-component-text {
      color: white
    }
  }

  &-link {
    padding: 30px;
  }
}

</style>
<template>
  <v-dialog v-model="isActive" v-bind="$attrs">
    <slot></slot>
  </v-dialog>
</template>

<script>
export default {
  name: "Modal",
  props: {
    name: {type: String, required: true}
  },
  computed: {
    isActive: {
      get() {
        return this.$store.getters['modals/allOpen'].includes(this.name)
      },
      set(val) {
        if (val) this.$store.dispatch('modals/open', this.name)
        else this.$store.dispatch('modals/close', this.name)
      }
    }
  },
  methods: {
    close() {
      this.$store.dispatch("modals/close", this.name)
    }
  },
  beforeDestroy() {
    if (this.isActive) this.close()
  }
}
</script>

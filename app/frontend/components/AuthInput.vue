<template>
  <div class="d-flex flex-column wrapper">
    {{ title }}
    <div class="input-wrapper ">
      <input v-model="content" class="input rounded-lg"
             :type="(icon || !isPassword) ? 'text' : (icon||isEmail) ? 'email':'password'"/>
      <v-btn class="hide-button" v-if="isPassword" icon @click='icon=!icon'>
        <v-icon>{{ icon ? 'mdi-eye-outline' : 'mdi-eye-off-outline' }}</v-icon>
      </v-btn>
    </div>
  </div>
</template>

<script>
export default {
  name: "AuthInput",

  props: {

    isPassword: {
      type: Boolean,
      default: false,
    },
    isEmail: {
      type: Boolean,
      default: false,
    },
    title: {
      type: String,
      required: true,
    },
    value: {}
  },
  data() {
    return {
      icon: false
    }
  },
  computed: {
    content: {
      get() {
        return this.value
      },
      set(val) {
        this.$emit('input', val)
      }
    }
  },
  methods: {}
  // {
  //   handleInput(e) {
  //     this.$emit('input', this.content)
  //   }
  // },
}
</script>

<style scoped>
.error-outline {
  border-bottom: 1px solid red;
}

.wrapper {
  padding: 0 21px;
  font-size: 18px
}

.input {
  height: 30px;
  width: 100%;
  background: rgba(142, 142, 142, 0.3);
  border-radius: 6px;
  padding-left: 10px;
  color: #fff;
}

input:focus {
  outline: none;
}

.input-wrapper {
  position: relative;

}

.hide-button {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  right: 0;
}
</style>

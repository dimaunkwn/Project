<template>
  <div class="d-flex justify-center">
    <v-row class="no-gutters header pa-4 ">
      <v-col cols="12" md="2" class="d-flex align-center pl-5">
        <img class="logo" alt="logo" src="/img/BAYSEE.svg"/>
      </v-col>
      <v-col cols="12" offset-md="1" md="8" lg="5" class="d-flex align-center justify-center">
        <input type="text" placeholder="Search"/>
        <v-btn class="ml-2" icon>
          <img class="magnify " alt="logo" src="/img/magnify.svg"/>
        </v-btn>
      </v-col>
      <v-col v-if="$vuetify.breakpoint.lgAndUp" cols="12" md="4" class="d-flex header--buttons align-center justify-center">
        <v-btn color="secondary">Setting</v-btn>
        <v-btn color="secondary">Lobby</v-btn>
        <v-btn @click="openAuthDialog()" color="secondary">Login</v-btn>
        <v-btn @click="openAuthDialog()" color="primary">Sign Up</v-btn>
      </v-col>
    </v-row>
  </div>
</template>

<script>
export default {
  name: "Navbar",
  methods: {
    openAuthDialog() {
      this.$store.dispatch('modals/open', 'auth')
    }
  }
}
</script>

<style scoped lang="scss">
.header {
  background-color: #283851;
  max-width: 1520px;

  &--buttons {
    gap: 12px;
  }
}

input {
  height: 42px;
  width: 100%;
  background: rgba(142, 142, 142, 0.3);
  border-radius: 6px;
  padding-left: 10px;
}

input:focus {
  outline: none;
}

input::placeholder {
  color: #D0D0D0;

}

.magnify {
  height: 30px;
  width: 30px;
}
</style>

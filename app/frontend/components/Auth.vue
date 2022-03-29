<template>

  <modal name="auth" max-width="456">
    <v-card class="d-flex flex-column justify-center " color="#2B2D37">
      <div class="d-flex align-center justify-center logo-wrapper">
        <img height="35px" class="logo" alt="logo" src="/img/BAYSEE.svg"/>
      </div>
      <v-toolbar color="#2B2D37" flat>
        <template>
          <v-tabs height="42px" color="white" centered>
            <v-tab style="font-size:18px;">Login</v-tab>
            <v-tab style="font-size:18px;">Sign up</v-tab>

          </v-tabs>
        </template>
      </v-toolbar>

      <form @submit.prevent="checkData()" class="d-flex justify-center flex-column">
        <auth-input v-model="username" class="mb-8" title="Username"/>
        <auth-input v-model='password' class="mb-8" :is-password="true" title="Password"/>
        <auth-input v-model='confirm_password' class="mb-8" :is-password="true"
                    title="Confirm password"/>
        <birthday-input v-model="date" class="mb-8"/>
        <auth-input v-model="email" class="mb-8" :is-email="true" title="Email"/>
        <div class="button rounded-lg">
          <input
            type="submit"
            value="Sign Up"
          />
        </div>
      </form>
    </v-card>
  </modal>
</template>

<script>


export default {
  name: "RegistrationDialog",
  data() {
    return {
      username: '',
      email: '',
      password: '',
      confirm_password: '',
      date: {
        day: '',
        month: '',
        year: ''
      },

      validDate: false,
      validUsername: false,
      validEmail: false,
      isDataChecked: false,
    }
  },


  methods: {
    checkData() {
      let today = new Date()
      let regExDate = /^(?:(?:31(\/|-|\.)(?:0?[13578]|1[02]))\1|(?:(?:29|30)(\/|-|\.)(?:0?[13-9]|1[0-2])\2))(?:(?:1[6-9]|[2-9]\d)?\d{2})$|^(?:29(\/|-|\.)0?2\3(?:(?:(?:1[6-9]|[2-9]\d)?(?:0[48]|[2468][048]|[13579][26])|(?:(?:16|[2468][048]|[3579][26])00))))$|^(?:0?[1-9]|1\d|2[0-8])(\/|-|\.)(?:(?:0?[1-9])|(?:1[0-2]))\4(?:(?:1[6-9]|[2-9]\d)?\d{2})$/;
      let regExName = /^(\w|\d){5,20}$/;
      let regExEmail =
        /^(?!.*@.*@.*$)(?!.*@.*--.*\..*$)(?!.*@.*-\..*$)(?!.*@.*-$)(.*@.+(\..{1,11})?)$/;
      let date = new Date(this.date.year, this.date.month, this.date.day);
      // let regExPhone = /\(?([0-9]{3})\)?([ .-]?)([0-9]{3})\2([0-9]{4})/;
      if ((today - date) / 1000 / 60 / 60 / 24 / 365.25 >= 8) {
        this.validDate = regExDate.test(this.date.day + '/' + this.date.month + '/' + this.date.year);
      } else {
        this.validDate = false
      }
      this.validEmail = regExEmail.test(this.email);
      this.validUsername = regExName.test(this.username);

      this.isDataChecked = true;
    },
  },
}
</script>

<style scoped>


input {
  font-size: 24px;
}

.logo-wrapper {
  padding: 21px 0 15px 0;
}

.logo {
  width: 143px;
}

.button {
  background-color: #235FC0;
  display: flex;
  align-items: center;
  justify-content: center;
  height: 56px;
  margin: 15px 38px 15px 38px;
}

.auth-wrapper {
  max-width: 456px;
}
</style>

<template>
  <div class="d-flex flex-column wrapper">
    Day of Birth
    <div class="input-wrapper d-flex flex-row">
      <div class="input-wrapper--day pr-6">
        Day
        <input v-model="content.day" class="input rounded-lg"/>
      </div>
      <div class="input-wrapper--month">
        Month
        <select v-model="content.month">
          <option value="" disabled selected hidden></option>
          <option :value="month.count" label="" v-for="(month,i) in months" :key="i">{{ month.name }}</option>
        </select>
      </div>
      <div class="input-wrapper--year pl-6">
        Year
        <input v-model="content.year" class="input rounded-lg"/>
      </div>

    </div>
  </div>
</template>

<script>
export default {
  props: {
    value: {
      type: Object
    }
  },
  name: "BirthdayInput",
  data() {
    return {

      months: [
        {
          count: 1,
          name: 'January'
        },
        {
          count: 2,
          name: 'February'
        },
        {
          count: 3,
          name: 'March'
        },
        {
          count: 4,
          name: 'April'
        },
        {
          count: 5,
          name: 'May'
        },
        {
          count: 6,
          name: 'June'
        },
        {
          count: 7,
          name: 'July'
        },
        {
          count: 8,
          name: 'August'
        },
        {
          count: 9,
          name: 'September'
        },
        {
          count: 10,
          name: 'October'
        },
        {
          count: 11,
          name: 'November'
        },
        {
          count: 12,
          name: 'December'
        },

      ]
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
}
</script>


<style lang="scss" scoped>
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

select {
  height: 30px;
  width: 100%;
  background: rgba(142, 142, 142, 0.3);
  border-radius: 6px;
  padding-left: 10px;
  color: white
}

select option {
  background-color: #2B2D37
}

select:focus {
  outline: none;
}

input:focus {
  outline: none;
}

.input-wrapper {
  font-size: 18px;

  &--day {
    display: flex;
    flex-direction: column;
    width: 160px;

  }

  &--year {
    display: flex;
    flex-direction: column;
    width: 160px;
  }

  &--month {
    display: flex;
    flex-direction: column;
    width: 100%;
  }
}


</style>

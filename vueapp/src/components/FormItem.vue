<template lang="pug">
  form(@submit="submit")
    .form-body.shadow
      InputItem(
        v-for="(item, index) in itemsData.concat([''])"
        :styles="styles ? styles(item) : null"
        :name="name"
        :items="itemsData"
        :index="index"
        :key="index"
      )

    BaseButton(
      :class="btnClass"
      type.native="submit"
    )
      | Save {{ saveName }}
</template>

<script>
import BaseButton from './BaseButton.vue'
import InputItem from './InputItem.vue'

export default {
  name: 'FormItem',
  props: {
    items: {
      type: Array,
      required: true,
    },
    styles: {
      type: Function,
      required: false,
    },
    name: {
      type: String,
      required: true,
    },
    saveName: {
      type: String,
      required: true,
    },
    url: {
      type: String,
      required: true,
    },
  },
  data() {
    return {
      itemsData: this.items,
      btnClass: '',
    }
  },
  components: {
    BaseButton,
    InputItem,
  },
  methods: {
    submit(e) {
      e.preventDefault();
      this.$http.post(this.url, {items: this.itemsData.filter(item => item !== null)})
        .then(response => {
          this.itemsData = response.data.data;
          this.tempClass('success');
        })
        .catch(error => {
          console.error(error);
          this.tempClass('error');
        })
    },
    tempClass(cls) {
      this.btnClass = cls;
      setTimeout(() => {
        this.btnClass = ''
      }, 1000)
    },
  },
}
</script>

<style scoped lang="stylus">
.form-body
  border-radius 3px
  display flex
  flex-direction column
  margin-block-end 20px
</style>
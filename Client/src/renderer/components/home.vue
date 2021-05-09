<template>
  <div class="home">
    <img src="../assets/images/bg.jpg" round @click="GoToPredict()" class="image"/>
  </div>
</template>

<script>
export default {
  methods: {
    GoToPredict() {
      this.$router.push("./predict");
    },
  },
};
</script>

<style scoped>
* {
  margin: 0;
  padding: 0;
}
.home {
  background-color: #ffffff;
  width: 100%;
  height: 100%;
}
.image{
  width: 100%;
  height: 100%;
}
</style>
<template>
  <el-container>
    <div class="result">
      <div v-if="channel == 0" class="imgContainer">
        <img src="../assets/images/1.png" alt="可回收" class="img"/>
      </div>
      <div v-else-if="channel == 1" class="imgContainer">
        <img src="../assets/images/2.png" alt="其他垃圾不可回收" class="img"/>
      </div>
      <div v-else-if="channel == 2" class="imgContainer">
        <img src="../assets/images/3.png" alt="厨余垃圾" class="img"/>
      </div>
      <div v-else class="imgContainer">
        <img src="../assets/images/4.png" alt="有害垃圾" class="img"/>
      </div>
      <div class="btnContainer">
        <el-button type="success" round @click="GoToPredict()">再次识别</el-button>
      </div>
    </div>
  </el-container>
</template>

<script>
var self;
export default {
  data() {
    return {
      src:
        "https://cube.elemecdn.com/6/94/4d3ea53c084bad6931a56d5158a48jpeg.jpeg",
      channel: "",
    };
  },
  created: function () {
    this.channel = this.$route.params.channel;
    var channel = this.channel;
    self = this;
  },
  methods: {
    GoToHome() {
      this.$router.push("./");
    },
    GoToPredict() {
      this.$router.push("./predict");
    },
  },
};
</script>

<style>
* {
  margin: 0;
  padding: 0;
}
.result {
	background-color: #FFFFFF;
  width: 100%;
  height: 100%;
  position: relative;
}
.imgContainer{
  width: 70%;
  height: 70%;
  position: relative;
  left: 50%;
  transform: translateX(-50%);
}
.img{
  height: 70%;
  width: 70%;
}
.btnContainer{
  position: absolute;
  bottom: 50%;
  transform: translateY(-50%);
  right: 20%;
  z-index: 999;
}
</style>

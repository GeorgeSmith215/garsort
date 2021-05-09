<template>
  <div class="predict">
    <div class="imageContainer">
      <img src="http://127.0.0.1:5000/video_img_url" class="image" />
    </div>
    <div class="buttonContainer">
        <el-button type="primary" round @click="takeAPhotho()" icon="el-icon-camera">拍照</el-button>
      <div class="homeBtn">
        <el-button type="primary" round @click="GoToHome()" icon="el-icon-home">回到首页</el-button>
      </div>
    </div>
  </div>
</template>

<script>
var self;
export default {
  data() {
    return {
      src:
        "https://likecy.oss-cn-beijing.aliyuncs.com/0194a25dcd1b46a8012053c074fa37.jpg@2o_1574846777533.jpg",
    };
  },
  created: function () {
    self = this;
  },
  methods: {
    GoToResult() {
      this.$router.push("./result");
    },
    GoToHome() {
      this.$router.push("./");
    },
    takeAPhotho() {
      this.$http
        .get("http://127.0.0.1:5000/take_photo", {})
        .then(function (res) {
          self.deltailDataFromServers(res.data);
          console.log(res);
        })
        .catch(function (error) {
          console.log(error);
        });
    },
    deltailDataFromServers(data) {
      var result = data.split("/");
      switch (result[0]) {
        case "可回收物":
          self.$router.push({ name: "result", params: { channel: 0 } });
          break;
        case "其他垃圾":
          self.$router.push({
            name: "result",
            params: {
              channel: 1,
            },
          });
          break;
        case "厨余垃圾":
          self.$router.push({
            name: "result",
            params: {
              channel: 2,
            },
          });
          break;
        case "有害垃圾":
          self.$router.push({
            name: "result",
            params: {
              channel: 3,
            },
          });
          break;
      }
    },
  },
};
</script>

<style>
* {
  margin: 0;
  padding: 0;
}
.predict {
  background-color: #ffffff;
  width: 100%;
  height: 100%;
  position: relative;
}
.imageContainer{
  width: 80%;
  position: relative;
  left: 50%;
  transform: translateX(-50%);
}
.image {
  width: 80%;
}

.buttonContainer{
  position: absolute;
  bottom: 20%;
  right: 10%;
}
.homeBtn{
  padding-top: 3rem;
}
</style>

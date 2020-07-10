<template>
  <div>

      <el-row style="margin-top:8px;" :gutter="8">
          <el-col :span="8">
            <el-row >
                <div class="block" :style="{height:(height)+'px'}"  style="overflow-x:hide;overflow:auto;">
                  <el-col :span="24" class="col-xs-3 areainfotype">
                      <div class="energy-icon" style="float: left;">
                        <!-- <span class="el-icon-info" style="font-size: 30px" aria-hidden="true"></span> -->
                        <a class="sub-title" style="font-size: 20px">匹配度</a>
                      </div>
                  </el-col>

                  <el-col :span="24" class="col-xs-9" style="margin-top: 20px">
                      <div class="banyuan" @click="openItem" style="cursor:pointer">
                        <div class="banyuan1">
                          <span ref="baifen" style="font-size: 26px;margin: 30px 0 0 40px;position: absolute;">96.7%</span>
                        </div>
                      </div>
                  </el-col>
                  <el-col :span="24" class="col-xs-9" style="margin-top: 20px">
                      <div class="banyuan" @click="openItem1" style="cursor:pointer">
                        <div class="banyuan1">
                          <span ref="baifen1" style="font-size: 26px;margin: 30px 0 0 40px;position: absolute;">96.1%</span>
                        </div>
                      </div>
                  </el-col>
                  <el-col :span="24" class="col-xs-9" style="margin-top: 20px">
                      <div class="banyuan" @click="openItem2" style="cursor:pointer">
                        <div class="banyuan1">
                          <span ref="baifen2" style="font-size: 26px;margin: 30px 0 0 40px;position: absolute;">95.8%</span>
                        </div>
                      </div>
                  </el-col>
                  <el-col :span="24" class="col-xs-9" style="margin-top: 20px">
                      <div class="banyuan" @click="openItem3" style="cursor:pointer">
                        <div class="banyuan1">
                          <span ref="baifen3" style="font-size: 26px;margin: 30px 0 0 40px;position: absolute;">91.7%</span>
                        </div>
                      </div>
                  </el-col>
                  <el-col :span="24" class="col-xs-9" style="margin-top: 20px">
                      <div class="banyuan" @click="openItem4" style="cursor:pointer">
                        <div class="banyuan1">
                          <span ref="baifen4" style="font-size: 26px;margin: 30px 0 0 40px;position: absolute;">91.0%</span>
                        </div>
                      </div>
                  </el-col>
                </div>
            </el-row>
          </el-col>
          <el-col :span="8">
            <el-row >
                <div class="block" :style="{height:(height1)+'px'}">
                  <el-col :span="24" class="col-xs-3 areainfotype" style="margin-bottom: 20px">
                      <div class="energy-icon" style="float: left;">
                        <!-- <span class="el-icon-info" style="font-size: 30px" aria-hidden="true"></span> -->
                        <a class="sub-title" style="font-size: 20px">工艺运行参数</a>
                      </div>
                  </el-col>

                  <el-row class="row">
                    <!-- <el-col :span="6">&nbsp;</el-col> -->
                    <el-col :span="8" class="col-xs-9" style="margin-left: 20%">
                        <el-row class="row" style="margin-left: 12%">
                            <div class="yuan">
                              <h4>缺氧段ORP</h4>
                              <p style="font-size: 20px">{{description.orp}}</p>
                              <span>mv</span>
                            </div>
                        </el-row>
                    </el-col>
                    <el-col :span="8" class="col-xs-9">
                        <el-row class="row">
                            <div class="yuan">
                              <h4>好氧段DO</h4>
                              <p style="font-size: 20px">{{description.hyddo}}</p>
                              <span>mg/L</span>
                            </div>
                        </el-row>
                    </el-col>
                  </el-row>
                  <el-row class="row">
                    <el-col :span="8" class="col-xs-9">
                        <el-row class="row" style="margin-left: 28%">
                            <div class="yuan">
                              <h4>好氧段MLSS</h4>
                              <p style="font-size: 20px">{{description.mlss}}</p>
                              <span>mg/L</span>
                            </div>
                        </el-row>
                    </el-col>
                    <el-col :span="8" class="col-xs-9">
                        <el-row class="row" style="margin-left: 15%">
                            <div class="yuan">
                              <h4>污泥回流比</h4>
                              <p style="font-size: 20px">{{description.wnhlb}}</p>
                              <span>%</span>
                            </div>
                        </el-row>
                    </el-col>
                    <el-col :span="8" class="col-xs-9">
                        <el-row class="row">
                            <div class="yuan">
                              <h4>内回流比</h4>
                              <p style="font-size: 20px">{{description.nhlb}}</p>
                              <span>%</span>
                            </div>
                        </el-row>
                    </el-col>
                  </el-row>
                </div>
            </el-row>

            <el-row style="margin-top: 10px">
                <div class="block" :style="{height:(height1)+'px'}">
                  <el-col :span="24" class="col-xs-3 areainfotype" style="margin-bottom: 25px">
                      <div class="energy-icon" style="float: left;">
                        <!-- <span class="el-icon-info" style="font-size: 30px" aria-hidden="true"></span> -->
                        <a class="sub-title" style="font-size: 20px">HRT</a>
                      </div>
                  </el-col>

                  <el-row class="row" style="margin: 90px 0 0 35px">
                    <el-col :span="8" class="col-xs-9">
                        <el-row class="row">
                            <div class="sanjiao"></div>
                            <div class="sanjiao1"></div>
                            <div style="position: relative;">
                              <p style="margin:-50px 0px 0px 63px "><span style="font-size: 20px">2</span>h</p>
                              <h4 style="margin:0px 0px 0px 53px ">厌氧段</h4>
                            </div>
                        </el-row>
                    </el-col>
                    <el-col :span="8" class="col-xs-9">
                      <el-row class="row">
                          <div class="daosanjiao"></div>
                          <div class="daosanjiao1"></div>
                          <div style="position: relative;">
                            <h4 style="margin:-75px 0px 0px 53px ">缺氧段</h4>
                            <p style="margin:0px 0px 0px 63px "><span style="font-size: 20px">2</span>h</p>
                          </div>
                      </el-row>
                  </el-col>
                    <el-col :span="8" class="col-xs-9">
                        <el-row class="row">
                            <div class="sanjiao"></div>
                            <div class="sanjiao1"></div>
                            <div style="position: relative;">
                              <p style="margin:-50px 0px 0px 63px "><span style="font-size: 20px">9</span>h</p>
                              <h4 style="margin:0px 0px 0px 53px ">好氧段</h4>
                            </div>
                        </el-row>
                    </el-col>
                  </el-row>
                </div>
            </el-row>

          </el-col>

          <el-col :span="8">
            <el-row >
                <div class="block" :style="{height:(height)+'px'}"  style="overflow-x:hide;overflow:auto;">
                  <el-col :span="24" class="col-xs-3 areainfotype">
                      <div class="energy-icon" style="float: left;">
                        <!-- <span class="el-icon-info" style="font-size: 30px" aria-hidden="true"></span> -->
                        <a class="sub-title" style="font-size: 20px">预期出水水质</a>
                      </div>
                  </el-col>

                  <el-col :span="24" class="col-xs-9">
                      <el-row class="row">
                          <div class="imgsty">
                            <h4 class="cod">COD</h4>
                            <p class="cod1">{{description.cod}}</p>
                            <span class="cod2">mg/L</span>
                          </div>
                          <div class="imgsty">
                            <h4 class="cod">NH3-N</h4>
                            <p class="cod1">{{description.nh3n}}</p>
                            <span class="cod2">mg/L</span>
                          </div>
                          <div class="imgsty">
                            <h4 class="cod">SS</h4>
                            <p class="cod1">{{description.ss}}</p>
                            <span class="cod2">mg/L</span>
                          </div>
                          <div class="imgsty">
                            <h4 class="cod">TN</h4>
                            <p class="cod1">{{description.tn}}</p>
                            <span class="cod2">mg/L</span>
                          </div>
                          <div class="imgsty">
                            <h4 class="cod">TP</h4>
                            <p class="cod1">{{description.tp}}</p>
                            <span class="cod2">mg/L</span>
                          </div>
                      </el-row>
                  </el-col>
                  <!-- <el-col :span="12" class="col-xs-9">
                      <el-row class="row">
                          <div class="sanjiao"></div>
                          <div class="sanjiao1"></div>
                          <div style="position: relative;">
                            <h4 style="margin:-50px 0px 0px 63px ">9h</h4>
                            <p style="margin:0px 0px 0px 53px ">好氧段</p>
                          </div>
                      </el-row>
                  </el-col> -->

                </div>
            </el-row>
          </el-col>

      </el-row>

  </div>
</template>

<script>

export default {
  name: 'input-query',
  components: {},
  props:['sidid'],
  watch:{},
  data () {
    return {
      height: 100,
      height1:0,
      alarmtypeId:0,
      warningPoints: [],
      total:0,
      loading:false,
      description:'',
      countermeasure:'',
      cause:'',
      interpretation:'',
      allItems:[],
      type:0,
      type1:0,
      input:'',
      input1:[],
      answer:'',
      countermeasures:[],
      radio:'1',
    }
  },
  mounted:function(){
    this.openItem();

    this.height = $(window).height() - 150;
    this.height = this.height < 250 ? 250 : this.height;

    this.height1 = ($(window).height() - 170) / 2;
  },
  methods:{
    openItem:function(){
      this.$refs.baifen.style.color="#18bbbd";
      this.$refs.baifen1.style.color="#cee1e1";
      this.$refs.baifen2.style.color="#cee1e1";
      this.$refs.baifen3.style.color="#cee1e1";
      this.$refs.baifen4.style.color="#cee1e1";
      var str1 = {};
      str1 = window.str;
      this.$http.post(baseEnergyPath+"/rest/expertest/getTechnologyGuidanceInfoById",str1).then(function(data){

            this.description = data.body.data;

            console.log(data.body);

            this.loading = false;
        },function(err){
            this.loading = false;
        });

    },
    openItem1:function(){
      this.$refs.baifen1.style.color="#18bbbd";
      this.$refs.baifen.style.color="#cee1e1";
      this.$refs.baifen2.style.color="#cee1e1";
      this.$refs.baifen3.style.color="#cee1e1";
      this.$refs.baifen4.style.color="#cee1e1";
      this.$http.post(baseEnergyPath+"/rest/expertest/getTechnologyGuidanceInfoById",{id:2}).then(function(data){

            this.description = data.body.data;

            console.log(data.body);

            this.loading = false;
        },function(err){
            this.loading = false;
        });
    },
    openItem2:function(){
      this.$refs.baifen2.style.color="#18bbbd";
      this.$refs.baifen1.style.color="#cee1e1";
      this.$refs.baifen.style.color="#cee1e1";
      this.$refs.baifen3.style.color="#cee1e1";
      this.$refs.baifen4.style.color="#cee1e1";
      this.$http.post(baseEnergyPath+"/rest/expertest/getTechnologyGuidanceInfoById",{id:3}).then(function(data){

            this.description = data.body.data;

            console.log(data.body);

            this.loading = false;
        },function(err){
            this.loading = false;
        });
    },
    openItem3:function(){
      this.$refs.baifen3.style.color="#18bbbd";
      this.$refs.baifen1.style.color="#cee1e1";
      this.$refs.baifen2.style.color="#cee1e1";
      this.$refs.baifen.style.color="#cee1e1";
      this.$refs.baifen4.style.color="#cee1e1";
      this.$http.post(baseEnergyPath+"/rest/expertest/getTechnologyGuidanceInfoById",{id:4}).then(function(data){

            this.description = data.body.data;

            console.log(data.body);

            this.loading = false;
        },function(err){
            this.loading = false;
        });
    },
    openItem4:function(){
      this.$refs.baifen4.style.color="#18bbbd";
      this.$refs.baifen1.style.color="#cee1e1";
      this.$refs.baifen2.style.color="#cee1e1";
      this.$refs.baifen3.style.color="#cee1e1";
      this.$refs.baifen.style.color="#cee1e1";
      this.$http.post(baseEnergyPath+"/rest/expertest/getTechnologyGuidanceInfoById",{id:5}).then(function(data){

            this.description = data.body.data;

            console.log(data.body);

            this.loading = false;
        },function(err){
            this.loading = false;
        });
    },




  }
}
</script>

<style scoped>
.el-table {
  font-size:12px !important;
}

.el-collapse {
  border-top: none !important;
}

.yuan {
    width: 110px;
    height: 110px;
    border: 10px solid #47dcfd;
    box-sizing: border-box;
    border-radius: 50%;
    text-align: center;
    padding-top: 18px;
    color: #43d4fe;
}

.sanjiao {
    position: relative;
    width: 0;
    height: 0;
    top: 18px;
    left: 0px;
    border-left: 70px solid transparent;
    border-right: 70px solid transparent;
    border-bottom: 120px solid #47dcfd;
}

.sanjiao1 {
    position: absolute;
    width: 0px;
    height: 0px;
    top: 42px;
    left: 25px;
    border-left: 45px solid transparent;
    border-right: 45px solid transparent;
    border-bottom: 85px solid #125667;
}

.daosanjiao {
    position: relative;
    width: 0;
    height: 0;
    top: 18px;
    left: 0px;
    border-left: 70px solid transparent;
    border-right: 70px solid transparent;
    border-top: 120px solid #47dcfd;
}

.daosanjiao1 {
    position: absolute;
    width: 0px;
    height: 0px;
    top: 30px;
    left: 26px;
    border-left: 45px solid transparent;
    border-right: 45px solid transparent;
    border-top: 85px solid #125667;
}

.imgsty {
    height: 120px;
    width: 70%;
    background-image: url(../../static/images/bjs.png);
    background-size: 100% 100%;
    margin-left: 15%;
    margin-bottom: 25px;
    position: relative;
}

.cod {
    position: absolute;
    margin: 43px 0 0 25px;
    font-size: 18px;
}
.cod1 {
    position: absolute;
    margin: 70px 0 0 205px;
    /*text-decoration: underline;*/
    font-size: 20px;
}
.cod2 {
    position: absolute;
    margin: 74px 0 0 270px;
    font-size: 16px;
}

.banyuan {
    width: 200px;
    height: 100px;
    border: 10px solid #47dcfd;
    /*background-color: #47dcfd;*/
    /*border-radius:110px 110px 0 0;*/
    border-radius: 50% 50% 0 0/100% 100% 0 0;
    /*border-bottom: 1px solid;*/
    margin-left: 30%;
} 

.banyuan1 {
    width: 151px;
    height: 75px;
    border: 5px solid #47dcfd;
    border-radius: 50% 50% 0 0/100% 100% 0 0;
    border-bottom: none;
    margin: 15px 0 0 22px;
    position: relative;
}
 
</style>

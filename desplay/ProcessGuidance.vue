<template>
  <div style="overflow:hidden">

      <el-row style="margin-top:8px;" :gutter="8">
           <el-col :xs="24" :sm="24" :md="24" :lg="24" :xl="24">
            <el-row >
              <div class="block" :style="{height:(height)+'px'}" style="background-image: url(../../static/images/gongyi.jpg) ; background-size: 100% 100%;">
                <el-col :xs="16" :sm="16" :md="16" :lg="16" :xl="16" class="col-xs-9" style="margin-left: 50px">
                  <!-- <el-row class="row">
                    <div>季节类型</div>
                  </el-row> -->
                    <el-row class="row">

                        <el-col :xs="14" :sm="14" :md="14" :lg="14" :xl="14"  style="margin-top: 105px;">
                          <div style="margin-left: 30%;font-size: 22px">季节类型</div>
                          <div class="btn" v-for="(item,k) in allItems" :key="k" >
                              <div style="cursor:pointer" ref="changebtn" class="spbtn" v-model="season" @click="btns(item,k)">{{item.label}}</div>
                          </div> 
                        </el-col>
                    </el-row>
                    <el-row class="row">
                      <el-col :xs="10" :sm="10" :md="10" :lg="10" :xl="10">
                          <div style="margin-left: 40%;font-size: 22px">工业水比例</div>
                          <div class="btn1" v-for="(items,index) in proportions" v-model="flog" :key="index" >
                              <div style="cursor:pointer" ref="changebtn1" class="spbtn"  @click="clicBtn(items,index)">{{items.label}}</div>
                          </div>  
                        </el-col>
                    </el-row>

                    <el-row class="row">

                      <div style="margin-left: 17%;font-size: 22px;margin-bottom: 10px">运行参数</div>

                      <el-col :xs="3" :sm="3" :md="3" :lg="3" :xl="3" style="margin: 0 10px 0 1%">
                          <div>
                              <el-tag style="margin-left: 29%">污泥浓度</el-tag>
                              <el-input v-model="input1">
                                <template slot="append"><div style="color: #fff">mg/L</div></template>
                              </el-input>

                          </div> 
                      </el-col>
                      <el-col :xs="3" :sm="3" :md="3" :lg="3" :xl="3" style="margin-right: 10px">
                          <div >
                            <el-tag style="margin-left: 25%">好氧段DO</el-tag>
                              <el-input v-model="input2">
                                <template slot="append"><div style="color: #fff">mg/L</div></template>
                              </el-input>

                          </div> 
                      </el-col>
                      <el-col :xs="3" :sm="3" :md="3" :lg="3" :xl="3">
                          <div >
                            <el-tag style="margin-left: 31%">进水水量</el-tag>
                              <el-input v-model="input3">
                                <template slot="append"><div style="color: #fff">m³/d</div></template>
                              </el-input>

                          </div> 
                      </el-col>
                    </el-row>
                </el-col>

                <el-col :xs="7" :sm="7" :md="7" :lg="7" :xl="7" class="col-xs-9">
                  <el-row class="row">
                      <el-col :span="20">
                          <div style="margin-left: 25%;font-size: 22px;margin-top: 115px">水质指标</div>
                          <div class="inp">
                            <el-input v-model="input4">
                              <template slot="prepend" style="width: 34px"><div style="color: #fff">COD</div></template>
                              <template slot="append"><div style="color: #fff">mg/L</div></template>
                            </el-input>
                          </div>
                          <div class="inps">
                            <el-input v-model="input5">
                              <template slot="prepend" style="width: 34px"><div style="color: #fff">BOD</div></template>
                              <template slot="append"><div style="color: #fff">mg/L</div></template>
                            </el-input>
                          </div>
                          <div class="inps">
                            <el-input v-model="input6">
                              <template slot="prepend" style="width: 34px"><div style="color: #fff">&nbsp;氨氮</div></template>
                              <template slot="append"><div style="color: #fff">mg/L</div></template>
                            </el-input>
                          </div>
                          <div class="inps">
                            <el-input v-model="input7">
                              <template slot="prepend" style="width: 34px"><div style="color: #fff">&nbsp;&nbsp;SS&nbsp;</div></template>
                              <template slot="append"><div style="color: #fff">mg/L</div></template>
                            </el-input>
                          </div>
                          <div class="inps">
                            <el-input v-model="input8">
                              <template slot="prepend" style="width: 34px"><div style="color: #fff">&nbsp;&nbsp;TN&nbsp;</div></template>
                              <template slot="append"><div style="color: #fff">mg/L</div></template>
                            </el-input>
                          </div>
                          <div class="inps">
                            <el-input v-model="input9">
                              <template slot="prepend" style="width: 34px"><div style="color: #fff">&nbsp;&nbsp;TP&nbsp;</div></template>
                              <template slot="append"><div style="color: #fff">mg/L</div></template>
                            </el-input>
                          </div>
                      </el-col>
                    </el-row>
                </el-col>

                <div style="margin-left: 43%;margin-top: 40%">
                  <router-link :to="{path:'input-query',params:{areaSIDid:109}}">
                    <el-button type="primary" >实时数据查询</el-button>
                  </router-link>
                  <router-link :to="{path:'input-query',params:{areaSIDid:109}}"><el-button type="primary" @click="checkOut">手动输入查询</el-button></router-link>
                    <!-- <a href="/#/cascade/13/input-query?areaSIDid=109">手动输入查询</a> -->
                </div>
                
              </div>
            </el-row>
          </el-col>
      </el-row>

  </div>
</template>

<script>

export default {
  name: 'process-guidance',
  components: {},
  props:['sidid'],
  watch:{
      'sidid':function(val,oldVal) {
          this.searchForm.sidid = val;
          console.log("devicegroup : "+this.searchForm.sidid);
          this.loadAlarmPointList();
      }
  },
  data () {
    return {
      height: 100,
      alarmtypeId:0,
      warningPoints: [],
      deviceDialog:false,
      searchForm:{
          procstatus:'',
          alarmcontent:'',
          searchParameter:'',
          pageNum:1,
          pageSize:10
      },
      total:0,
      loading:false,
      description:'',
      countermeasure:'',
      cause:'',
      interpretation:'',
      allItems:[
        {label:'春',value:'0'},
        {label:'夏',value:'1'},
        {label:'秋',value:'2'},
        {label:'冬',value:'3'}
      ],
      proportions:[
        {label:'>40%',value:'0'},
        {label:'<40%',value:'1'}
      ],
      type:0,
      type1:0,
      input:'',
      radio3:'上海',
      input1:5061,
      input2:1.9,
      input3:32698.1,
      input4:254,
      input5:75.5,
      input6:24.03,
      input7:190,
      input8:39.34,
      input9:5.43,
      season:'0',
      flog:'0',
      k1:0,
      k2:0,
    }
  },
  mounted:function(){
    // this.loadExpertDecisionInfoById();

    this.height = $(window).height() - 140;
    this.height = this.height < 250 ? 250 : this.height;
  },
  methods:{
    btns:function(item,k){
      console.log(item,k);
      this.season = item.value;
      this.$refs.changebtn[this.k1].style.background="#1b88ab";
      this.k1 = k;
      this.$refs.changebtn[k].style.background="#18bbbd";
    },
    clicBtn:function(items,index){
      console.log(items,index);
      this.flog = items.value;
      this.$refs.changebtn1[this.k2].style.background="#1b88ab";
      this.k2 = index;
      this.$refs.changebtn1[index].style.background="#18bbbd";
    },
    checkOut:function(){
      window.str={};
      window.str.id = 1;
      window.str.season = this.season;
      window.str.flog = this.flog;
      window.str.wnnd = this.input1;
      window.str.hyddo = this.input2;
      window.str.jssl = this.input3;
      window.str.cod = this.input4;
      window.str.bod = this.input5;
      window.str.ad = this.input6;
      window.str.ss = this.input7;
      window.str.tn = this.input8;
      window.str.tp = this.input9;
      // this.$http.post(baseEnergyPath+"/rest/expertest/getTechnologyGuidanceInfoById",{id:1,season:this.season,flog:this.flog,wnnd:this.input1,hyddo:this.input2,jssl:this.input3,cod:this.input4,bod:this.input5,ad:this.input6,ss:this.input7,tn:this.input8,tp:this.input9}).then(function(data){

      //       // this.description = data.body.data;

      //       // console.log(data.body);

      //       this.loading = false;
      //   },function(err){
      //       this.loading = false;
      //   });
    }

  }
}
</script>


<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.el-table {
  font-size:12px !important;
}

.el-collapse {
  border-top: none !important;
}

.inp {
  margin: 15px 0 0 100px;
}
.inps {
  margin: 30px 0 0 100px;
}

.container{
    margin: 0 auto; 
    padding-top: 30px; 
    width: 600px;
}
.btn{
    width: 100px;
    height: 100px;
    float: left;
    margin: 10px 0 15px 3%;
    border-radius: 100px;
    background: #1b88ab;
    position: relative;
}
.spbtn {
    position: absolute;
    font-size: 16px;
    width: 100px;
    line-height: 100px;
    text-align: center;
    border-radius: 100px;
    background: #1b88ab;
}
.btn1 {
    width: 100px;
    height: 100px;
    float: left;
    margin: 10px 0 15px 20%;
    border-radius: 100px;
    background: #1b88ab;
    position: relative;
}


</style>

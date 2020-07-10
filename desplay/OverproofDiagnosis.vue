<template>
  <div>

      <el-row style="margin-top:8px;" :gutter="8">
          <el-col :xs="8" :sm="8" :md="8" :lg="8" :xl="8">
            <el-row >
                <div class="block" :style="{height:(height)+'px'}" style="overflow-x:hide;overflow:auto;">
                  <el-col :span="10" class="col-xs-3 areainfotype">
                      <div class="energy-icon" style="float: left;">
                        <!-- <span class="el-icon-info" style="font-size: 30px" aria-hidden="true"></span> -->
                        <p class="sub-title" style="font-size: 20px">诊断对象</p>
                      </div>
                  </el-col>

                  <el-col :xs="24" :sm="24" :md="24" :lg="24" :xl="24" class="col-xs-9">
                      <el-row class="row">
                          <div v-for="(item,k) in allItems" :key="k" class="btn">
                            <div style="cursor:pointer" @click="openItem(item,k)" id="field" ref="changebtn" class="spbtn">{{item.title}}
                            <span class="shadow">{{item.title}}</span>
                            </div>
                          </div>


                          <div class="water"></div>
                      </el-row>
                  </el-col>
                </div>
            </el-row>
          </el-col>
          <el-col :xs="16" :sm="16" :md="16" :lg="16" :xl="16">
            <el-row >
              <div class="block" :style="{height:(height)+'px'}" style="overflow-x:hide;overflow:auto;padding: 0 20px" id="relheight">
                <el-col :span="24" v-for="(items,index) in countermeasures" class="col-xs-9">
                    <el-row v-if="items.content != '是' && items.content != '否'"  class="row">
                        <el-col :span="24"  style="margin-top: 30px">
                            <div class="robot" style="float: left;margin: 10px -10px 0 3px;">设备</div>
<!--                          <img src="../../static/images/robot1.png" >-->
                          <div class="innerDiv" style="float: left;margin:17px 0 0 20px"></div>
                          <div class="el-dialog">
                            <p style="margin-left: 10px;">{{items.content}}</p>

                            <div v-if="items.leafflog != '1'" style="float: right;margin: 0 10px 6px 0">
                              <el-button style="width: 70px;border-radius: 5px" type="primary" size="mini" @click="isOk(items,index,'1')">是</el-button>
                              <el-button style="width: 70px;border-radius: 5px" type="primary" size="mini" v-if="items.emflog == '0'" @click="isNo(items,index,'0')">否</el-button>
                            </div>

                          </div>
                        </el-col>
                    </el-row>

                    <el-row v-if="items.content == '是' || items.content == '否'" class="row" >
                        <el-col :span="24" class="col-xs-6 norightpadding">
                          <div class="custom" style="float: right; margin: 5px 3px 0 -10px;">我</div>
<!--                          <img src="../../static/images/custom1.png">-->
                          <div class="innerDivr" style="float: right;margin:15px 20px 0px 0px"></div>
                          <div class="el-dialogr" style="float: right;">&nbsp;&nbsp;{{items.content}}</div>
                        </el-col>
                    </el-row>
                </el-col>
                <!-- <div style="position: absolute;left:0;bottom:0;width: 50%">
                  <el-input v-model="input" placeholder="请输入内容" style="float: left;" v-on:keyup.13.native="upDate(input)">
                    <el-button @click="upDate(input)" style="float: left;">确定</el-button>
                  </el-input>

                </div> -->
              </div>
            </el-row>
          </el-col>
      </el-row>

  </div>
</template>

<script>

export default {
  name: 'overproof-diagnosis',
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
      allItems:[],
      type:0,
      type1:0,
      input:'',
      input1:[],
      answer:'',
      countermeasures:[],
      radio:'1',
      pId:0,
      leafFlog:'',
      flog:'',
      title:'',
      k1:0,
    }
  },
  mounted:function(){
    this.getExperInfo();
    this.height = $(window).height() - 150;
    this.height = this.height < 250 ? 250 : this.height;
  },
  methods:{

    getExperInfo:function(){
      this.$http.post(baseEnergyPath+"/rest/expertest/getExperInfo",{}).then(function(data){

            this.allItems = data.body.rows;
            // console.log(data.body);

            this.loading = false;
        },function(err){
            this.loading = false;
        });
    },

    openItem:function(item,k){
      console.log(item,k);

      this.$refs.changebtn[this.k1].className="spbtn";
      // this.$refs.changebtn[this.k1].style.fontSize="25px";
      // this.$refs.changebtn[this.k1].style.width="130px";
      // this.$refs.changebtn[this.k1].style.height="130px";
      // this.$refs.changebtn[this.k1].style.textAlign="center";
      this.k1 = k;
      this.$refs.changebtn[k].className="is-selected";
      // this.$refs.changebtn[k].style.fontSize="30px";
      // this.$refs.changebtn[k].style.width="140px";
      // this.$refs.changebtn[k].style.height="140px";
      // this.$refs.changebtn[k].style.textAlign="center";


      this.title = item.title;
      this.countermeasures = [];
      this.$http.post(baseEnergyPath+"/rest/expertest/getEquipGroupList",{pid:0,title:this.title}).then(function(data){

            this.description = data.body.data;
            this.countermeasures.push(this.description);
            console.log(data.body);

            this.loading = false;
        },function(err){
            this.loading = false;
        });
    },


    isOk:function(items,index,num){
      console.log(items,index,num);
      if(this.flog != num && this.pId != items.id || this.flog == num && this.pId != items.id || this.flog != num && this.pId == items.id){
          this.pId = items.id;
          var isTrue = {};
          if(num == '1'){
            this.flog = num;
            isTrue.content = '是';
          }else if(num == '0'){
            this.flog = num;
            isTrue.content = '否';
          }

          this.countermeasures.push(isTrue);
          console.log(this.countermeasures);

          // this.openItem()
          this.$http.post(baseEnergyPath+"/rest/expertest/getEquipGroupList",{pid:this.pId,title:this.title,flog:this.flog}).then(function(data){

              this.description = data.body.data;
              this.countermeasures.push(this.description);
              console.log(data.body);
              this.$nextTick(() => {
                var container = document.getElementById("relheight");
                  container.scrollTop = container.scrollHeight;
                  console.log(container.scrollTop);
               })

              this.loading = false;
          },function(err){
              this.loading = false;
          });



          this.countermeasures[index+1].flog = num;
          console.log(this.countermeasures[index+1].flog);
          for(var i=1;i<this.countermeasures.length;i++){
            if(0<index || index<this.countermeasures.length){
              this.countermeasures = this.countermeasures.slice(0, index+2);
              // this.countermeasures[index+1].ans = '否';
              if(this.countermeasures[index+1].flog == '1'){
                this.countermeasures[index+1].content = '是';
              }else{
                this.countermeasures[index+1].content = '否';
              }
              console.log(this.countermeasures);
            }
          }

          return;
      }


    },
    isNo:function(items,index,num){
      console.log(items,index,num);
      if(this.flog != num && this.pId != items.id || this.flog == num && this.pId != items.id || this.flog != num && this.pId == items.id){
        this.pId = items.id;
        var isTrue = {};
        if(num == '1'){
          this.flog = num;
          isTrue.content = '是';
        }else if(num == '0'){
          this.flog = num;
          isTrue.content = '否';
        }
        this.countermeasures.push(isTrue);

        console.log(this.countermeasures);

        // this.openItem()
        this.$http.post(baseEnergyPath+"/rest/expertest/getEquipGroupList",{pid:this.pId,title:this.title,flog:this.flog}).then(function(data){

              this.description = data.body.data;
              this.countermeasures.push(this.description);
              console.log(data.body);
              this.$nextTick(() => {
                var container = document.getElementById("relheight");
                  container.scrollTop = container.scrollHeight;
                  console.log(container.scrollTop);
               })

              this.loading = false;
          },function(err){
              this.loading = false;
          });

        this.countermeasures[index+1].flog = num;
        console.log(this.countermeasures[index+1].flog);
        for(var i=1;i<this.countermeasures.length;i++){
          if(0<index || index<this.countermeasures.length){
            this.countermeasures = this.countermeasures.slice(0, index+2);
            if(this.countermeasures[index+1].flog == '1'){
              this.countermeasures[index+1].content = '是';
            }else{
              this.countermeasures[index+1].content = '否';
            }
            console.log(this.countermeasures);
          }
        }
        return;
      }
    },
    upDate:function(input){
      console.log(input);
      this.type1 = 2;
      if(input != ''){
        this.input1.push(input);
        // this.openItem();
        this.input = '';
      }else{
        this.$message({
            type: 'warning',
            message: '请输入内容！'
        });
      }

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

.el-dialog {
    float: left;
    /*border: 1px solid rgb(77, 172, 199);*/
    font-size: 18px;
    line-height: 35px;
    width: 50%;
    /*margin-left: 20px;*/
    background:rgba(16,28,77,.5);
    border-radius:8px;
    border:1px solid rgba(84,118,255,.5);
    margin-bottom: 30px;
    margin-top: 10px;
}

.el-dialogr {
    /*border: 1px solid rgb(77, 172, 199);*/
    font-size: 18px;
    line-height: 35px;
    width: 30%;
    /*margin-right: 20px;*/
    background:rgba(16,28,77,.5);
    border-radius:8px;
    border:1px solid rgba(84,118,255,.5);
    margin-bottom: 25px;
    margin-top: 10px;
}


.innerDiv{
    /*margin-left:-9px;*/
    z-index:-1;
    width:0;
    height:0;
    border-top:10px solid transparent;
    border-bottom:10px solid transparent;
    border-right:10px solid rgba(16,28,77,.5);
}

.innerDivr{
    /*margin-left:-9px;*/
    z-index:-1;
    width:0;
    height:0;
    border-top:10px solid transparent;
    border-bottom:10px solid transparent;
    border-left:10px solid rgba(16,28,77,.5);
}

.btn {
    width: 128px;
    height: 128px;
    float: left;
    margin: 35px 28px 44px 10%;
    /*border-radius: 50%;*/
    /*background: #1b88ab;*/
    position: relative;
}

/*.spbtn:hover {
    background: #18bbbd;
}
*/

.spbtn {
    position: absolute;
    font-size: 22px;
    width: 128px;
    height: 128px;
    padding: 16px;
    /* line-height: 128px; */
    overflow: hidden;
    text-align: left;
    background-color: rgba(84,118,255,.2);
    border-radius: 17px;
}
.spbtn .shadow {
    font-size: 44px;
    color: rgba(255,255,255,.1);
    position: absolute;
    bottom: -17px;
    right: -11px;
    white-space: nowrap;
}
.is-selected {
    position: absolute;
    left:-20%;
    top:-20%;
    font-size: 50px;
    width: 180px;
    height: 180px;
    padding: 16px;
    /* line-height: 128px; */
    overflow: hidden;
    text-align: left;
    border-radius:30px;
    background: rgb(0,211,255); /* Old browsers */
    background: -moz-linear-gradient(top,  rgba(0,211,255,0.6) 0%, rgba(0,235,255,0.6) 100%); /* FF3.6-15 */
    background: -webkit-linear-gradient(top,  rgba(0,211,255,0.6) 0%,rgba(0,235,255,0.6) 100%); /* Chrome10-25,Safari5.1-6 */
    background: linear-gradient(to bottom,  rgba(0,211,255,0.6) 0%,rgba(0,235,255,0.6) 100%); /* W3C, IE10+, FF16+, Chrome26+, Opera12+, Safari7+ */
    filter: progid:DXImageTransform.Microsoft.gradient( startColorstr='#00d3ff', endColorstr='#00ebff',GradientType=0 ); /* IE6-9 */

}
.is-selected .shadow {
    font-size: 100px;
    color: rgba(255,255,255,.1);
    position: absolute;
    bottom: -55px;
    right: -25px;
    white-space: nowrap;
}
.robot{
    line-height: 56px;
    width: 56px;
    color:#fff;
    background-color:rgba(84,118,255,.2);
    border-radius:12px;
    text-align: center;

}
.custom {
    text-align: center;
    line-height: 56px;
    width: 56px;
    color:#fff;
    box-shadow:0 6px 11px 0 rgba(0,58,70,0.38);
    border-radius:12px;
    background: rgb(0,211,255); /* Old browsers */
    background: -moz-linear-gradient(top,  rgba(0,211,255,0.6) 0%, rgba(0,235,255,0.6) 100%); /* FF3.6-15 */
    background: -webkit-linear-gradient(top,  rgba(0,211,255,0.6) 0%,rgba(0,235,255,0.6) 100%); /* Chrome10-25,Safari5.1-6 */
    background: linear-gradient(to bottom,  rgba(0,211,255,0.6) 0%,rgba(0,235,255,0.6) 100%); /* W3C, IE10+, FF16+, Chrome26+, Opera12+, Safari7+ */
    filter: progid:DXImageTransform.Microsoft.gradient( startColorstr='#00d3ff', endColorstr='#00ebff',GradientType=0 ); /* IE6-9 */

}
.water {
    /*width: 130px;
    height: 130px;
    border: 10px solid #47dcfd;
    box-sizing: border-box;
    border-radius: 50%;*/
        /*width: 10em;
        height: 10em;
        border-radius: 80% 0 55% 50% / 55% 0 80% 50%;
        background-color: #1b88ab;
        transform: rotate(-45deg);*/
    }

/**{margin:0;padding:0;}
    body{ background-color: #522350 }*/
    /*.water {
        position: relative;
        width: 200px;
        height: 200px;
        background-color: rgb(118, 218, 255);
        border-radius: 50%;
        margin:200px auto 0;
        overflow: hidden;
    }
    .water:before,.water:after{
           content: "";
           position: absolute;
           width: 400px;
           height: 400px;
           top: 0;
           left: 50%;
           background-color: rgba(255, 255, 255, .4);
           border-radius: 45%;
           transform: translate(-50%, -70%) rotate(0);
           animation: rotate 6s linear infinite;
           z-index: 10;
    }

    .water:after {
           border-radius: 47%;
           background-color: rgba(255, 255, 255, .9);
           transform: translate(-50%, -70%) rotate(0);
           animation: rotate 10s linear -5s infinite;
           z-index: 20;
    }

    @keyframes rotate {
        50% {
            transform: translate(-50%, -70%) rotate(180deg);
        } 100% {
            transform: translate(-50%, -70%) rotate(360deg);
        }
    }*/


</style>

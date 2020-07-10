<template>
  <div style="overflow:hidden">

      <el-row style="margin-top:8px;" :gutter="8">
          <el-col :span="12">
            <el-row >
                <div class="block" :style="{height:(height)+'px'}">
                  <el-col :span="8" class="col-xs-3 areainfotype">
                      <div class="energy-icon" style="float: left;">
                        <span class="el-icon-info" style="font-size: 20px;float: left;" aria-hidden="true"></span>
                        <p class="sub-title" style="font-size: 18px;float: left;margin-left: 10px;color: #606266">现象描述</p>
                      </div>
                      <!-- <div class="sub-title">现象描述</div> -->
                  </el-col>

                  <el-col :span="24" class="col-xs-9">
                    <el-row class="row">
                        <el-col :span="24" class="col-xs-6 norightpadding">
                          <div class="sub-title" style="margin-left: 10px;overflow-x:hide;overflow:auto;height:220px;font-size: 14px;color: #606266">{{this.description}}</div>
                        </el-col>
                    </el-row>
                  </el-col>
                </div>
            </el-row>
          </el-col>
           <el-col :span="12">
            <el-row >
              <div class="block" :style="{height:(height)+'px'}">
                <el-col :span="8" class="col-xs-3 areainfotype">
                    <div class="energy-icon" style="float: left;">
                      <span class="el-icon-edit-outline" style="font-size: 20px;float: left;" aria-hidden="true"></span>
                        <p class="sub-title" style="font-size: 18px;float: left;margin-left: 10px;color: #606266">对策</p>
                    </div>
                    <!-- <div class="sub-title">对策</div> -->
                </el-col>

                <el-col :span="24" class="col-xs-9">
                    <el-row class="row">
                        <el-col :span="24" class="col-xs-6 norightpadding">
                          <div class="sub-title" style="margin-left: 10px;overflow-x:hide;overflow:auto;height:220px;font-size: 14px;color: #606266">{{this.countermeasure}}</div>
                        </el-col>
                    </el-row>
                </el-col>
              </div>
            </el-row>
          </el-col>
      </el-row>
      <el-row style="margin-top:8px;" :gutter="8">
          <el-col :span="12">
            <el-row >
              <div class="block" :style="{height:(height)+'px'}">
                <el-col :span="8" class="col-xs-3 areainfotype">
                    <div class="energy-icon" style="float: left;">
                      <span class="el-icon-question" style="font-size: 20px;float: left;" aria-hidden="true"></span>
                      <p class="sub-title" style="font-size: 18px;float: left;margin-left: 10px;color: #606266">原因分析</p>
                    </div>
                    <!-- <div class="sub-title">原因分析</div> -->
                </el-col>

                <el-col :span="24" class="col-xs-9">
                    <el-row class="row">
                        <el-col :span="24" class="col-xs-6 norightpadding">
                          <div class="sub-title" style="margin-left: 10px;overflow-x:hide;overflow:auto;height:220px;font-size: 14px;color: #606266">{{this.cause}}</div>
                        </el-col>
                    </el-row>
                </el-col>
              </div>
            </el-row>
          </el-col>
           <el-col :span="12">
            <el-row >
              <div class="block" :style="{height:(height)+'px'}">
                <el-col :span="8" class="col-xs-3 areainfotype">
                    <div class="energy-icon" style="float: left;">
                      <span class="el-icon-star-on" style="font-size: 20px;float: left;" aria-hidden="true"></span>
                      <p class="sub-title" style="font-size: 18px;float: left;margin-left: 10px;color: #606266">术语解释</p>
                    </div>
                    <!-- <div class="sub-title">术语解释</div> -->
                </el-col>

                <el-col :span="24" class="col-xs-9">
                    <el-row class="row">
                        <el-col :span="24" class="col-xs-6 norightpadding">
                          <div class="sub-title" style="margin-left: 10px;overflow-x:hide;overflow:auto;height:220px;font-size: 14px;color: #606266">{{this.interpretation}}</div>
                        </el-col>
                    </el-row>
                </el-col>
              </div>
            </el-row>
          </el-col>
      </el-row>

  </div>
</template>

<script>

export default {
  name: 'knowledge-base',
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
      radio:'2',
      alarmtypeId:0,
      alarmtype:'1',
      lineHeight:500,
      active: 0,
      resultParams:{},
      warningPoints: [],
      deviceDialog:false,
      pointDialogTitle:'',
      diagItemTypeList:[],
      getAlarmLevelId:0,

      searchForm:{
          procstatus:'',
          alarmcontent:'',
          searchParameter:'',
          pageNum:1,
          pageSize:10
      },
      total:0,
      loading:false,
      totalNotifications:0,
      selectedRecords:[],
      graphDialog:false,
      levelsAlarm:[],
      alarmChange:false,

      description:'',
      countermeasure:'',
      cause:'',
      interpretation:'',
    }
  },
  mounted:function(){
    // this.loadExpertDecisionInfoById();

    this.height = ($(window).height() - 300) / 2;
    this.height = this.height < 250 ? 250 : this.height;
  },
  methods:{

    // loadExpertDecisionInfoById:function(){
    //     this.loading = true;
    //     // this.alarmtypeId = alarmtypeid;
    //     // console.log(this.alarmtypeId);
    //     this.$http.get(basePath+"/expert/getExpertDecisionInfoById",{params:{leveltwoid:this.leveltwoId,groupid:this.groupId,expertid:this.expertId}}).then(function(data){

    //         this.warningPoints = data.body.data;
    //         this.total = data.body.amountNum;

    //         this.loading = false;
    //     },function(err){
    //         this.loading = false;
    //     });
    // },

    loadExpertDecisionInfoByIds:function(leveltwoid,groupid,id){
        this.loading = true;
        this.leveltwoId = leveltwoid;
        this.groupId = groupid;
        this.expertId = id;
        console.log(groupid);
        console.log(leveltwoid);

        this.$http.get(basePath+"/expert/getExpertDecisionInfoById",{params:{leveltwoid:this.leveltwoId,groupid:this.groupId,expertid:this.expertId}}).then(function(data){

            this.description = data.body.description;
            this.countermeasure = data.body.countermeasure;
            this.cause = data.body.cause;
            this.interpretation = data.body.interpretation;
            console.log(data.body);

            this.loading = false;
        },function(err){
            this.loading = false;
        });
    },

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

</style>

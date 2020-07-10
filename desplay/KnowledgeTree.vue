<template>
    <div>

        <el-row :gutter="4" style="margin-bottom:15px">
          <div class="block" :style="{height:'40px'}">
            <el-col :span="16" style="padding-top: 3px">
              <el-radio-group style="margin-right:50px" size="mini" v-model="radio">
                <el-radio-button v-for="levelNm in expertGroup" :label="levelNm.groupid" @click.native.prevent="onFindLevel(levelNm)">{{levelNm.name}}</el-radio-button>
              </el-radio-group>

              <!-- <el-radio-group size="mini">
                <el-radio-button v-bind:style="{color:levelNm.color}" v-for="levelNm in levelsAlarm"  @click.native.prevent="onFindLevel(levelNm)">{{levelNm.alarmlevelnm}}</el-radio-button>
              </el-radio-group> -->
            </el-col>
            <el-col :span="8">
              <el-input placeholder="请输入搜索关键字" size="mini" v-model="filterText" class="input-with-select">
                  <el-button slot="append" icon="el-icon-search" @click="getExpertQuestionInfoListByName"></el-button>
              </el-input>
            </el-col>
          </div>
        </el-row>
        <el-row :gutter="4" style="margin-bottom:10px">
          <div class="block" :style="{height:'40px'}">
            <el-col :span="24" style="padding-top: 5px">
              <!-- <el-button-group style="margin-right:50px">
                <el-button type="primary" v-for="levelNm1 in expertLevel" size="mini" @click="onFindLevel1(levelNm1)">{{levelNm1.name}}</el-button>
              </el-button-group> -->

              <el-radio-group style="margin-right:50px" size="mini" v-model="radio1">
                <el-radio-button v-for="levelNm1 in expertLevel" :label="levelNm1.leveltwoid" @click.native.prevent="onFindLevel1(levelNm1)">{{levelNm1.name}}</el-radio-button>
              </el-radio-group>
            </el-col>
          </div>
        </el-row>
        <el-container>
            <transition name="el-fade-in">
              <el-aside v-show="showAside" width="200px">
                <div @contextmenu.prevent="treeViewContextMenu" style="margin-top:5px; height: 640px;" >
                <el-tree :data="data" ref="zoneTree" :props="defaultProps" accordion node-key="id" @node-click="handleNodeClick" :highlight-current="true" :expand-on-click-node="true" :filter-node-method="filterNode" >
                  <span class="span-ellipsis" slot-scope="{ node, data }">
                    <span :title="node.label">{{ node.label }}</span>
                  </span>
                </el-tree>
                </div>
            </el-aside>
          </transition>
            <el-main style="margin-left:20px">
                <knowledge-base class="view one" ref="diaggroup"></knowledge-base>
            </el-main>
        </el-container>   
            
    </div>
</template>

<script>

import KnowledgeBase from '@/expertLibrary/KnowledgeBase';
import TreeAlarmBuild from '@/alarm/TreeAlarmBuild'

export default {
    name: 'alarm-tree',
    components: {KnowledgeBase,TreeAlarmBuild},
  data() {
    return {
      data: [],
      defaultProps: {
        children: "children",
        label: "name"
      },
      radio:1,
      radio1:1,
      expertGroup:[],
      expertLevel:[],
      searchForm:{
          publicmark:'0',
          // knowledgetype:0,
          searchParameter:'',
      },
      groupId:'',
      leveltwoId:'',

      loading:false,
      showAside:true,
      systemType:1,
      filterText:'',
    };
  },
  watch: {
      filterText(val) {
        this.$refs.zoneTree.filter(val);
    }
  },
  mounted:function(){
      this.loadSubItems();
      this.getExpertQuestionGroup();
      this.getExpertQuestionLevelTwo();
    },

  methods: {
    handleNodeClick(data) {
      console.log(data);
      // console.log(data.leveltwoid);
      if(data.parentid != 0){
        this.$refs.diaggroup.loadExpertDecisionInfoByIds(data.leveltwoid,data.groupid,data.id);
      }else{
        this.$refs.diaggroup.loadExpertDecisionInfoByIds();
      }
      
      // console.log(data.groupid);
      // console.log(data.leveltwoid);
      // console.log(data.id);
      
    },
    filterNode(value, data) {
      console.log(value);
      console.log(data);
      if (!value) return true;
      return data.name.indexOf(value) !== -1;
    },

    getExpertQuestionInfoListByName:function(){
      var p = this.filterText;
      this.$http.get(basePath+"/expert/getExpertQuestionInfoListByName",{params:{p:p}}).then(function(data){
          this.data = data.body.rows;
          console.log(this.data);
        },function(err){
          console.log(err);
        });
    },

    loadSubItems:function(leveltwoid,groupid){
        // console.log(leveltwoid);
        // console.log(groupid);
        this.leveltwoId = leveltwoid;
        this.groupId = groupid;
        this.$http.get(basePath+"/expert/getExpertQuestionInfoList",{params:{leveltwoid:this.leveltwoId,groupid:this.groupId}}).then(function(data){
          this.data = data.body.rows;
          console.log(this.data);
        },function(err){
          console.log(err);
        });
    },

    treeViewContextMenu:function($event){
      console.log('treeViewContextMenu');
      this.$refs['deviceCtx'].ctxVisible = false;
      this.$refs['deviceCtx'].open($event, null);

      if ($event) $event.preventDefault();

      if ( $event && $event.stopPropagation ){
          $event.stopPropagation(); //因此它支持W3C的stopPropagation()方法
      }else{
          window.event.cancelBubble = true; //否则，我们需要使用IE的方式来取消事件冒泡
      }
      return true;
    },

    getExpertQuestionGroup:function(){
      var req = {};
      req.publicmark = '0';
      this.$http.post(basePath+"/expert/getExpertQuestionGroup",req).then(function(data){

            this.expertGroup = data.body.rows;
            // console.log(this.expertGroup);
            this.groupId = this.expertGroup[0].groupid;
            this.getExpertQuestionLevelTwo(this.groupId);
            // this.loadSubItems(this.groupId);
        },function(err){

        });
    },
    getExpertQuestionLevelTwo:function(groupid){
      // console.log(groupid);
      this.groupId = groupid;
      this.$http.get(basePath+"/expert/getExpertQuestionLevelTwo",{params:{groupid:this.groupId}}).then(function(data){

            this.expertLevel = data.body.rows;
            console.log(this.expertLevel);
            if(this.expertLevel.length != 0){
              this.leveltwoId = this.expertLevel[0].leveltwoid;
              this.loadSubItems(this.leveltwoId,this.groupId);
            }else{
              this.data = [];
            }
            
        },function(err){

        });
    },
    onFindLevel:function(levelNm){
      console.log(levelNm);
      this.groupId = levelNm.groupid;
      // console.log(this.groupId);
      this.getExpertQuestionLevelTwo(this.groupId);
      // this.loadSubItems(this.groupId);
      this.radio = levelNm.groupid;
      this.handleNodeClick(this.data);
    },
    onFindLevel1:function(levelNm1){
      console.log(levelNm1);
      // this.radio = '2';
      this.leveltwoId = levelNm1.leveltwoid;
      this.groupId = levelNm1.groupid;
      this.radio1 = levelNm1.leveltwoid;
      // console.log(this.leveltwoId);
      this.loadSubItems(this.leveltwoId,this.groupId);

    },

  }
};

</script>


<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.is-current {
  background-color: red;
}

.float-button {
  position:absolute;
  top:-10px;
  margin-left: 6px;
  left:180px;
  width:100px;
  height:30px;
  z-index: 1999;

}

.span-ellipsis {
  width: 100%;
  overflow: hidden;
  white-space: nowrap;
  text-overflow: ellipsis;
}
</style>




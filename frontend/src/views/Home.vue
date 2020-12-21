<template>
  <div class="home">
    <h1>Todoリスト</h1>
    <div class="icon">
      <i class="el-icon-circle-plus"></i>
    </div>
    <el-tabs class="tab-zone" v-model="activeName">
      <el-tab-pane v-for="tableData in tableDatas" v-bind:key="tableData.tabName" v-bind:label="tableData.tabName" v-bind:name="tableData.tabName">
        <el-table class="data-table" :data=tableData.data stripe>
          <el-table-column prop="id" label="ID" width="180"></el-table-column>
          <el-table-column prop="name" label="件名" width="180"></el-table-column>
          <el-table-column prop="status" label="状態" width="180"></el-table-column>
          <el-table-column prop="limit" label="期限"></el-table-column>
          <el-table-column align="right" class="el-icon-edit" size="mini">
            <template slot-scope="scope">
              <el-button class="el-icon-edit" size="mini" @click="handleEdit(scope.row)"></el-button>
              <el-button class="el-icon-delete" size="mini" @click="handleDelete(scope.row)"></el-button>
            </template>
          </el-table-column>
        </el-table>
      </el-tab-pane>
    </el-tabs>
  </div>
</template>

<script>
const axios =
  process.env.VUE_APP_REST_SERVER === 'json-mock'
    ? require('axios').create({ baseURL: 'http://localhost:3000' })
    : require('axios').create()
export default {
  name: 'home',
  data () {
    return {
      tableData: [],
      tableDatas: [],
      activeName: 'All'
    }
  },
  mounted () {
    this.updataTableData()
  },
  methods: {
    updataTableData: async function () {
      const response = await axios.get('/api/task')
      this.tableData = response.data
      this.tableDatas.push(
        { tabName: 'All', data: this.tableData },
        { tabName: 'Todo', data: this.tableData.filter(task => task.status === 'Todo') },
        { tabName: 'Doing', data: this.tableData.filter(task => task.status === 'Doing') },
        { tabName: 'Done', data: this.tableData.filter(task => task.status === 'Done') }
      )
    },
    handleEdit (row) {
      console.log('editボタンを押下')
      console.log(JSON.stringify(row))
    },
    handleDelete (row) {
      console.log('deleteボタンを押下')
      console.log(JSON.stringify(row))
      axios.delete('/api/task', { data: JSON.stringify(row) })
      this.updataTableData()
    }

  }
}
</script>

<style scoped>
.data-table {
  margin: auto;
}
.tab-zone {
  width: 60%;
  margin: auto;
  margin-top: 40px;
}
.icon {
  width: 60%;
  margin: auto;
}
.el-icon-circle-plus {
  float: right;
  color: ＃409EFF;
}
</style>

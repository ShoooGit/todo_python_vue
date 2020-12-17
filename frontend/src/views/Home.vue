<template>
  <div class="home">
    <h1>Todoリスト</h1>
    <el-tabs class="tab-zone" v-model="activeName">
      <el-tab-pane label="All" name="all">
        <el-table class="data-table" :data="tableDataAll" stripe>
          <el-table-column prop="id" label="ID" width="180"></el-table-column>
          <el-table-column prop="name" label="名前" width="180"></el-table-column>
          <el-table-column prop="status" label="状態" width="180"></el-table-column>
          <el-table-column prop="limit" label="期限"></el-table-column>
        </el-table>
      </el-tab-pane>
      <el-tab-pane label="Todo" name="todo">
        <el-table class="data-table" :data="tableDataTodo" stripe>
          <el-table-column prop="id" label="ID" width="180"></el-table-column>
          <el-table-column prop="name" label="名前" width="180"></el-table-column>
          <el-table-column prop="status" label="状態" width="180"></el-table-column>
          <el-table-column prop="limit" label="期限"></el-table-column>
        </el-table>
      </el-tab-pane>
      <el-tab-pane label="Doing" name="doing">
        <el-table class="data-table" :data="tableDataDoing" stripe>
          <el-table-column prop="id" label="ID" width="180"></el-table-column>
          <el-table-column prop="name" label="名前" width="180"></el-table-column>
          <el-table-column prop="status" label="状態" width="180"></el-table-column>
          <el-table-column prop="limit" label="期限"></el-table-column>
        </el-table>
      </el-tab-pane>
      <el-tab-pane label="Done" name="done">
        <el-table class="data-table" :data="tableDataDone" stripe>
          <el-table-column prop="id" label="ID" width="180"></el-table-column>
          <el-table-column prop="name" label="名前" width="180"></el-table-column>
          <el-table-column prop="status" label="状態" width="180"></el-table-column>
          <el-table-column prop="limit" label="期限"></el-table-column>
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
      tableDataAll: [],
      tableDataTodo: [],
      tableDataDoing: [],
      tableDataDone: [],
      activeName: 'all'
    }
  },
  mounted () {
    this.updataTableData()
  },
  methods: {
    updataTableData: async function () {
      const response = await axios.get('/api/task')
      this.tableDataAll = response.data
      this.tableDataTodo = response.data.filter(
        task => task.status === 'Todo'
      )
      this.tableDataDoing = response.data.filter(
        task => task.status === 'Doing'
      )
      this.tableDataDone = response.data.filter(
        task => task.status === 'Done'
      )
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
}
</style>

<template>
  <div class="home">
    <h1>Todoリスト</h1>
    <div class="form-button">
      <DialogForm/>
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
import DialogForm from '../components/DialogForm.vue'
const axios =
  process.env.VUE_APP_REST_SERVER === 'json-mock'
    ? require('axios').create({ baseURL: 'http://localhost:3000' })
    : require('axios').create()
export default {
  components: {
    DialogForm
  },
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
      // DBから取得したデータを各ステータス用の配列に振り分け、その配列をtableDatasに追加する
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
      // DB側のデータ削除
      axios.delete('/api/task', { data: JSON.stringify(row) })

      // フロント側が保持しているデータを非同期で削除
      var i = 0

      // Allタブのデータを削除
      this.tableDatas[0].data.forEach(function (data, index) {
        if (data.id === row.id) {
          i = index
        }
      })
      this.tableDatas[0].data.splice(i, 1)

      // 各ステータスタブのデータを削除
      switch (row.status) {
        case 'Todo':
          this.tableDatas[1].data.forEach(function (data, index) {
            if (data.id === row.id) {
              i = index
            }
          })
          this.tableDatas[1].data.splice(i, 1)
          break
        case 'Doing':
          this.tableDatas[2].data.forEach(function (data, index) {
            if (data.id === row.id) {
              i = index
            }
          })
          this.tableDatas[2].data.splice(i, 1)
          break
        case 'Done':
          this.tableDatas[3].data.forEach(function (data, index) {
            if (data.id === row.id) {
              i = index
            }
          })
          this.tableDatas[3].data.splice(i, 1)
          break
      }
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
  margin-top: 50px;
}

.form-button {
  width: 60%;
  margin: auto;
}
</style>

<template>
  <div class="home">
    <h1>Todoリスト</h1>
    <el-button class="el-icon-circle-plus" size="mini" @click="dialogFormVisible = true"></el-button>
    <el-dialog title="タスク登録" :visible.sync="dialogFormVisible">
      <el-form :model="formData" class="form">
        <el-form-item label="件名" :label-width="formLabelWidth">
          <el-input v-model="formData.name" autocomplete="off" class="input"></el-input>
        </el-form-item>
        <el-form-item label="状態" :label-width="formLabelWidth">
          <el-select v-model="formData.status" placeholder="タスクの状態を選択して下さい" class="input">
            <el-option label="Todo" value="Todo"></el-option>
            <el-option label="Doing" value="Doing"></el-option>
            <el-option label="Done" value="Done"></el-option>
          </el-select>
        </el-form-item>
        <el-form-item label="期限" :label-width="formLabelWidth">
          <el-date-picker
            v-model="formData.limit"
            type="date"
            placeholder="日付を選択して下さい"
            class="input"
            format="yyyy-MM-dd"
            value-format="yyyy-MM-dd">
          </el-date-picker>
        </el-form-item>
        <el-form-item label="詳細" :label-width="formLabelWidth">
          <el-input
            type="textarea"
            :autosize="{ minRows: 2, maxRows: 4}"
            placeholder="詳細を入力して下さい"
            v-model="formData.detail">
          </el-input>
        </el-form-item>
      </el-form>
      <span slot="footer" class="dialog-footer">
        <el-button @click="dialogFormVisible = false">キャンセル</el-button>
        <el-button type="primary" @click="submit">登録</el-button>
      </span>
    </el-dialog>
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
      activeName: 'All',
      dialogFormVisible: false,
      formData: {
        name: '',
        status: '',
        limit: '',
        detail: ''
      },
      name: [],
      formLabelWidth: '120px',
      pickerOptions: {
        disabledDate (time) {
          return time.getTime() > Date.now()
        },
        shortcuts: [{
          text: 'Today',
          onClick (picker) {
            picker.$emit('pick', new Date())
          }
        }, {
          text: 'Yesterday',
          onClick (picker) {
            const date = new Date()
            date.setTime(date.getTime() - 3600 * 1000 * 24)
            picker.$emit('pick', date)
          }
        }, {
          text: 'A week ago',
          onClick (picker) {
            const date = new Date()
            date.setTime(date.getTime() - 3600 * 1000 * 24 * 7)
            picker.$emit('pick', date)
          }
        }]
      }
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
    },
    submit: function () {
      axios.post('/api/task', this.formData)
        .then(response => {
          console.log(response.data)
        })
      this.dialogFormVisible = false
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

<template>
  <div>
    <!-- Form -->
    <el-button class="el-icon-edit" size="mini" @click="handleEdit(scope)"></el-button>
    <el-dialog title="タスク登録" :visible.sync="dialogFormVisible" class="title">
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
            class="input"
            v-model="formData.limit"
            type="date"
            placeholder="日付を選択して下さい"
            format="yyyy-MM-dd"
            value-format="yyyy-MM-dd">
          </el-date-picker>
        </el-form-item>
        <el-form-item label="詳細" :label-width="formLabelWidth">
          <el-input
            type="textarea"
            :autosize="{ minRows: 2, maxRows: 4}"
            placeholder="詳細を入力して下さい"
            v-model="formData.detail"
            class="input">
          </el-input>
        </el-form-item>
      </el-form>
      <span slot="footer" class="dialog-footer">
        <el-button @click="dialogFormVisible = false">キャンセル</el-button>
        <el-button type="primary" @click="submit">登録</el-button>
      </span>
    </el-dialog>
  </div>
</template>

<script>
const axios = require('axios').create()
export default {
  name: 'edit-form',
  props: { row: JSON },
  data () {
    return {
      dialogFormVisible: false,
      formData: {
        id: this.row.id,
        name: this.row.name,
        status: this.row.status,
        limit: this.row.limit,
        detail: this.row.detail
      },
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
  methods: {
    submit: function () {
      axios.put('/api/task', this.formData)
        .then(response => {
          console.log(response.data)
        })
      this.dialogFormVisible = false
    },
    handleEdit (row) {
      this.dialogFormVisible = true
      console.log('editボタンを押下')
      console.log(JSON.stringify(row))
    }
  }
}
</script>

<style scoped>
.form {
  width: 50%;
}

.input {
  width: 100%;
  float: left;
}

</style>

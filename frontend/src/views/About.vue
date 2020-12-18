<template>
  <div class="about">
    <!-- Form -->
    <el-button class="el-icon-circle-plus" size="mini" @click="dialogFormVisible = true"></el-button>
    <el-dialog title="タスク登録" :visible.sync="dialogFormVisible">
      <el-form :model="form" class="form">
        <el-form-item label="件名" :label-width="formLabelWidth">
          <el-input v-model="form.name" autocomplete="off" class="input"></el-input>
        </el-form-item>
        <el-form-item label="状態" :label-width="formLabelWidth">
          <el-select v-model="form.region" placeholder="タスクの状態を選択して下さい" class="input">
            <el-option label="Todo" value="Todo"></el-option>
            <el-option label="Doing" value="Doing"></el-option>
            <el-option label="Done" value="Done"></el-option>
          </el-select>
        </el-form-item>
        <el-form-item label="期限" :label-width="formLabelWidth">
          <el-date-picker
            v-model="value"
            type="date"
            placeholder="日付を選択して下さい"
            class="input">
          </el-date-picker>
        </el-form-item>
        <el-form-item label="詳細" :label-width="formLabelWidth">
          <el-input
            type="textarea"
            :autosize="{ minRows: 2, maxRows: 4}"
            placeholder="詳細を入力して下さい"
            v-model="textarea">
          </el-input>
        </el-form-item>
      </el-form>
      <span slot="footer" class="dialog-footer">
        <el-button @click="dialogFormVisible = false">キャンセル</el-button>
        <el-button type="primary" @click="dialogFormVisible = false">登録</el-button>
      </span>
    </el-dialog>
  </div>
</template>

<script>
export default {
  name: 'about',
  data () {
    return {
      dialogFormVisible: false,
      form: {
        name: '',
        region: '',
        date1: '',
        date2: '',
        delivery: false,
        type: [],
        resource: '',
        desc: ''
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
      },
      value: '',
      textarea: ''
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
}
</style>

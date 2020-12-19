<template>
  <div class="form">
    <!-- Form -->
      <el-form :model="form" class="form">
        <el-form-item label="件名" :label-width="formLabelWidth">
          <el-input v-model="form.name" autocomplete="off" class="input"></el-input>
        </el-form-item>
        <el-button @click="dialogFormVisible = false">キャンセル</el-button>
        <el-button type="primary" @click="submitData">登録</el-button>
      </el-form>
  </div>
</template>

<script>
const axios = require('axios').create()
export default {
  name: 'form',
  data () {
    return {
      form: {
        name: ''
      },
      formLabelWidth: '120px'
    }
  },
  methods: {
    submitData: function () {
      axios.post('/api/task', this.form)
        .then(response => {
          console.log(response.data.results)
        })
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

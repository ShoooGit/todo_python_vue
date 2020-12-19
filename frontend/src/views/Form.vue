<template>
  <div class="form">
    <!-- Form -->
      <el-form :model="form" class="form">
        <el-form-item label="件名" :label-width="formLabelWidth">
          <el-input v-model="form.name" autocomplete="off" class="input"></el-input>
        </el-form-item>
        <el-button @click="dialogFormVisible = false">キャンセル</el-button>
        <el-button type="primary" @click="dialogFormVisible = false">登録</el-button>
      </el-form>
  </div>
</template>

<script>
export default {
  name: 'form',
  data () {
    return {
      form: {
        name: ''
      },
      formLabelWidth: '120px'
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

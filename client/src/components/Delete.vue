<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>Data Deletion</h1>
        <hr><br><br>
        <button type="button" class="btn btn-success btn-sm" v-b-modal.data-modal>Delete</button>
        <br><br>
      </div>
    </div>
    <b-modal ref="deleteDataModel"
            id="data-modal"
            name="Delete Data"
            hide-footer>
      <b-form @submit="onSubmit" class="w-100">
      <b-form-group id="form-delete-group"
                    label="id:"
                    label-for="form-delete-input">
          <b-form-input id="form-delete-input"
                        type="number"
                        v-model="deleteDataForm.id"
                        required
                        placeholder="Enter id">
          </b-form-input>
        </b-form-group>
        <b-button-group>
          <b-button type="submit" variant="primary">Submit</b-button>
        </b-button-group>
      </b-form>
    </b-modal>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      deleteDataForm: {
        id: '',
      },
    };
  },
  methods: {
    deleteData(payload) {
      const path = 'http://localhost:5000/delete';
      axios.delete(path, { data: payload });
    },
    initForm() {
      this.deleteDataForm.id = '';
    },
    onSubmit(evt) {
      evt.preventDefault();
      this.$refs.deleteDataModel.hide();
      const payload = {
        id: this.deleteDataForm.id,
      };
      this.deleteData(payload);
      this.initForm();
    },
  },
};
</script>

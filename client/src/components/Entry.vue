<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>Data Entry</h1>
        <hr><br><br>
        <button type="button" class="btn btn-success btn-sm" v-b-modal.data-modal>Add</button>
        <br><br>
      </div>
    </div>
    <b-modal ref="addDataModal"
            id="data-modal"
            name="Add a data"
            hide-footer>
      <b-form @submit="onSubmit" class="w-100">
      <b-form-group id="form-name-group"
                    label="Name:"
                    label-for="form-name-input">
          <b-form-input id="form-name-input"
                        type="text"
                        v-model="addDataForm.name"
                        required
                        placeholder="Enter name">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-count-group"
                      label="Count:"
                      label-for="form-count-input">
            <b-form-input id="form-count-input"
                          type="text"
                          v-model="addDataForm.count"
                          required
                          placeholder="Enter count">
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
      addDataForm: {
        name: '',
        count: '',
      },
    };
  },
  methods: {
    addData(payload) {
      const path = 'http://localhost:5000/entry';
      axios.post(path, payload);
    },
    initForm() {
      this.addDataForm.name = '';
      this.addDataForm.count = '';
    },
    onSubmit(evt) {
      evt.preventDefault();
      this.$refs.addDataModal.hide();
      const payload = {
        name: this.addDataForm.name,
        count: this.addDataForm.count,
      };
      this.addData(payload);
      this.initForm();
    },
  },
};
</script>

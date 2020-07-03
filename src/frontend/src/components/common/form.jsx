import React, { Component } from "react";
import Joi from "joi-browser";
import Input from "./input";
import Select from "./select";
import { toast, ToastContainer } from "react-toastify";

class Form extends Component {
  state = {
    data: {},
    errors: {},
  };

  validate = () => {
    const options = { abortEarly: false };
    const { error } = Joi.validate(this.state.data, this.schema, options);
    if (!error) return null;

    const errors = {};
    for (let item of error.details) errors[item.path[0]] = item.message;
    return errors;
  };

  validateProperty = ({ name, value }) => {
    const obj = { [name]: value };
    const schema = { [name]: this.schema[name] };
    const { error } = Joi.validate(obj, schema);
    return error ? error.details[0].message : null;
  };

  handleSubmit = (e) => {
    e.preventDefault();

    const errors = this.validate();
    this.setState({ errors: errors || {} });
    if (errors) return;

    this.doSubmit();
  };

  handleChange = ({ currentTarget: input }) => {
    const errors = { ...this.state.errors };
    const errorMessage = this.validateProperty(input);

    if (errorMessage) errors[input.name] = errorMessage;
    else delete errors[input.name];

    const data = { ...this.state.data };
    data[input.name] = input.value;

    this.setState({ data, errors });
  };

  renderButton(label) {
    // if (code === 201) {
    //   toast.success("Open Your Email and Verify");
    // } else if (code === 202) {
    //   toast.warning("User Already EXISTS");
    // } else if (code === 402) {
    //   toast.error("Token Expired");
    // } else {
    //   toast.error("UNKNOWN ERROR");
    // }
    return (
      <div>
        <button disabled={this.validate()} className="btn btn-primary">
          {label}
        </button>
      </div>
    );
  }

  renderSelect(name, label, options) {
    const { data, errors } = this.state;

    return (
      <Select
        name={name}
        value={data[name]}
        label={label}
        options={options}
        onChange={this.handleChange}
        error={errors[name]}
      />
    );
  }

  renderInput(name, label, type = "text", field = "default") {
    const { data, errors } = this.state;

    return (
      <Input
        field={field}
        type={type}
        name={name}
        // value={data[name]}
        data={data}
        label={label}
        onChange={this.handleChange}
        error={errors[name]}
        errors={errors}
      />
    );
  }
}

export default Form;

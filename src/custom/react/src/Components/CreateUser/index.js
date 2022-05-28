import React, { Component } from 'react';
import './index.css';
const CreateUser = ({ onChangeForm, createUser }) => {
    return (
        <div className="input-container">
            <h2>Create User</h2>
            <form>
                <div>
                    <input type="text" onChange={(e) => onChangeForm(e)} className="form-control" name="firstname" id="firstname" placeholder="Enter First Name" />
                </div>
                <div>
                    <input type="text" onChange={(e) => onChangeForm(e)} className="form-control" name="lastname" id="lastname" placeholder="Enter Last Name" />
                </div>
                <div>
                    <input type="text" onChange={(e) => onChangeForm(e)} className="form-control" name="username" id="username" placeholder="Enter User Name" />
                </div>
                <button type="button" onClick={(e) => createUser()} className="btn btn-danger">Submit</button>
            </form>
        </div>
    )
}
export default CreateUser;
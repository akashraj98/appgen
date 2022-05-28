import React, { Component } from 'react';
import './App.css';
import Users  from './Components/Users'
import CreateUser from './Components/CreateUser'
import { getAllUsers, createUser } from './UserService'

class App extends Component {

  state = {
    user: {},
    users: [],
    numberOfUsers: 0
  }
  // users = new Map();
  // users = Object.keys(this.state.users).length>0 ? this.state.users : {
  //   "userName1": { firstName: 'User1FirstName', lastName: 'User1LastName' },
  //   "userName2": { firstName: 'User2FirstName', lastName: 'User2LastName' },
  //   "userName3": { firstName: 'User3FirstName', lastName: 'User3LastName' },
  //   "userName4": { firstName: 'User3FirstName', lastName: 'User3LastName' },
  // }

  createUser = (e) => {
      createUser(this.state.user)
        .then(response => {
          console.log(response);
      });
      this.setState({user: {}})
  }

  getAllUsers = () => {
    getAllUsers()
      .then(users => {
        console.log(users)
        this.setState({users: users, numberOfUsers: users.length})
      });
  }

  onChangeForm = (e) => {
      let user = this.state.user
      if (e.target.name === 'firstname') {
          user.firstName = e.target.value;
      } else if (e.target.name === 'lastname') {
          user.lastName = e.target.value;
      } else if (e.target.name === 'username') {
          user.username = e.target.value;
      }
      this.setState({user})
  }

  render() {
    
    return (
      <div className="App">
        <div className="container mrgnbtm">
          <div className="row">
            <div className="col-md-8">
                <CreateUser 
                  user={this.state.user}
                  onChangeForm={this.onChangeForm}
                  createUser={this.createUser}
                  >
                </CreateUser>
            </div>
          </div>
        </div>
        <div >
          <Users 
          getAllUsers={this.getAllUsers}
          users={this.state.users}></Users>
        </div>
      </div>
    );
  }
}

export default App;
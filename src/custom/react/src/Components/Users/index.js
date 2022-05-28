import React from 'react'
import './index.css';

export const Users = ({ getAllUsers, users }) => {
    getAllUsers();
    var obj = new Map(Object.entries(users));
    var arrayUsers = Array.from(obj);
    console.log('users length:::', arrayUsers.length)
    if (arrayUsers.length === 0) return null
    const UserRow = (user) => {

        return (
            <tr>
                <td>{user[1].firstName}</td>
                <td>{user[1].lastName}</td>
            </tr>
        )
    }

    const userTable = arrayUsers.map((arrayUsers) => UserRow(arrayUsers))
    // const userTable= keys.forEach(key=>{
    //     UserRow(users[key]);
    // })

    return (
        <div className="container">
            <h2>Users</h2>
            <table className="table table-bordered">
                <thead>
                    <tr>
                        <th>Firstname</th>
                        <th>Lastname</th>
                    </tr>
                </thead>
                <tbody>
                    {userTable}
                </tbody>
            </table>
        </div>
    )
}
export default Users;
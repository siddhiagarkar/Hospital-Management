import React, { Component } from 'react';

class Login extends Component {

    state = {
        credentials: {username: '', password: ''}
    }

    login = event => {
        console.log(this.state.credentials);
    }

    inputChanged = event => {
        const cred = this.state.credentials
        cred[event.target.name] = event.target.value;
        this.setState({credentials: cred});
    }

    render(){
        return (
            <div className="App">
                <h1>Login User</h1>

                <label>
                    Username : <input type='text' name='username' value ={this.state.credentials.username} onChange={this.inputChanged}></input>
                    <br/><br/>
                    Password : <input type='password' name='password' value ={this.state.credentials.password} onChange={this.inputChanged}></input>
                </label>

                <button onClick={this.login}>Login</button>
            </div>
          ); 
    }
}

export default Login;

import axios from 'axios';
import { useState } from 'react';

export interface LoginProps {
    setToken: (token: string) => void;
}

const Login = (props: LoginProps) => {
    const [username, setUsername] = useState<string>("");
    const [password, setPassword] = useState<string>("");

    const getToken = async () => {
        let resp = await axios.post("http://localhost:8000/auth", {
            'username': username,
            'password': password,
        });
        const token = resp.data['token'];
        console.log(token);
        props.setToken(token);
    }

    return (
        <div className=''> 
            <input placeholder='Username' onChange={(val) => { setUsername(val.target.value) }} /> 
            <input placeholder='Password' onChange={(val) => { setPassword(val.target.value) }}/> 
            <input type='button' value="Send" onClick={() => getToken()}/>
        </div>
    );
}

export default Login;

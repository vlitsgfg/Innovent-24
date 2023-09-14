import React, { useState } from "react";
import First from "./first";
//import { auth } from "./firebase"; 
//import {getAuth,createUserWithEmailAndPassword} from "firebase/auth";
import { createUserWithEmailAndPassword } from "firebase/auth";

const Login = () => {
  const [data, setData] = useState({
    email: "",
    password: ""
  });
  const { email, password } = data;

  const changeHandler = (e) => {
    setData({ ...data, [e.target.name]: e.target.value });
  };

  const signUp = (e) => {
    e.preventDefault();
    <First/>
  };

  const signIn = (e) => {
    e.preventDefault();
   
  };

  return (
    <div>
      <center>
        <form autoComplete="off">
          <h1>Authentication</h1>
          <label>Email: </label>
          <input
            type="email"
            name="email"
            placeholder="enter email"
            onChange={changeHandler}
          />
          <br />
          <br />
          <label>Password:</label>
          <input
            type="password"
            name="password"
            placeholder="enter password"
            onChange={changeHandler}
          />
          <br />
          <br />
          <button onClick={signIn}>Sign In</button>
          &nbsp;&nbsp;
          <button onClick={signUp}>Sign Up</button>
        </form>
      </center>
    </div>
  );
};

export default Login
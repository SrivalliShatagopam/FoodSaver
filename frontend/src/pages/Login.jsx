import { useState } from "react";
import axios from "axios";

function Login() {
  const [formData, setFormData] = useState({
    email: "",
    password: "",
  });

  const [message, setMessage] = useState("");

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const response = await axios.post(
        "http://127.0.0.1:5000/api/auth/login",
        formData
      );

      setMessage(response.data.message);

      console.log(response.data);
    } catch (error) {
      setMessage(
        error.response?.data?.message || "Login failed."
      );
    }
  };

  return (
    <div className="container" style={{ maxWidth: "500px", margin: "80px auto" }}>
      <h1>Login</h1>

      <form onSubmit={handleSubmit}>

        <input
          type="email"
          name="email"
          placeholder="Email"
          value={formData.email}
          onChange={handleChange}
        />

        <br /><br />

        <input
          type="password"
          name="password"
          placeholder="Password"
          value={formData.password}
          onChange={handleChange}
        />

        <br /><br />

        <button className="btn primary">
          Login
        </button>

      </form>

      <p>{message}</p>

    </div>
  );
}

export default Login;
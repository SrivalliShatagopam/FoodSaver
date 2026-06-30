import { useState } from "react";
import { useNavigate, Link } from "react-router-dom";
import { registerUser } from "../services/authService";

function Register() {
  const navigate = useNavigate();

  const [formData, setFormData] = useState({
    full_name: "",
    email: "",
    phone: "",
    password: "",
    role: "donor",
  });

  const [message, setMessage] = useState("");
  const [isError, setIsError] = useState(false);

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    setMessage("");

    try {
      const response = await registerUser(formData);

      setIsError(false);
      setMessage(response.data.message);

      setTimeout(() => {
        navigate("/login");
      }, 1500);

    } catch (error) {
      setIsError(true);
      setMessage(
        error.response?.data?.message || "Registration failed."
      );
    }
  };

  return (
    <div className="container" style={{ maxWidth: "500px", margin: "60px auto" }}>
      <h1>Create Account</h1>

      <form onSubmit={handleSubmit}>

        <input
          type="text"
          name="full_name"
          placeholder="Full Name"
          value={formData.full_name}
          onChange={handleChange}
          required
        />

        <br /><br />

        <input
          type="email"
          name="email"
          placeholder="Email"
          value={formData.email}
          onChange={handleChange}
          required
        />

        <br /><br />

        <input
          type="text"
          name="phone"
          placeholder="Phone Number"
          value={formData.phone}
          onChange={handleChange}
          required
        />

        <br /><br />

        <input
          type="password"
          name="password"
          placeholder="Password"
          value={formData.password}
          onChange={handleChange}
          required
        />

        <br /><br />

        <select
          name="role"
          value={formData.role}
          onChange={handleChange}
        >
          <option value="donor">Donor</option>
          <option value="ngo">NGO</option>
          <option value="volunteer">Volunteer</option>
        </select>

        <br /><br />

        <button className="btn primary">
          Register
        </button>

      </form>

      {message && (
        <p style={{ color: isError ? "red" : "green" }}>
          {message}
        </p>
      )}

      <p>
        Already have an account?{" "}
        <Link to="/login">Login</Link>
      </p>

    </div>
  );
}

export default Register;
import { BrowserRouter, Routes, Route } from "react-router-dom";

import Home from "../pages/Home";
import Register from "../pages/Register";
import Login from "../pages/Login";

import DonorDashboard from "../pages/DonorDashboard";
function AppRoutes() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/login" element={<Login />} />
        <Route path="/register" element={<Register />} />
        <Route path="/dashboard" element={<DonorDashboard />} />
      </Routes>
    </BrowserRouter>
  );
}

export default AppRoutes;
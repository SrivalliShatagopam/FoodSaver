import { BrowserRouter, Routes, Route } from "react-router-dom";

import Home from "../pages/Home";
import Login from "../pages/Login";
import DonorDashboard from "../pages/DonorDashboard";
function AppRoutes() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/login" element={<Login />} />
        <Route path="/dashboard" element={<DonorDashboard />} />
      </Routes>
    </BrowserRouter>
  );
}

export default AppRoutes;
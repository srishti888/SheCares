import React from "react";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import Login from "./components/Login";
import { AuthProvider } from "./context/AuthContext"; // Wrap in AuthProvider

function Auth() {
    return (
        <AuthProvider>
            <Router>
                <Routes>
                    <Route path="/login" element={<Login />} />
                    <Route path="/doctor-dashboard" element={<DoctorDashboard />} />
                    <Route path="/patient-dashboard" element={<PatientDashboard />} />
                </Routes>
            </Router>
        </AuthProvider>
    );
}

export default Auth;

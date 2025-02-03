import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import Login from "./components/Login";
import DoctorDashboard from "./components/DoctorDashboard"; // Add your doctor dashboard component
import PatientDashboard from "./components/PatientDashboard"; // Add your patient dashboard component
import { AuthProvider } from "./context/AuthContext"; // Wrap in AuthProvider

function App() {
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

export default App;

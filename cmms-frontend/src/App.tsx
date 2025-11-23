import * as React from 'react';
import { Routes, Route, Navigate, BrowserRouter } from "react-router-dom";

// Material Dashboard React components
import CssBaseline from "@mui/material/CssBaseline";
import { ThemeProvider } from "@mui/material/styles";
import theme from "./assets/theme";
import DashboardLayout from "./layouts/dashboard";
import DashboardApp from "./pages/DashboardApp";
import Login from "./pages/Login";
import Register from "./pages/Register";

export default function App() {
  // Simple authentication state logic (replace with your logic)
  const [authenticated, setAuthenticated] = React.useState(false);

  React.useEffect(() => {
    // Replace with actual token check
    const token = localStorage.getItem('token');
    setAuthenticated(!!token);
  }, []);

  const handleLoginSwitch = (page: string) => {
    if (page === 'assets' || page === 'dashboard') {
      setAuthenticated(true);
    } else {
      setAuthenticated(false);
    }
  };

  if (!authenticated) {
    return (
      <ThemeProvider theme={theme}>
        <CssBaseline />
        <BrowserRouter>
          <Routes>
            <Route path="/login" element={<Login onSwitch={handleLoginSwitch} />} />
            <Route path="/register" element={<Register onSwitch={handleLoginSwitch} />} />
            <Route path="*" element={<Navigate to="/login" replace />} />
          </Routes>
        </BrowserRouter>
      </ThemeProvider>
    );
  }

  return (
    <ThemeProvider theme={theme}>
      <CssBaseline />
      <BrowserRouter>
        <DashboardLayout>
          <Routes>
            <Route path="/dashboard" element={<DashboardApp />} />
            {/* Add other dashboard routes here */}
            <Route path="*" element={<Navigate to="/dashboard" replace />} />
          </Routes>
        </DashboardLayout>
      </BrowserRouter>
    </ThemeProvider>
  );
}

import React, { useState } from "react";
import { Box, Button, Container, TextField, Typography, Checkbox, FormControlLabel, Alert, CircularProgress } from "@mui/material";

export default function Login({ onSwitch }: { onSwitch: (page: string) => void }) {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const submit = async (e: React.FormEvent) => {
    e.preventDefault();
    setError(null);
    if (!email.trim()) return setError("Email is required");
    if (!password) return setError("Password is required");
    setLoading(true);
    try {
      // Replace with real login API call
      // await loginUser({ username: email.trim(), password });
      onSwitch("assets");
    } catch (err: any) {
      setError(err?.response?.data?.detail || err.message || "Login failed");
    } finally {
      setLoading(false);
    }
  };

  return (
    <Container maxWidth="xs" sx={{ mt: 8, bgcolor: "background.paper", p: 4, borderRadius: 2, boxShadow: 3 }}>
      <Typography variant="h5" component="h1" align="center" gutterBottom>
        Sign In
      </Typography>

      <Box component="form" onSubmit={submit} noValidate>
        <TextField
          margin="normal"
          required
          fullWidth
          id="email"
          label="Email Address"
          name="email"
          autoComplete="email"
          autoFocus
          value={email}
          onChange={(e) => setEmail(e.target.value)}
        />
        <TextField
          margin="normal"
          required
          fullWidth
          name="password"
          label="Password"
          type="password"
          id="password"
          autoComplete="current-password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />
        <FormControlLabel control={<Checkbox value="remember" color="primary" />} label="Remember me" />

        {error && (
          <Alert severity="error" sx={{ mt: 2 }}>
            {error}
          </Alert>
        )}

        <Button type="submit" fullWidth variant="contained" sx={{ mt: 3, mb: 2 }} disabled={loading}>
          {loading ? <CircularProgress size={24} /> : "Sign In"}
        </Button>

        <Box display="flex" justifyContent="space-between">
          <Button variant="text" onClick={() => onSwitch("forgot")}>
            Forgot password?
          </Button>
          <Button variant="text" onClick={() => onSwitch("register")}>
            Create new account
          </Button>
        </Box>
      </Box>
    </Container>
  );
}

import React, { useState } from "react";
import { Box, Button, Container, TextField, Typography, Checkbox, FormControlLabel, Alert, CircularProgress } from "@mui/material";

export default function Register({ onSwitch }: { onSwitch: (page: string) => void }) {
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const submit = async (e: React.FormEvent) => {
    e.preventDefault();
    setError(null);
    if (!name.trim()) return setError("Name is required");
    if (!password || password.length < 6) return setError("Password must be at least 6 characters");
    setLoading(true);
    try {
      // Replace with real register API call
      // await registerUser({ username: name.trim(), email: email.trim() || undefined, password });
      // await loginUser({ username: name.trim(), password });
      onSwitch("assets");
    } catch (err: any) {
      setError(err?.response?.data?.detail || err.message || "Registration failed");
    } finally {
      setLoading(false);
    }
  };

  return (
    <Container maxWidth="xs" sx={{ mt: 8, bgcolor: "background.paper", p: 4, borderRadius: 2, boxShadow: 3 }}>
      <Typography variant="h5" component="h1" align="center" gutterBottom>
        Create Account
      </Typography>

      <Box component="form" onSubmit={submit} noValidate>
        <TextField
          margin="normal"
          required
          fullWidth
          id="name"
          label="Name"
          name="name"
          autoComplete="name"
          autoFocus
          value={name}
          onChange={(e) => setName(e.target.value)}
        />
        <TextField
          margin="normal"
          fullWidth
          id="email"
          label="Email Address"
          name="email"
          autoComplete="email"
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
          autoComplete="new-password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />
        <FormControlLabel
          control={<Checkbox value="agree" color="primary" />}
          label={
            <>
              I agree with the <a href="#" onClick={(e) => e.preventDefault()}>Privacy Policy</a>
            </>
          }
        />

        {error && (
          <Alert severity="error" sx={{ mt: 2 }}>
            {error}
          </Alert>
        )}

        <Button type="submit" fullWidth variant="contained" sx={{ mt: 3, mb: 2 }} disabled={loading}>
          {loading ? <CircularProgress size={24} /> : "Create Account"}
        </Button>

        <Box display="flex" justifyContent="flex-end">
          <Button variant="text" onClick={() => onSwitch("login")}>
            Already have an account? Sign In
          </Button>
        </Box>
      </Box>
    </Container>
  );
}

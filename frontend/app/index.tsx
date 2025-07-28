import React, { useState } from 'react';
import { View, Text, TouchableOpacity, StyleSheet, Alert } from 'react-native';
import axios from 'axios';

export default function Home() {
  const [status, setStatus] = useState('Idle');
  const [error, setError] = useState('');
  const BASE_URL = "http://192.168.0.103:8000"; // Update if IP changes

  const startDetection = async () => {
    try {
      const res = await axios.post(`${BASE_URL}/start_detection`);
      setStatus(res.data.status);
      setError('');
    } catch (err) {
      setError('❌ Could not connect to backend');
      console.log(err);
    }
  };

  const stopDetection = async () => {
    try {
      const res = await axios.post(`${BASE_URL}/stop_detection`);
      setStatus(res.data.status);
      setError('');
    } catch (err) {
      setError('❌ Could not connect to backend');
      console.log(err);
    }
  };

  const triggerSOS = async () => {
    try {
      const res = await axios.post(`${BASE_URL}/trigger_sos`);
      Alert.alert('🚨 SOS Sent', 'Call and SMS with location has been triggered.');
      console.log(res.data);
    } catch (err) {
      setError('❌ SOS Failed: Check backend');
      console.log(err);
    }
  };

  return (
    <View style={styles.container}>
      <Text style={styles.title}>🚨 SOS Via Distress Detection 🎤</Text>

      <TouchableOpacity style={styles.button} onPress={startDetection}>
        <Text style={styles.buttonText}>Start Detection</Text>
      </TouchableOpacity>

      <TouchableOpacity style={[styles.button, { backgroundColor: 'red' }]} onPress={stopDetection}>
        <Text style={styles.buttonText}>Stop Detection</Text>
      </TouchableOpacity>

      <TouchableOpacity style={[styles.button, { backgroundColor: 'orange' }]} onPress={triggerSOS}>
        <Text style={styles.buttonText}>Trigger SOS 🚨</Text>
      </TouchableOpacity>

      <Text style={styles.status}>Status: {status}</Text>
      {error ? <Text style={styles.error}>{error}</Text> : null}
    </View>
  );
}

const styles = StyleSheet.create({
  container: { flex: 1, justifyContent: 'center', alignItems: 'center', backgroundColor: '#fff' },
  title: { fontSize: 24, fontWeight: 'bold', marginBottom: 30 },
  button: { backgroundColor: 'green', padding: 15, borderRadius: 10, marginTop: 15, width: 250, alignItems: 'center' },
  buttonText: { color: 'white', fontSize: 18 },
  status: { marginTop: 30, fontSize: 18 },
  error: { marginTop: 20, color: 'red', fontWeight: 'bold' },
});

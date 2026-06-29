import React, { useState, useEffect } from 'react';
import axios from 'axios';

function App() {
  const [habits, setHabits] = useState([]);

  useEffect(() => {
    axios.get('http://localhost:8000/api/v1/habits/')
      .then(response => {
        setHabits(response.data);
      })
      .catch(error => {
        console.error(error);
      });
  }, []);

  return (
    <div>
      <h1>Habit Tracker</h1>
      <ul>
        {habits.map(habit => (
          <li key={habit.id}>{habit.name}</li>
        ))}
      </ul>
    </div>
  );
}

export default App;
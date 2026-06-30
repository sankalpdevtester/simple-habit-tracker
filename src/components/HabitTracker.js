import React, { useState, useEffect } from 'react';
import axios from 'axios';

function HabitTracker() {
    const [habits, setHabits] = useState([]);
    const [newHabit, setNewHabit] = useState({ name: '', category: '', frequency: '' });
    const [checkins, setCheckins] = useState({});

    useEffect(() => {
        axios.get('/api/habits/')
            .then(response => {
                setHabits(response.data);
            })
            .catch(error => {
                console.error(error);
            });
    }, []);

    const handleCreateHabit = (event) => {
        event.preventDefault();
        axios.post('/api/habits/', newHabit)
            .then(response => {
                setHabits([...habits, response.data]);
                setNewHabit({ name: '', category: '', frequency: '' });
            })
            .catch(error => {
                console.error(error);
            });
    };

    const handleUpdateHabit = (habit) => {
        axios.put(`/api/habits/${habit.id}/`, habit)
            .then(response => {
                setHabits(habits.map(h => h.id === habit.id ? response.data : h));
            })
            .catch(error => {
                console.error(error);
            });
    };

    const handleDeleteHabit = (habitId) => {
        axios.delete(`/api/habits/${habitId}/`)
            .then(() => {
                setHabits(habits.filter(h => h.id !== habitId));
            })
            .catch(error => {
                console.error(error);
            });
    };

    const handleCheckin = (habitId, date) => {
        axios.post(`/api/habits/${habitId}/checkins/`, { date: date })
            .then(response => {
                setCheckins({ ...checkins, [habitId]: response.data });
            })
            .catch(error => {
                console.error(error);
            });
    };

    return (
        <div>
            <h1>Habit Tracker</h1>
            <form onSubmit={handleCreateHabit}>
                <label>Name:</label>
                <input type="text" value={newHabit.name} onChange={(event) => setNewHabit({ ...newHabit, name: event.target.value })} />
                <br />
                <label>Category:</label>
                <input type="text" value={newHabit.category} onChange={(event) => setNewHabit({ ...newHabit, category: event.target.value })} />
                <br />
                <label>Frequency:</label>
                <input type="text" value={newHabit.frequency} onChange={(event) => setNewHabit({ ...newHabit, frequency: event.target.value })} />
                <br />
                <button type="submit">Create Habit</button>
            </form>
            <ul>
                {habits.map(habit => (
                    <li key={habit.id}>
                        <h2>{habit.name}</h2>
                        <p>Category: {habit.category}</p>
                        <p>Frequency: {habit.frequency}</p>
                        <button onClick={() => handleUpdateHabit(habit)}>Update</button>
                        <button onClick={() => handleDeleteHabit(habit.id)}>Delete</button>
                        <button onClick={() => handleCheckin(habit.id, new Date().toISOString().split('T')[0])}>Checkin</button>
                    </li>
                ))}
            </ul>
        </div>
    );
}

export default HabitTracker;
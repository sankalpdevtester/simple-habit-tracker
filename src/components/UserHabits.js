import React, { useState, useEffect } from 'react';
import axios from 'axios';

function UserHabits() {
    const [userHabits, setUserHabits] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        axios.get('/api/user_habits/')
            .then(response => {
                setUserHabits(response.data);
                setLoading(false);
            })
            .catch(error => {
                setError(error);
                setLoading(false);
            });
    }, []);

    if (loading) {
        return <div>Loading...</div>;
    }

    if (error) {
        return <div>Error: {error.message}</div>;
    }

    return (
        <div>
            <h1>User Habits</h1>
            <ul>
                {userHabits.map(userHabit => (
                    <li key={userHabit.id}>
                        {userHabit.habit.name}
                    </li>
                ))}
            </ul>
        </div>
    );
}

export default UserHabits;
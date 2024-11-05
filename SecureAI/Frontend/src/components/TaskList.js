// src/components/TaskList.js

import React from 'react';

const TaskList = ({ tasks, onSelectTask }) => (
    <div>
        <h2>Lista de Tareas</h2>
        <ul>
            {tasks.map((task) => (
                <li key={task.id} onClick={() => onSelectTask(task.id)}>
                    {task.title}
                </li>
            ))}
        </ul>
    </div>
);

export default TaskList;

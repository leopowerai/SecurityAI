// src/components/TaskDetail.js

import React from 'react';

const TaskDetail = ({ task }) => (
    <div>
        <h2>Detalle de la Tarea</h2>
        {task ? (
            <>
                <h3>{task.title}</h3>
                <p>{task.description}</p>
            </>
        ) : (
            <p>No se ha seleccionado ninguna tarea</p>
        )}
    </div>
);

export default TaskDetail;

class Task {
    constructor(content) {
        this.id = Date.now().toString(); 
        this.content = content;
        this.completed = false;
    }
}

class TaskManager {
    static TASK_KEY = 'dashboardTasks';

    static getTasks = () => {
        const data = localStorage.getItem(TaskManager.TASK_KEY);
        return data ? JSON.parse(data) : [];
    };

    static saveTasks = (tasks) => {
        localStorage.setItem(TaskManager.TASK_KEY, JSON.stringify(tasks));
    };

    static async getTasksAsync() {
        await new Promise(resolve => setTimeout(resolve, 1000));
        return TaskManager.getTasks();
    }
}

const taskInput = document.getElementById('task-input');
const addTaskBtn = document.getElementById('add-task-btn');
const taskList = document.getElementById('task-list');
const loadingMessage = document.getElementById('loading-message');

let currentTasks = [];

const createTaskElement = (task) => {
    return `
        <li class="task-item ${task.completed ? 'completed' : ''}" data-id="${task.id}">
            <span class="task-content" data-action="toggle">${task.content}</span>
            <div class="task-actions">
                <button class="edit-btn" data-id="${task.id}" data-action="edit">Edit</button>
                <button class="delete-btn" data-id="${task.id}" data-action="delete">Hapus</button>
            </div>
        </li>
    `;
};

const renderTasks = () => {
    const htmlList = currentTasks.map(createTaskElement).join('');
    taskList.innerHTML = htmlList;
};

const addTask = () => {
    const content = taskInput.value.trim();
    if (content) {
        const newTask = new Task(content);
        currentTasks.push(newTask);
        TaskManager.saveTasks(currentTasks);
        renderTasks();
        taskInput.value = '';
    }
};

const toggleTaskCompletion = (taskId) => {
    currentTasks = currentTasks.map(task => {
        if (task.id === taskId) {
            return { ...task, completed: !task.completed }; 
        }
        return task;
    });
    TaskManager.saveTasks(currentTasks);
    renderTasks();
};

const deleteTask = (taskId) => {
    currentTasks = currentTasks.filter(task => task.id !== taskId);
    TaskManager.saveTasks(currentTasks);
    renderTasks();
};

const editTask = (taskId, oldContent) => {
    const newContent = prompt('Edit tugas:', oldContent);
    if (newContent && newContent.trim() !== '') {
        currentTasks = currentTasks.map(task => {
            if (task.id === taskId) {
                return { ...task, content: newContent.trim() };
            }
            return task;
        });
        TaskManager.saveTasks(currentTasks);
        renderTasks();
    }
};

addTaskBtn.addEventListener('click', addTask);

taskInput.addEventListener('keypress', (e) => {
    if (e.key === 'Enter') {
        addTask();
    }
});

taskList.addEventListener('click', (e) => {
    const target = e.target;
    const taskId = target.dataset.id || target.closest('li').dataset.id;
    const action = target.dataset.action;

    if (!taskId) return;

    if (action === 'delete') {
        deleteTask(taskId);
    } else if (action === 'toggle') {
        toggleTaskCompletion(taskId);
    } else if (action === 'edit') {
        const taskItem = currentTasks.find(task => task.id === taskId);
        if (taskItem) {
            editTask(taskId, taskItem.content);
        }
    }
});

const initializeDashboard = async () => {
    try {
        loadingMessage.style.display = 'block';

        const tasks = await TaskManager.getTasksAsync();
        
        loadingMessage.style.display = 'none';

        currentTasks = tasks;
        renderTasks();

    } catch (error) {
        console.error("Gagal memuat data:", error);
        loadingMessage.textContent = 'Gagal memuat data.';
    }
};
initializeDashboard();
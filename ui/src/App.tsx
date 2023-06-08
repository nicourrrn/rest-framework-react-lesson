import axios from 'axios';
import { useEffect, useState } from 'react';
import './App.module.sass';

class Project{
    id: number;
    title: string;
    owner: string;
    
    public constructor(id: number, title: string, owner: string) {
        this.id = id;
        this.title = title;
        this.owner = owner;
    }
}

class Task {
    id: number;
    title: string;
    isDone: boolean;

    public constructor(id: number, title: string, isDone: boolean) {
        this.id = id;
        this.title = title;
        this.isDone = isDone;
    }
}

const App = () => {
    const [projects, setProjects] = useState<Array<Project>>([]);
    const [actualProject, setActualProject] = useState<number>(0); 
    const [tasks, setTasks] = useState<Array<Task>>([]);

    const updateProjects = async () => {
        let resp = await axios.get("http://localhost:8000/projects");
        setProjects(resp.data);
    }

    const updateTasks = async () => {
        let resp = await axios
            .get(`http://localhost:8000/projects/${actualProject}/tasks`);
        setTasks(resp.data);
    }
    
    useEffect(() => { updateProjects() }, []);
    useEffect(() => { updateTasks() }, [actualProject]);

    return (
    <div className="App">
        <div className='Projects'>
            <ul>
                {projects.map( (el: Project) => 
                    <li key={el.id} 
                        onClick={() => setActualProject(el.id)}> 
                    {el.title} </li>)}
            </ul>
        </div>
        <div className='Tasks'>
            {tasks.map((el: Task) => 
                <div className='task'>
                    <input type='checkbox' value='{el.isDone}'/>
                    {el.title}
                </div>
            )} 
        </div>
    </div>
    );
}

export default App;

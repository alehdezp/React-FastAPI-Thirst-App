import { BrowserRouter as Router } from "react-router-dom";
import { Header } from "./ui/Header";
import { Home } from "./ui/Home";
import styles from './App.module.css';

function App() {
    return (
        <Router>
            <div className={styles.App}>
                <Header />
                <Home />
                <button onClick={getDrinks}> Get drinks </button>
            </div>
        </Router>
    )
}




async function getDrinks(){
    // Make an async request to localhost and return de response in json
    console.log(await fetch('http://localhost:8000/drinks')
        .then(response => response.json())
        .then(data => data))
}   


export default App;

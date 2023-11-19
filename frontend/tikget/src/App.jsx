import { useState } from 'react'
import './App.css'
import { Navigate, Link, Route, Routes } from 'react-router-dom'
import Home from "./components/Home"
import Login from './components/Login'
import Register from './components/Register'



function App() {
  const [count, setCount] = useState(0)


  const [user, setUser] = useState('Robert')

  
  

  return (
    <>
      <div>
        <nav>
          <ul>
            <li>
              <Link to="/Home" >Home</Link>
            </li>
            <li>
              <Link to="/login">Login</Link>
            </li>
            <li>
              <Link to="/register">Register</Link>
            </li>
          </ul>
        </nav>
      </div>
      <Routes>
        <Route path="/*" element={<Navigate to="/home" />} />
        <Route path="/home" element={<Home />} />
        <Route path="/login" element={<Login />} />
        <Route path="/register" element={<Register />} />
      </Routes>
    </>
  )
}

export default App

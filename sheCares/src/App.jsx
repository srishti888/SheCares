import { useState } from 'react'
import Rectangle from './assets/Rectangle 10.svg'
import Card from './card'


function App() {
  const [email, setEmail] = useState('')
  const [password, setPassword] = useState('')

  return (
    <>
    <div>
     <img src={Rectangle} alt="" />
     <Card />
    </div> 
    
    </>
  )
}

export default App

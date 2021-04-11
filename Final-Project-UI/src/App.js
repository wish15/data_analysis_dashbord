import React from 'react'
import {BrowserRouter  as Router ,Route,Switch} from 'react-router-dom';
import Form from './Components/Form';
import Form2 from './Components/Form2';
import Sidebar from './Components/Sidebar';
import TextDash from './Components/Text/TextDash';
import VideoDash from './Components/Video/VideoDash';
import AudioDash from './Components/Audio/AudioDash';
function App() {
  return (
    <Router>
    <div className="App">
      <header style={{background:"#9be0b8",padding:"10px 25px"}}>
        <span style={{color:"forestgreen",fontSize:"22px"}}>Know Your Data</span>
      </header>

      
      
        
        <switch>

        
        <Route exact path="/">
        <TextDash/>
        </Route>
        <Route exact path="/video">
          <VideoDash/>
        </Route>
        <Route exact path="/audio">
          <AudioDash/>
        </Route>
        

        </switch>
        </div>
        
    
    </Router>
  );
}

export default App;

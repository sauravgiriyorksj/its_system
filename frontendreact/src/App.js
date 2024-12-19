import React from "react";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";

import Shape from "./shape";
import Quiz from "./quiz";

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Shape />} />
        <Route path="/quiz" element={<Quiz />} />
        
      </Routes>
    </Router>
  );
}

export default App;

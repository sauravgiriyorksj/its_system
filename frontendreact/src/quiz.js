import React, { useState, useEffect } from 'react';
import quizData from './quiz.json'; // Import the JSON file
import { useNavigate } from 'react-router-dom';

const Quiz = () => {
    const navigate = useNavigate();
  const [questions, setQuestions] = useState([]);
  const [currentQuestionIndex, setCurrentQuestionIndex] = useState(0);
  const [score, setScore] = useState(0);
  const [selectedOption, setSelectedOption] = useState(null);
  const [showResult, setShowResult] = useState(false);

  useEffect(() => {
    // Randomly select 10 questions from the quiz JSON
    const shuffledQuestions = quizData.quiz.sort(() => 0.5 - Math.random()).slice(0, 10);
    setQuestions(shuffledQuestions);
  }, []);

  const handleOptionClick = (option) => {
    setSelectedOption(option);
  };

  const handleNextQuestion = () => {
    if (selectedOption === questions[currentQuestionIndex].answer) {
      setScore(score + 1);
    }
    setSelectedOption(null);

    if (currentQuestionIndex < questions.length - 1) {
      setCurrentQuestionIndex(currentQuestionIndex + 1);
    } else {
      setShowResult(true);
    }
  };

  const handleRestart = () => {
    setCurrentQuestionIndex(0);
    setScore(0);
    setShowResult(false);
    setSelectedOption(null);
    const shuffledQuestions = quizData.quiz.sort(() => 0.5 - Math.random()).slice(0, 10);
    setQuestions(shuffledQuestions);
  };

  return (
    <div className="min-h-screen bg-gray-100 flex flex-col items-center p-6">
      <h1 className="text-4xl font-bold text-gray-800 mb-8">Quiz</h1>
      {showResult ? (
        <div className="text-center">
          <h2 className="text-2xl font-bold text-gray-800">Quiz Completed!</h2>
          <p className="mt-4 text-lg text-gray-600">
            Your score: <span className="text-blue-500">{score}</span> out of{" "}
            <span className="text-blue-500">{questions.length}</span>
          </p>
          <button
            className="mt-6 px-4 py-2 bg-blue-500 text-white rounded-md hover:bg-blue-600 mb-3"
            onClick={handleRestart}
          >
            Restart Quiz
          </button>
          <br></br>
          <br />
                    
                    {/* Back to Home Button */}
                    <button
      className="px-4 py-2 bg-blue-500 text-white rounded-md hover:bg-blue-600"
      onClick={() => navigate("/")}
    >
      Back to Home
    </button>
        </div>
      ) : (
        questions.length > 0 && (
          <div className="w-full max-w-3xl bg-white shadow-lg rounded-lg p-6">
            <h2 className="text-xl font-bold mb-4">
              Question {currentQuestionIndex + 1} of {questions.length}
            </h2>
            <p className="text-gray-700 mb-6">{questions[currentQuestionIndex].question}</p>
            <div className="grid gap-4">
              {Object.entries(questions[currentQuestionIndex].options).map(([key, value]) => (
                <button
                  key={key}
                  onClick={() => handleOptionClick(parseInt(key))}
                  className={`px-4 py-2 rounded-md text-left w-full ${
                    selectedOption === parseInt(key)
                      ? "bg-blue-500 text-white"
                      : "bg-gray-200 text-gray-800 hover:bg-gray-300"
                  }`}
                >
                  {value}
                </button>
              ))}
            </div>
            <button
              onClick={handleNextQuestion}
              disabled={selectedOption === null}
              className="mt-6 px-4 py-2 bg-blue-500 text-white rounded-md hover:bg-blue-600 disabled:bg-gray-300"
            >
              {currentQuestionIndex === questions.length - 1 ? "Finish Quiz" : "Next Question"}
            </button>
          </div>
        )
      )}
    </div>
  );
};

export default Quiz;

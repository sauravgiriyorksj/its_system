import React, { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom'; // Import useNavigate
import axios from 'axios';

// Component for individual Shape card
const ShapeCard = ({ shape, onClick }) => {
  return (
    <div
      className="bg-white shadow rounded-lg p-6 m-4 cursor-pointer"
      onClick={() => onClick(shape)}
    >
      {shape.image_url && (
        <img
          src={shape.image_url}
          alt={`${shape.name} illustration`}
          className="w-full h-40 rounded-md"
        />
      )}
      <h2 className="text-2xl font-bold mb-4 text-center">{shape.name}</h2>
    </div>
  );
};

// Component for Shape details modal
const ShapeDetails = ({ shape, onClose }) => {
  return (
    <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center">
      <div className="bg-white p-6 rounded-lg shadow-lg max-w-5xl w-full relative">
        <button
          onClick={onClose}
          className="bg-red-500 text-white px-4 py-2 rounded-full absolute top-4 right-4"
        >
          Close
        </button>
        <h2 className="text-2xl font-bold mb-4">{shape.name}</h2>
        <div className="mb-4">
          <h3 className="text-lg font-semibold">Properties:</h3>
          <p className="text-gray-700 whitespace-pre-wrap">{shape.property}</p>
        </div>
        <div className="mb-4">
          <h3 className="text-lg font-semibold">Applications:</h3>
          <p className="text-gray-700 whitespace-pre-wrap">{shape.application}</p>
        </div>
        <div className="mb-4">
          <h3 className="text-lg font-semibold">Formula:</h3>
          <p className="text-gray-700">{shape.formula}</p>
        </div>
      </div>
    </div>
  );
};

// Main Shape component
const Shape = () => {
  const [shapes, setShapes] = useState([]); // Default to empty array
  const [selectedShape, setSelectedShape] = useState(null);
  const navigate = useNavigate(); // Initialize useNavigate

  useEffect(() => {
    // Fetch data from the API
    axios
      .get('http://127.0.0.1:8000/shapes')
      .then((response) => {
        console.log(response.data); // Log response to check structure
        if (response.data && Array.isArray(response.data.shapes)) {
          setShapes(response.data.shapes);
        } else {
          console.error('Unexpected API response format:', response.data);
          setShapes([]); // Fallback to empty array if format is incorrect
        }
      })
      .catch((error) => {
        console.error('Error fetching shape data:', error);
        setShapes([]); // Fallback to empty array on error
      });
  }, []);

  const startQuiz = () => {
    navigate('/quiz'); // Navigate to /quiz route
  };

  return (
    <div className="min-h-screen bg-gray-100 flex flex-col items-center p-6 relative">
      {/* Start Quiz Button */}
      <button
        onClick={startQuiz}
        className="bg-green-500 text-white px-6 py-2 rounded-lg absolute top-4 right-4"
      >
        Start Quiz
      </button>

      {/* Title */}
      <h1 className="text-4xl font-bold text-gray-800 mb-8">Shape Details</h1>

      {/* Shapes Display */}
      <div className="flex flex-wrap justify-center">
        {shapes.length > 0 ? (
          shapes.map((shape, index) => (
            <ShapeCard key={index} shape={shape} onClick={setSelectedShape} />
          ))
        ) : (
          <p className="text-gray-600 text-lg">No shapes available to display.</p>
        )}
      </div>

      {/* Shape Details Modal */}
      {selectedShape && (
        <ShapeDetails
          shape={selectedShape}
          onClose={() => setSelectedShape(null)}
        />
      )}
    </div>
  );
};

export default Shape;

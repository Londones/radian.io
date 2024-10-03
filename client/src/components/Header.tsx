import React from "react";
import { Link } from "react-router-dom";

const Header: React.FC = () => {
  return (
    <header className="bg-white shadow-md">
      <div className="container mx-auto px-4 py-6 flex justify-between items-center">
        <Link to="/" className="text-2xl font-bold text-gray-800">
          Art Review
        </Link>
        <nav>
          <Link to="/" className="text-gray-600 hover:text-gray-800 mx-2">
            Home
          </Link>
          <Link to="/login" className="text-gray-600 hover:text-gray-800 mx-2">
            Login
          </Link>
          <Link
            to="/register"
            className="text-gray-600 hover:text-gray-800 mx-2"
          >
            Register
          </Link>
        </nav>
      </div>
    </header>
  );
};

export default Header;

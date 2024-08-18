"use client"
import React, { useState } from 'react';
import Link from 'next/link';

export default function Navbar() {
  const [isOpen, setIsOpen] = useState(false);

  return (
    <nav className="bg-gray-800 p-4">
      <div className="container mx-auto flex justify-between items-center">
        <div className="text-white font-bold">Logo</div>
        
        {/* Hamburger menu for mobile */}
        <div className="md:hidden">
          <button
            onClick={() => setIsOpen(!isOpen)}
            className="text-white focus:outline-none"
          >
            {isOpen ? 'Close' : 'Menu'}
          </button>
        </div>
        
        {/* Navigation links */}
        <div className={`md:flex ${isOpen ? 'block' : 'hidden'}`}>
          <Link href="/" className="block md:inline-block text-white hover:text-gray-300 mt-4 md:mt-0 md:ml-6">
            Home
          </Link>
          <Link href="/about" className="block md:inline-block text-white hover:text-gray-300 mt-4 md:mt-0 md:ml-6">
            About
          </Link>
          <Link href="/contact" className="block md:inline-block text-white hover:text-gray-300 mt-4 md:mt-0 md:ml-6">
            Contact
          </Link>
        </div>
      </div>
    </nav>
  );
};

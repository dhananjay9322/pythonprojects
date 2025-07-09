@tailwind base;
@tailwind components;
@tailwind utilities;

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Oxygen',
    'Ubuntu', 'Cantarell', 'Fira Sans', 'Droid Sans', 'Helvetica Neue',
    sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  background-color: #1c1c1c;
  overflow-x: hidden;
}

/* Custom scrollbar */
::-webkit-scrollbar {
  width: 8px;
}

::-webkit-scrollbar-track {
  background: #1c1c1c;
}

::-webkit-scrollbar-thumb {
  background: #f97316;
  border-radius: 4px;
}

::-webkit-scrollbar-thumb:hover {
  background: #ea580c;
}

/* Smooth scrolling */
html {
  scroll-behavior: smooth;
}

/* Custom animations */
@keyframes float {
  0%, 100% { transform: translateY(0px); }
  50% { transform: translateY(-20px); }
}

@keyframes glow {
  0%, 100% { box-shadow: 0 0 20px rgba(251, 146, 60, 0.3); }
  50% { box-shadow: 0 0 30px rgba(251, 146, 60, 0.6); }
}

@keyframes pulse-orange {
  0%, 100% { opacity: 0.7; }
  50% { opacity: 1; }
}

.animate-float {
  animation: float 3s ease-in-out infinite;
}

.animate-glow {
  animation: glow 2s ease-in-out infinite;
}

.animate-pulse-orange {
  animation: pulse-orange 2s ease-in-out infinite;
}

/* Custom cursor */
.cursor-custom {
  cursor: none;
}

.cursor-custom::after {
  content: '';
  position: fixed;
  top: 0;
  left: 0;
  width: 20px;
  height: 20px;
  background: radial-gradient(circle, #f97316 0%, transparent 70%);
  border-radius: 50%;
  pointer-events: none;
  z-index: 9999;
  opacity: 0.8;
  transform: translate(-50%, -50%);
}

/* Light theme styles */
.light {
  background-color: #f8fafc;
  color: #1f2937;
}

.light .bg-gray-900 {
  background-color: #f8fafc;
}

.light .bg-gray-800 {
  background-color: #e5e7eb;
}

.light .bg-gray-700 {
  background-color: #d1d5db;
}

.light .text-white {
  color: #1f2937;
}

.light .text-gray-300 {
  color: #6b7280;
}

.light .text-gray-400 {
  color: #9ca3af;
}

.light .border-gray-700 {
  border-color: #d1d5db;
}

.light .border-gray-800 {
  border-color: #e5e7eb;
}

/* Responsive design utilities */
@media (max-width: 768px) {
  .container {
    padding-left: 1rem;
    padding-right: 1rem;
  }
}

/* Project card hover effects */
.project-card {
  transition: all 0.3s ease;
}

.project-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 20px 40px rgba(0, 0, 0, 0.3);
}

/* Skill card animations */
.skill-card {
  position: relative;
  overflow: hidden;
}

.skill-card::before {
  content: '';
  position: absolute;
  top: -50%;
  left: -50%;
  width: 200%;
  height: 200%;
  background: linear-gradient(45deg, transparent, rgba(255, 255, 255, 0.1), transparent);
  transform: rotate(45deg);
  transition: all 0.5s;
  opacity: 0;
}

.skill-card:hover::before {
  animation: shimmer 1s ease-in-out;
  opacity: 1;
}

@keyframes shimmer {
  0% { transform: translateX(-100%) translateY(-100%) rotate(45deg); }
  100% { transform: translateX(100%) translateY(100%) rotate(45deg); }
}
document.addEventListener("DOMContentLoaded", () => {
    const users = []; // Array to hold user objects
  
    const signupForm = document.getElementById("signupForm");
    signupForm.addEventListener("submit", (event) => {
      
  
      const firstName = document.getElementById("firstName").value;
      const lastName = document.getElementById("lastName").value;
      const email = document.getElementById("email").value;
      const birthdate = document.getElementById("birthdate").value;
      const password = document.getElementById("password").value;
      const confirmPassword = document.getElementById("confirmPassword").value;
  
      // Validate form input
      if (!validateEmail(email)) {
        alert("Please enter a valid email address.");
        event.preventDefault();
        return false;
      }
  
      if (password !== confirmPassword) {
        event.preventDefault();
        alert("Passwords do not match.");
        return false;
      }
  
      // Calculate age
      const today = new Date();
      const birthDate = new Date(birthdate);
      let age = today.getFullYear() - birthDate.getFullYear();
      const monthDiff = today.getMonth() - birthDate.getMonth();
      if (monthDiff < 0 || (monthDiff === 0 && today.getDate() < birthDate.getDate())) {
        age--;
      }
  
      if (age < 16) {
        alert("You must be at least 16 years old to sign up.");
        event.preventDefault();
        return false;
      }
  
      return true;
    });
  
    const validateEmail = (email) => {
      const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      return regex.test(email);
    };
  });
  
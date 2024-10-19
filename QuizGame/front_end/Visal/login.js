document.getElementById('login-form').addEventListener('submit', function(event) {
  event.preventDefault();

  // Get the username from the form
  const username = document.getElementById('username').value;

  // Send a POST request to your backend server
  fetch('/login', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ username: username })
  })
  .then(response => response.json())
  .then(data => {
    // Handle the response from the server
    if (data.success) {
      // Redirect to the home page or display a welcome message
      window.location.href = 'home.html';
    } else {
      alert('Login failed. Please check your credentials.');
    }
  })
  .catch(error => {
    console.error('Error:', error);
  });
});

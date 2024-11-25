//Function to check credentials and redirect 
function POP() { // Get the username and password values 
    let username = document.querySelector('.username').value; let password = document.querySelector('.password').value; 
    // Check if the credentials are correct 
    if (username === "daksh" && password === "060513") { 
        // Redirect to the YouTube 
         window.location.href = "https://www.youtube.com/watch?v=s-K_PDc68BY"; 
    } else { 
            // Show an alert if the credentials are incorrect 
            alert("Incorrect username or password."); 
        } 
    } // Adding event listener for the button click 
    document.querySelector('.button').addEventListener('click', POP);

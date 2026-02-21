function toggleDoors() {
  const shoji = document.getElementById('shoji');
  shoji.classList.toggle('open');
}
setTimeout(() =>{
toggleDoors();
},700)

function goToUserTodo() {
            var username = document.getElementById('user').value.trim();
            if (username === "") {
                alert("Please enter a username first!");
                return;
            }
            // Use encodeURIComponent to handle spaces or special characters safely
            window.location.href = "/index/" + encodeURIComponent(username);
        }
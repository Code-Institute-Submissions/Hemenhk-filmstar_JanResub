const navLinks = document.getElementById('navLinks');
const message = document.getElementById('msg');


// Function showing navbar menu for smaller screens 
const showMenu = () => {
    navLinks.style.right = '0px';
}

// Function closing navbar menu for smaller screens 
const hideMenu = () => {
    navLinks.style.right = '-200px';
}

// Function for closing alert messages
const TimeOut = () => {
    const alert = new bootstrap.Alert(message);
    alert.close();
};

setTimeout(TimeOut, 3000);
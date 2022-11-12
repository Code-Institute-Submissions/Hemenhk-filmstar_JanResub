const navLinks = document.getElementById('navLinks');
const message = document.getElementById('msg');


// Function showing navbar menu for smaller screens 
const showMenu = () => {
    navLinks.style.right = '0';
}

// Function closing navbar menu for smaller screens 
const hideMenu = () => {
    navLinks.style.right = '-200px';
}
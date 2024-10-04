// Floating Particles Animation
const particlesContainer = document.querySelector('.particles');

for (let i = 0; i < 50; i++) {
    const particle = document.createElement('div');
    particle.classList.add('particle');
    particle.style.left = `${Math.random() * 100}vw`;
    particle.style.top = `${Math.random() * 100}vh`;
    particle.style.animationDuration = `${Math.random() * 5 + 2}s`;  // Varying duration
    particle.style.animationDelay = `${Math.random() * 2}s`;  // Varying start time
    particlesContainer.appendChild(particle);
}

// Cursor interaction with particles
document.addEventListener('mousemove', (event) => {
    const mouseX = event.clientX;
    const mouseY = event.clientY;

    document.querySelectorAll('.particle').forEach(particle => {
        const particleX = particle.offsetLeft + 5;
        const particleY = particle.offsetTop + 5;

        const distX = mouseX - particleX;
        const distY = mouseY - particleY;
        const distance = Math.sqrt(distX * distX + distY * distY);

        if (distance < 150) {
            const angle = Math.atan2(distY, distX);
            const moveX = Math.cos(angle) * 100;
            const moveY = Math.sin(angle) * 100;

            particle.style.transform = `translate(${moveX}px, ${moveY}px)`;
        } else {
            particle.style.transform = '';
        }
    });
});

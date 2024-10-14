// home.js

// Swipe gesture detection for mobile users
const swipeSections = document.querySelectorAll('.swipe-section');
let startX, endX;

function handleTouchStart(event) {
    startX = event.touches[0].clientX;
}

function handleTouchMove(event) {
    endX = event.touches[0].clientX;
}

function handleTouchEnd(event) {
    if (startX > endX + 50) {
        // Swipe left to the next section
        nextSection();
    } else if (startX < endX - 50) {
        // Swipe right to the previous section
        previousSection();
    }
}

swipeSections.forEach(section => {
    section.addEventListener('touchstart', handleTouchStart);
    section.addEventListener('touchmove', handleTouchMove);
    section.addEventListener('touchend', handleTouchEnd);
});

let currentSectionIndex = 0;

function nextSection() {
    if (currentSectionIndex < swipeSections.length - 1) {
        currentSectionIndex++;
        scrollToSection(currentSectionIndex);
    }
}

function previousSection() {
    if (currentSectionIndex > 0) {
        currentSectionIndex--;
        scrollToSection(currentSectionIndex);
    }
}

function scrollToSection(index) {
    swipeSections[index].scrollIntoView({ behavior: 'smooth' });
}

// Add click event listeners to each slide
const slides = document.querySelectorAll('.slide');

slides.forEach(slide => {
    slide.addEventListener('click', () => {
        const topic = slide.getAttribute('data-topic');
        // Redirect to the lesson page with the topic as a query parameter
        window.location.href = `lesson.html?topic=${topic}`;
    });
});

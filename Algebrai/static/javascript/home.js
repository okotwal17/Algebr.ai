// Swipe gesture detection for mobile users and dynamic lesson fetching

const swipeSections = document.querySelectorAll('.swipe-section');
let startX, endX;
let currentSectionIndex = 0;

// Handle swipe gestures
function handleTouchStart(event) {
    startX = event.touches[0].clientX;
}

function handleTouchMove(event) {
    endX = event.touches[0].clientX;
}

function handleTouchEnd() {
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

// Scroll to the next section
function nextSection() {
    if (currentSectionIndex < swipeSections.length - 1) {
        currentSectionIndex++;
        scrollToSection(currentSectionIndex);
    }
}

// Scroll to the previous section
function previousSection() {
    if (currentSectionIndex > 0) {
        currentSectionIndex--;
        scrollToSection(currentSectionIndex);
    }
}

// Scroll to the specified section
function scrollToSection(index) {
    swipeSections[index].scrollIntoView({ behavior: 'smooth' });
}

// Add click event listeners to each slide
const slides = document.querySelectorAll('.slide');

slides.forEach(slide => {
    slide.addEventListener('click', () => {
        const topic = slide.getAttribute('data-topic');
        window.location.href = `lesson.html?topic=${topic}`;
    });
});

// Fetch the topic from the URL
const urlParams = new URLSearchParams(window.location.search);
const topic = urlParams.get('topic');
const topicNameElement = document.getElementById('topic-name');
const lessonContentElement = document.getElementById('lesson-content');

// Update the topic name displayed on the page
topicNameElement.textContent = topic.replace(/_/g, ' ').replace(/\b\w/g, c => c.toUpperCase()); // Format for display

// Function to fetch lesson content dynamically
async function fetchLessonContent(topic) {
    const response = await fetch('/api/generate-lesson', { // Adjust this URL based on your server configuration
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ topic })
    });

    if (response.ok) {
        const data = await response.json();
        lessonContentElement.innerHTML = data.lesson; // Assuming the API returns lesson content in a field named 'lesson'
    } else {
        lessonContentElement.innerHTML = '<p>Error loading lesson content.</p>';
    }
}

// Call the function to fetch the lesson content
fetchLessonContent(topic);

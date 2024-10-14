// Fetch the topic from the URL
const urlParams = new URLSearchParams(window.location.search);
const topic = urlParams.get('topic');
const topicNameElement = document.getElementById('topic-name');
const lessonContentElement = document.getElementById('lesson-content');

// Update the topic name displayed on the page
topicNameElement.textContent = topic.replace(/_/g, ' ').replace(/\b\w/g, c => c.toUpperCase()); // Format for display

// Function to fetch lesson content from OpenAI API
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

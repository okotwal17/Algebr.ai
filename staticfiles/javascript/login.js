document.addEventListener("DOMContentLoaded", function() {
    console.log("JavaScript is working!");

    // Function to generate random bubbles (this part remains the same)
    function createBubble() {
        const bubble = document.createElement("div");
        bubble.classList.add("bubble");

        // Set random size, position, and color for the bubble
        const size = Math.random() * 50 + 20 + "px";
        bubble.style.width = size;
        bubble.style.height = size;
        bubble.style.left = Math.random() * 100 + "vw";
        bubble.style.top = Math.random() * 100 + "vh";

        // Random color
        const colors = ['#ff6b6b', '#f7ff6b', '#6bff6b', '#6bbfff', '#ff6bbf'];
        bubble.style.backgroundColor = colors[Math.floor(Math.random() * colors.length)];

        // Add the bubble to the body
        document.body.appendChild(bubble);

        // Make bubble disappear on mouse hover
        bubble.addEventListener("mouseenter", function() {
            bubble.style.opacity = "0";
            setTimeout(() => {
                bubble.remove(); // Remove bubble after fade-out
            }, 500);
        });

        // Remove bubble after its life ends
        setTimeout(() => {
            bubble.remove();
        }, 8000); // Adjust time for the bubbles to disappear naturally
    }

    // Create a new bubble every 0.5 second
    setInterval(createBubble, 500);

    // Automatically dismiss error messages after a few seconds
    const errorMessages = document.querySelectorAll('.error-messages li');
    if (errorMessages.length > 0) {
        setTimeout(() => {
            errorMessages.forEach(message => {
                message.style.opacity = "0"; // Smoothly fade out error messages
                setTimeout(() => {
                    message.remove(); // Remove the message after fade-out
                }, 500); // Matches the fade-out duration
            });
        }, 5000); // Time before error messages disappear (5 seconds)
    }
});

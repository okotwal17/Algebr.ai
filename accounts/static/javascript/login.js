document.addEventListener("DOMContentLoaded", () => {
    const background = document.createElement("div");
    background.classList.add("background");
    document.body.appendChild(background);

    // Generate bubbles with continuous up-and-down animation
    for (let i = 0; i < 30; i++) {
        const bubble = document.createElement("div");
        bubble.classList.add("bubble");

        const size = `${Math.random() * 4 + 4}rem`;
        const position = `${Math.random() * 100}%`;
        const time = `${Math.random() * 6 + 4}s`;
        const delay = `${Math.random() * 4}s`;

        bubble.style.setProperty("--size", size);
        bubble.style.setProperty("--position", position);
        bubble.style.setProperty("--time", time);
        bubble.style.setProperty("--delay", delay);

        background.appendChild(bubble);
    }

    // Add wavy animation effect to the background
    background.style.setProperty(
        "background",
        "linear-gradient(145deg, #0e2a47, #193c5b)"
    );
    background.style.animation = "waveBackground 10s infinite linear";
});

document.addEventListener("DOMContentLoaded", () => {
    const background = document.createElement("div");
    background.classList.add("background");
    document.body.appendChild(background);

    // Generate bubbles
    for (let i = 0; i < 30; i++) {
        const bubble = document.createElement("div");
        bubble.classList.add("bubble");

        bubble.style.setProperty("--size", `${Math.random() * 4 + 4}rem`);
        bubble.style.setProperty("--position", `${Math.random() * 100}%`);
        bubble.style.setProperty("--time", `${Math.random() * 6 + 4}s`);
        bubble.style.setProperty("--delay", `${Math.random() * 4}s`);

        background.appendChild(bubble);
    }
});

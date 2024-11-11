document.addEventListener("DOMContentLoaded", () => {
    const background = document.createElement("div");
    background.classList.add("background");
    document.body.appendChild(background);

    for (let i = 0; i < 20; i++) {
        const bubble = document.createElement("div");
        bubble.classList.add("bubble");

        bubble.style.setProperty("--size", `${Math.random() * 5 + 5}rem`);
        bubble.style.setProperty("--position", `${Math.random() * 100}%`);
        bubble.style.setProperty("--time", `${Math.random() * 3 + 2}s`);
        bubble.style.setProperty("--delay", `${Math.random() * 3}s`);

        background.appendChild(bubble);
    }
});

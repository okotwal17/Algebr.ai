document.addEventListener('DOMContentLoaded', () => {
    const loginBox = document.querySelector('.login-box');
    const button = document.querySelector('button');
    const inputs = document.querySelectorAll('input');

    // Dynamic background color shift for input focus
    inputs.forEach(input => {
        input.addEventListener('focus', () => {
            loginBox.style.boxShadow = '0 0 20px rgba(255, 95, 109, 0.8)';
        });
        input.addEventListener('blur', () => {
            loginBox.style.boxShadow = '0 4px 10px rgba(0, 0, 0, 0.1)';
        });
    });

    // Button ripple effect
    button.addEventListener('click', (e) => {
        const ripple = document.createElement('span');
        ripple.classList.add('ripple');
        ripple.style.left = `${e.offsetX}px`;
        ripple.style.top = `${e.offsetY}px`;
        button.appendChild(ripple);

        setTimeout(() => ripple.remove(), 600);
    });

    // Floating animations for background
    const bubbles = Array.from({ length: 20 }, () => {
        const bubble = document.createElement('div');
        bubble.classList.add('bubble');
        document.body.appendChild(bubble);
        return bubble;
    });

    function animateBubbles() {
        bubbles.forEach(bubble => {
            bubble.style.left = `${Math.random() * 100}vw`;
            bubble.style.animationDuration = `${3 + Math.random() * 7}s`;
            bubble.style.animationDelay = `${Math.random() * 2}s`;
        });
    }
    animateBubbles();
});

// Bubble styles
const styleSheet = document.createElement('style');
styleSheet.innerHTML = `
    .bubble {
        position: absolute;
        bottom: -50px;
        width: 20px;
        height: 20px;
        background: rgba(255, 255, 255, 0.2);
        border-radius: 50%;
        animation: float-up linear infinite;
    }

    @keyframes float-up {
        from { transform: translateY(0); }
        to { transform: translateY(-200vh); }
    }

    .ripple {
        position: absolute;
        transform: translate(-50%, -50%);
        border-radius: 50%;
        background: rgba(255, 255, 255, 0.4);
        pointer-events: none;
        animation: ripple-effect 0.6s ease-out;
    }

    @keyframes ripple-effect {
        from { transform: scale(0); opacity: 1; }
        to { transform: scale(5); opacity: 0; }
    }
`;
document.head.appendChild(styleSheet);

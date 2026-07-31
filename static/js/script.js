// ===============================
// CloudShield AI Dashboard Script
// ===============================

// Auto Refresh Dashboard
setInterval(function () {
    location.reload();
}, 10000);

// Card Hover Animation
document.querySelectorAll(".cyber-card").forEach(card => {

    card.addEventListener("mouseenter", function () {

        this.style.transform = "translateY(-5px) scale(1.02)";

    });

    card.addEventListener("mouseleave", function () {

        this.style.transform = "translateY(0) scale(1)";

    });

});

// Counter Animation
document.querySelectorAll(".card-number").forEach(counter => {

    const target = parseInt(counter.innerText);

    if (!isNaN(target)) {

        let count = 0;

        const speed = Math.ceil(target / 50);

        const update = () => {

            count += speed;

            if (count >= target) {

                counter.innerText = target;

            } else {

                counter.innerText = count;

                requestAnimationFrame(update);

            }

        };

        update();

    }

});

// Current Date & Time
function updateClock() {

    const now = new Date();

    console.log("Dashboard Updated:", now.toLocaleString());

}

setInterval(updateClock, 1000);

updateClock();
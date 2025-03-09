document.addEventListener("DOMContentLoaded", function () {
    const runeContainer = document.createElement("div");
    runeContainer.classList.add("eldritch-background");
    document.body.appendChild(runeContainer);

    const runes = ["ᛟ", "ᚨ", "ᛉ", "ᛏ", "ᛖ", "ᛝ", "ᚠ", "ᛇ", "ᚾ", "ᛚ", "⚛", "☾", "☉"];
    const runeCount = 15; // Number of runes

    for (let i = 0; i < runeCount; i++) {
        const rune = document.createElement("span");
        rune.classList.add("rune");
        rune.innerText = runes[Math.floor(Math.random() * runes.length)];

        // Random positioning
        rune.style.left = Math.random() * 100 + "vw";
        rune.style.top = Math.random() * 100 + "vh";

        // Random animation delay
        rune.style.animationDelay = Math.random() * 5 + "s";

        // Random size variation
        rune.style.fontSize = Math.random() * 2 + 2 + "rem";

        runeContainer.appendChild(rune);
    }
});

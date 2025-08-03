document.addEventListener('DOMContentLoaded', function() {
    const pageCounts = document.querySelectorAll('.page-count');

    pageCounts.forEach(function(element) {
        const pageCount = parseInt(element.textContent, 10);
        const readingSpeed = 40; // pages par heure, ajustez selon votre besoin
        const readingTime = Math.ceil(pageCount / readingSpeed);

        const readingTimeElement = document.createElement('span');
        readingTimeElement.textContent = ` (~${readingTime}h de lecture)`;
        element.parentNode.appendChild(readingTimeElement);
    });
});
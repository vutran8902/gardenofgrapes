document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('subscription-form');
    const subscriptionSection = document.getElementById('subscription-section');
    const thankYouSection = document.getElementById('thank-you-section');
    const returnHomeButton = document.getElementById('return-home');

    form.addEventListener('submit', function(e) {
        e.preventDefault();
        const name = document.getElementById('name').value;
        const email = document.getElementById('email').value;

        // Here you would typically send the data to your server
        // For now, we'll just log it to the console
        console.log('Submitted:', { name, email });

        // Show the thank you section
        subscriptionSection.style.display = 'none';
        thankYouSection.style.display = 'block';
    });

    returnHomeButton.addEventListener('click', function() {
        // Return to the subscription form
        thankYouSection.style.display = 'none';
        subscriptionSection.style.display = 'block';
        form.reset(); // Clear the form fields
    });
});

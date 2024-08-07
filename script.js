document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('subscription-form');
    const subscriptionSection = document.getElementById('subscription-section');
    const thankYouSection = document.getElementById('thank-you-section');
    const returnHomeButton = document.getElementById('return-home');

    form.addEventListener('submit', function(e) {
        e.preventDefault();
        const name = document.getElementById('name').value;
        const email = document.getElementById('email').value;

        // Send the data to the server
        fetch('/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
            },
            body: `name=${encodeURIComponent(name)}&email=${encodeURIComponent(email)}`
        }).then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok');
            }
            return response.json();
        }).then(data => {
            if (data.status === 'success') {
                // Show the thank you section
                subscriptionSection.style.display = 'none';
                thankYouSection.style.display = 'block';
            } else {
                throw new Error('Submission failed');
            }
        }).catch(error => {
            console.error('Error:', error);
            alert('An error occurred. Please try again.');
        });
    });

    returnHomeButton.addEventListener('click', function() {
        // Return to the subscription form
        thankYouSection.style.display = 'none';
        subscriptionSection.style.display = 'block';
        form.reset(); // Clear the form fields
    });
});

/* Additional JavaScript functionality for WAB AI Assistant */

// Handle form submission with loading state
document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('form');
    const button = document.querySelector('.btn');
    const input = document.getElementById('user_input');
    
    // Focus on input field
    input.focus();
    
    // Add loading state to form submission
    form.addEventListener('submit', function(e) {
        // Show loading state
        button.innerHTML = '🤔 Thinking...';
        button.disabled = true;
        
        // Re-enable after a delay (in case of quick response)
        setTimeout(() => {
            button.innerHTML = 'Ask WAB AI';
            button.disabled = false;
        }, 3000);
    });
    
    // Enter key handling
    input.addEventListener('keypress', function(e) {
        if (e.key === 'Enter') {
            form.submit();
        }
    });
    
    // Auto-resize textarea if we convert input to textarea later
    function autoResize(element) {
        element.style.height = 'auto';
        element.style.height = element.scrollHeight + 'px';
    }
});

// Smooth scroll to response
function scrollToResponse() {
    const responseContainer = document.querySelector('.response-container');
    if (responseContainer) {
        responseContainer.scrollIntoView({ 
            behavior: 'smooth', 
            block: 'start' 
        });
    }
}

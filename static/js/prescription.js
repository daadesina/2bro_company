// alert('Hello')

const prescription_action = document.getElementById('prescription_action');
const prescription_checkbox = document.getElementById('prescription_checkbox');

prescription_action.style.opacity = '0.3';

// Function to update the style dynamically
function updatePrescriptionAction() {
  if (prescription_checkbox.checked) {
    prescription_action.style.opacity = '1';
  } else {
    prescription_action.style.opacity = '0.3'; // Reset opacity when unchecked
  }
}

// Add event listener to the checkbox
prescription_checkbox.addEventListener('change', updatePrescriptionAction);

// Initialize on page load
updatePrescriptionAction();



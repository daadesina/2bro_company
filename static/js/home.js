const profile_btn = document.getElementById('profile_btn');
const caregiver_btn = document.getElementById('caregiver_btn');
const settings_btn = document.getElementById('settings_btn');

const profile_part = document.getElementById('profile_part');
const caregiver_part = document.getElementById('caregiver_part');

profile_part.style.display = 'none';
caregiver_part.style.display = 'none';

profile_btn.addEventListener('click', function() {
    if (profile_part.style.display == 'none'){
        profile_part.style.display = '';
    }
    else {
        profile_part.style.display = 'none';
    }
});

caregiver_btn.addEventListener('click', function() {
    if (caregiver_part.style.display == 'none'){
        caregiver_part.style.display = '';
    }
    else {
        caregiver_part.style.display = 'none';
    }
});
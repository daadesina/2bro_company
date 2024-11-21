// side bar
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



// create participant
const create_parti_btn = document.getElementById('create_parti_btn');
let home_div = document.getElementById('home_div');
const create_parti_div = document.getElementById('create_parti_div');
const cancle_parti_btn = document.getElementById('cancle_parti_btn');


function styleHomeFunc (){
    home_div.style.position = 'absolute';
    home_div.style.inset = 0;
    home_div.style.opacity = 0.5;
};

function styleCreateFunc () {
    create_parti_div.style.position = 'absolute';
    create_parti_div.style.inset = 0;
    create_parti_div.style.backgroundColor = 'rgb(239 68 68 / var(--tw-bg-opacity, 1))';
    create_parti_div.style.display = 'block';
    

}

function styleCancelFunc() {
    home_div.style.position = '';
    home_div.style.inset = '';
    home_div.style.opacity = '';
    create_parti_div.style.position = '';
    create_parti_div.style.inset ='';
    create_parti_div.style.backgroundColor = '';
    create_parti_div.style.display = 'none';
;}

create_parti_btn.addEventListener('click', function () {
    styleHomeFunc();
    styleCreateFunc();
});


cancle_parti_btn.addEventListener('click', function () {
    styleCancelFunc();
});



// dose time

function addDoseTimes() {
    const dose = parseInt(document.getElementById('dose').value);
    const doseTimesDiv = document.getElementById('dose-times');
    doseTimesDiv.innerHTML = ''; // Clear previous fields

    for (let i = 1; i <= dose; i++) {
        const label = document.createElement('label');
        label.style.color = 'white';
        label.textContent = `Dose Time ${i}:`;
        doseTimesDiv.appendChild(label);

        const input = document.createElement('input');
        input.style.border = '2px solid white';
        input.style.borderRadius = '10px';
        input.style.backgroundColor = 'inherit';
        input.type = 'time';
        input.name = `dose_time_${i}`;
        input.required = true;
        doseTimesDiv.appendChild(input);

        doseTimesDiv.appendChild(document.createElement('br'));
    }
}
let startTime, elapsedTime = 0, interval;
const display = document.getElementById('display');
const startStopBtn = document.getElementById('startStopBtn');
const lapsList = document.getElementById('lapsList');

startStopBtn.addEventListener('click', () => {
    if (interval) {
        clearInterval(interval);
        interval = null;
        startStopBtn.textContent = 'Start';
    } else {
        startTime = Date.now() - elapsedTime;
        interval = setInterval(updateTime, 10);
        startStopBtn.textContent = 'Stop';
    }
});

document.getElementById('resetBtn').addEventListener('click', () => {
    clearInterval(interval);
    interval = null;
    elapsedTime = 0;
    display.textContent = '00:00:00:00';
    startStopBtn.textContent = 'Start';
    lapsList.innerHTML = '';
});

document.getElementById('lapBtn').addEventListener('click', () => {
    if (interval) {
        const lapTime = display.textContent;
        const li = document.createElement('li');
        li.textContent = lapTime;
        lapsList.appendChild(li);
    }
});

function updateTime() {
    elapsedTime = Date.now() - startTime;
    display.textContent = formatTime(elapsedTime);
}

function formatTime(ms) {
    const milliseconds = Math.floor((ms % 1000) / 10);
    const seconds = Math.floor((ms / 1000) % 60);
    const minutes = Math.floor((ms / (1000 * 60)) % 60);
    const hours = Math.floor(ms / (1000 * 60 * 60));

    return `${pad(hours)}:${pad(minutes)}:${pad(seconds)}:${pad(milliseconds)}`;
}

function pad(num) {
    return num.toString().padStart(2, '0');
}
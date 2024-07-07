$(function() {
    $('#date').text(moment().format('MMMM Do YYYY'));
    $('#timestamp').text(moment().format('h:mm:ss a'));
    $('#start-btn').click(function() {
        startStopWatch();
    });
    $('#pause-btn').click(function() {
        pauseStopWatch();
    });
    $('#stop-btn').click(function() {
        stopStopWatch();
    });
    alert('Page Ready!');
});

let stopwatchInterval;
let stopwatchRunning = false;
let paused = false;
let elapsedTime = 0;
let startTime;

function startStopWatch() {
    if (!stopwatchRunning) {
        startTime = Date.now();
        stopwatchInterval = setInterval(updateStopWatch, 1000);
        stopwatchRunning = true;
        paused = false;
    }
}

function pauseStopWatch() {
    if (stopwatchRunning && !paused) {
        clearInterval(stopwatchInterval);
        elapsedTime = Date.now() - startTime;
        paused = true;
        stopwatchRunning = false;
    }
}

function stopStopWatch() {
    clearInterval(stopwatchInterval);
    stopwatchRunning = false;
    paused = false;
    elapsedTime = 0;
    $('#stopwatch').text("00:00:00");
}

function updateStopWatch() {
    let elapsedTime = Date.now() - startTime;
    let hours = Math.floor(elapsedTime / (1000 * 60 * 60));
    let minutes = Math.floor((elapsedTime % (1000 * 60 * 60)) / (1000 * 60));
    let seconds = Math.floor((elapsedTime % (1000 * 60)) / 1000);
    let formattedTime = pad(hours, 2) + ":" + pad(minutes, 2) + ":" + pad(seconds, 2);
    $('#stopwatch').text(formattedTime);
}

function pad(num, size) {
    let s = num + "";
    while (s.length < size)
        s = "0" + s;
    return s;
}

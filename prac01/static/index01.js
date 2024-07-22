let $date = $('#date');
let $timestamp = $('#timestamp');
let date = new Date();
let timestamp = moment().from(currentDate);
let countdownTime = 10; // Initial time in seconds
let intervalId = setInterval( () => {
    countdownTime--;
    $('#formattedDate').text('Time: ' + countdownTime + ' seconds...');
    if (countdownTime <= 0) {
        clearInterval(intervalId);  // Stop the interval when time reaches zero
    }
}, 1000);   // Interval duration 1 second

$(function() {
	$date.text('The local date and time is: ' + date);
	$timestamp.text('That was ' + timestamp);
    
	let currentDate = moment().format('YYYY-MM-DD HH:mm:ss');
	$('#formattedDate').text('Current Date: ' + currentDate);
	
	alert('Page ready!');
});

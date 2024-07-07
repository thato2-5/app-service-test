$(function() {
	$date.text('The local date and time is: ' + date);
	$timestamp.text('That was ' + timestamp);
    
	let currentDate = moment().format('YYYY-MM-DD HH:mm:ss');
	$('#formattedDate').text('Current Date: ' + currentDate);
	
	alert('Page ready!');
});

let $date = $('#date');
let $timestamp = $('#timestamp');
let date = new Date();
let timestamp = moment().from(currentDate);

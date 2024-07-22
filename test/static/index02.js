$(document).ready(function() {
    $('#showLoadingBtn').on('click', function() {
        showLoading();
    });

    $('#hideLoadingBtn').on('click', function() {
        hideLoading();
    });

    function showLoading() {
        $('#loading-overlay').css('visibility', 'visible');
        setTimeout(hideLoading, 3500); // Hide after 3.5 seconds
    }

    function hideLoading() {
        $('#loading-overlay').css('visibility', 'hidden');
    }
});
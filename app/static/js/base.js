$(document).ready(function () {
    $("#myForm").submit(function (event) {
        event.preventDefault(); // Prevent the form from submitting via the browser
        $.ajax({
            url: '/process/',
            type: 'post',
            data: {
                inputData: $('#inputData').val(),
                csrfmiddlewaretoken: '{{ csrf_token }}'  // Ensure CSRF token is sent with POST request
            },
            success: function (response) {
                $("#output").html(response.outputData);
            }
        });
    });
});

function moveFormToBottom() {
    // Change the form style to position it at the bottom
    $("#myForm").css({
        "transition": "transform 0.5s ease",
        "transform": "translateY(45vh)"
    });
    // Adjust textarea height if necessary
    $("#inputData").css("height", "auto");
}

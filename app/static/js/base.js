$(document).ready(function () {
    $("#myForm").submit(function (event) {
        event.preventDefault(); // Prevent the form from submitting via the browser
        $.ajax({
            url: '/gpt4turbo/',
            type: 'post',
            data: {
                inputData: $('#inputData').val(),
                csrfmiddlewaretoken: '{{ csrf_token }}'  // Ensure CSRF token is sent with POST request
            },
            success: function (response) {
                $("#gpt4turbooutput").html(response.outputData);
                $("#gpt4turbo").css({
                    "background-color": "green",
                });
            }
        });
        $.ajax({
            url: '/gpt4/',
            type: 'post',
            data: {
                inputData: $('#inputData').val(),
                csrfmiddlewaretoken: '{{ csrf_token }}'  // Ensure CSRF token is sent with POST request
            },
            success: function (response) {
                $("#gpt4output").html(response.outputData);
                $("#gpt4").css({
                    "background-color": "green",
                });
            }
        });
        $.ajax({
            url: '/gpt35turbo/',
            type: 'post',
            data: {
                inputData: $('#inputData').val(),
                csrfmiddlewaretoken: '{{ csrf_token }}'  // Ensure CSRF token is sent with POST request
            },
            success: function (response) {
                $("#gpt35turbooutput").html(response.outputData);
                $("#gpt35turbo").css({
                    "background-color": "green",
                });
            }
        });
        $.ajax({
            url: '/claude3opus/',
            type: 'post',
            data: {
                inputData: $('#inputData').val(),
                csrfmiddlewaretoken: '{{ csrf_token }}'  // Ensure CSRF token is sent with POST request
            },
            success: function (response) {
                $("#claude3opusoutput").html(response.outputData);
                $("#claude3opus").css({
                    "background-color": "green",
                });
            }
        });
        $.ajax({
            url: '/claude21/',
            type: 'post',
            data: {
                inputData: $('#inputData').val(),
                csrfmiddlewaretoken: '{{ csrf_token }}'  // Ensure CSRF token is sent with POST request
            },
            success: function (response) {
                $("#claude21output").html(response.outputData);
                $("#claude21").css({
                    "background-color": "green",
                });
            }
        });
        $.ajax({
            url: '/mistral7b/',
            type: 'post',
            data: {
                inputData: $('#inputData').val(),
                csrfmiddlewaretoken: '{{ csrf_token }}'  // Ensure CSRF token is sent with POST request
            },
            success: function (response) {
                $("#mistral7boutput").html(response.outputData);
                $("#mistral7b").css({
                    "background-color": "green",
                });
            }
        });
        $.ajax({
            url: '/mixtral8x7b/',
            type: 'post',
            data: {
                inputData: $('#inputData').val(),
                csrfmiddlewaretoken: '{{ csrf_token }}'  // Ensure CSRF token is sent with POST request
            },
            success: function (response) {
                $("#mixtral8x7boutput").html(response.outputData);
                $("#mixtral8x7b").css({
                    "background-color": "green",
                });
            }
        });
        $.ajax({
            url: '/sonarmedium/',
            type: 'post',
            data: {
                inputData: $('#inputData').val(),
                csrfmiddlewaretoken: '{{ csrf_token }}'  // Ensure CSRF token is sent with POST request
            },
            success: function (response) {
                $("#sonarmediumoutput").html(response.outputData);
                $("#sonarmedium").css({
                    "background-color": "green",
                });
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

function visible(model) {
    $("#gpt4turbooutput").css({
        "display": "none",
    });
    $("#gpt4output").css({
        "display": "none",
    });
    $("#gpt35turbooutput").css({
        "display": "none",
    });
    $("#claude3opusoutput").css({
        "display": "none",
    });
    $("#claude21output").css({
        "display": "none",
    });
    $("#mistral7boutput").css({
        "display": "none",
    });
    $("#mixtral8x7boutput").css({
        "display": "none",
    });
    $("#sonarmediumoutput").css({
        "display": "none",
    });
    output = $('#' + model + 'output');
    output.css({
        "display": "block",
    });
}
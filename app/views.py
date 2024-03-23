from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


def home(request):
    return render(request, "base.html")

@require_POST
@csrf_exempt
def process_string(request):
    # if request.method == 'POST':
    #     form = YourForm(request.POST)
    #     if form.is_valid():
    #         # Extract the string from the form
    #         input_string = form.cleaned_data['input_string_field_name']
            
    #         # Process the string here (this is your backend processing)
    #         processed_string = input_string.upper()  # Example processing

    #         # Pass the processed string back to the frontend
    #         return render(request, 'app_name/result_template.html', {'processed_string': processed_string})
    # else:
    #     form = YourForm()

    # return render(request, 'app_name/index.html', {'form': form})


    input_data = request.POST.get('inputData')
    # Process your data here
    processed_data = input_data.upper()  # Example processing
    return JsonResponse({'outputData': "processed_data"})
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from openai import OpenAI
import anthropic
import threading
import time
import os

# Create your views here.


def home(request):
    return render(request, "base.html")

@require_POST
@csrf_exempt
def process_string(request):


    question = request.POST.get('inputData')
    # Process your data here

    def askOpenAI(question, model_name, answers):
        completion = client.chat.completions.create(
        model = model_name,
        messages = [
            {"role": "system", "content": "You are a helpful assistant"},
            {"role": "user", "content": question}
        ]
        )

        answers_dict[model_name] = completion.choices[0].message.content

    def askAnthropic(question, model_name, answers):
        message = client.messages.create(
            model = model_name,
            max_tokens = 1000,
            temperature = 0.0,
            system = "Respond only in Yoda-speak.",
            messages = [
                {"role": "user", "content": "How are you today?"}
            ]
        )

        answers[model_name] = message.content[0]

    answers_dict = dict()

    # OpenAI
    client = OpenAI(api_key = os.getenv('OPENAI_API_KEY'))

    models = ["gpt-4-turbo-preview", "gpt-4", "gpt-3.5-turbo"]

    threads = []

    for model in models:
        thread = threading.Thread(target = askOpenAI, args = (question, model, answers_dict))
        threads.append(thread)
        thread.start()
        time.sleep(1)

    for thread in threads:
        thread.join()

    # Claude
    client = anthropic.Anthropic(api_key = os.getenv('CLAUDE_API_KEY'))

    models = ["claude-3-opus-20240229"]

    threads = []

    for model in models:
        thread = threading.Thread(target = askAnthropic, args = (question, model, answers_dict))
        threads.append(thread)
        thread.start()
        time.sleep(1)

    for thread in threads:
        thread.join()


    for value in answers_dict.values():
        print(type(value))
    # Example processing
    return JsonResponse({'outputData': answers_dict["gpt-4"]})
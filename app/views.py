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

answers_dict = dict()

def home(request):
    return render(request, "base.html")

@require_POST
@csrf_exempt
def gpt4turbo(request):
    question = request.POST.get('inputData')
    client = OpenAI(api_key = os.getenv('OPENAI_API_KEY'))
    model_name = "gpt-4-turbo-preview"

    completion = client.chat.completions.create(
        model = model_name,
        messages = [
            {"role": "system", "content": "You are a helpful assistant"},
            {"role": "user", "content": question}
        ]
        )

    answers_dict[model_name] = completion.choices[0].message.content

    return JsonResponse({'outputData': answers_dict[model_name]})

@require_POST
@csrf_exempt
def gpt4(request):
    question = request.POST.get('inputData')
    client = OpenAI(api_key = os.getenv('OPENAI_API_KEY'))
    model_name = "gpt-4"

    completion = client.chat.completions.create(
        model = model_name,
        messages = [
            {"role": "system", "content": "You are a helpful assistant"},
            {"role": "user", "content": question}
        ]
        )

    answers_dict[model_name] = completion.choices[0].message.content

    return JsonResponse({'outputData': answers_dict[model_name]})

@require_POST
@csrf_exempt
def gpt35turbo(request):
    question = request.POST.get('inputData')
    client = OpenAI(api_key = os.getenv('OPENAI_API_KEY'))
    model_name = "gpt-3.5-turbo"

    completion = client.chat.completions.create(
        model = model_name,
        messages = [
            {"role": "system", "content": "You are a helpful assistant"},
            {"role": "user", "content": question}
        ]
        )

    answers_dict[model_name] = completion.choices[0].message.content

    return JsonResponse({'outputData': answers_dict[model_name]})

@require_POST
@csrf_exempt
def claude3opus(request):
    question = request.POST.get('inputData')
    client = anthropic.Anthropic(api_key = os.getenv('CLAUDE_API_KEY'))
    model_name = "claude-3-opus-20240229"

    message = client.messages.create(
        model = model_name,
        max_tokens = 4096,
        temperature = 0.0,
        system = "You are a helpful assistant.",
        messages = [
            {"role": "user", "content": question}
    ]
    )

    answers_dict[model_name] = message.content[0].text

    return JsonResponse({'outputData': answers_dict[model_name]})

@require_POST
@csrf_exempt
def claude21(request):
    question = request.POST.get('inputData')
    client = anthropic.Anthropic(api_key = os.getenv('CLAUDE_API_KEY'))
    model_name = "claude-2.1"

    message = client.messages.create(
        model = model_name,
        max_tokens = 4096,
        temperature = 0.0,
        system = "You are a helpful assistant.",
        messages = [
            {"role": "user", "content": question}
    ]
    )

    answers_dict[model_name] = message.content[0].text

    return JsonResponse({'outputData': answers_dict[model_name]})

@require_POST
@csrf_exempt
def mistral7b(request):
    question = request.POST.get('inputData')
    client = OpenAI(api_key=os.getenv('PERPLEXITY_API_KEY'), base_url="https://api.perplexity.ai")
    model_name = "mistral-7b-instruct"

    completion = client.chat.completions.create(
    model = model_name,
    messages = [
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": question}
    ]
    )

    answers_dict[model_name] = completion.choices[0].message.content

    return JsonResponse({'outputData': answers_dict[model_name]})

@require_POST
@csrf_exempt
def mixtral8x7b(request):
    question = request.POST.get('inputData')
    client = OpenAI(api_key=os.getenv('PERPLEXITY_API_KEY'), base_url="https://api.perplexity.ai")
    model_name = "mixtral-8x7b-instruct"

    completion = client.chat.completions.create(
    model = model_name,
    messages = [
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": question}
    ]
    )

    answers_dict[model_name] = completion.choices[0].message.content
    
    return JsonResponse({'outputData': answers_dict[model_name]})

@require_POST
@csrf_exempt
def sonarmedium(request):
    question = request.POST.get('inputData')
    client = OpenAI(api_key=os.getenv('PERPLEXITY_API_KEY'), base_url="https://api.perplexity.ai")
    model_name = "sonar-medium-chat"

    completion = client.chat.completions.create(
    model = model_name,
    messages = [
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": question}
    ]
    )

    answers_dict[model_name] = completion.choices[0].message.content
    
    return JsonResponse({'outputData': answers_dict[model_name]})

@require_POST
@csrf_exempt
def confer(request):
    question = request.POST.get('inputData')
    client = anthropic.Anthropic(api_key = os.getenv('CLAUDE_API_KEY'))
    model_name = "claude-3-opus-20240229"

    final_question = "I want you to consider the next few responses from various other AI. The responses are not necessarily correct or incorrect; it is up to you whether they influence your next answer or not.\n"
    for key, value in answers_dict.items():
        final_question += f"{key} wrote this answer: \n {value}"

    final_question += f"Having seen these other responses (including your own), I want you to answer this question: {question}.  You may allow the other AI's to influence your answer if you think it is an improvement, but you are not obliged to do so."

    message = client.messages.create(
        model = model_name,
        max_tokens = 4096,
        temperature = 0.0,
        system = "You are a helpful assistant. You can consider the input of other AI's to help you find the best answer.",
        messages = [
            {"role": "user", "content": final_question}
    ]
    )

    answers_dict["confer"] = message.content[0].text

    return JsonResponse({'outputData': answers_dict[model_name]})

@require_POST
@csrf_exempt
def process_string(request):
    question = request.POST.get('inputData')

    def askOpenAI(question, model_name, answers):
        client = OpenAI(api_key = os.getenv('OPENAI_API_KEY'))
        completion = client.chat.completions.create(
        model = model_name,
        messages = [
            {"role": "system", "content": "You are a helpful assistant"},
            {"role": "user", "content": question}
        ]
        )

        answers_dict[model_name] = completion.choices[0].message.content

    def askAnthropic(question, model_name, answers):
        client = anthropic.Anthropic(api_key = os.getenv('CLAUDE_API_KEY'))
        message = client.messages.create(
            model = model_name,
            max_tokens = 4096,
            temperature = 0.0,
            system = "You are a helpful assistant. Sometimes you consider the input of other AI's to help you find the best answer.",
            messages = [
                {"role": "user", "content": question}
        ]
        )

        answers[model_name] = message.content[0].text

    def askPerplexity(question, model_name, answers):
        client = OpenAI(api_key=os.getenv('PERPLEXITY_API_KEY'), base_url="https://api.perplexity.ai")

        completion = client.chat.completions.create(
        model = model_name,
        messages = [
            {"role": "system", "content": "You are a helpful assistant"},
            {"role": "user", "content": question}
        ]
        )

        answers_dict[model_name] = completion.choices[0].message.content

    # OpenAI
    def runOpenAI():
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
    def runClaude():
        models = ["claude-3-opus-20240229", "claude-2.1"]

        threads = []

        for model in models:
            thread = threading.Thread(target = askAnthropic, args = (question, model, answers_dict))
            threads.append(thread)
            thread.start()
            time.sleep(1)

        for thread in threads:
            thread.join()

    # Perplexity
    def runPerplexity():
        models = ["mistral-7b-instruct", "mixtral-8x7b-instruct", "sonar-medium-chat"]

        threads = []

        for model in models:
            thread = threading.Thread(target = askPerplexity, args = (question, model, answers_dict))
            threads.append(thread)
            thread.start()
            time.sleep(1)

        for thread in threads:
            thread.join()

    claudeThread = threading.Thread(target = runClaude)
    openAIThread = threading.Thread(target = runOpenAI)
    perplexityThread = threading.Thread(target = runPerplexity)

    claudeThread.start()
    openAIThread.start()
    perplexityThread.start()

    claudeThread.join()
    openAIThread.join()
    perplexityThread.join()

    final_question = "I want you to consider the next few responses from various other AI. The responses are not necessarily correct or incorrect; it is up to you whether they influence your next answer or not.\n"
    for key, value in answers_dict.items():
        final_question += f"{key} wrote this answer: \n {value}"

    final_question += f"Having seen these other responses (including your own), I want you to answer this question: {question}.  You may allow the other AI's to influence your answer if you think it is an improvement, but you are not obliged to do so."

    askAnthropic(final_question, "claude-3-opus-20240229", answers_dict)

    return JsonResponse({'outputData': final_question})
    return JsonResponse({'outputData': answers_dict["claude-3-opus-20240229"]})
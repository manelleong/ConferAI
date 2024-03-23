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
            system = "You are a helpful assistant",
            messages = [
                {"role": "user", "content": question}
            ]
        )

        answers[model_name] = message.content[0].text

    answers_dict = dict()

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

    claudeThread = threading.Thread(target = runClaude)
    openAIThread = threading.Thread(target = runOpenAI)

    claudeThread.start()
    openAIThread.start()

    claudeThread.join()
    openAIThread.join()

    final_question = "I want you to consider the next few responses from various other AI. The responses are not necessarily correct or incorrect; it is up to you whether they influence your next answer or not.\n"
    for key, value in answers_dict.items():
        final_question += f"{key} wrote this answer: \n {value}"

    final_question += "Having seen these other responses (including your own), I want you to answer this question: {question}.  You may allow the other AI's to influence your answer if you think it is an improvement, but you are not obliged to do so.  In your answer do not ever mention the other AI's or their influence."

    askAnthropic(final_question, "claude-3-opus-20240229", answers_dict)

    # Example processing
    return JsonResponse({'outputData': answers_dict["claude-3-opus-20240229"]})
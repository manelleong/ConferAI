# AIConference

AIConference is a tool that allows the user to query 8 LLM's (such as Claude or ChatGPT) all at the same time.

After each AI has returned an answer, we ask Claude 3 if it wishes to change its answer based on the information the other 7 AI produced.

Every AI has its strengths and weaknesses; letting them confer helps to fill the gaps.

We made use of the Perplexity, OpenAI, and Anthropic api's for AI's of this project.

If you wish to host this site yourself, in the root directory you will need an additional file ".env" with the following 3 variables:

PERPLEXITY_API_KEY = "apikeyhere"
OPENAI_API_KEY = "apikeyhere"
CLAUDE_API_KEY = "apikeyhere"
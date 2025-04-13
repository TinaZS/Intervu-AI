import os
from dotenv import load_dotenv
from langchain_openai import AzureChatOpenAI

load_dotenv()

llm = AzureChatOpenAI(
    azure_endpoint=os.environ["AZURE_CHATOPENAI_ENDPOINT"],
    azure_deployment=os.environ["AZURE_CHATOPENAI_DEPLOYMENT"],
    openai_api_version=os.environ["CHATOPENAI_API_VERSION"],
    openai_api_key=os.environ["AZURE_CHATOPENAI_API_KEY"]
)


#Ask user a PM question
question_prompt = """You are a product management interviewer. 
Ask *exactly one* thoughtful interview question for a candidate. 
Do not include multiple questions, explanations, categories, or lists. 
Just return one standalone question only."""

question = llm.invoke(question_prompt).content
print(question)

#User types in their response (for now)
user_response = input("\n Your answer: ")

#Agent followup (optional)
followup_prompt = f"""You are a product management interviewer.
You asked the candidate: "{question}"
They answered: "{user_response}"
If the answer is brief, vague, irrelevant, or does not engage with the question meaningfully, you must respond with a follow-up question that probes deeper into what was missing or needs clarification.
Only if the answer is genuinely strong, detailed, and complete, respond with exactly: "No follow-up needed."
Do not include explanations or commentary—only give the follow-up question or "No follow-up needed."
"""


followup = llm.invoke(followup_prompt).content
if "no follow-up needed" not in followup.strip().lower():
    print(f"\nFollow-up question: {followup}")
    followup_response = input("\nYour follow-up answer: ")
    user_response += f"\nFollow-up: {followup_response}"
else:
    print("\nThank you for your response.")


#Feedback prompt
feedback_prompt = f"""You are a PM interviewer.
You asked the candidate: "{question}"
They answered: "{user_response}"
Please provide feedback on their answer.
Be specific and constructive. Include what they did well, what they could improve, and any other relevant comments.
If they did not answer the question, please say so.
Do not include any follow-up questions or ask for clarification.
Be concise and to the point.
"""
feedback = llm.invoke(feedback_prompt).content
print(f"\nFeedback: {feedback}")


    
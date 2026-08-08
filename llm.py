from langchain_google_genai import ChatGoogleGenerativeAI
import os

llm = ChatGoogleGenerativeAI(
    model = "gemini-3.5-flash-lite",
    google_api_key=os.getenv("GOOGLE_API_KEY")
)


def generate_response(prompt):

    response = llm.invoke(prompt)

    content = response.content

    if isinstance(content, str):
        return content

    if isinstance(content, list):
        text_parts = []

        for item in content:
            if isinstance(item, dict) and item.get("type") == "text":
                text_parts.append(item.get("text", ""))

        return " ".join(text_parts).strip()

    return str(content)

from groq import Groq
import os
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_report(topic, sources):
    try:
        content = ""

        for s in sources:
            content += s["content"] + "\n\n"

        prompt = f"""
        Generate a detailed research report on: {topic}

        Include:
        - Introduction
        - Advantages
        - Challenges
        - Conclusion

        Use the following content:
        {content}
        """

        response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[{"role": "user", "content": prompt}]
)

        return response.choices[0].message.content

    except Exception as e:
        print("ERROR:", e)
        return "Error generating report"
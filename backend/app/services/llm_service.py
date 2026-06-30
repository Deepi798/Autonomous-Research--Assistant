from groq import Groq
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Groq Client
client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

# Generate AI Research Report
def generate_report(topic, sources):

    try:

        # Combine all source content
        content = ""

        for s in sources:

            content += (
                s.get("content", "")
                + "\n\n"
            )

        # Compare Topics Mode
        if "vs" in topic.lower():

            prompt = f"""
            Compare the following topics:

            {topic}

            Create a professional comparison report.

            Include:

            ## Quick Overview
            ## Similarities
            ## Differences
            ## Advantages
            ## Challenges
            ## Future Scope
            ## Conclusion

            Use simple and clear language.
            """

        # Normal Research Mode
        else:

            prompt = f"""
            Generate a professional research report on:

            {topic}

            The report should contain:

            ## Quick Overview
            Give a short and simple explanation.

            ## Detailed Analysis
            Explain advantages, applications, and challenges.

            ## Advanced Insights
            Discuss technical details and future scope.

            ## Conclusion

            Use this research content:

            {content[:4000]}
            """

        # Generate response
        response = client.chat.completions.create(

            model="llama-3.1-8b-instant",

            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],

            temperature=0.5,
            max_tokens=1200
        )

        # Extract AI response
        answer = (
            response
            .choices[0]
            .message.content
        )

        return answer

    except Exception as e:

        print("Groq Error:", e)

        return """
        ## Error

        Failed to generate report.

        Please check:
        - GROQ API KEY
        - Internet connection
        - API limits
        """
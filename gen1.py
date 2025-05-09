from google import genai

client=genai.Client(api_key="AIzaSyDcqVRf-8LuJ-2AXCjMaNjcvCH7rrhEO_Y")
idea=input("what kind of idea you wnat to generate?\n")

prompt_engineering_response=f'''Create a detailed, optimized prompt for generating an AI image based on this idea: '{idea}'

The prompt should:
- Be specific about style, composition, lighting, colors, and mood
- Include relevant technical specifications (aspect ratio, quality level)
- Use descriptive language that AI image generators respond well to
- Be structured in a way that prioritizes the most important elements
- Be between 50-150 words for optimal results

Just provide the final prompt without explanations.'''

respone= client.models.generate_content(
    model="genmini-2.0-flash",
    content=prompt_engineering_response
)
print("the prompt is : ")
print(respone.text.strip())
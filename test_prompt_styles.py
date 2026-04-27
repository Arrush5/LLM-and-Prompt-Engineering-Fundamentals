import os
from google import genai
from google.genai import types

# Read the API key from the local file
try:
    with open("API_Key.txt", "r") as key_file:
        # .strip() removes any accidental spaces or newlines from the file
        my_api_key = key_file.read().strip() 
except FileNotFoundError:
    print("Error: API_Key.txt not found. Please create the file and add your API key.")
    exit()

# Initialize the client using the fetched key
client = genai.Client(api_key=my_api_key)
model_id = "gemini-2.5-flash"

def test_single_prompt(style_name, prompt_text):
    print(f"--- Testing Style: {style_name} ---")
    print(f"Prompt:\n{prompt_text}\n")
    
    response = client.models.generate_content(
        model=model_id,
        contents=prompt_text
    )
    
    print(f"Response:\n{response.text}\n")
    print("="*60 + "\n")

# ---------------------------------------------------------
# 1. Zero-Shot Prompting
# Directly asking the question. The model might just spit out a number or a brief sentence.
# ---------------------------------------------------------
prompt_zero_shot = """
Roger has 5 tennis balls. He buys 2 more cans of tennis balls. Each can has 3 tennis balls. How many tennis balls does he have now?
"""
test_single_prompt("Zero-Shot Prompting", prompt_zero_shot)

# ---------------------------------------------------------
# 2. Few-Shot Prompting
# Showing the model that we expect just the final number, without explanation, by providing examples.
# ---------------------------------------------------------
prompt_few_shot = """
Q: John has 3 apples. He buys 4 more. How many does he have?
A: 7

Q: Sarah has 10 dollars. She spends 2. How much does she have left?
A: 8

Q: Roger has 5 tennis balls. He buys 2 more cans of tennis balls. Each can has 3 tennis balls. How many tennis balls does he have now?
A:
"""
test_single_prompt("Few-Shot Prompting", prompt_few_shot)

# ---------------------------------------------------------
# 3. Chain of Thought (CoT) Prompting
# Adding the magic phrase "Let's think step-by-step" to force the model to show its math.
# ---------------------------------------------------------
prompt_cot = """
Roger has 5 tennis balls. He buys 2 more cans of tennis balls. Each can has 3 tennis balls. How many tennis balls does he have now? 
Let's think step-by-step.
"""
test_single_prompt("Chain of Thought (CoT)", prompt_cot)

# ---------------------------------------------------------
# 4. Self Consistency
# Asking a slightly trickier question multiple times with CoT, then finding the consensus.
# ---------------------------------------------------------
print("--- Testing Style: Self Consistency ---")
consistency_prompt = """
A baker has 15 batches of cookies. He sells 3/5 of them in the morning. He then bakes 4 more batches. Finally, he sells half of all the batches he currently has. How many batches does he have left?
Think step-by-step and end your response with exactly: "Final Answer: X" where X is the number.
"""

print(f"Prompt:\n{consistency_prompt}\n")

# We make 3 separate calls to generate 3 distinct reasoning paths
for i in range(3):
    print(f"Generating reasoning path {i+1}...")
    response = client.models.generate_content(
        model=model_id,
        contents=consistency_prompt,
        # Setting temperature to 0.7 to encourage slight variations in how it does the math
        config=types.GenerateContentConfig(temperature=0.7) 
    )
    print(f"Path {i+1} Output:\n{response.text}\n")
    print("-" * 30)

print("To implement self-consistency, your code would parse the 'Final Answer' from these 3 paths and pick the most frequent one (the majority vote).")
print("="*60 + "\n")
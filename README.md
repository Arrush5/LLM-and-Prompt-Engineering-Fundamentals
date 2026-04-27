# LLM Fundamentals & Prompt Engineering

## Objective
This repository contains the implementation for Week 2, Day 6 tasks focusing on Large Language Model (LLM) fundamentals and prompt engineering basics[cite: 1, 2, 5]. The goal is to explore how different prompt structures influence the output of an LLM.

## Tasks Completed
1. **API Setup:** Registered and generated an API key using Google AI Studio[cite: 14, 15].
2. **Script Implementation:** Wrote a Python script (`test_prompt_styles.py`) utilizing the `google-genai` SDK to programmatically test different prompting techniques[cite: 17].
3. **Execution & Analysis:** Ran the script using a standard mathematical reasoning problem to document how responses change based on the prompt[cite: 18].
4. **Comparison:** Compared the outputs to note what worked and what didn't[cite: 19].

---

## Output Comparison & Documentation

The following table documents the behavior of the `gemini-2.5-flash` model when presented with four distinct prompt styles.

| Prompt Style | Prompt Summary | Output Summary | Observations & Effectiveness |
| :--- | :--- | :--- | :--- |
| **Zero-Shot** | Asked the math word problem directly without any prior examples or formatting instructions. | Correctly calculated the answer (11) and automatically provided a brief 2-step breakdown of the math. | **Worked well:** The model naturally recognized it as a math problem and chose to show its work, even without being prompted to do so. |
| **Few-Shot** | Provided two examples of a Q&A format where the answer was strictly a single number, followed by the target question. | Correctly calculated the answer (11) but failed to strictly follow the single-number format. It explained the math first, then outputted "11" at the bottom. | **Didn't work perfectly:** The model failed to perfectly mimic the concise style of the examples. This shows that for newer models, stronger constraints (e.g., "Output ONLY the final number") might be needed alongside few-shot examples. |
| **Chain of Thought (CoT)** | Asked the problem directly and added the instruction "Let's think step-by-step." | Correctly calculated the answer (11) using a highly structured, 5-step numbered list detailing starting balls, cans bought, balls per can, new balls, and the total. | **Worked exactly as intended:** The specific phrase forced a much more granular and explicit breakdown of the logic compared to the Zero-Shot response. |
| **Self Consistency** | Asked a complex fraction problem, instructed to think step-by-step, and requested a specific final output string. Generated 3 separate times. | Generated 3 distinct reasoning paths. Paths 1 & 2 used bullet points; Path 3 used "Step X:" text. All three paths correctly arrived at the exact same conclusion: "Final Answer: 5". | **Highly effective:** Despite slight variations in how the model formatted its internal scratchpad (the reasoning steps), the logic remained sound across all three iterations, proving the reliability of the consensus approach for complex tasks. |

---

## Key Takeaways
* **Default Behavior:** Modern LLMs are naturally inclined to explain their reasoning (as seen in the Zero-Shot and Few-Shot outputs) rather than just providing raw answers.
* **Controlling Output:** Simply providing examples (Few-Shot) isn't always enough to restrict the model's verbosity. Explicit system instructions or negative prompts (e.g., "Do not explain your steps") may be required for strict formatting.
* **Reliability:** The Self Consistency test demonstrated that for multi-step logic, allowing the model to generate multiple Chain of Thought paths yields highly reliable and verifiable results.

## Files Included
* `test_prompt_styles.py`: The Python script used to run the API calls.
* `check.py`: A check script for Integration of Google API
* `README.md`: This documentation file.

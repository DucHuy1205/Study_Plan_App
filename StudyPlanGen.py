# study_plan_app.py
import streamlit as st
import openai

openai.api_key = 'YOUR_API_KEY'

def generate_study_plan(documents, student_context):
    prompt = f"""
You are an expert education planner.

Given the following course materials:

{documents}

And the following student context:

{student_context}

Create a detailed weekly study plan, including:
- Topics to cover
- Estimated time per topic
- Prioritization based on student's needs
- Deadlines if necessary
- Motivational tips for the student

Format it clearly, preferably as a week-by-week breakdown.
"""

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful and detailed study plan assistant."},
            {"role": "user", "content": prompt}
        ]
    )

    return response['choices'][0]['message']['content']

# --- Streamlit App ---
st.title("📚 AI Study Plan Generator")

st.write("""
Upload your course materials and tell us about your study goals — 
our AI will generate a customized study plan for you! 🚀
""")

# Input fields
documents = st.text_area("Paste your course materials (or key points):", height=200)

student_context = st.text_area("Tell us about your goals, strengths, weaknesses, and deadlines:", height=150)

if st.button("Generate Study Plan"):
    if not documents or not student_context:
        st.warning("Please fill in both the course materials and the student context.")
    else:
        with st.spinner("Generating your study plan..."):
            plan = generate_study_plan(documents, student_context)
            st.success("Here is your personalized study plan!")
            st.markdown(plan)

st.markdown("---")
st.caption("Powered by OpenAI GPT-4 | Built by Your Name")

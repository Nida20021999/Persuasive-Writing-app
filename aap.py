import streamlit as st
import re

st.set_page_config(
    page_title="Persuasive Writing Assistant",
    layout="centered"
)

st.title("Persuasive Writing Assistant")
st.write(
    """
    This tool supports Pakistani ESL undergraduate learners in improving
    persuasive academic writing through level-based feedback.
    """
)

level = st.selectbox(
    "Select Difficulty Level",
    ["Beginner", "Intermediate", "Advanced"]
)

essay = st.text_area(
    "Write or paste your persuasive essay below:",
    height=250,
    placeholder="Enter your essay text here..."
)

def analyze_essay(text, level):
    feedback = []

    if len(text.split()) < 80:
        feedback.append(
            "Your essay is quite short. Persuasive writing usually requires further idea development."
        )

    if " very " in text.lower():
        feedback.append(
            "Avoid vague intensifiers like 'very'. Use more precise academic vocabulary."
        )

    if re.search(r"\bi think\b|\bi believe\b", text.lower()):
        feedback.append(
            "Avoid personal expressions such as 'I think' or 'I believe' in academic persuasive writing."
        )

    if level in ["Intermediate", "Advanced"]:
        connectors = ["because", "therefore", "however", "thus", "moreover"]
        if not any(word in text.lower() for word in connectors):
            feedback.append(
                "Add logical connectors (e.g., because, therefore, however) to improve cohesion."
            )

    if level == "Advanced":
        counter_markers = [
            "although",
            "some may argue",
            "on the other hand",
            "critics argue"
        ]
        if not any(marker in text.lower() for marker in counter_markers):
            feedback.append(
                "Advanced persuasive writing should address counter-arguments."
            )

    return feedback

if st.button("Analyze Essay"):
    if essay.strip() == "":
        st.error("Please enter an essay before analysis.")
    else:
        results = analyze_essay(essay, level)
        st.subheader("Feedback")
        if not results:
            st.success(
                "Your essay demonstrates appropriate control for this level. "
                "You may further refine argument depth and vocabulary."
            )
        else:
            for item in results:
                st.warning(item)

st.markdown("---")
st.caption("Academic writing support tool for ESL learners")

import streamlit as st
from src.rag_crewai.crew import RagCrewai

# Streamlit UI
st.title("🏛️ Arabic Heritage RAG Assistant")
st.write("Ask questions about Arabic heritage and culture")

# User input
user_question = st.text_area(
    "Enter your question:",
    placeholder="e.g., Tell me about Arabic calligraphy traditions",
    height=100
)

# Run button
if st.button("🔍 Search & Answer", type="primary"):
    if user_question:
        with st.spinner("🤖 Crew is researching..."):
            try:
                # Initialize your crew
                crew_instance = RagCrewai()

                # Run the crew with user input
                result = crew_instance.crew().kickoff(inputs={"question": user_question})

                # Display results
                st.success("✅ Research complete!")
                st.markdown("### Answer:")
                st.write(result.raw)

            except Exception as e:
                st.error(f"❌ Error: {str(e)}")
    else:
        st.warning("⚠️ Please enter a question first")

# Optional: Sidebar with info
with st.sidebar:
    st.header("ℹ️ About")
    st.write("This app uses CrewAI with RAG to answer questions about Arabic heritage.")
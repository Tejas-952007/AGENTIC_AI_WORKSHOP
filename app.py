import streamlit as st
import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate

# Page configuration
st.set_page_config(page_title="Research Paper Explainer", page_icon="�", layout="wide")

load_dotenv()

# Get API key from environment or streamlit secrets
google_api_key = os.getenv("GOOGLE_API_KEY")
if not google_api_key and "GOOGLE_API_KEY" in st.secrets:
    google_api_key = st.secrets["GOOGLE_API_KEY"]

# Initialize LLM
if not google_api_key:
    st.error("⚠️ **GOOGLE_API_KEY Missing.** Please add it to your secrets or .env file.")
    st.stop()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash-lite",
    temperature=0.3,
    google_api_key=google_api_key
)

# Custom CSS for Premium UI improvement
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

    html, body, [class*="css"]  {
        font-family: 'Inter', sans-serif;
    }
    
    /* Titles and Headers */
    .main-header {
        font-size: 2.8rem;
        font-weight: 800;
        background: -webkit-linear-gradient(45deg, #2563eb, #9333ea);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 5px;
        padding-top: 10px;
    }
    .sub-header {
        font-size: 1.15rem;
        font-weight: 400;
        color: #4b5563;
        margin-bottom: 35px;
    }

    /* Buttons */
    .stButton>button {
        background-color: #2563eb;
        color: white;
        border: none;
        border-radius: 10px;
        font-weight: 600;
        padding: 0.6rem 1.2rem;
        transition: all 0.2s ease-in-out;
        box-shadow: 0 4px 6px -1px rgba(37, 99, 235, 0.2);
    }
    .stButton>button:hover {
        background-color: #1d4ed8;
        transform: translateY(-2px);
        box-shadow: 0 6px 12px -2px rgba(37, 99, 235, 0.3);
        color: white;
    }

    /* Inputs and Selectboxes */
    .stSelectbox div[data-baseweb="select"] > div {
        border-radius: 8px;
        border: 1px solid #e5e7eb;
        box-shadow: inset 0 1px 2px rgba(0, 0, 0, 0.05);
        transition: border-color 0.2s ease-in-out, box-shadow 0.2s ease-in-out;
    }
    .stSelectbox div[data-baseweb="select"] > div:hover {
        border-color: #3b82f6;
    }
    
    .stTextInput input {
        border-radius: 8px;
        border: 1px solid #e5e7eb;
        padding: 0.6rem 1rem;
    }

    /* Containers */
    [data-testid="stVerticalBlock"] {
        gap: 1.2rem;
    }
    div[data-testid="stContainer"] {
        background-color: #ffffff;
        padding: 24px;
        border-radius: 12px;
        border: 1px solid #f3f4f6;
        box-shadow: 0 10px 25px -5px rgba(0, 0, 0, 0.05), 0 8px 10px -6px rgba(0, 0, 0, 0.01);
    }

    /* Expander / Messages */
    .stChatMessage {
        background-color: #ffffff;
        border-radius: 12px;
        padding: 18px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05);
        border: 1px solid #f3f4f6;
    }

</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-header">Research Paper AI Synthesizer</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Unlock the secrets of complex scientific literature. Select a paper and let our AI agents explain, summarize, and break down the math for you.</div>', unsafe_allow_html=True)

# Predefined 10 research papers with their publication years
predefined_papers = [
    {"year": 2017, "title": "1. Attention Is All You Need", "content": "The dominant sequence transduction models are based on complex recurrent or convolutional neural networks that include an encoder and a decoder. The best performing models also connect the encoder and decoder through an attention mechanism. We propose a new simple network architecture, the Transformer, based solely on attention mechanisms, dispensing with recurrence and convolutions entirely."},
    {"year": 2018, "title": "2. BERT: Pre-training of Deep Bidirectional Transformers", "content": "We introduce a new language representation model called BERT, which stands for Bidirectional Encoder Representations from Transformers. Unlike recent language representation models, BERT is designed to pre-train deep bidirectional representations from unlabeled text by jointly conditioning on both left and right context in all layers."},
    {"year": 2020, "title": "3. GPT-3: Language Models are Few-Shot Learners", "content": "Recent work has demonstrated substantial gains on many NLP tasks and benchmarks by pre-training on a large corpus of text followed by fine-tuning on a specific task. While typically task-agnostic in architecture, this method still requires task-specific fine-tuning datasets of thousands or tens of thousands of examples. By contrast, humans can generally perform a new language task from only a few examples or from simple instructions - something which current NLP systems still largely struggle to do. Here we show that scaling up language models greatly improves task-agnostic, few-shot performance."},
    {"year": 2023, "title": "4. Llama 2: Open Foundation and Fine-Tuned Chat Models", "content": "In this work, we develop and release Llama 2, a collection of pretrained and fine-tuned large language models (LLMs) ranging in scale from 7 billion to 70 billion parameters. Our fine-tuned LLMs, called Llama 2-Chat, are optimized for dialogue use cases."},
    {"year": 2021, "title": "5. DALL-E: Creating Images from Text", "content": "We show that text-to-image synthesis is a scalable task. We demonstrate that a model trained on a large dataset of text and image pairs can learn to generate complex images from text descriptions, exhibiting understanding of the world and visual concepts."},
    {"year": 2020, "title": "6. RAG: Retrieval-Augmented Generation", "content": "Large pre-trained language models have been shown to store factual knowledge in their parameters, and achieve state-of-the-art results when fine-tuned on downstream NLP tasks. However, their ability to access and precisely manipulate knowledge is still limited. We explore RAG models which combine pre-trained parametric and non-parametric memory for language generation."},
    {"year": 2021, "title": "7. LoRA: Low-Rank Adaptation of Large Language Models", "content": "An important paradigm of natural language processing consists of large-scale pre-training on general domain data and adaptation to particular tasks or domains. As we pre-train larger models, full fine-tuning, which retrains all model parameters, becomes less feasible. We propose LoRA, which freezes the pre-trained model weights and injects trainable rank decomposition matrices into each layer of the Transformer architecture."},
    {"year": 2021, "title": "8. Diffusion Models Beat GANs on Image Synthesis", "content": "We show that diffusion models can achieve image sample quality superior to the current state-of-the-art generative models. We achieve this on unconditional image synthesis by finding a better architecture through a series of ablations. For conditional image synthesis, we further improve sample quality with classifier guidance."},
    {"year": 2021, "title": "9. AlphaFold: Highly accurate protein structure prediction", "content": "Proteins are essential to life, and understanding their structure can facilitate a mechanistic understanding of their function. Here we describe AlphaFold, which can predict protein structures with atomic accuracy even where no similar structure is known, demonstrating accuracy competitive with experimental structures."},
    {"year": 2022, "title": "10. InstructGPT: Training language models to follow instructions", "content": "Making language models bigger does not inherently make them better at following a user's intent. For example, large language models can generate outputs that are untruthful, toxic, or simply not helpful to the user. In this paper, we show an avenue for aligning language models with user intent on a wide range of tasks by fine-tuning with human feedback."}
]

# Initialize session state variables to track results
if "explanation_result" not in st.session_state:
    st.session_state.explanation_result = None

# Extract unique years and create year filter
years = sorted(list(set(paper["year"] for paper in predefined_papers)), reverse=True)

# ----------------- UI LAYOUT -----------------

with st.sidebar:
    st.markdown("### ⚙️ Engine Settings")
    st.caption("Customize how the AI processes the paper.")
    
    selected_year = st.selectbox("Publication Year", ["All"] + years)
    
    st.divider()
    
    style = st.selectbox(
        "Explanation Style",
        ["Beginner Friendly", "Technical Explanation", "Code-oriented", "Mathematical", "Bullet Points"]
    )
    
    length = st.selectbox(
        "Detail Level",
        ["Short Summary", "Medium Breakdown", "Detailed Analysis"]
    )
    
    summarize = st.toggle("Include TL;DR Summary?", value=True)
    
    st.divider()
    st.info("💡 **Pro Tip:** Select 'Mathematical' or 'Code-oriented' to force the AI to extract and explain equations and architecture blocks.")

# Filter papers by year
if selected_year != "All":
    filtered_papers = [p for p in predefined_papers if p["year"] == selected_year]
else:
    filtered_papers = predefined_papers

st.markdown("---")

col_left, col_right = st.columns([3, 1])

with col_left:
    # Select paper from filtered list
    paper_titles = [p["title"] for p in filtered_papers]
    selected_paper_title = st.selectbox("Select Target Paper:", paper_titles) if paper_titles else None
    if not paper_titles:
        st.warning("No papers found for the selected year filter.")

if "current_paper" not in st.session_state:
    st.session_state.current_paper = selected_paper_title

# Reset explanation if the user changes the selected paper
if selected_paper_title != st.session_state.current_paper:
    st.session_state.current_paper = selected_paper_title
    st.session_state.explanation_result = None

if selected_paper_title is not None:
    # Get content of selected paper
    selected_paper_data = next((p for p in predefined_papers if p["title"] == selected_paper_title), None)
    text = selected_paper_data["content"] if selected_paper_data else ""

    with col_right:
        st.write("") # Vertical alignment spacing
        st.write("")
        if st.button("✨ Synthesize", use_container_width=True):
            prompt_template = ChatPromptTemplate.from_messages([
                ("system", "You are an elite AI research assistant. Provide well-structured markdown formatting, using neat headers (###), bold text, and beautiful code blocks."),
                ("human", """
Analyze and summarize the following research paper: {paper_name}

Formatting constraints:
- Style: {style}
- Depth: {length}

Core Requirements:
1. Extract and format mathematical equations cleanly using LaTeX format if relevant.
2. Provide simple, conceptual code snippets for algorithmic ideas.
3. Use powerful, relatable real-world analogies to explain tricky concepts.

TL;DR Check: {summarize}
If true, start with a highly condensed, bolded 1-2 sentence TL;DR.

Paper Content:
{text}
                """)
            ])

            chain = prompt_template | llm

            with st.spinner("Analyzing neural architecture & reading paper..."):
                try:
                    result = chain.invoke({
                        "paper_name": selected_paper_title,
                        "style": style,
                        "length": length,
                        "summarize": summarize,
                        "text": text[:7000]
                    })
                    st.session_state.explanation_result = result.content
                except Exception as e:
                    st.error(f"⚠️ **API Quota Exhausted.** Please try again later or update your API key.\n\n`{e}`")

    # Display the Result
    if st.session_state.explanation_result:
        st.markdown("<br>", unsafe_allow_html=True)
        
        # Wrapped container to act like a premium card
        with st.container():
            st.markdown(st.session_state.explanation_result)

        st.markdown("<br><hr>", unsafe_allow_html=True)
        
        # Follow-up Section
        st.markdown("### 💬 Ask a Follow-up Question")
        st.caption("Want more details? Ask the AI specific questions about this paper's architecture.")
        
        q_col1, q_col2 = st.columns([5, 1])
        with q_col1:
            custom_question = st.text_input("Follow-up:", label_visibility="collapsed", placeholder="e.g. Can you explain the multi-head attention mechanism further?")
        with q_col2:
            ask_btn = st.button("Send", type="primary", use_container_width=True)
            
        if ask_btn:
            if custom_question:
                follow_up_prompt = ChatPromptTemplate.from_messages([
                    ("system", "You are an elite AI research assistant. Provide neat markdown text."),
                    ("human", """
Paper Context: {paper_name}
Original Text: {text}
Previous AI Output: {explanation}

User Question: {custom_question}

Answer the user's question directly, clearly, and concisely based on the paper context.
                    """)
                ])
                
                follow_up_chain = follow_up_prompt | llm
                
                with st.spinner("Thinking..."):
                    try:
                        follow_up_result = follow_up_chain.invoke({
                            "paper_name": selected_paper_title,
                            "text": text[:7000],
                            "explanation": st.session_state.explanation_result,
                            "custom_question": custom_question
                        })
                    
                        with st.chat_message("assistant"):
                            st.markdown(follow_up_result.content)
                    except Exception as e:
                         st.error(f"⚠️ **API Quota Exhausted.** Please try again later or update your API key.\n\n`{e}`")
            else:
                st.warning("✏️ Please enter a question to ask.")
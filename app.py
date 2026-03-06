import streamlit as st
import os
from langchain_ollama import ChatOllama, OllamaEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import ChatPromptTemplate

# --- 1. IMPORTS ROBUSTES (Gestion des versions 2026) ---
try:
    from langchain_classic.chains.combine_documents import create_stuff_documents_chain
    from langchain_classic.chains import create_retrieval_chain
except ImportError:
    from langchain.chains.combine_documents import create_stuff_documents_chain
    from langchain.chains import create_retrieval_chain

# --- 2. CONFIGURATION ET STYLE ---
st.set_page_config(page_title="IA Locale 2026", page_icon="🤖", layout="centered")

st.markdown("""
    <style>
    [data-testid="stSidebar"] {
        background-color: #161b22;
    }
    .main-title {
        font-size: 45px;
        font-weight: 800;
        color: #00FFA3;
        text-shadow: 2px 2px 4px #000000;
        margin-bottom: 0px;
    }
    .stChatMessage {
        border-radius: 15px;
        padding: 10px;
        margin-bottom: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. BARRE LATÉRALE ---
with st.sidebar:
    st.image("https://cdn-icons-png.flaticon.com/512/4712/4712027.png", width=100)
    st.title("Configuration")
    
    with st.expander("ℹ️ Informations Document"):
        st.write("📄 **Fichier :** OUMIMA Khalid CV.pdf")
        st.write("📊 **Segments :** 6 morceaux")
        st.write("🧠 **Modèle :** Llama 3 (Local)")
    
    if st.button("🗑️ Effacer l'historique"):
        st.session_state.messages = []
        st.rerun()

# --- 4. TITRE PRINCIPAL ---
st.markdown('<h1 class="main-title">AI Resume Assistant 🤖</h1>', unsafe_allow_html=True)
st.subheader("Discute en direct avec ton document")
st.markdown("---")

# --- 5. LOGIQUE RAG (Backend) ---
DB_PATH = "faiss_index_react"

if os.path.exists(DB_PATH):
    # Chargement des outils Ollama
    embeddings = OllamaEmbeddings(model="nomic-embed-text")
    vectorstore = FAISS.load_local(DB_PATH, embeddings, allow_dangerous_deserialization=True)
    retriever = vectorstore.as_retriever()
    llm = ChatOllama(model="llama3", temperature=0.3)

    # Configuration du Prompt
    system_prompt = (
        "Tu es un assistant virtuel expert en recrutement. "
        "Réponds en français de manière professionnelle en utilisant le contexte fourni. "
        "Contexte : {context}"
    )
    prompt_template = ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        ("human", "{input}"),
    ])

    # Création de la chaîne
    combine_docs_chain = create_stuff_documents_chain(llm, prompt_template)
    rag_chain = create_retrieval_chain(retriever, combine_docs_chain)

    # --- 6. INTERFACE DE CHAT ---
    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if user_query := st.chat_input("Pose une question sur ton CV..."):
        st.session_state.messages.append({"role": "user", "content": user_query})
        with st.chat_message("user"):
            st.markdown(user_query)

        with st.chat_message("assistant"):
            with st.spinner("L'IA analyse le document..."):
                try:
                    response = rag_chain.invoke({"input": user_query})
                    answer = response["answer"]
                    st.markdown(answer)
                    st.session_state.messages.append({"role": "assistant", "content": answer})
                except Exception as e:
                    st.error(f"Erreur : {e}")
else:
    # Cas où la base de données n'est pas encore créée
    st.warning("⚠️ Base de données introuvable. Lancez 'python ingestion.py' d'abord.")
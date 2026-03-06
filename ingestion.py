import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings
from langchain_community.vectorstores import FAISS

def run_ingestion():
    print("--- ⚙️ Ingestion LOCALE lancée ---")
    
    # 1. Trouver le PDF
    pdf_folder = "data"
    files = [f for f in os.listdir(pdf_folder) if f.endswith('.pdf')]
    if not files:
        print("❌ Erreur : Aucun PDF trouvé dans le dossier 'data' !")
        return

    pdf_path = os.path.join(pdf_folder, files[0])
    print(f"📖 Lecture de : {pdf_path}")

    # 2. Charger et découper le texte
    loader = PyPDFLoader(pdf_path)
    documents = loader.load()
    
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    chunks = text_splitter.split_documents(documents)
    print(f"✂️ Document découpé en {len(chunks)} morceaux.")

    # 3. Créer les vecteurs avec Ollama (Nomic)
    print("🧠 Création de la mémoire (Embeddings)...")
    # C'est ici qu'Ollama travaille !
    embeddings = OllamaEmbeddings(model="nomic-embed-text")
    
    # 4. Sauvegarder dans la base FAISS
    vectorstore = FAISS.from_documents(chunks, embeddings)
    vectorstore.save_local("faiss_index_react")
    print("--- ✅ SUCCÈS : Le dossier 'faiss_index_react' a été créé ! ---")

if __name__ == "__main__":
    run_ingestion()
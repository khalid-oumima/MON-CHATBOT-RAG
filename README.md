# 🤖 Local-RAG Resume Assistant (Privacy-First)
![Interface du Chatbot](assets/screenshot3.png)

Ce projet est un assistant IA conversationnel basé sur l'architecture **RAG (Retrieval-Augmented Generation)**. Il permet d'interroger un CV (ou tout document PDF) de manière totalement locale, garantissant une confidentialité absolue des données.



## ✨ Fonctionnalités
- **Confidentialité totale** : Aucun transfert de données vers le cloud (OpenAI/Google). Tout tourne sur votre machine.
- **Performance locale** : Utilisation de modèles optimisés pour le matériel grand public.
- **Interface Intuitive** : UI moderne développée avec Streamlit, incluant un historique de chat.
- **Recherche Sémantique** : Indexation vectorielle précise avec FAISS.

## 🛠️ Stack Technique
- **LLM :** Llama 3 (via [Ollama](https://ollama.com/))
- **Embeddings :** nomic-embed-text
- **Orchestrateur :** LangChain (Core & Classic)
- **Base de données vectorielle :** FAISS
- **Frontend :** Streamlit
- **Langage :** Python 3.13+

## ⚙️ Installation et Configuration

### 1. Prérequis
- Installer [Ollama](https://ollama.com/)
- Télécharger les modèles nécessaires :
  ```bash
  ollama pull llama3
  ollama pull nomic-embed-text
2. Configurer l'environnement
Bash

# Cloner le dépôt
git clone [https://github.com/khalid-oumima/MON-CHATBOT-RAG.git](https://github.com/khalid-oumima/MON-CHATBOT-RAG.git)
cd MON-CHATBOT-RAG

# Créer l'environnement virtuel
python -m venv venv

# Activer l'environnement (Windows)
.\venv\Scripts\activate 

# Installer les bibliothèques nécessaires
pip install -r requirements.txt

🚀 Utilisation

    Chargement du document : Placez votre fichier PDF (ex: votre CV) dans le dossier data/.

    Ingestion des données : Transformez le texte en vecteurs mathématiques stockés localement.
    Bash

    python ingestion.py

    Lancement du Chatbot : Démarrez l'interface utilisateur.
    Bash

    streamlit run app.py

📂 Structure du projet

    app.py : Le moteur de l'application et l'interface utilisateur Streamlit personnalisée.

    ingestion.py : Le pipeline de données (chargement, découpage du texte, vectorisation via Ollama).

    assets/ : Captures d'écran et ressources visuelles du projet.

    data/ : Dossier contenant les documents sources à analyser (PDF).

    faiss_index_react/ : La base de données vectorielle générée localement (exclue de Git par sécurité).

Développé avec ❤️ par Khalid Oumima

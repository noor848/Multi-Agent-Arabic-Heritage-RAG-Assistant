# 🏛️ Multi-Agent Arabic Heritage RAG Assistant

A sophisticated multi-agent RAG (Retrieval-Augmented Generation) application built with CrewAI that provides intelligent answers about Arabic heritage and culture. The system features a hierarchical multi-agent architecture with 5 specialized agents coordinated by a manager, supporting both Arabic and English queries with automatic language detection.

## 🌟 Features

- **Multilingual Support**: Understands and responds in both Arabic and English
- **Intelligent RAG System**: Semantic search over 39,000+ lines of Arabic heritage knowledge
- **Hierarchical Multi-Agent Architecture**: 5 specialized agents coordinated through CrewAI's hierarchical process
- **Local LLM**: Uses Ollama's aya-expanse:8b model for privacy and performance
- **Interactive Web UI**: Clean Streamlit interface for easy interaction
- **Automated Language Detection**: Detects query language and responds accordingly
- **Weather Integration**: Provides weather forecasts for heritage locations

## 🏗️ Architecture

┌─────────────────────────────────────────────────────────────────────────┐
│                          USER INTERFACE LAYER                            │
│                                                                          │
│  ┌───────────────────────────────────────────────────────────────────┐  │
│  │                    Streamlit Web Interface                        │  │
│  │                          (app.py)                                 │  │
│  │  - User query input                                               │  │
│  │  - Display multi-agent results                                    │  │
│  │  - Real-time processing status                                    │  │
│  └─────────────────────────────┬─────────────────────────────────────┘  │
└─────────────────────────────────┼──────────────────────────────────────┘
                                  │
                                  ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                      ORCHESTRATION LAYER                                │
│                         (CrewAI Framework)                               │
│                                                                          │
│  ┌───────────────────────────────────────────────────────────────────┐  │
│  │                    HIERARCHICAL PROCESS                           │  │
│  │                  (Process.hierarchical)                           │  │
│  │                                                                   │  │
│  │  ┌────────────────────────────────────────────────────────────┐  │  │
│  │  │              ⭐ MANAGER AGENT                               │  │  │
│  │  │            (Project Manager)                               │  │  │
│  │  │                                                            │  │  │
│  │  │  • Analyzes user questions                                │  │  │
│  │  │  • Delegates to specialist agents                         │  │  │
│  │  │  • Coordinates workflow                                   │  │  │
│  │  │  • Ensures task completion                                │  │  │
│  │  │  • LLM: Ollama (aya-expanse:8b)                          │  │  │
│  │  │  • Delegation: Enabled                                    │  │  │
│  │  └─────────────────────┬──────────────────────────────────────┘  │  │
│  │                        │                                          │  │
│  │          ┌─────────────┼─────────────┬──────────────┐            │  │
│  │          │             │             │              │            │  │
│  │          ▼             ▼             ▼              ▼            │  │
│  │  ┌──────────────┐ ┌──────────┐ ┌──────────┐ ┌──────────────┐  │  │
│  │  │   Language   │ │ Heritage │ │ Weather  │ │   Reporter   │  │  │
│  │  │   Detector   │ │  Expert  │ │Specialist│ │    Agent     │  │  │
│  │  │              │ │          │ │          │ │              │  │  │
│  │  │  Language    │ │ Heritage │ │ Weather  │ │   Report     │  │  │
│  │  │  Detection   │ │ Research │ │ Research │ │  Formatting  │  │  │
│  │  │  Specialist  │ │   Task   │ │   Task   │ │     Task     │  │  │
│  │  └──────────────┘ └──────────┘ └──────────┘ └──────────────┘  │  │
│  └───────────────────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────────────┘
                              │
            ┌─────────────────┼─────────────────┐
            │                 │                 │
            ▼                 ▼                 ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                          TOOLS LAYER                                    │
│                                                                          │
│  ┌──────────────────┐  ┌──────────────────┐  ┌──────────────────────┐  │
│  │  Language        │  │  Heritage        │  │  Weather Forecast    │  │
│  │  Detection Tool  │  │  Search Tool     │  │  Tool                │  │
│  │                  │  │                  │  │                      │  │
│  │  - XLM-RoBERTa   │  │  - Semantic      │  │  - Weather API       │  │
│  │  - Multilingual  │  │    Search        │  │  - Location-based    │  │
│  │  - Returns       │  │  - RAG Pipeline  │  │  - Forecast data     │  │
│  │    'ar' or 'en'  │  │  - Top-3         │  │  - Real-time         │  │
│  │                  │  │    Retrieval     │  │    information       │  │
│  └──────────────────┘  └────────┬─────────┘  └──────────────────────┘  │
└─────────────────────────────────┼──────────────────────────────────────┘
                                  │
                                  ▼
┌─────────────────────────────────────────────────────────────────────────┐
│                      DATA & MODEL LAYER                                 │
│                                                                          │
│  ┌──────────────────┐  ┌──────────────────┐  ┌──────────────────────┐  │
│  │  Knowledge Base  │  │  Embedding Model │  │  Language Models     │  │
│  │                  │  │                  │  │                      │  │
│  │  - 39,000+ lines │  │  - SentenceXfer  │  │  - Ollama (Local)    │  │
│  │  - Arab heritage │  │  - MiniLM-L6-v2  │  │  - aya-expanse:8b    │  │
│  │  - Text chunks   │  │  - Cosine        │  │  - Arabic/English    │  │
│  │  - 400 words/    │  │    similarity    │  │    support           │  │
│  │    chunk         │  │  - Normalized    │  │  - Used by all 5     │  │
│  │                  │  │    vectors       │  │    agents            │  │
│  └──────────────────┘  └──────────────────┘  └──────────────────────┘  │
└─────────────────────────────────────────────────────────────────────────┘

### Technology Stack

- **CrewAI**: Multi-agent orchestration framework with hierarchical process
- **Ollama (aya-expanse:8b)**: Local LLM with Arabic/English support
- **Streamlit**: Web interface
- **sentence-transformers**: Semantic search using MiniLM-L6-v2
- **Hugging Face Transformers**: Language detection with XLM-RoBERTa

### Multi-Agent System

The system employs a **hierarchical multi-agent architecture** with 5 specialized agents:

#### 1. **Manager Agent** (Project Manager)

- **Role**: Orchestrates and delegates tasks to specialist agents
- **Process**: Hierarchical coordination using CrewAI's manager pattern
- **Capabilities**: Delegation, task assignment, workflow optimization

#### 2. **Language Detector Agent** (Language Detection Specialist)

- **Role**: Identifies the language of user queries
- **Tools**: Language Detection Tool (XLM-RoBERTa)
- **Output**: Language code ('ar' for Arabic, 'en' for English)

#### 3. **Heritage Expert Agent** (Heritage and History Researcher)

- **Role**: Searches and retrieves relevant cultural heritage information
- **Tools**: Heritage Search Tool (RAG with semantic search)
- **Knowledge Base**: 39,000+ lines of Arabic heritage content

#### 4. **Weather Specialist Agent** (Weather Forecasting Expert)

- **Role**: Provides weather forecasts for heritage site locations
- **Tools**: Weather Forecast Tool
- **Capabilities**: Location-based weather information

#### 5. **Reporter Agent** (Report Writer)

- **Role**: Formats and presents final responses in the detected language
- **Output**: Coherent, well-formatted answers in Arabic or English

### Task Workflow

The system executes 4 sequential tasks:

1. **Language Detection Task**: Identifies query language using the Language Detector agent
2. **Heritage Research Task**: Retrieves relevant heritage information via Heritage Expert agent
3. **Weather Research Task**: Fetches weather data when applicable through Weather Specialist agent
4. **Report Formatting Task**: Synthesizes all information into a coherent response via Reporter agent

### Core Components

#### 1. Web Interface ([app.py](app.py))

- Streamlit-based UI for user interaction
- Accepts questions about Arabic heritage
- Displays coordinated multi-agent research results

#### 2. Crew System ([src/rag_crewai/crew.py](src/rag_crewai/crew.py))

- 5 specialized agents with distinct roles
- Hierarchical process with manager-based delegation
- Integrated custom tools for each specialist

#### 3. Custom Tools

**Heritage Search Tool** ([tools/heritage_tool.py](src/rag_crewai/tools/heritage_tool.py)):

- Loads heritage knowledge base from text corpus
- Creates semantic chunks (400 words each)
- Generates embeddings using sentence-transformers
- Retrieves top-3 most relevant chunks using cosine similarity

**Language Detection Tool** ([tools/language_detection.py](src/rag_crewai/tools/language_detection.py)):

- Detects whether question is in Arabic or English
- Uses XLM-RoBERTa multilingual model
- Returns language code ('ar' or 'en')

**Weather Tool** ([tools/weather_tool.py](src/rag_crewai/tools/weather_tool.py)):

- Provides weather forecasts for heritage locations
- Location-based weather information

#### 4. Configuration

**Agents** ([config/agents.yaml](src/rag_crewai/config/agents.yaml)):

- 5 agent definitions: Manager, Language Detector, Heritage Expert, Weather Specialist, Reporter
- Role, goal, and backstory for each agent

**Tasks** ([config/tasks.yaml](src/rag_crewai/config/tasks.yaml)):

- 4 task definitions with clear descriptions and expected outputs
- Agent assignment for each task

## 📚 Knowledge Base

The system includes a comprehensive knowledge base (`knowledge/_ALL_ARAB_HERITAGE_EN.txt`):

- 39,000+ lines of curated content
- Information about Arab heritage sites
- Historical locations including Jerusalem, Palestine, and more
- Compiled from Wikipedia and authoritative sources

## 🚀 Getting Started

### Prerequisites

1. **Python 3.8+**
2. **Ollama** installed with aya-expanse:8b model
   ```bash
   ollama pull aya-expanse:8b
   ```

### Installation

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd Multi-Agent-Arabic-Heritage-RAG-Assistant-main
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   uv run
   ```

### Running the Application

Start the Streamlit app:

```bash
streamlit run app.py
```

The application will open in your browser at `http://localhost:8501`

## 💡 Usage

1. Open the web interface
2. Enter your question in Arabic or English
3. Click "🔍 Search & Answer"
4. The system will:
   - **Manager Agent** receives your query and delegates tasks
   - **Language Detector Agent** identifies the language
   - **Heritage Expert Agent** searches the knowledge base for relevant information
   - **Weather Specialist Agent** provides weather data if location-related
   - **Reporter Agent** formats everything into a coherent answer in your language

### Workflow Example

**Question**: "Tell me about the history of Jerusalem and the weather there"

1. **Manager** delegates to Language Detector → detects "en" (English)
2. **Manager** delegates to Heritage Expert → retrieves historical information about Jerusalem
3. **Manager** delegates to Weather Specialist → fetches current weather for Jerusalem
4. **Manager** delegates to Reporter → combines all information into English response

### Example Questions

**English:**

- "Tell me about Arabic calligraphy traditions"
- "What is the history of the Great Mosque of Damascus?"
- "Describe traditional Arabic architecture"
- "What's the weather like in Cairo?"

**Arabic:**

- "أخبرني عن تقاليد الخط العربي"
- "ما هو تاريخ المسجد الأموي؟"
- "صف العمارة العربية التقليدية"
- "كيف الطقس في القاهرة؟"

## 📁 Project Structure

```
.
├── app.py                          # Streamlit web interface
├── requirements.txt                # Python dependencies
├── pyproject.toml                  # Project configuration
├── README.md                       # Documentation
├── documentation.md                # Comprehensive technical docs
├── knowledge/
│   ├── _ALL_ARAB_HERITAGE_EN.txt  # Heritage knowledge base (39,000+ lines)
│   └── user_preference.txt        # User preference storage
└── src/
    └── rag_crewai/
        ├── __init__.py
        ├── crew.py                 # 5 Agents + Hierarchical Crew
        ├── main.py                 # Entry point
        ├── config/
        │   ├── agents.yaml         # 5 Agent definitions (Manager, Language Detector,
        │   │                         Heritage Expert, Weather Specialist, Reporter)
        │   └── tasks.yaml          # 4 Task definitions (Language detection, Heritage
        │                             research, Weather research, Report formatting)
        └── tools/
            ├── __init__.py
            ├── custom_tool.py      # Base custom tool
            ├── heritage_tool.py    # RAG semantic search tool
            ├── language_detection.py # Language detection tool
            └── weather_tool.py     # Weather forecast tool
```




## 🔧 Configuration

### Agent Configuration ([config/agents.yaml](src/rag_crewai/config/agents.yaml))

Defines 5 specialized agents:

- **Manager**: Orchestrates task delegation
- **Language Detector**: Identifies query language
- **Heritage Expert**: Retrieves cultural information
- **Weather Specialist**: Provides weather data
- **Reporter**: Formats final responses

### Task Configuration ([config/tasks.yaml](src/rag_crewai/config/tasks.yaml))

Defines 4 sequential tasks executed by the crew:

1. Language Detection Task
2. Heritage Research Task
3. Weather Research Task
4. Report Formatting Task

### LLM Configuration

The system uses Ollama's aya-expanse:8b model for all agents. The hierarchical process allows the Manager agent to intelligently coordinate specialist agents. To change the model, update the configuration in [crew.py](src/rag_crewai/crew.py).

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.


## 🙏 Acknowledgments

- Knowledge base compiled from Wikipedia and public sources
- Built with CrewAI framework
- Powered by Ollama and open-source LLMs

## 📧 Support

For questions or issues, please open an issue on the repository.

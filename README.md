# VocabAssistant: Personalized Language Learning Powered by LLMs

VocabAssistant is an intelligent language learning application that uses Large Language Models (LLMs), LangGraph, and LangMem to create a personalized and adaptive learning experience. The system helps users learn vocabulary in their target language through interactive exercises, spaced repetition, and personalized feedback.

## 🌟 Key Features

- **Profile-Based Personalization**: Collects user information to tailor the learning experience to individual goals, interests, and proficiency level
- **LLM-Driven Content Generation**: Creates dynamic vocabulary lists, practice exercises, and grammar explanations based on user needs
- **Intelligent Assessment**: Provides detailed feedback on user responses with personalized explanations and correction
- **Spaced Repetition System**: Schedules vocabulary reviews at optimal intervals for maximum retention
- **Memory Management**: Stores learning progress and user interactions to create a continuously improving experience
- **Adaptive Difficulty**: Adjusts content complexity based on user performance and confidence

## 📚 System Architecture

VocabAssistant uses a single-agent architecture with multiple specialized tools. The agent orchestrates the learning experience by selecting the appropriate tool based on the user's needs and context.

### Core Components:

1. **User Profiling System**: Collects and stores user information (name, target language, proficiency, interests)
2. **Vocabulary Introduction Tool**: Generates personalized vocabulary lists with translations and examples
3. **Exercise Creation Tool**: Creates custom practice exercises based on the user's level and recent vocabulary
4. **Assessment Tool**: Evaluates user responses and provides detailed feedback
5. **Spaced Repetition Tool**: Schedules vocabulary reviews based on confidence levels and learning patterns
6. **Grammar Explanation Tool**: Produces comprehensive explanations of grammar concepts with relevant examples
7. **Memory Management**: Stores and retrieves information about the user's learning journey

## 🔧 Technical Implementation

The application is built using several key technologies:

- **LangChain**: Framework for building applications with LLMs
- **LangGraph**: Orchestrates the workflow and state management
- **LangMem**: Manages semantic and episodic memory for personalized learning
- **OpenAI Models**: Powers the intelligent agent and tools (GPT-4o)
- **Jupyter Notebook**: Provides an interactive environment for development and usage

## 🚀 Getting Started

### Prerequisites

- Python 3.11 or higher
- Poetry (dependency management)
- OpenAI API key

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/username/vocab-assistant.git
   cd vocab-assistant
   ```

2. Install dependencies using Poetry:
   ```bash
   poetry install
   ```

3. Create a `.env` file with your API keys:
   ```
   OPENAI_API_KEY=your_openai_api_key
   ```

4. Activate the virtual environment:
   ```bash
   poetry shell
   ```

5. Launch Jupyter to run the application:
   ```bash
   jupyter notebook app.ipynb
   ```

## 💡 How It Works

1. **Onboarding**: When a user first interacts with VocabAssistant, the system collects information about their name, target language, proficiency level, learning goals, and interests.

2. **Learning Session**: Based on the user's profile, the system introduces new vocabulary relevant to their interests and learning goals.

3. **Practice**: The system creates custom exercises to help users practice the newly introduced vocabulary.

4. **Assessment**: When users submit their answers, the system provides detailed feedback, identifying correct and incorrect responses with explanations.

5. **Memory Management**: The system stores information about the user's learning progress, including vocabulary items and confidence levels.

6. **Spaced Repetition**: The system schedules reviews of previously learned vocabulary at optimal intervals based on the user's confidence levels.

## 🌐 Use Cases

- **Language Learners**: Individuals who want to learn vocabulary in a new language with personalized guidance
- **Travelers**: People preparing for trips to foreign countries who need essential vocabulary
- **Students**: Language students looking for additional practice outside of formal classes
- **Self-learners**: Anyone interested in efficiently acquiring vocabulary in a foreign language

## 🔍 Project Structure

- `app.ipynb`: Main application notebook with interactive interface
- `prompts.py`: Contains prompts for the LLM-based tools
- `pyproject.toml` & `poetry.lock`: Poetry dependency management files
- `README.md`: Documentation (this file)

## 🤝 Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues for bugs and feature requests.

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

Built with ❤️ using LangChain, LangGraph, and LangMem
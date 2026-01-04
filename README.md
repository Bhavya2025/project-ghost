# 🕵️ Project Ghost: Forensic AI Engine

**A hackathon tool built for hackers that analyzes failed projects and suggests winning strategies.**

## The Problem

At every hackathon, developers struggle with:
- **Decision Paralysis**: "What tech stack should I use?"
- **Project Validation**: "Is this actually a good idea?"
- **Learning from Failure**: "Why do winning projects win?"

Project Ghost solves this by analyzing any GitHub repository and providing AI-powered insights using a noir detective theme.

## The Solution

### Core Features

1. **Multimodal Analysis**
   - Analyze GitHub repository URLs using Gemini 1.5 Flash
   - Upload UI screenshots for contextual understanding
   - Combines code intelligence + visual design feedback

2. **Coroner's Report**
   - **Cause of Death**: Why the project failed
   - **Smoking Gun**: Critical technical or UX flaw
   - **Resurrection Plan**: How to win with this idea today

3. **AI-Powered Narration**
   - Text-to-speech via ElevenLabs API
   - Noir detective voice (Adam, Clyde, or Nicole)
   - Makes analysis engaging and memorable

### Tech Stack

- **Frontend**: Streamlit (rapid development, judges love it)
- **AI Analysis**: Google Gemini 1.5 Flash (multimodal, cost-effective)
- **Voice**: ElevenLabs API (natural, professional narration)
- **Environment**: Python 3.10+

## Why This Wins

### ✅ Category Coverage
- **Gemini API**: Full multimodal integration (text + images)
- **Developer Tools**: Solves a real pain point for hackers
- **Hackathon Meta**: A tool built by hackers, for hackers

### ✅ Judging Criteria
- **Innovation**: Novel combination of Gemini + ElevenLabs + Noir theme
- **Execution**: Clean, working code with proper error handling
- **Polish**: Professional UI with dark mode + noir aesthetic
- **Practicality**: Actually useful for analyzing hackathon projects

### ✅ Security Best Practices
- `.env` file for API keys (never committed)
- `.env.example` for documentation
- Input validation on all user inputs
- Error handling that doesn't expose secrets

## Setup Instructions

### 1. Clone & Install Dependencies
```bash
git clone https://github.com/yourusername/project-ghost.git
cd project-ghost
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Configure API Keys
```bash
cp .env.example .env
# Edit .env and add your API keys:
# GEMINI_API_KEY=sk-xxx...
# ELEVENLABS_API_KEY=sk-xxx...
```

### 3. Run the App
```bash
streamlit run app.py
```

Navigate to `http://localhost:8501` and start analyzing projects!

## Usage

1. **Paste a GitHub URL** (e.g., a previous hackathon project)
2. **Optionally upload a screenshot** of the UI
3. **Click "Execute Forensic Autopsy"**
4. **Read the Coroner's Report** and listen to narration
5. **Learn from the failures** to build something better

## API Keys Required

### Google Gemini
- [Get API Key](https://ai.google.dev/tutorials/setup)
- Free tier available with rate limits
- Used for multimodal analysis

### ElevenLabs
- [Get API Key](https://elevenlabs.io)
- Free tier: 10,000 characters/month
- Used for voice narration

## Demo

**Ideal Demo Flow for Judges:**

1. Paste link to a real failing hackathon project
2. Upload a screenshot of messy UI/old design
3. Let Gemini analyze both
4. Play the ElevenLabs narration
5. Show the "Resurrection Plan" section

**Why this impresses judges:**
- Shows real multimodal AI capability
- Demonstrates API integration skills
- Proves the tool actually works
- Memorable demo (noir detective theme)

## Commit History (Strategic for Judges)

Each commit tells a story of thoughtful development:

1. `feat: env setup and security best practices` - Shows you think about security
2. `feat: core forensic engine with Gemini integration` - Core value
3. `feat: multimodal image analysis support` - Advanced feature
4. `feat: elevenlabs voice narration` - Polish & engagement
5. `feat: ui polish and error handling` - Professional execution
6. `docs: comprehensive README and setup guide` - Clear documentation

This progression shows judges:
- You plan ahead (security first)
- You iterate thoughtfully
- You add features incrementally
- You document thoroughly

## Future Enhancements

- [ ] Cache results to reduce API calls
- [ ] GitHub OAuth for auto-fetching repo details
- [ ] Batch analysis of multiple repos
- [ ] Custom prompts for different analysis types
- [ ] Dark/Light mode toggle
- [ ] Save reports as PDF

## License

MIT - Built for hackers, shared freely.

---

**Built in ~4 hours by [Your Team] at [Hackathon Name] 2026**

*"Where failed projects become winning ideas."*

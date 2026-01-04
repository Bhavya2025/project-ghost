# 🕵️ Project Ghost: Forensic AI Engine

**Analyzes GitHub repos and screenshots using Gemini to generate  noir detective-themed project reports with AI narration.**

## What It Does

Point it at a GitHub repo URL, optionally upload a screenshot, and it'll analyze the code using Gemini's multimodal capabilities to generate a "Coroner's Report" complete with AI narration. Built as a hackathon project to test out Gemini + ElevenLabs + Vultr together.

## The Solution

### Core Features

1. **Multimodal Analysis**
   - Analyze GitHub repository URLs using Gemini 2.5 Flash
   - Upload UI screenshots for contextual understanding
   - Combines code intelligence + visual design feedback in a single request

2. **Coroner's Report**
   - **Cause of Death**: Why the project failed
   - **Smoking Gun**: Critical technical or UX flaw
   - **Resurrection Plan**: How to win with this idea today

3. **AI-Powered Narration**
   - Text-to-speech via ElevenLabs API (v0.2.15)
   - Dynamic voice selection from available voices
   - Makes analysis engaging and memorable

### Tech Stack

- **Frontend**: Streamlit (built a 300+ student grade calculator in it, so figured I'd use it again as it makes frontend much simpler)
- **AI Analysis**: Google Gemini 2.5 Flash
- **Voice**: ElevenLabs v0.2.15
- **Cloud**: Vultr Ubuntu 22.04
- **Environment**: Python 3.10+

## Implementation Notes

### What I Learned Building This

**Dependencies Matter**: Had to pin ElevenLabs to v0.2.15 due to Pydantic v2 conflicts. Stable versions beat latest versions when under time pressure.

**Streamlit State Management**: Session state needs explicit initialization or you crash on reload. Learned this the hard way.

### Security & Best Practices
- `.env` file for API keys (never committed, gitignored)
- `.env.example` for documentation
- Session state initialization to prevent Streamlit crashes
- Markdown stripping before voice generation for clean narration
- Tested and deployed on production cloud infrastructure

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
- Used for multimodal analysis

### ElevenLabs
- [Get API Key](https://elevenlabs.io)
- Used for voice narration

## Live Demo

**Running at:** http://207.246.125.6

Full stack deployed and working. No local setup needed if you just want to try it out.

## How to Use It

1. Visit http://207.246.125.6
2. Paste a GitHub URL
3. Optionally upload a screenshot
4. Click "EXECUTE FORENSIC AUTOPSY"
5. Read the report and listen to the narration

## Bugs Fixed

- ElevenLabs v0.2.15 pinned to avoid Pydantic v2 conflicts
- Streamlit session state initialized explicitly (prevents reload crashes)
- Markdown stripped before voice generation (no more reading asterisks aloud)
- Model selection locked to gemini-2.5-flash (most stable option)
- Ubuntu venv setup required explicit python3.10-venv install

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

**Built by Ryan and Bhavya at Hacks for Hackers 2026**

*"Where failed projects become winning ideas."*

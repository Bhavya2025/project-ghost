import streamlit as st
import google.generativeai as genai
from elevenlabs.client import ElevenLabs
import PIL.Image
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# --- 🕵️ DETECTIVE UI STYLING ---
st.set_page_config(page_title="Project Ghost", page_icon="🕵️", layout="wide")
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; color: #ffffff; }
    h1 { color: #ff4b4b; font-family: 'Courier New', monospace; text-shadow: 0 0 10px #ff4b4b; }
    h3 { color: #ff9500; }
    .stButton>button { width: 100%; background-color: #ff4b4b; color: white; border-radius: 5px; height: 3em; font-weight: bold; }
    .stButton>button:hover { background-color: #ff6b6b; }
    .stTextInput > div > div > input { background-color: #161b22; border: 1px solid #30363d; }
    .stInfo { background-color: #161b22; border-left: 4px solid #ff4b4b; }
    </style>
    """, unsafe_allow_html=True)

st.title("🕵️ PROJECT GHOST: FORENSIC AI ENGINE")
st.write("*Analyzing dead projects. Resurrection guaranteed.*")

# --- ⚙️ SIDEBAR: THE GEAR ---
with st.sidebar:
    st.header("🔧 Detective Credentials")
    
    # Try to load from .env, allow manual override
    default_gemini = os.getenv("GEMINI_API_KEY", "")
    default_eleven = os.getenv("ELEVENLABS_API_KEY", "")
    
    gemini_key = st.text_input("Gemini API Key", value=default_gemini, type="password", 
                                placeholder="sk-xxx... or from .env")
    eleven_key = st.text_input("ElevenLabs API Key", value=default_eleven, type="password",
                               placeholder="sk-xxx... or from .env")
    
    voice_options = {
        "Adam": "pNInY6obpgc4xHiPF9nJ",
        "Clyde": "2EiwWnXFnvU5JabPgLCt",
        "Nicole": "piTKgcLEGmPLwcF1v8Qu"
    }
    voice_name = st.selectbox("Choose Narrator Voice", list(voice_options.keys()))
    voice_id = voice_options[voice_name]

# --- 🔦 THE INVESTIGATION ---
st.divider()
st.subheader("🔍 Upload Evidence")

col1, col2 = st.columns(2)
with col1:
    repo_url = st.text_input(
        "GitHub Repo URL (The 'Crime Scene')", 
        placeholder="https://github.com/user/dead-project"
    )
with col2:
    screenshot = st.file_uploader(
        "Upload UI Screenshot (Optional Multimodal Evidence)", 
        type=["jpg", "jpeg", "png"]
    )

# --- 🚨 AUTOPSY EXECUTION ---
if st.button("🔍 EXECUTE FORENSIC AUTOPSY", use_container_width=True):
    # Validation
    if not gemini_key:
        st.error("⚠️ Missing Gemini API Key. Set it in the sidebar or create a .env file.")
        st.stop()
    
    if not repo_url or not repo_url.startswith("https://github.com"):
        st.error("⚠️ Please enter a valid GitHub URL (https://github.com/...).")
        st.stop()
    
    try:
        # Configure Gemini
        genai.configure(api_key=gemini_key)
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        with st.spinner("🔬 Analyzing the code wreckage..."):
            # Build Multimodal Prompt
            prompt = f"""
You are a hardboiled noir detective investigating a project failure at a hackathon. 
Your job is to deliver a "Coroner's Report" that's brutally honest.

REPO TO INVESTIGATE: {repo_url}

Provide your report with these sections:
1. CAUSE OF DEATH: Why did this project fail? (Technical or UX reasons)
2. THE SMOKING GUN: One critical flaw that stands out
3. RESURRECTION PLAN: How to win with a similar idea TODAY

TONE: Gritty, noir detective. Think hard-boiled detective fiction. Keep it under 200 words.
FORMAT: Use short, punchy sentences. Be blunt.

Example tone: "The code was a mess. No tests. No docs. Dead on arrival."
"""
            
            # Build multimodal inputs
            inputs = [prompt]
            if screenshot:
                try:
                    image = PIL.Image.open(screenshot)
                    inputs.append(image)
                    st.write("📸 *Added screenshot to analysis...*")
                except Exception as e:
                    st.warning(f"Could not load screenshot: {e}")
            
            # Call Gemini
            response = model.generate_content(inputs)
            report_text = response.text
            
            # Display Report
            st.divider()
            st.markdown("### 📜 THE CORONER'S REPORT")
            st.info(report_text)
            
            # --- 🎙️ ELEVENLABS NARRATION ---
            if eleven_key:
                try:
                    with st.spinner("🎙️ The detective narrates..."):
                        client = ElevenLabs(api_key=eleven_key)
                        audio_stream = client.text_to_speech.convert(
                            text=report_text,
                            voice_id=voice_id,
                            model_id="eleven_multilingual_v2"
                        )
                        # Convert stream to bytes
                        audio_bytes = b"".join(chunk for chunk in audio_stream if chunk)
                        st.audio(audio_bytes, format='audio/mp3')
                        st.success("🎬 Narration complete.")
                except Exception as e:
                    st.error(f"🎙️ Voice engine failed: {e}")
            else:
                st.warning("🎙️ No ElevenLabs key provided. Skipping narration.")
    
    except Exception as e:
        st.error(f"🚨 Investigation failed: {str(e)}")

# --- 📋 FOOTER ---
st.divider()
st.caption("*Project Ghost v1.0 | Built for Hackers, by Hackers | 2026*")
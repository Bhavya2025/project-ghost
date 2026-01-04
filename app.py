import streamlit as st
import google.generativeai as genai
from elevenlabs.client import ElevenLabs
import PIL.Image
import io

# --- 🕵️ DETECTIVE UI STYLING ---
st.set_page_config(page_title="Project Ghost", page_icon="🕵️")
st.markdown("""
    <style>
    .stApp { background-color: #0e1117; color: #ffffff; }
    h1 { color: #ff4b4b; font-family: 'Courier New', monospace; }
    .stButton>button { width: 100%; background-color: #ff4b4b; color: white; border-radius: 5px; height: 3em; }
    </style>
    """, unsafe_allow_html=True)

st.title("🕵️ PROJECT GHOST: FORENSIC AI")
st.write("Checking the pulse of dead projects. Put the evidence on the table.")

# --- ⚙️ SIDEBAR: THE GEAR ---
with st.sidebar:
    st.header("🔧 Detective Credentials")
    gemini_key = st.text_input("Gemini API Key", type="password")
    eleven_key = st.text_input("ElevenLabs API Key", type="password")
    voice_id = st.selectbox("Choose Narrator", ["Adam", "Clyde", "Nicole"])

# --- 🔦 THE INVESTIGATION ---
repo_url = st.text_input("GitHub Repo URL (The 'Crime Scene')", placeholder="https://github.com/user/dead-project")
screenshot = st.file_uploader("Upload UI Screenshot (Multimodal Evidence)", type=["jpg", "jpeg", "png"])

if st.button("🔍 EXECUTE AUTOPSY"):
    if not (gemini_key and repo_url):
        st.error("I need a Gemini key and a repo link to start the investigation, kid.")
    else:
        # Configure Gemini
        genai.configure(api_key=gemini_key)
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        with st.spinner("Analyzing the code wreckage..."):
            # Build Multimodal Prompt
            prompt = f"""
            Act as a Noir Detective investigating why a hackathon project failed.
            Repo: {repo_url}
            Give me a gritty report including:
            1. CAUSE OF DEATH: Why did it fail?
            2. THE SMOKING GUN: One major technical or UX flaw.
            3. RESURRECTION: How to win with this today.
            Tone: Gritty, blunt, noir. Keep it under 150 words.
            """
            
            inputs = [prompt]
            if screenshot:
                inputs.append(PIL.Image.open(screenshot))
            
            response = model.generate_content(inputs)
            report_text = response.text
            
            st.markdown("### 📜 THE CORONER'S REPORT")
            st.info(report_text)

            # --- 🎙️ ELEVENLABS NARRATION ---
            if eleven_key:
                try:
                    client = ElevenLabs(api_key=eleven_key)
                    audio_stream = client.text_to_speech.convert(
                        text=report_text,
                        voice_id=voice_id,
                        model_id="eleven_multilingual_v2"
                    )
                    # Convert stream to bytes for Streamlit
                    audio_bytes = b"".join(chunk for chunk in audio_stream if chunk)
                    st.audio(audio_bytes, format='audio/mp3')
                except Exception as e:
                    st.warning(f"Voice engine stalled: {e}")
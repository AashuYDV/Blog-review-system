import streamlit as st

st.set_page_config(
    page_title="Blog Reviewer",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ── MASTER CSS ──────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;500;600;700;800&family=DM+Sans:ital,opsz,wght@0,9..40,300;0,9..40,400;0,9..40,500;1,9..40,300&display=swap');

/* ── RESET & BASE ── */
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

html, body, [data-testid="stAppViewContainer"], [data-testid="stMain"],
.main, .block-container {
    background: #0a0a0a !important;
    color: #e8e8e8 !important;
    font-family: 'DM Sans', sans-serif !important;
}

[data-testid="stAppViewContainer"] {
    background: radial-gradient(ellipse 80% 50% at 50% -10%, rgba(34,197,94,0.08) 0%, transparent 60%),
                radial-gradient(ellipse 60% 40% at 80% 80%, rgba(34,197,94,0.04) 0%, transparent 50%),
                #0a0a0a !important;
    min-height: 100vh;
}

.block-container {
    max-width: 860px !important;
    padding: 0 2rem 8rem 2rem !important;
    margin: 0 auto !important;
}

/* hide streamlit chrome */
#MainMenu, footer, header, [data-testid="stToolbar"],
[data-testid="stDecoration"], [data-testid="stStatusWidget"] { display: none !important; }

/* ── HERO ── */
.hero-wrap {
    text-align: center;
    padding: 56px 0 32px;   /* 🔑 reduced top + bottom */
    position: relative;
}
.hero-logo {
    width: 52px; height: 52px;
    margin: 0 auto 28px;
    background: linear-gradient(135deg, #22c55e, #16a34a);
    border-radius: 16px;
    display: flex; align-items: center; justify-content: center;
    font-size: 26px;
    box-shadow: 0 0 40px rgba(34,197,94,0.3), 0 0 80px rgba(34,197,94,0.1);
    position: relative;
}
.hero-logo::after {
    content: '';
    position: absolute; inset: -3px;
    border-radius: 18px;
    background: linear-gradient(135deg, rgba(34,197,94,0.4), transparent);
    z-index: -1;
}
.hero-title {
    font-family: 'Syne', sans-serif !important;
    font-size: clamp(2.9rem, 6vw, 4.1rem) !important;
    font-weight: 650 !important;   /* 🔑 this is the key */
    letter-spacing: -0.015em;      /* less tight */
    line-height: 1.15;             /* more airy */
    color: #ffffff !important;
    margin-bottom: 18px;
}

.hero-title span {
    color: #22c55e;
    font-weight: 650;
}
.hero-sub {
    font-size: 1rem;
    color: rgba(255,255,255,0.55);
    font-weight: 400;
    max-width: 520px;
    margin: 16px auto 0;
    line-height: 1.7;
}

/* ── CARDS ── */
.cards-row {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 14px;
    margin: 44px 0 36px;
}
.card {
    background: rgba(255,255,255,0.03);
    border: 1px solid rgba(255,255,255,0.07);
    border-radius: 16px;
    padding: 24px 20px;
    transition: all 0.25s ease;
    cursor: default;
    position: relative;
    overflow: hidden;
}
.card::before {
    content: '';
    position: absolute; top: 0; left: 0; right: 0;
    height: 1px;
    background: linear-gradient(90deg, transparent, rgba(34,197,94,0.3), transparent);
    opacity: 0;
    transition: opacity 0.25s;
}
.card:hover { 
    border-color: rgba(34,197,94,0.25);
    background: rgba(34,197,94,0.04);
    transform: translateY(-2px);
    box-shadow: 0 8px 32px rgba(0,0,0,0.4);
}
.card:hover::before { opacity: 1; }
.card-icon {
    width: 36px; height: 36px;
    background: rgba(34,197,94,0.1);
    border-radius: 10px;
    display: flex; align-items: center; justify-content: center;
    margin-bottom: 14px;
    font-size: 16px;
    border: 1px solid rgba(34,197,94,0.15);
}
.card-title {
    font-family: 'Syne', sans-serif;
    font-size: 0.95rem;
    font-weight: 600;
    color: #ffffff;
    margin-bottom: 8px;
}
.card-desc {
    font-size: 0.82rem;
    color: rgba(255,255,255,0.55);
    line-height: 1.6;
    font-weight: 400;
}
/* ── FIRST-FOLD COMPRESSION ── */
.cards-row {
    margin: 28px 0 24px;   /* was too tall */
}

.tabs-wrap {
    margin: 20px 0 18px;
}

.status-badge {
    margin-bottom: 22px;
}

/* ── TABS (REFERENCE STYLE) ── */
.tabs-wrap {
    display: flex;
    gap: 20px;
    justify-content: center;
    margin: 28px 0 34px;
    border-bottom: none;
}
.tab-btn {
    font-size: 0.85rem;
    color: #6b7280;
    background: none;
    border: none;
    padding: 0 2px 6px;
    cursor: pointer;
    border-bottom: 2px solid transparent;
    transition: all 0.2s ease;
}
.tab-btn.active {
    color: #22c55e;
    border-bottom-color: #22c55e;
    font-weight: 500;
}
.tab-btn:hover:not(.active) {
    color: #d1d5db;
}

/* ── CHATGPT-STYLE INPUT ── */
.input-outer {
    position: fixed;
    bottom: 0;
    left: 0;
    right: 0;
    padding: 20px;
    background: linear-gradient(to top, #0a0a0a 65%, transparent);
}
.input-inner {
    max-width: 860px;
    margin: 0 auto;
    position: relative;
}
.input-box {
    width: 100%;
    background: #ffffff;
    color: #111827;
    border-radius: 999px;
    border: none;
    padding: 16px 56px 16px 48px;
    font-size: 0.95rem;
    outline: none;
    box-shadow: 0 10px 30px rgba(0,0,0,0.35);
}
.input-box::placeholder {
    color: #9ca3af;
}
.input-left-icon {
    position: absolute;
    left: 18px;
    top: 50%;
    transform: translateY(-50%);
    color: #9ca3af;
}
.input-send-btn {
    position: absolute;
    right: 8px;
    top: 50%;
    transform: translateY(-50%);
    width: 38px;
    height: 38px;
    background: #22c55e;
    border-radius: 50%;
    border: none;
    color: white;
    font-size: 16px;
    cursor: pointer;
}

/* ── STATUS BADGE ── */
.status-badge {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    background: rgba(34,197,94,0.08);
    border: 1px solid rgba(34,197,94,0.15);
    border-radius: 99px;
    padding: 5px 14px;
    font-size: 0.73rem;
    color: #22c55e;
    font-weight: 500;
    letter-spacing: 0.04em;
    text-transform: uppercase;
    margin: 0 auto 32px;
    display: block;
    width: fit-content;
}
.status-dot {
    width: 6px; height: 6px;
    background: #22c55e;
    border-radius: 50%;
    display: inline-block;
    animation: pulse-dot 2s ease-in-out infinite;
}
@keyframes pulse-dot {
    0%, 100% { opacity: 1; transform: scale(1); }
    50% { opacity: 0.5; transform: scale(0.8); }
}
.home-input-wrap {
    margin-top: -12px;   /* 🔑 pulls input upward */
}

/* ── CHAT MESSAGES ── */
.chat-msg-user {
    display: flex; justify-content: flex-end;
    margin: 16px 0;
}
.chat-msg-user .bubble {
    background: rgba(34,197,94,0.12);
    border: 1px solid rgba(34,197,94,0.2);
    border-radius: 18px 18px 4px 18px;
    padding: 12px 18px;
    max-width: 75%;
    font-size: 0.9rem;
    color: #d1fae5;
    line-height: 1.6;
}
.chat-msg-ai {
    display: flex; align-items: flex-start; gap: 12px;
    margin: 16px 0;
}
.ai-avatar {
    width: 32px; height: 32px;
    background: linear-gradient(135deg, #22c55e, #16a34a);
    border-radius: 10px;
    display: flex; align-items: center; justify-content: center;
    font-size: 14px;
    flex-shrink: 0;
    box-shadow: 0 0 12px rgba(34,197,94,0.3);
}
.chat-msg-ai .bubble {
    background: rgba(255,255,255,0.04);
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 4px 18px 18px 18px;
    padding: 14px 18px;
    max-width: 82%;
    font-size: 0.9rem;
    color: #d1d5db;
    line-height: 1.7;
}

/* ── DIVIDER ── */
.section-divider {
    height: 1px;
    background: linear-gradient(90deg, transparent, rgba(255,255,255,0.08), transparent);
    margin: 40px 0;
}

/* ── STREAMLIT OVERRIDES ── */
.stTextInput > div > div > input {
    background: rgba(255,255,255,0.05) !important;
    border: 1px solid rgba(255,255,255,0.1) !important;
    border-radius: 16px !important;
    color: #e2e8f0 !important;
    padding: 18px 20px !important;
    font-family: 'DM Sans', sans-serif !important;
    font-size: 0.95rem !important;
}
.stTextInput > div > div > input:focus {
    border-color: rgba(34,197,94,0.4) !important;
    box-shadow: 0 0 0 3px rgba(34,197,94,0.08) !important;
}
.stButton > button {
    background: linear-gradient(135deg, #22c55e, #16a34a) !important;
    color: white !important;
    border: none !important;
    border-radius: 12px !important;
    font-family: 'Syne', sans-serif !important;
    font-weight: 600 !important;
    font-size: 0.88rem !important;
    padding: 12px 28px !important;
    letter-spacing: 0.02em !important;
    transition: all 0.2s !important;
    box-shadow: 0 4px 16px rgba(34,197,94,0.3) !important;
}
.stButton > button:hover {
    transform: translateY(-1px) !important;
    box-shadow: 0 8px 24px rgba(34,197,94,0.4) !important;
}
.stSpinner > div { border-top-color: #22c55e !important; }

/* scrollbar */
::-webkit-scrollbar { width: 4px; }
::-webkit-scrollbar-track { background: transparent; }
::-webkit-scrollbar-thumb { background: rgba(255,255,255,0.1); border-radius: 4px; }
::-webkit-scrollbar-thumb:hover { background: rgba(34,197,94,0.3); }
</style>
""", unsafe_allow_html=True)


# ── SESSION STATE ────────────────────────────────────────────────────────────
if "messages" not in st.session_state:
    st.session_state.messages = []
if "phase" not in st.session_state:
    st.session_state.phase = "home"   # home | chat
if "doc_url" not in st.session_state:
    st.session_state.doc_url = ""


# ════════════════════════════════════════════════════════════════════════════
# HOME SCREEN
# ════════════════════════════════════════════════════════════════════════════
if st.session_state.phase == "home":

    # Hero
    st.markdown("""
    <div class="hero-wrap">
        <div class="hero-logo">✦</div>
        <div class="hero-title">How can I help<br>you <span>today?</span></div>
        <p class="hero-sub">Paste a Google Doc link and I'll review it in Krutika's style —<br>
        section-by-section, with fixes and a fully rewritten version.</p>
    </div>
    """, unsafe_allow_html=True)

    # Status badge
    st.markdown("""
    <div class="status-badge">
        <span class="status-dot"></span>&nbsp; Krutika AI · Ready
    </div>
    """, unsafe_allow_html=True)

    # Feature cards
    st.markdown("""
    <div class="cards-row">
        <div class="card">
            <div class="card-icon">📋</div>
            <div class="card-title">Section-Wise Review</div>
            <div class="card-desc">Every H2 and H3 reviewed individually with 🔴 issues and ✅ fixes — exactly how Krutika does it.</div>
        </div>
        <div class="card">
            <div class="card-icon">✍️</div>
            <div class="card-title">Rewritten Blog</div>
            <div class="card-desc">A fully rewritten version of your blog incorporating every fix — download-ready as a Word doc.</div>
        </div>
        <div class="card">
            <div class="card-icon">📊</div>
            <div class="card-title">Scorecard + SEO Audit</div>
            <div class="card-desc">10-category scorecard, SEO compliance check, grammar audit, and a priority action list.</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Tabs (decorative for now)
    st.markdown("""
    <div class="tabs-wrap">
    <button class="tab-btn active">All</button>
    <button class="tab-btn">Text</button>
    <button class="tab-btn">Image</button>
    <button class="tab-btn">Video</button>
    <button class="tab-btn">Music</button>
    <button class="tab-btn">Analytics</button>
</div>
    """, unsafe_allow_html=True)

    # URL Input
    st.markdown('<div class="home-input-wrap">', unsafe_allow_html=True)

    col1, col2 = st.columns([5, 1])
    with col1:
        url = st.text_input(
            "",
            placeholder="✦  Paste your Google Doc link here...",
            key="url_input",
            label_visibility="collapsed"
        )
    with col2:
        go = st.button("Review →", use_container_width=True)

    if go and url:
        st.session_state.doc_url = url
        st.session_state.phase = "chat"
        st.session_state.messages = [
            {
                "role": "ai",
                "content": f"Got it — I've received your Google Doc link.\n\n✦ Fetching blog content...\n✦ Running full review against Krutika's guidelines...\n\nThis will take about 30–60 seconds. I'll return:\n\n**① Section-wise Review Document** (.docx)\n**② Rewritten Blog** (.docx)\n**③ Scorecard + Priority Action List**\n\nHang tight."
            }
        ]
        st.rerun()

    elif go and not url:
        st.markdown("""
        <div style="text-align:center; color:#ef4444; font-size:0.85rem; margin-top:12px;">
            Please paste a Google Doc link before clicking Review →
        </div>
        """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)
# ════════════════════════════════════════════════════════════════════════════
# CHAT SCREEN
# ════════════════════════════════════════════════════════════════════════════
else:

    # Compact header
    st.markdown("""
    <div style="padding: 28px 0 8px; display:flex; align-items:center; gap:12px;">
        <div style="width:32px;height:32px;background:linear-gradient(135deg,#22c55e,#16a34a);
                    border-radius:10px;display:flex;align-items:center;justify-content:center;
                    font-size:14px;box-shadow:0 0 12px rgba(34,197,94,0.3);">✦</div>
        <div>
            <div style="font-family:'Syne',sans-serif;font-weight:700;font-size:1rem;color:#f0f0f0;">
                Krutika AI
            </div>
            <div style="font-size:0.72rem;color:#22c55e;letter-spacing:0.05em;text-transform:uppercase;font-weight:500;">
                <span style="display:inline-block;width:5px;height:5px;background:#22c55e;border-radius:50%;
                             margin-right:5px;vertical-align:middle;animation:pulse-dot 2s infinite;"></span>
                Reviewing · Active
            </div>
        </div>
    </div>
    <div class="section-divider"></div>
    """, unsafe_allow_html=True)
    # Doc URL pill
    if st.session_state.doc_url:
        short_url = st.session_state.doc_url[:55] + "..." if len(st.session_state.doc_url) > 55 else st.session_state.doc_url
        st.markdown(f"""
        <div style="display:flex;align-items:center;gap:8px;margin-bottom:20px;
                    background:rgba(255,255,255,0.03);border:1px solid rgba(255,255,255,0.07);
                    border-radius:10px;padding:10px 14px;width:fit-content;max-width:100%;">
            <span style="font-size:13px;">🔗</span>
            <span style="font-size:0.78rem;color:#6b7280;font-family:'DM Sans',sans-serif;
                         overflow:hidden;text-overflow:ellipsis;white-space:nowrap;">{short_url}</span>
        </div>
        """, unsafe_allow_html=True)

    # Chat messages
    for msg in st.session_state.messages:
        if msg["role"] == "user":
            st.markdown(f"""
            <div class="chat-msg-user">
                <div class="bubble">{msg["content"]}</div>
            </div>
            """, unsafe_allow_html=True)
        else:
            content_html = msg["content"].replace("\n", "<br>").replace("**", "<strong>").replace("**", "</strong>")
            # simple bold replacement
            import re
            content_html = re.sub(r'\*\*(.*?)\*\*', r'<strong style="color:#d1fae5;">\1</strong>', msg["content"])
            content_html = content_html.replace("\n", "<br>")
            st.markdown(f"""
            <div class="chat-msg-ai">
                <div class="ai-avatar">✦</div>
                <div class="bubble">{content_html}</div>
            </div>
            """, unsafe_allow_html=True)

    # Spacer for fixed input bar
    st.markdown("<div style='height:100px'></div>", unsafe_allow_html=True)

    # ── FIXED INPUT BAR ──
    st.markdown("""
    <div class="input-outer">
        <div class="input-inner">
            <span class="input-left-icon">✦</span>
            <input class="input-box" placeholder="Ask a follow-up — e.g. 'Rewrite only the intro' or 'Make the conclusion punchier'..." />
            <button class="input-send-btn">→</button>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Streamlit-functional chat input (hidden visually but functional)
    with st.container():
        c1, c2 = st.columns([6, 1])
        with c1:
            follow_up = st.text_input("", placeholder="Ask a follow-up...",
                                      key="followup", label_visibility="collapsed")
        with c2:
            send = st.button("Send", key="send_btn")

        if send and follow_up:
            st.session_state.messages.append({"role": "user", "content": follow_up})
            st.session_state.messages.append({
                "role": "ai",
                "content": f"Got it — working on that now.\n\n*(This is a UI prototype — Gemini API will power real responses once connected.)*"
            })
            st.rerun()

    # Back button
    st.markdown("<div style='height:16px'></div>", unsafe_allow_html=True)
    if st.button("← New Review", key="back"):
        st.session_state.phase = "home"
        st.session_state.messages = []
        st.session_state.doc_url = ""
        st.rerun()

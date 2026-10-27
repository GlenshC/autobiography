"""CSIT 349 - Applied AI | Autobiography & Portfolio.

Run with:  streamlit run app.py
"""

from __future__ import annotations

import base64
from datetime import datetime
from pathlib import Path

import altair as alt
import pandas as pd
import streamlit as st

# --------------------------------------------------------------------------
# Page config
# --------------------------------------------------------------------------

st.set_page_config(
    page_title="Glensh Belarmino | Portfolio",
    page_icon="🎮",
    layout="wide",
    initial_sidebar_state="auto",
)

ROOT = Path(__file__).parent
ASSETS = ROOT / "assets"

NAME = "Glensh"
FULL_NAME = "Glenshayne G. Belarmino"
SECTION = "F1"
PROGRAM = "BSCS 3"
COURSE = "CSIT 349 · Applied AI"
INSTRUCTOR = "Jun Albert S. Pardillo"
EMAIL = "glenshc@gmail.com"
GITHUB = "https://github.com/GlenshC"
ITCH = "https://glensh.itch.io"
TAGLINE = "Hesitate and you'll lose your moment."

# --------------------------------------------------------------------------
# Assets
# --------------------------------------------------------------------------


def resume_file() -> tuple[bytes, str, str] | None:
    """Return the resume bytes plus a filename and MIME type that match reality."""
    path = ASSETS / "cv.pdf"
    if not path.exists():
        return None
    data = path.read_bytes()
    if data.startswith(b"%PDF"):
        return data, "Glensh-Belarmino-Resume.pdf", "application/pdf"
    if data.startswith(b"\xff\xd8"):
        return data, "Glensh-Belarmino-Resume.jpg", "image/jpeg"
    return None


def project_shot(filename: str) -> Path | None:
    """Screenshot for a project, ignoring files that are really the resume."""
    path = ASSETS / filename
    if not path.exists():
        return None
    resume = ASSETS / "cv.pdf"
    if resume.exists() and path.stat().st_size == resume.stat().st_size:
        if path.read_bytes() == resume.read_bytes():
            return None
    return path


def standin(label: str) -> None:
    st.markdown(
        f'<div class="standin"><div><span class="standin-tag">IMAGE PENDING</span>'
        f"<br>{label}</div></div>",
        unsafe_allow_html=True,
    )


def shot(filename: str, caption: str, label: str, pixelate: bool = False) -> None:
    path = project_shot(filename)
    if not path:
        standin(label)
        return
    if not pixelate:
        st.image(str(path), caption=caption, width="stretch")
        return
    # Inline the pixel-art screenshot so it can be upscaled without soft edges.
    data = base64.b64encode(path.read_bytes()).decode("ascii")
    mime = "image/png" if path.suffix.lower() == ".png" else "image/jpeg"
    st.markdown(
        f'<figure class="shot pixel"><img src="data:{mime};base64,{data}" alt="{caption}">'
        f"<figcaption>{caption}</figcaption></figure>",
        unsafe_allow_html=True,
    )


# --------------------------------------------------------------------------
# Data
# --------------------------------------------------------------------------

SKILLS = [
    # skill, score, category
    ("Godot / GDExtension", 100, "Engines"),
    ("Multithreading", 100, "Systems"),
    ("C", 90, "Languages"),
    ("C++", 90, "Languages"),
    ("C#", 90, "Languages"),
    ("Java", 90, "Languages"),
    ("JavaScript", 90, "Languages"),
    ("Systems architecture", 80, "Systems"),
    ("OpenGL / rendering", 80, "Engines"),
    ("Python", 70, "Languages"),
    ("Kotlin", 70, "Languages"),
    ("SQL", 70, "Languages"),
    ("Git", 70, "Tooling"),
    ("JavaFX", 70, "Tooling"),
    ("React Native", 70, "Tooling"),
    ("Lua", 40, "Languages"),
    ("AutoHotkey", 40, "Tooling"),
]

CHART_DEFAULT = [
    "C",
    "C++",
    "C#",
    "Python",
    "Java",
    "Godot / GDExtension",
    "OpenGL / rendering",
]

MILESTONES = [
    {
        "year": "2024",
        "title": "Zira POS goes live in a restaurant",
        "note": "First paid work. React Native, a Bluetooth receipt printer, and a crash course in why architecture matters.",
    },
    {
        "year": "2025",
        "title": "Adobo Engine, plus a jam win",
        "note": "A C and OpenGL engine written from docs alone. Same year, 9Lives: Ame took 1st at Sugbuanon Saga.",
    },
    {
        "year": "2026",
        "title": "Two podiums and one rewrite",
        "note": "1st at UP Game Jam with Pool Party, 3rd at DOST NEXT LEVEL with Limitless, and Netfox C++ underway.",
    },
    {
        "year": "2027",
        "title": "Target: a working embedded system",
        "note": "Something with servos in it. The Arduino kit was a start, not the plan.",
        "future": True,
    },
    {
        "year": "2028",
        "title": "Target: graduate, then agriculture",
        "note": "BS Computer Science, and the first honest attempt at tech for Philippine farming.",
        "future": True,
    },
]

MORE_WORK = [
    {
        "Project": "Adobo Engine",
        "Role": "Solo developer",
        "Year": "2025",
        "Stack": "C, OpenGL, GLFW, GLAD, cglm, Dear ImGui",
        "Note": "Modular 2D/3D engine: ECS, sprite batching, shaders, AABB and circle collision, built-in editor, CMake for Windows/Linux/macOS.",
        "core": True,
    },
    {
        "Project": "$-Family Gesture Port",
        "Role": "Solo developer",
        "Year": "2025",
        "Stack": "C++, GDExtension",
        "Note": "Ported $1, $N, $P, $P+ and $Q unistroke and multistroke recognition into a reusable Godot module.",
        "core": True,
    },
    {
        "Project": "OnlyCodes",
        "Role": "Team lead, lead developer",
        "Year": "2026",
        "Stack": "Java, JavaFX, SQL",
        "Note": "Offline code judge for a five-person capstone. Multithreaded judging, file-based problem sharing.",
        "core": True,
    },
    {
        "Project": "9Lives: Ame",
        "Role": "Contributor",
        "Year": "2025",
        "Stack": "Godot, 2.5D",
        "Note": "Story-driven horror jam entry. 1st place at Sugbuanon Saga 2025, shipped through a tight schedule and bad weather.",
        "core": True,
    },
    {
        "Project": "NetfoxCs",
        "Role": "Contributor",
        "Year": "2026",
        "Stack": "C#, Godot",
        "Note": "C# bridge for Netfox, built as a replacement for NetfoxSharp.",
        "core": False,
    },
    {
        "Project": "Zira POS",
        "Role": "Solo developer",
        "Year": "2024",
        "Stack": "React Native, JavaScript",
        "Note": "Restaurant point of sale: ordering, transaction history, Bluetooth receipt printing. First paid product.",
        "core": False,
    },
]

PAGES = ["Home", "Autobiography", "Skills", "Projects", "Contact"]

# --------------------------------------------------------------------------
# Sidebar
# --------------------------------------------------------------------------

with st.sidebar:
    st.markdown(
        f"""
        <div class="brand">
            <div class="brand-badge">GB</div>
            <div>
                <div class="brand-name">{NAME}</div>
                <div class="brand-meta">{PROGRAM} · Section {SECTION}</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    page = st.radio("Sections", PAGES, label_visibility="collapsed")

    st.divider()
    st.caption("QUICK FACTS")
    st.markdown(
        """
- Cebu City, Philippines
- BS Computer Science, CIT-U
- 3 game jam podiums
- C / C++ / C# first
- Chivalry 2 enjoyer
        """
    )

    st.divider()
    st.link_button("GitHub", GITHUB, width="stretch")
    st.link_button("itch.io", ITCH, width="stretch")
    st.link_button("Email", f"mailto:{EMAIL}", width="stretch")

    resume = resume_file()
    if resume:
        data, filename, mime = resume
        label = "Download résumé" if mime == "application/pdf" else "Download résumé (image)"
        st.download_button(label, data, file_name=filename, mime=mime, width="stretch")
    else:
        st.caption("Résumé upload pending")

    st.divider()
    pixel = st.toggle("Pixel headings", value=True)
    st.caption(f"{COURSE} · Built with Streamlit")

# --------------------------------------------------------------------------
# Styling
# --------------------------------------------------------------------------

FONT_IMPORT = (
    "@import url('https://fonts.googleapis.com/css2?family=Press+Start+2P&"
    "family=IBM+Plex+Mono:wght@400;500;600&display=swap');"
    if pixel
    else "@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500;600&display=swap');"
)
HEADING_FONT = (
    "'Press Start 2P', 'IBM Plex Mono', monospace"
    if pixel
    else "'IBM Plex Mono', monospace"
)
HEADING_SIZE = "2.7rem" if pixel else "2.4rem"

st.markdown(
    "<style>"
    + FONT_IMPORT
    + """
    .stApp {
        --heading-font: __HEADING_FONT__;
        --h1-size: __H1_SIZE__;
        background:
            radial-gradient(1100px 500px at 15% -10%, rgba(224, 27, 36, 0.10), transparent 60%),
            #0a0a0c;
    }
    html, body, [class*="st-"] { font-family: 'IBM Plex Mono', ui-monospace, monospace; }
    /* the rule above also hits icon spans, which must keep their glyph font */
    [data-testid="stIconMaterial"], .material-symbols-rounded {
        font-family: "Material Symbols Rounded" !important;
        font-feature-settings: "liga" !important;
        line-height: 1;
    }
    .stApp p, .stApp li { font-size: 0.94rem; line-height: 1.75; color: #d3d3da; }

    h1, h2 {
        font-family: var(--heading-font) !important;
        letter-spacing: 0 !important;
        line-height: 1.55 !important;
        color: #f6f6f8 !important;
    }
    h1 { font-size: var(--h1-size) !important; text-shadow: 0 0 26px rgba(224, 27, 36, 0.45); }
"""
    .replace("__HEADING_FONT__", HEADING_FONT)
    .replace("__H1_SIZE__", HEADING_SIZE)
    + """
    h2 { font-size: 1.02rem !important; }
    h3, h4 {
        font-family: 'IBM Plex Mono', monospace !important;
        text-transform: uppercase;
        letter-spacing: 0.12em !important;
        font-size: 0.82rem !important;
        color: #f0f0f3 !important;
    }
    .eyebrow {
        font-size: 0.68rem;
        letter-spacing: 0.28em;
        text-transform: uppercase;
        color: #e01b24;
        margin-bottom: 0.4rem;
    }
    .lede {
        color: #b8b8c2;
        font-size: 1rem;
        max-width: 68ch;
    }
    .tagline {
        color: #f0f0f3;
        font-size: 1.05rem;
        border-left: 3px solid #e01b24;
        padding-left: 0.9rem;
        margin: 0.2rem 0 1.1rem 0;
    }
    .byline { color: #8f8f9b; font-size: 0.86rem; margin-bottom: 0.9rem; }

    .brand { display: flex; gap: 0.75rem; align-items: center; margin-bottom: 0.4rem; }
    .brand-badge {
        width: 46px; height: 46px; flex: 0 0 46px;
        display: flex; align-items: center; justify-content: center;
        border: 2px solid #e01b24; color: #f2f2f4;
        font-family: 'Press Start 2P', monospace; font-size: 0.78rem;
        background: #150b0d;
    }
    .brand-name { font-weight: 600; letter-spacing: 0.14em; text-transform: uppercase; font-size: 0.9rem; color: #f4f4f6; }
    .brand-meta { color: #8f8f9b; font-size: 0.72rem; letter-spacing: 0.06em; }

    .card {
        border: 1px solid #26262e;
        background: linear-gradient(180deg, #15161a 0%, #101014 100%);
        padding: 1.05rem 1.15rem;
        height: 100%;
    }
    .card h4 { margin: 0 0 0.55rem 0; color: #ffffff !important; }
    .card p { margin: 0; color: #b6b6c0; font-size: 0.88rem; line-height: 1.65; }
    .card-accent { border-left: 3px solid #e01b24; }

    .badge {
        display: inline-block;
        border: 1px solid #34343e;
        background: #1a1b21;
        color: #dcdce2;
        font-size: 0.7rem;
        letter-spacing: 0.04em;
        padding: 0.15rem 0.45rem;
        margin: 0 0.3rem 0.3rem 0;
    }

    .standin {
        border: 2px dashed #4a2024;
        background: repeating-linear-gradient(45deg, #121317 0 12px, #0d0e11 12px 24px);
        min-height: 300px;
        display: flex;
        align-items: center;
        justify-content: center;
        text-align: center;
        color: #8d8d98;
        font-size: 0.78rem;
        padding: 1rem;
    }
    .standin-tag { color: #e01b24; letter-spacing: 0.22em; font-size: 0.66rem; }

    .tl { border-left: 1px solid #2a2a32; margin-left: 0.35rem; padding-left: 1.1rem; }
    .tl-item { position: relative; padding-bottom: 1.35rem; }
    .tl-item::before {
        content: ""; position: absolute; left: -1.42rem; top: 0.42rem;
        width: 8px; height: 8px; background: #e01b24;
    }
    .tl-item.future::before { background: #0a0a0c; border: 1px solid #6b2a2f; }
    .tl-year { color: #e01b24; font-size: 0.72rem; letter-spacing: 0.16em; }
    .tl-title { color: #f2f2f5; font-size: 0.9rem; margin: 0.15rem 0 0.25rem 0; }
    .tl-note { color: #a9a9b4; font-size: 0.82rem; line-height: 1.6; }

    .log {
        border: 1px solid #26262e;
        border-left: 3px solid #e01b24;
        background: #101014;
        padding: 0.85rem 1rem;
        margin-bottom: 0.6rem;
    }
    .log-head { color: #e01b24; font-size: 0.68rem; letter-spacing: 0.16em; text-transform: uppercase; }
    .log-body { color: #d3d3da; font-size: 0.88rem; margin-top: 0.3rem; }

    .shot { margin: 0; }
    .shot img {
        width: 100%;
        display: block;
        border: 1px solid #26262e;
        background: #0d0e11;
    }
    .shot.pixel img { image-rendering: pixelated; }
    .shot figcaption { color: #8f8f9b; font-size: 0.74rem; margin-top: 0.45rem; }

    [data-testid="stDecoration"] { display: none; }
    /* keep the header alive: it holds the expand-sidebar button when the sidebar is closed */
    [data-testid="stAppDeployButton"],
    [data-testid="stMainMenu"],
    [data-testid="stStatusWidget"] { display: none; }

    [data-testid="stMetricValue"] {
        font-family: 'Press Start 2P', monospace;
        font-size: 1.5rem !important;
        color: #ffffff;
    }
    [data-testid="stMetricLabel"] p {
        text-transform: uppercase;
        letter-spacing: 0.14em;
        font-size: 0.68rem !important;
        color: #8f8f9b !important;
    }
    [data-testid="stMetric"] {
        border-left: 2px solid #e01b24;
        padding-left: 0.9rem;
    }
    [data-testid="stSidebar"] { background: #08080a; border-right: 1px solid #1e1e25; }
    [data-testid="stHeader"] { background: transparent; }
    .footer {
        margin-top: 3rem;
        padding-top: 1rem;
        border-top: 1px solid #1e1e25;
        color: #74747f;
        font-size: 0.74rem;
        letter-spacing: 0.08em;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


# --------------------------------------------------------------------------
# Shared pieces
# --------------------------------------------------------------------------


def page_header(number: str, title: str, blurb: str) -> None:
    st.markdown(f'<div class="eyebrow">{number} / {COURSE}</div>', unsafe_allow_html=True)
    st.header(title)
    st.markdown(f'<p class="lede">{blurb}</p>', unsafe_allow_html=True)


def footer() -> None:
    st.markdown(
        f'<div class="footer">{FULL_NAME} · {PROGRAM} · Section {SECTION} · '
        f"{COURSE} · Instructor: {INSTRUCTOR}</div>",
        unsafe_allow_html=True,
    )


def timeline(items: list[dict]) -> str:
    rows = []
    for item in items:
        cls = "tl-item future" if item.get("future") else "tl-item"
        rows.append(
            f'<div class="{cls}"><div class="tl-year">{item["year"]}</div>'
            f'<div class="tl-title">{item["title"]}</div>'
            f'<div class="tl-note">{item["note"]}</div></div>'
        )
    return f'<div class="tl">{"".join(rows)}</div>'


def badges(tools: list[str]) -> None:
    html = " ".join(f'<span class="badge">{tool}</span>' for tool in tools)
    st.markdown(html, unsafe_allow_html=True)


# --------------------------------------------------------------------------
# Home
# --------------------------------------------------------------------------


def page_home() -> None:
    left, right = st.columns([1.55, 1], gap="large")

    with left:
        st.markdown(
            f'<div class="eyebrow">{COURSE} · SECTION {SECTION}</div>', unsafe_allow_html=True
        )
        st.title(NAME)
        st.markdown(
            f'<div class="byline">{FULL_NAME} · he/him · {PROGRAM} · Cebu City</div>',
            unsafe_allow_html=True,
        )
        st.markdown(f'<div class="tagline">“{TAGLINE}”</div>', unsafe_allow_html=True)
        st.write(
            "I write game systems, engine code, and the tooling that keeps both from slowing "
            "me down. Mostly C++, C#, and C. Self-taught since a cousin installed Scratch on "
            "the family computer, now three years into a Computer Science degree, still "
            "shipping on jam deadlines."
        )
        st.write(
            "Most of what I build ends up being the part players never look at: netcode, "
            "scene systems, a renderer, the editor panel that saves the team four hours. "
            "That is the work I want."
        )

        link_a, link_b, link_c = st.columns(3)
        link_a.link_button("See the games", ITCH, width="stretch")
        link_b.link_button("Source code", GITHUB, width="stretch")
        link_c.link_button("Email me", f"mailto:{EMAIL}", width="stretch")

    with right:
        st.image(
            str(ASSETS / "profile.jpg"),
            caption="Glensh, third year BSCS at CIT-U",
            width="stretch",
        )

    st.divider()

    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Podium finishes", "3", "2 champions · 1 third", delta_color="off")
    m2.metric("Projects shipped", "8+", "games, engines, a POS", delta_color="off")
    m3.metric("Codebase authored", "~90%", "on every team I led", delta_color="off")
    m4.metric("Graduating", "2028", "BS Computer Science", delta_color="off")

    st.divider()
    st.subheader("What I actually do")

    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown(
            """
            <div class="card card-accent">
                <h4>Multiplayer &amp; netcode</h4>
                <p>Client-side prediction, server reconciliation, entity interpolation, lag
                compensation. The server owns the truth, so cheating has no door to walk
                through.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with c2:
        st.markdown(
            """
            <div class="card card-accent">
                <h4>Engine &amp; tooling</h4>
                <p>OpenGL renderers, ECS, sprite batching, Dear ImGui editor panels, and
                GDExtension modules that make Godot do things it does not ship with.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with c3:
        st.markdown(
            """
            <div class="card card-accent">
                <h4>Shipping on a deadline</h4>
                <p>Three jam podiums, a capstone with five people, a paid mobile POS. I own
                the repo, the architecture, and the unglamorous merge conflicts.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.divider()
    st.subheader("Right now")

    st.progress(0.8, text="Netfox C++ · ~80% done, already running Infinitus' multiplayer")
    st.progress(0.7, text="Infinitus · contest build finished, public release pending")
    st.progress(0.5, text="Adobo Engine · playable core, editor half built")

    st.info(
        "Open to game jams, engine and netcode work, and teams that need a backend-leaning "
        "developer who reads the docs before the forum post.",
        icon="🎮",
    )

    st.caption("Currently playing: Chivalry 2. Currently avoiding: sleep.")
    footer()


# --------------------------------------------------------------------------
# Autobiography
# --------------------------------------------------------------------------


def page_autobiography() -> None:
    page_header(
        "01",
        "Autobiography",
        "A cousin's Scratch install, a restaurant with a problem, and a plan my parents "
        "had that was not my plan.",
    )

    prose, side = st.columns([1.5, 1], gap="large")

    with prose:
        st.subheader("The family computer")
        st.write(
            "I grew up around computers and games, which in our house mostly meant watching "
            "them. The first thing I could actually control was Scratch, installed on the "
            "family computer by a cousin who worked in IT. I built a game where you catch "
            "falling balls. The balls fall faster the longer you survive, and there is a "
            "score. That is the entire design. It is still funny to me that this is what "
            "started it."
        )

        st.subheader("The Pygame detour")
        st.write(
            "Senior high brought the interest back. I worked through a Python book on Pygame "
            "on my own: ASCII games first, then an asteroid shooter. No AI, no copy-pasted "
            "tutorials. Docs, YouTube, and code that broke in ways I had to sit with until "
            "it made sense."
        )

        st.subheader("The first real client")
        st.write(
            "A restaurant owner near us had a problem with ordering, so I offered to fix it. "
            "Zira POS came out of that: React Native on Android, menu management, transaction "
            "history, and a Bluetooth receipt printer, which ate the most weekends. It sold, "
            "and it was my first paid work. It also ran slower than it should have, because I "
            "built it before I knew what architecture meant. That is the reason I care about "
            "systems design now."
        )

        st.subheader("Education, and the plan I inherited")
        st.write(
            "I passed the Caraga State University entrance exam and they offered me a "
            "scholarship. My parents wanted me in Cebu with my cousin instead, so I enrolled "
            "at CIT-U. I had wanted mechanical engineering, and before that I wanted to be "
            "the agricultural engineer who finally drags Philippine farming into the tech "
            "era. I still want that one. A seminar where graduates from different programs "
            "showed what they do, and roughly what they earn, pushed me toward Computer "
            "Science as the way in."
        )
        st.write(
            "Embedded systems is where I actually wanted to land. I bought an Arduino kit and "
            "wired up sensors, but the kit had no servos, so nothing moved. Moving parts are "
            "the point, and those cost money I did not have. That ambition is parked, not "
            "canceled."
        )

        st.subheader("Now")
        st.write(
            "Most of my hours go to game development and the tools around it. I am rewriting "
            "Netfox in C++ as a GDExtension with client-side prediction, server reconciliation "
            "and lag compensation, because our jam games needed it and the existing addon did "
            "not fit. I also poke at ethical hacking, at the level where I know what I am "
            "doing and know exactly where my knowledge stops."
        )

        st.subheader("What comes next")
        st.write(
            "Game development is where I want to design: ideas, systems, the process, with a "
            "budgeted amount of coding. The long game is agriculture. Embedded systems get me "
            "there once there is hardware money. I would rather build the controller for a "
            "rice field than the dashboard that watches it."
        )

        with st.expander("The honest version (hobbies, or lack of them)"):
            st.write(
                "Outside code I play Chivalry 2 and not much else. Coding all day is not a "
                "hobby, it is a warning sign, and I know it. The plan for this year is to run "
                "a mile or two and pick up one hobby with no keyboard in it. Updates pending."
            )

    with side:
        st.subheader("Milestones")
        st.markdown(timeline(MILESTONES), unsafe_allow_html=True)

        st.subheader("Fast facts")
        facts = pd.DataFrame(
            {
                "Field": [
                    "Based in",
                    "Studying",
                    "Expected",
                    "Languages",
                    "Award",
                    "Currently playing",
                ],
                "Detail": [
                    "Cebu City, Philippines",
                    "BS Computer Science, CIT-U",
                    "2028",
                    "English, Filipino / Bisaya",
                    "Academic Achiever, Parangal 2025 & 2026",
                    "Chivalry 2",
                ],
            }
        )
        st.table(facts, hide_index=True, width="stretch")

        st.info(
            "Section " + SECTION + " · " + COURSE + " · " + INSTRUCTOR,
            icon="📌",
        )

    footer()


# --------------------------------------------------------------------------
# Skills
# --------------------------------------------------------------------------


def page_skills() -> None:
    page_header(
        "02",
        "Skills",
        "Scores are mine, not a framework's. 100 means I will debug it at 2am without "
        "complaining; 40 means I can read it and still reach for the docs.",
    )

    st.write(
        "In plain text: C++ and C# for anything with a loop that matters, C when I want to see "
        "the memory, Python for scripts and quick tools, Java when the school or the capstone "
        "asks for threads, and Godot's GDExtension layer for everything that has to run inside "
        "an engine."
    )

    skill_df = pd.DataFrame(SKILLS, columns=["Skill", "Score", "Category"])

    filter_a, filter_b, filter_c, filter_d = st.columns([2, 1.1, 1.1, 1])
    picked = filter_a.multiselect(
        "Skills to plot",
        options=skill_df["Skill"].tolist(),
        default=CHART_DEFAULT,
        key="skill_pick",
    )
    minimum = filter_b.slider("Minimum score", 0, 100, 0, step=10, key="skill_min")
    focus = filter_c.selectbox(
        "Focus", ["Everything"] + sorted(skill_df["Category"].unique()), key="skill_focus"
    )
    view = filter_d.radio(
        "View", ["Chart", "Table", "Both"], index=2, horizontal=True, key="skill_view"
    )

    if st.button("Reset filters"):
        for key in ("skill_pick", "skill_min", "skill_focus", "skill_view"):
            st.session_state.pop(key, None)
        st.rerun()

    view_df = skill_df[skill_df["Skill"].isin(picked) & (skill_df["Score"] >= minimum)]
    if focus != "Everything":
        view_df = view_df[view_df["Category"] == focus]

    if view_df.empty:
        st.warning("Nothing matches those filters. Loosen the score or add a skill.")
    else:
        if view in ("Chart", "Both"):
            ordered = view_df.sort_values("Score", ascending=False)
            order = ordered["Skill"].tolist()

            bars = (
                alt.Chart(ordered)
                .mark_bar(size=18)
                .encode(
                    x=alt.X("Score:Q", scale=alt.Scale(domain=[0, 100]), title=None),
                    y=alt.Y(
                        "Skill:N",
                        sort=order,
                        title=None,
                        axis=alt.Axis(labelLimit=200, labelFontSize=11),
                    ),
                    color=alt.Color(
                        "Score:Q",
                        scale=alt.Scale(range=["#4a1115", "#e01b24"]),
                        legend=None,
                    ),
                    tooltip=["Skill:N", "Score:Q", "Category:N"],
                )
            )
            labels = (
                alt.Chart(ordered)
                .mark_text(align="left", dx=5, color="#c9c9d2", fontSize=11)
                .encode(
                    x="Score:Q",
                    y=alt.Y("Skill:N", sort=order),
                    text=alt.Text("Score:Q", format=".0f"),
                )
            )
            chart = (
                (bars + labels)
                .properties(height=max(240, 34 * len(ordered)), background="transparent")
                .configure_view(strokeWidth=0)
                .configure_axis(
                    grid=False,
                    domainColor="#2c2c34",
                    tickColor="#2c2c34",
                    labelColor="#b9b9c3",
                    labelFont="IBM Plex Mono",
                )
            )
            st.altair_chart(chart, width="stretch")

        if view in ("Table", "Both"):
            st.dataframe(
                view_df.sort_values("Score", ascending=False)[["Skill", "Category", "Score"]],
                hide_index=True,
                width="stretch",
                column_config={
                    "Score": st.column_config.ProgressColumn(
                        "Confidence", min_value=0, max_value=100, format="%d"
                    )
                },
            )

    st.divider()
    st.subheader("Average by area")
    averages = (
        skill_df.groupby("Category", as_index=False)["Score"]
        .mean()
        .round(0)
        .sort_values("Score", ascending=False)
    )
    st.bar_chart(averages, x="Category", y="Score", color="#e01b24", height=260)
    st.caption(
        "The averages include the skills I am still learning. Lua at 40 is honest, not modest."
    )

    st.divider()
    st.subheader("How I work")

    w1, w2 = st.columns(2)
    with w1:
        st.markdown(
            """
            <div class="card">
                <h4>Read the source, then decide</h4>
                <p>I taught myself C and OpenGL from documentation with no AI in the loop.
                That habit stuck: when something breaks, I read the implementation before I
                ask anyone.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with w2:
        st.markdown(
            """
            <div class="card">
                <h4>Own the unglamorous part</h4>
                <p>On every team I led I took the repo, the merges, and the bugs other people
                introduced. A jam is won by whoever is willing to do the rebase at 3am.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with st.expander("A loop I have written more times than I can count"):
        st.code(
            """// fixed-timestep accumulator, Adobo Engine style
double now   = glfwGetTime();
double delta = now - last;
last = now;

accumulator += delta;
while (accumulator >= FIXED_DT) {
    world_update(&world, FIXED_DT);   // physics, netcode, gameplay
    accumulator -= FIXED_DT;
}

render(&world, accumulator / FIXED_DT); // interpolate for a smooth frame
""",
            language="c",
        )
        st.caption("Illustrative, not the literal file. The shape is the point.")

    footer()


# --------------------------------------------------------------------------
# Projects
# --------------------------------------------------------------------------


def project_card(
    title: str,
    pitch: str,
    role: str,
    tools: list[str],
    outcome: str,
    details: list[str],
    links: list[tuple[str, str]],
    shot_file: str | None,
    shot_caption: str,
    standin_label: str,
    note: str | None = None,
    pixelate: bool = False,
) -> None:
    media, body = st.columns([1.05, 1], gap="large")

    with media:
        if shot_file:
            shot(shot_file, shot_caption, standin_label, pixelate=pixelate)
        else:
            standin(standin_label)

    with body:
        st.subheader(title)
        st.write(pitch)
        st.markdown(f"**Role** · {role}")
        st.markdown(f"**Outcome** · {outcome}")
        badges(tools)

        if links:
            cols = st.columns(len(links))
            for col, (label, url) in zip(cols, links):
                col.link_button(label, url, width="stretch")

        if note:
            st.caption(note)

        with st.expander("What I actually built"):
            for line in details:
                st.markdown(f"- {line}")


def page_projects() -> None:
    page_header(
        "03",
        "Projects",
        "Three games and the networking layer underneath them. Two of these repos are private "
        "because the code belongs to a team or a client, so ask and I will walk you through it.",
    )

    tab_infinitus, tab_netfox, tab_pool, tab_more = st.tabs(
        ["Infinitus", "Netfox C++", "InParallel, Apart", "More work"]
    )

    with tab_infinitus:
        project_card(
            title="Infinitus",
            pitch=(
                "A top-down battle royale where you draw sigils mid-fight to cast spells. "
                "Built with the Limitless team for DOST NEXT LEVEL: Esports Game Dev Challenge, "
                "where it placed third."
            ),
            role="Lead developer · game design and architecture · main VFX artist",
            tools=["Godot", "GDExtension (C++)", "C#", "Krita", "Git"],
            outcome="3rd place, DOST NEXT LEVEL 2026. Contest build finished, public release pending.",
            details=[
                "Wrote roughly 90% of the codebase: backend systems, core game logic, and the "
                "internal tools the team used to build faster.",
                "Designed the multiplayer model, then took it apart and rebuilt it around "
                "server authority once cheating became the obvious problem.",
                "Built the 3D VFX and textures myself, including the sigil casting effects, in "
                "Krita and Godot.",
                "Handled every merge, rebase and conflict as the only person with repository "
                "ownership.",
                "Led the team from concept to final delivery, with the design direction and "
                "the task breakdown landing on me.",
            ],
            links=[("Play the build", "https://glensh.itch.io/infinitus")],
            shot_file="infinitus.jpg",
            shot_caption="Infinitus key art",
            standin_label="Infinitus key art",
            note=(
                "Repository is private, the codebase is the property of Limitless, and there "
                "is no public gameplay capture yet. The shot above is the cover."
            ),
        )

    with tab_netfox:
        project_card(
            title="Netfox C++",
            pitch=(
                "A client-server authoritative multiplayer layer for Godot, rewritten in C++ "
                "for speed and simplicity. It started as a port of Godot's Netfox addon and "
                "stopped being one once the design diverged."
            ),
            role="Main and only developer",
            tools=["C++", "GDExtension", "Godot", "Git"],
            outcome="About 80% complete, and already handling Infinitus' multiplayer.",
            details=[
                "Client-side prediction, server reconciliation, entity interpolation and lag "
                "compensation, with the server as the only authority.",
                "Rebuilt the API around what a developer actually types, instead of mirroring "
                "the original addon's surface.",
                "Because the server validates state, the anti-cheat falls out of the "
                "architecture instead of being bolted on afterwards.",
                "Grew out of earlier contributions to Netfox and NetfoxCs, then turned into a "
                "ground-up rewrite intended as the multiplayer backbone for Infinitus.",
            ],
            links=[("Preview on request", f"mailto:{EMAIL}?subject=Netfox%20C%2B%2B")],
            shot_file=None,
            shot_caption="",
            standin_label="Netfox C++ architecture diagram",
            note="Currently private. It goes public once the remaining bugs are fixed.",
        )

    with tab_pool:
        project_card(
            title="InParallel, Apart",
            pitch=(
                "A split-screen pixel puzzle game with two characters: one in the present, one "
                "in the past. What you move in the past rewrites the room in front of you."
            ),
            role="Lead developer · architect · designer",
            tools=["Godot", "C#", "Git"],
            outcome="1st place, UP Game Jam 2026.",
            details=[
                "Directed the architecture and the design, and wrote roughly 90% of the "
                "codebase.",
                "Reviewed and fixed AI-generated code from teammates before it reached the "
                "build.",
                "Ran the repository: merges, rebases and conflict resolution across multiple "
                "contributors.",
                "Assigned the technical work while another member handled logistics, which is "
                "the arrangement that kept the schedule honest.",
            ],
            links=[("Play on itch.io", "https://glensh.itch.io/in-parallel-apart")],
            shot_file="inparallel.png",
            shot_caption="InParallel, Apart",
            standin_label="InParallel, Apart gameplay",
            note="Repository is private. The codebase belongs to the team.",
            pixelate=True,
        )

    with tab_more:
        st.subheader("The rest of the shelf")
        include_archived = st.checkbox("Include early projects", value=False)

        rows = [row for row in MORE_WORK if row["core"] or include_archived]
        more_df = pd.DataFrame(rows).drop(columns=["core"])
        st.dataframe(more_df, hide_index=True, width="stretch")
        st.caption(
            "Adobo Engine is the one I would hand you first. A 2D/3D engine in C with an ECS, "
            "a sprite batcher, an ImGui editor, and no AI anywhere in the source."
        )

        st.divider()
        st.subheader("Podiums")
        podium = pd.DataFrame(
            {
                "Year": ["2025", "2026", "2026"],
                "Event": [
                    "Sugbuanon Saga Game Jam",
                    "UP Game Jam",
                    "DOST NEXT LEVEL: Esports Game Dev Challenge",
                ],
                "Project": ["9Lives: Ame", "InParallel, Apart", "Infinitus"],
                "Place": ["1st", "1st", "3rd"],
            }
        )
        st.table(podium, hide_index=True, width="stretch")

    footer()


# --------------------------------------------------------------------------
# Contact
# --------------------------------------------------------------------------


def page_contact() -> None:
    page_header(
        "04",
        "Contact",
        "Jam invitations, engine questions, or a game that needs netcode. I answer email "
        "faster than I answer anything else.",
    )

    form_col, info_col = st.columns([1.35, 1], gap="large")

    with form_col:
        with st.container(border=True):
            with st.form("feedback_form"):
                st.subheader("Send a note")
                row1, row2 = st.columns(2)
                name = row1.text_input("Your name", placeholder="Ada Lovelace")
                email = row2.text_input("Email", placeholder="you@example.com")

                project = st.selectbox(
                    "What is this about?",
                    [
                        "Just saying hi",
                        "Infinitus",
                        "Netfox C++",
                        "InParallel, Apart",
                        "A job or an internship",
                        "A jam team",
                    ],
                )
                interest = st.slider("How badly do you want to play these games?", 1, 10, 7)
                topics = st.multiselect(
                    "Topics",
                    ["Feedback", "Collaboration", "Hiring", "Engineering", "Networking"],
                    default=["Feedback"],
                )
                message = st.text_area(
                    "Message",
                    height=150,
                    placeholder="Tell me what you are building, or what broke.",
                )
                reply_ok = st.checkbox("You can reply to my email")
                submitted = st.form_submit_button("Send message", width="stretch")

        if submitted:
            problems = []
            if not name.strip():
                problems.append("I need a name to reply to.")
            if not message.strip():
                problems.append("The message is empty.")
            if reply_ok and ("@" not in email or "." not in email.split("@")[-1]):
                problems.append("That email does not look like an email.")

            for problem in problems:
                st.warning(problem, icon="⚠️")

            if not problems:
                st.session_state.setdefault("feedback", []).append(
                    {
                        "name": name.strip(),
                        "email": email.strip() or "not given",
                        "project": project,
                        "interest": interest,
                        "topics": topics,
                        "message": message.strip(),
                        "reply_ok": reply_ok,
                        "time": datetime.now().strftime("%H:%M:%S"),
                    }
                )
                st.toast("Message logged for this session", icon="📨")
                st.success(
                    f"Logged, {name.strip()}. Your message sits in this session only, because "
                    "the app is a static Streamlit deploy with no mail server. If you asked for "
                    "a reply, email me directly and it will actually reach me."
                )

    with info_col:
        st.subheader("Direct lines")
        st.link_button("Email · " + EMAIL, f"mailto:{EMAIL}", width="stretch")
        st.link_button("GitHub · GlenshC", GITHUB, width="stretch")
        st.link_button("itch.io · glensh", ITCH, width="stretch")

        resume = resume_file()
        if resume:
            data, filename, mime = resume
            st.download_button(
                "Download résumé",
                data,
                file_name=filename,
                mime=mime,
                width="stretch",
            )

        st.divider()
        st.markdown(
            """
            <div class="card">
                <h4>What I am looking for</h4>
                <p>Game jams with people who finish. Engine and netcode work. An internship
                where the codebase is older than I am. Embedded systems, eventually, once
                someone funds the servos.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.info("Usually reply within a day. Faster during finals week, for bad reasons.", icon="🕹️")
        st.caption(
            "Ask me about a project and you will get a real answer. Ask me on a date and I "
            "might say yes. Keyword: might."
        )

    st.divider()
    st.subheader("Session log")

    log = st.session_state.get("feedback", [])
    if not log:
        st.caption("Nothing sent yet. The first message shows up here.")
    else:
        for item in reversed(log):
            st.markdown(
                f"""
                <div class="log">
                    <div class="log-head">{item['time']} · {item['project']} · interest {item['interest']}/10</div>
                    <div class="log-body"><strong>{item['name']}</strong> ({item['email']})<br>{item['message']}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )
        if st.button("Clear the log"):
            st.session_state["feedback"] = []
            st.rerun()

    st.caption(
        "This form is front-end only. It writes to the session, not to a database, so nothing "
        "leaves your browser and nothing gets emailed. Use the links above for a real reply."
    )

    footer()


# --------------------------------------------------------------------------
# Router
# --------------------------------------------------------------------------

if page == "Home":
    page_home()
elif page == "Autobiography":
    page_autobiography()
elif page == "Skills":
    page_skills()
elif page == "Projects":
    page_projects()
else:
    page_contact()

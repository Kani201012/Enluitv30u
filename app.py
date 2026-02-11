import streamlit as st
import zipfile
import io
import json
import datetime
import re

# --- 1. APP CONFIGURATION ---
st.set_page_config(
    page_title="Titan v30.5 | Strategy Core", 
    layout="wide", 
    page_icon="🛡️",
    initial_sidebar_state="expanded"
)

# --- 2. ADVANCED UI SYSTEM (CSS) ---
st.markdown("""
    <style>
    :root { --primary: #0f172a; --accent: #3b82f6; }
    .stApp { background-color: #f8fafc; color: #1e293b; font-family: 'Inter', sans-serif; }
    [data-testid="stSidebar"] { background-color: #ffffff; border-right: 1px solid #e2e8f0; }
    [data-testid="stSidebar"] h1 { 
        background: linear-gradient(90deg, #0f172a, #3b82f6);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 900 !important;
        font-size: 1.8rem !important;
    }
    .stTextInput input, .stTextArea textarea, .stSelectbox div[data-baseweb="select"] {
        background-color: #ffffff !important; border: 1px solid #cbd5e1 !important; border-radius: 8px !important; color: #0f172a !important;
    }
    .stButton>button {
        width: 100%; border-radius: 8px; height: 3.5rem;
        background: linear-gradient(135deg, #0f172a 0%, #2563eb 100%);
        color: white; font-weight: 800; border: none;
        box-shadow: 0 4px 15px rgba(37, 99, 235, 0.3);
        text-transform: uppercase; letter-spacing: 1px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SIDEBAR: CONTROL CENTER ---
with st.sidebar:
    st.title("Titan Architect")
    st.caption("v30.5 | Strategy Edition")
    st.divider()
    
    with st.expander("🎨 Visual DNA", expanded=True):
        theme_mode = st.selectbox("Base Theme", ["Midnight SaaS (Dark)", "Clean Corporate (Light)", "Cyberpunk Neon", "Luxury Gold", "Forest Eco", "Ocean Breeze", "Stark Minimalist"])
        c1, c2 = st.columns(2)
        p_color = c1.color_picker("Primary Brand", "#3B82F6") 
        s_color = c2.color_picker("Action (CTA)", "#10B981")  
        h_font = st.selectbox("Headings", ["Space Grotesk", "Montserrat", "Playfair Display", "Oswald"])
        b_font = st.selectbox("Body Text", ["Inter", "Open Sans", "Roboto", "Satoshi"])
        border_rad = st.select_slider("Corner Roundness", ["0px", "4px", "12px", "24px"], value="12px")
        anim_type = st.selectbox("Animation Style", ["Fade Up", "Zoom In", "None"])

    with st.expander("🧩 Section Manager", expanded=False):
        show_hero = st.checkbox("Hero Carousel", value=True)
        show_stats = st.checkbox("Trust Stats/Logos", value=True)
        show_features = st.checkbox("Feature Grid", value=True)
        show_magic = st.checkbox("✨ Magic Section (Sheets CMS)", value=True)
        show_comparison = st.checkbox("📊 Comparison Table", value=True)
        show_inventory = st.checkbox("Inventory / Portfolio", value=True)
        show_gallery = st.checkbox("About Section", value=True)
        show_testimonials = st.checkbox("Testimonials", value=True)
        show_faq = st.checkbox("F.A.Q.", value=True)
        show_audit = st.checkbox("📝 Audit Form (Lead Gen)", value=True)
        show_cta = st.checkbox("Final Call to Action", value=False)

    with st.expander("⚙️ SEO & Analytics", expanded=False):
        seo_area = st.text_input("Service Area", "Global Deployment")
        seo_kw = st.text_area("Keywords", "stop web rent, no monthly fee website, 0.1s speed")
        gsc_tag = st.text_input("Google Verification ID")
        ga_tag = st.text_input("Google Analytics ID")
        og_image = st.text_input("Social Share Image URL")

# --- 4. MAIN WORKSPACE ---
st.title("🏗️ Site Content Builder")
tabs = st.tabs(["1. Identity", "2. Content", "3. Strategy", "4. Inventory", "5. Legal"])

with tabs[0]:
    c1, c2 = st.columns(2)
    with c1:
        biz_name = st.text_input("Business Name", "StopWebRent")
        biz_tagline = st.text_input("Tagline", "Stop Paying 'Web Rent' Forever.")
        biz_phone = st.text_input("Phone", "+966 57 256 2151")
        biz_email = st.text_input("Email", "deploy@stopwebrent.com")
    with c2:
        prod_url = st.text_input("Website URL", "https://stopwebrent.com")
        biz_addr = st.text_area("Address", "Kaydiem Script Lab, Kolkata Innovation Node.", height=100)
        map_iframe = st.text_area("Map Code", placeholder='<iframe src="..."></iframe>', height=100)
        seo_d = st.text_area("Meta Desc", "We build ultra-fast static websites. Pay once, own it forever.", height=100)
        logo_url = st.text_input("Logo URL")
    
    st.caption("Social Links")
    sc1, sc2, sc3 = st.columns(3)
    fb_link, ig_link, x_link = sc1.text_input("FB"), sc2.text_input("IG"), sc3.text_input("X")
    sc4, sc5, sc6 = st.columns(3)
    li_link, yt_link, wa_num = sc4.text_input("LI"), sc5.text_input("YT"), sc6.text_input("WA Number (No +)", "966572562151")

with tabs[1]:
    hero_h = st.text_input("Hero Headline", "Stop Renting Your Website.")
    hero_sub = st.text_input("Hero Subtext", "The Titan Engine is the world’s first 0.1s website architecture that runs on $0 monthly fees.")
    hc1, hc2, hc3 = st.columns(3)
    hero_img_1 = hc1.text_input("Slide 1", "https://images.unsplash.com/photo-1550751827-4bd374c3f58b?q=80&w=1600")
    hero_img_2 = hc2.text_input("Slide 2", "https://images.unsplash.com/photo-1497366216548-37526070297c?q=80&w=1600")
    hero_img_3 = hc3.text_input("Slide 3", "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?q=80&w=1600")
    
    st.divider()
    s1, s2, s3 = st.columns(3)
    stat_1, label_1 = s1.text_input("Stat 1", "$1,491"), s1.text_input("Label 1", "5-Year Savings")
    stat_2, label_2 = s2.text_input("Stat 2", "0.1s"), s2.text_input("Label 2", "Load Speed")
    stat_3, label_3 = s3.text_input("Stat 3", "100%"), s3.text_input("Label 3", "Ownership")

    st.divider()
    f_title = st.text_input("Features Title", "The 4 Pillars")
    feat_data = st.text_area("Features List", "water | 0.1s Speed | Google demands speed. Titan sites load instantly.\nshield | Zero Monthly Fees | No hosting bills. You own the code.\ndatabase | Google Sheets CMS | Update prices using a simple Google Sheet.\nlock | Bank-Grade Security | No database means unhackable architecture.", height=150)
    
    st.divider()
    about_h = st.text_input("About Title", "Restoring Logic")
    about_img = st.text_input("About Image", "https://images.unsplash.com/photo-1555099962-4199c345e5dd?q=80&w=1600")
    about_short = st.text_area("About Short", "Traditional agencies charge 'rent'. We changed the rules.")
    about_long = st.text_area("About Long", "**The Death of the Subscription Model**\nFor too long, agencies have forced local businesses into 'forever-payments'.")

with tabs[2]:
    magic_h = st.text_input("Magic Headline", "Control Your Empire from a Spreadsheet")
    magic_desc = st.text_area("Magic Desc", "No WordPress dashboard. Just open your private Google Sheet.")
    magic_img = st.text_input("Magic Img", "https://images.unsplash.com/photo-1460925895917-afdab827c52f?q=80&w=1600")
    st.divider()
    comp_h = st.text_input("Table Headline", "The 'Cost of Ownership' Calculator")
    c1, c2, c3 = st.columns(3)
    comp_my_price = c1.text_input("Your Price", "$249")
    comp_wix_price = c2.text_input("Competitor Price", "$1,815")
    comp_save = c3.text_input("Savings", "$1,491")

with tabs[3]:
    sheet_url = st.text_input("Sheet CSV", placeholder="https://docs.google.com/...")
    custom_feat = st.text_input("Default Product Image", "https://images.unsplash.com/photo-1460925895917-afdab827c52f?q=80&w=800")

with tabs[4]:
    testi_data = st.text_area("Testimonials", "Joe | Saved me $480.\nSarah | Fastest site ever.")
    faq_data = st.text_area("FAQ", "Hosting free? ? Yes.\nOwn code? ? Yes.")
    priv_txt = st.text_area("Privacy", "**Digital Sovereignty**\nWe respect data...")
    term_txt = st.text_area("Terms", "**Ownership**\nYou own the code...")

# --- 5. COMPILER ENGINE ---

def format_text(text):
    if not text: return ""
    processed_text = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', text)
    lines = processed_text.split('\n')
    html_out = ""
    in_list = False
    for line in lines:
        clean_line = line.strip()
        if not clean_line: continue
        if clean_line.startswith("* "):
            if not in_list: html_out += '<ul style="margin-bottom:1rem; padding-left:1.5rem;">'; in_list = True
            html_out += f'<li style="margin-bottom:0.5rem; opacity:0.9; color:inherit;">{clean_line[2:]}</li>'
        elif clean_line.startswith("<strong>") and clean_line.endswith("</strong>"):
            if in_list: html_out += "</ul>"; in_list = False
            html_out += f"<h3 style='margin-top:1.5rem; margin-bottom:0.5rem; color:var(--p); font-size:1.25rem;'>{clean_line.replace('<strong>','').replace('</strong>','')}</h3>"
        else:
            if in_list: html_out += "</ul>"; in_list = False
            html_out += f"<p style='margin-bottom:1rem; opacity:0.9; color:inherit;'>{clean_line}</p>"
    if in_list: html_out += "</ul>"
    return html_out

def gen_schema():
    schema = { "@context": "https://schema.org", "@type": "LocalBusiness", "name": biz_name, "image": logo_url, "telephone": biz_phone, "email": biz_email, "areaServed": seo_area, "url": prod_url, "description": seo_d }
    return f'<script type="application/ld+json">{json.dumps(schema)}</script>'

def get_theme_css():
    bg = "#0f172a" if "Midnight" in theme_mode else "#ffffff"
    txt = "#f8fafc" if "Midnight" in theme_mode else "#0f172a"
    card = "#1e293b" if "Midnight" in theme_mode else "#ffffff"
    glass = "rgba(15, 23, 42, 0.9)" if "Midnight" in theme_mode else "rgba(255, 255, 255, 0.95)"
    anim_css = ".reveal { opacity: 0; transform: translateY(30px); transition: all 0.8s ease-out; } .reveal.active { opacity: 1; transform: translateY(0); }" if anim_type == "Fade Up" else ""
    
    hero_css = """
    .hero { position: relative; min-height: 90vh; overflow: hidden; display: flex; align-items: center; justify-content: center; text-align: center; color: white; padding-top: 80px; background-color: var(--p); }
    .carousel-slide { position: absolute; top: 0; left: 0; width: 100%; height: 100%; background-size: cover; background-position: center; opacity: 0; transition: opacity 1.5s ease-in-out; z-index: 0; }
    .carousel-slide.active { opacity: 1; }
    .hero-overlay { background: rgba(0,0,0,0.5); position: absolute; top: 0; left: 0; width: 100%; height: 100%; z-index: 1; }
    .hero-content { z-index: 2; position: relative; animation: slideUp 1s ease-out; }
    """
    return f"""
    :root {{ --p: {p_color}; --s: {s_color}; --bg: {bg}; --txt: {txt}; --card: {card}; --radius: {border_rad}; --nav: {glass}; --h-font: '{h_font}', sans-serif; --b-font: '{b_font}', sans-serif; }}
    * {{ box-sizing: border-box; }}
    html {{ scroll-behavior: smooth; }}
    body {{ background-color: var(--bg); color: var(--txt); font-family: var(--b-font); margin: 0; line-height: 1.6; overflow-x: hidden; }}
    p, h1, h2, h3, h4, span, li, div {{ color: inherit; }}
    h1, h2, h3, h4 {{ font-family: var(--h-font); color: var(--p); line-height: 1.1; margin-bottom: 1rem; }}
    strong {{ color: var(--p); font-weight: 800; }}
    input, textarea, select {{ width: 100%; padding: 0.8rem; margin-bottom: 1rem; border: 1px solid #ccc; border-radius: 6px; font-family: inherit; }}
    label {{ color: var(--txt); font-weight: bold; margin-bottom: 0.5rem; display: block; }}
    .container {{ max-width: 1280px; margin: 0 auto; padding: 0 20px; }}
    .btn {{ display: inline-block; padding: 1rem 2.5rem; border-radius: var(--radius); font-weight: 700; text-decoration: none; transition: 0.3s; text-transform: uppercase; cursor: pointer; border: none; text-align: center; }}
    .btn-primary {{ background: var(--p); color: white !important; }}
    .btn-accent {{ background: var(--s); color: white !important; box-shadow: 0 10px 25px -5px var(--s); }}
    .btn:hover {{ transform: translateY(-3px); filter: brightness(1.15); }}
    nav {{ position: fixed; top: 0; width: 100%; z-index: 1000; background: var(--nav); backdrop-filter: blur(12px); border-bottom: 1px solid rgba(100,100,100,0.1); padding: 1rem 0; }}
    .nav-flex {{ display: flex; justify-content: space-between; align-items: center; }}
    .nav-links {{ display: flex; align-items: center; }}
    .nav-links a {{ margin-left: 2rem; text-decoration: none; font-weight: 600; color: var(--txt); font-size: 0.9rem; opacity: 0.8; transition:0.2s; }}
    .nav-links a:hover {{ opacity: 1; color: var(--s); }}
    .mobile-menu {{ display: none; font-size: 1.5rem; cursor: pointer; }}
    {hero_css}
    .hero h1 {{ color: white; font-size: clamp(2.5rem, 8vw, 5rem); margin-bottom: 1.5rem; }}
    .hero p {{ color: rgba(255,255,255,0.9); font-size: clamp(1.1rem, 2vw, 1.5rem); max-width: 700px; margin: 0 auto 2.5rem auto; }}
    section {{ padding: 5rem 0; }}
    .section-head {{ text-align: center; margin-bottom: 4rem; }}
    .section-head h2 {{ font-size: 2.5rem; }}
    .grid-3 {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 2rem; }}
    .contact-layout {{ display: grid; grid-template-columns: 1fr 2fr; gap: 3rem; }}
    .about-grid, .magic-grid {{ display: grid; grid-template-columns: 1fr 1fr; gap: 4rem; align-items: center; }}
    .card {{ background: var(--card); padding: 2rem; border-radius: var(--radius); border: 1px solid rgba(100,100,100,0.1); transition: 0.3s; height: 100%; display: flex; flex-direction: column; }}
    .card:hover {{ transform: translateY(-5px); box-shadow: 0 20px 40px -10px rgba(0,0,0,0.1); border-color: var(--s); }}
    .prod-img {{ width: 100%; height: 250px; object-fit: cover; border-radius: calc(var(--radius) - 4px); margin-bottom: 1.5rem; background: #f1f5f9; }}
    details {{ background: var(--card); border: 1px solid rgba(100,100,100,0.1); border-radius: 8px; margin-bottom: 1rem; padding: 1rem; cursor: pointer; color: var(--txt); }}
    details summary {{ font-weight: bold; font-size: 1.1rem; color: var(--txt); }}
    footer {{ background: var(--p); color: white; padding: 4rem 0; margin-top: auto; }}
    .footer-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 3rem; }}
    .footer a {{ color: rgba(255,255,255,0.8) !important; text-decoration: none; display: block; margin-bottom: 0.5rem; transition: 0.3s; }}
    .social-icon {{ width: 24px; height: 24px; fill: rgba(255,255,255,0.7); transition: 0.3s; }}
    .social-icon:hover {{ fill: #ffffff; transform: scale(1.1); }}
    .comp-table {{ width: 100%; border-collapse: collapse; margin: 20px 0; background: var(--card); border-radius: var(--radius); overflow: hidden; }}
    .comp-table th, .comp-table td {{ padding: 20px; text-align: left; border-bottom: 1px solid rgba(128,128,128,0.1); }}
    .comp-table th {{ background: var(--p); color: white; }}
    .savings-box {{ background: var(--s); color: white; padding: 2rem; border-radius: var(--radius); text-align: center; margin-top: 2rem; }}
    .share-btn {{ width: 42px; height: 42px; border-radius: 50%; display: flex; align-items: center; justify-content: center; border: none; cursor: pointer; transition: 0.3s; color: white; }}
    .share-wa {{ background: #25D366; }} .share-fb {{ background: #1877F2; }} .share-x {{ background: #000000; }} .share-li {{ background: #0A66C2; }} .share-cp {{ background: #64748b; }}
    .detail-view {{ display: grid; grid-template-columns: 1fr 1fr; gap: 4rem; align-items: start; }}
    .legal-text h1 {{ font-size: 3rem; margin-bottom: 2rem; color: var(--p); }}
    {anim_css}
    @media (max-width: 768px) {{
        .nav-links {{ position: fixed; top: 70px; left: -100%; width: 100%; height: calc(100vh - 70px); background: var(--bg); flex-direction: column; padding: 2rem; transition: 0.3s; align-items: flex-start; justify-content: flex-start; border-top: 1px solid rgba(0,0,0,0.1); }}
        .nav-links.active {{ left: 0; }}
        .mobile-menu {{ display: block; }}
        .hero {{ min-height: 70vh; }}
        .contact-layout, .detail-view, .about-grid, .magic-grid {{ grid-template-columns: 1fr !important; gap: 2rem; }}
        .about-grid img {{ order: 2; margin-top: 1rem; }} .about-grid div {{ order: 1; }}
    }}
    """

def gen_nav():
    logo = f'<img src="{logo_url}" height="40">' if logo_url else f'<span style="font-weight:900; font-size:1.5rem; color:var(--p)">{biz_name}</span>'
    return f"""<nav><div class="container nav-flex"><a href="index.html" style="text-decoration:none">{logo}</a>
        <div class="mobile-menu" onclick="document.querySelector('.nav-links').classList.toggle('active')">☰</div>
        <div class="nav-links">
            <a href="index.html">Home</a>
            {'<a href="index.html#features">Features</a>' if show_features else ''}
            {'<a href="index.html#inventory">Products</a>' if show_inventory else ''}
            <a href="about.html">About</a><a href="contact.html">Contact</a>
            {f'<a href="#audit" class="btn-accent" style="padding:0.6rem 1.5rem; margin-left:1.5rem; border-radius:50px; color:white!important;">Free Audit</a>' if show_audit else f'<a href="tel:{biz_phone}" class="btn-accent" style="padding:0.6rem 1.5rem; margin-left:1.5rem; border-radius:50px; color:white!important;">Call Now</a>'}
        </div></div></nav>"""

def gen_hero():
    return f"""<section class="hero"><div class="hero-overlay"></div>
    <div class="carousel-slide active" style="background-image: url('{hero_img_1}')"></div>
    <div class="carousel-slide" style="background-image: url('{hero_img_2}')"></div>
    <div class="carousel-slide" style="background-image: url('{hero_img_3}')"></div>
    <div class="container hero-content"><h1>{hero_h}</h1><p>{hero_sub}</p><div style="display:flex; gap:1rem; justify-content:center; flex-wrap:wrap;">
    {f'<a href="#audit" class="btn btn-accent">Get Free Audit</a>' if show_audit else '<a href="#inventory" class="btn btn-accent">Explore Now</a>'}
    <a href="#features" class="btn" style="background:rgba(255,255,255,0.2); backdrop-filter:blur(10px); color:white;">How It Works</a></div></div></section>
    <script>let slides = document.querySelectorAll('.carousel-slide'); let currentSlide = 0; setInterval(() => {{ slides[currentSlide].classList.remove('active'); currentSlide = (currentSlide + 1) % slides.length; slides[currentSlide].classList.add('active'); }}, 4000);</script>"""

def get_simple_icon(name):
    name = name.lower().strip()
    if "code" in name: return '<svg viewBox="0 0 24 24" width="32" height="32" fill="currentColor"><path d="M9.4 16.6L4.8 12l4.6-4.6L8 6l-6 6 6 6 1.4-1.4zm5.2 0l4.6-4.6-4.6-4.6L16 6l6 6-6 6-1.4-1.4z"/></svg>'
    if "database" in name: return '<svg viewBox="0 0 24 24" width="32" height="32" fill="currentColor"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm1 15h-2v-6h2v6zm0-8h-2V7h2v2z"/></svg>'
    if "truck" in name: return '<svg viewBox="0 0 24 24" width="32" height="32" fill="currentColor"><path d="M20 8h-3V4H3c-1.1 0-2 .9-2 2v11h2c0 1.66 1.34 3 3 3s3-1.34 3-3h6c0 1.66 1.34 3 3 3s3-1.34 3-3h2v-5l-3-4zM6 18.5c-.83 0-1.5-.67-1.5-1.5s.67-1.5 1.5-1.5 1.5.67 1.5 1.5-.67 1.5-1.5 1.5zm13.5-9l1.96 2.5H17V9.5h2.5zm-1.5 9c-.83 0-1.5-.67-1.5-1.5s.67-1.5 1.5-1.5 1.5.67 1.5 1.5-.67 1.5-1.5 1.5z"/></svg>'
    if "shield" in name or "lock" in name: return '<svg viewBox="0 0 24 24" width="32" height="32" fill="currentColor"><path d="M12 1L3 5v6c0 5.55 3.84 10.74 9 12 5.16-1.26 9-6.45 9-12V5l-9-4zm0 10.99h7c-.53 4.12-3.28 7.79-7 8.94V12H5V6.3l7-3.11v8.8z"/></svg>'
    if "water" in name: return '<svg viewBox="0 0 24 24" width="32" height="32" fill="currentColor"><path d="M12 22c4.97 0 9-4.03 9-9 0-4.97-9-13-9-13S3 8.03 3 13c0 4.97 4.03 9 9 9zm0-11c1.66 0 3 1.34 3 3s-1.34 3-3 3-3-1.34-3-3 1.34-3 3-3z"/></svg>'
    if "bolt" in name: return '<svg viewBox="0 0 24 24" width="32" height="32" fill="currentColor"><path d="M11 21h-1l1-7H7.5c-.58 0-.57-.32-.38-.66.19-.34.05-.08.07-.12C8.48 10.94 10.42 7.54 13 3h1l-1 7h3.5c.49 0 .56.33.47.51l-.07.15C12.96 17.55 11 21 11 21z"/></svg>'
    return '<svg viewBox="0 0 24 24" width="32" height="32" fill="currentColor"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 15l-5-5 1.41-1.41L10 14.17l7.59-7.59L19 8l-9 9z"/></svg>'

def gen_features():
    cards = ""
    for line in feat_data.split('\n'):
        if "|" in line:
            parts = line.split('|')
            icon = get_simple_icon(parts[0])
            cards += f"""<div class="card reveal"><div style="color:var(--s); margin-bottom:1rem;">{icon}</div><h3 style="color:var(--p); font-size:1.2rem;">{parts[1].strip()}</h3><div style="opacity:0.9; font-size:0.95rem;">{format_text(parts[2].strip())}</div></div>"""
    return f"""<section id="features"><div class="container"><div class="section-head reveal"><h2>{f_title}</h2></div><div class="grid-3">{cards}</div></div></section>"""

def gen_stats():
    return f"""<div style="background:var(--p); color:white; padding:3rem 0; text-align:center;"><div class="container grid-3"><div class="reveal"><h3>{stat_1}</h3><p>{label_1}</p></div><div class="reveal"><h3>{stat_2}</h3><p>{label_2}</p></div><div class="reveal"><h3>{stat_3}</h3><p>{label_3}</p></div></div></div>"""

def gen_magic():
    return f"""<section id="magic" style="background:rgba(0,0,0,0.02);"><div class="container"><div class="magic-grid"><div class="reveal"><h2 style="font-size:2.5rem;">{magic_h}</h2><p style="font-size:1.1rem; opacity:0.8; margin:1.5rem 0;">{magic_desc}</p></div><img src="{magic_img}" class="reveal" style="width:100%; border-radius:var(--radius); box-shadow:0 20px 50px -20px rgba(0,0,0,0.2);"></div></div></section>"""

def gen_comparison():
    return f"""<section id="pricing"><div class="container"><div class="section-head reveal" style="text-align:center;"><h2>{comp_h}</h2></div><table class="comp-table reveal"><tr><th>Expense Category</th><th>Titan Engine</th><th>Wix / Shopify</th></tr><tr><td>Initial Setup Fee</td><td>{comp_my_price} (One-time)</td><td>$0 (DIY)</td></tr><tr><td>Annual Hosting</td><td><strong>$0</strong></td><td>$348 ($29/mo)</td></tr><tr><td>Maintenance</td><td><strong>$0</strong></td><td>Time or Money</td></tr><tr><td><strong>5-Year Total</strong></td><td><strong>{comp_my_price}</strong></td><td><strong>{comp_wix_price}</strong></td></tr></table><div class="savings-box reveal"><h2>Your 5-Year Savings: {comp_save}</h2><p>Stop bleeding cash. Start owning your asset.</p></div></div></section>"""

def gen_audit_form():
    return f"""<section id="audit" style="background:var(--p); color:white;"><div class="container" style="max-width:600px; text-align:center;"><div class="reveal"><h2 style="color:white;">Get Your Free Audit</h2><p style="color:white; opacity:0.8; margin-bottom:2rem;">See exactly how much speed and money you are losing.</p><form action="https://formsubmit.co/{biz_email}" method="POST" style="text-align:left;"><label style="color:white;">Name</label><input type="text" name="name" required><label style="color:white;">Current Website</label><input type="text" name="website"><label style="color:white;">WhatsApp</label><input type="text" name="phone" required><button type="submit" class="btn-accent" style="width:100%; border:none; margin-top:1rem;">REQUEST AUDIT</button></form></div></div></section>"""

def gen_csv_parser():
    return """<script>function parseCSVLine(str){const res=[];let cur='';let inQuote=false;for(let i=0;i<str.length;i++){const c=str[i];if(c==='"'){if(inQuote&&str[i+1]==='"'){cur+='"';i++;}else{inQuote=!inQuote;}}else if(c===','&&!inQuote){res.push(cur.trim());cur='';}else{cur+=c;}}res.push(cur.trim());return res;}</script>"""

def gen_inventory_js(is_demo=False):
    demo_flag = "const isDemo = true;" if is_demo else "const isDemo = false;"
    return f"""{gen_csv_parser()}<script>{demo_flag}
    async function loadInv() {{ try {{ const res = await fetch('{sheet_url}'); const txt = await res.text(); const lines = txt.split(/\\r\\n|\\n/); const box = document.getElementById('inv-grid'); if(!box) return; box.innerHTML = ''; for(let i=1; i<lines.length; i++) {{ if(!lines[i].trim()) continue; const clean = parseCSVLine(lines[i]); let img = clean[3] && clean[3].length > 5 ? clean[3] : '{custom_feat}'; if(clean[6] && clean[6].length > 5) img = clean[6]; if(clean.length > 1) {{ const prodName = encodeURIComponent(clean[0]); box.innerHTML += `<div class="card reveal" style="color:var(--txt);"><img src="${{img}}" class="prod-img" loading="lazy" onerror="this.onerror=null;this.src='{custom_feat}';"><div style="flex-grow:1; display:flex; flex-direction:column; justify-content:space-between;"><div><h3 style="color:var(--p);">${{clean[0]}}</h3><p style="color:var(--s); font-weight:bold;">${{clean[1]}}</p><p style="opacity:0.9;">${{clean[2]}}</p></div><div style="margin-top:1rem; display:grid; grid-template-columns:1fr 1fr; gap:0.5rem;"><a href="product.html?item=${{prodName}}" class="btn" style="background:#e2e8f0; color:#0f172a !important; padding:0.8rem; font-size:0.8rem;">Details</a><a href="https://wa.me/{wa_num}?text=Interested in ${{prodName}}" class="btn-primary btn" style="padding:0.8rem; font-size:0.8rem;">WhatsApp</a></div></div></div>`; }} }} }} catch(e) {{}} }}
    if(document.getElementById('inv-grid')) window.addEventListener('load', loadInv);</script>"""

def gen_inventory():
    if not show_inventory: return ""
    return f"""<section id="inventory" style="background:rgba(0,0,0,0.02)"><div class="container"><div class="section-head reveal"><h2>Live Inventory</h2><p>Real-time availability.</p></div><div id="inv-grid" class="grid-3"><div style="grid-column:1/-1; text-align:center;">Loading...</div></div></div></section>{gen_inventory_js(False)}"""

def gen_about_section():
    return f"""<section id="about"><div class="container"><div class="about-grid"><div class="reveal"><h2 style="font-size:2.5rem; margin-bottom:1.5rem;">{about_h}</h2><div style="font-size:1.1rem; opacity:0.9; margin-bottom:2rem;">{format_text(about_short)}</div><a href="about.html" class="btn btn-primary">Read More</a></div><img src="{about_img}" class="reveal" loading="lazy" style="width:100%; border-radius:var(--radius); box-shadow:0 20px 50px -20px rgba(0,0,0,0.2);"></div></div></section>"""

def gen_faq_section():
    items = "".join([f"<details class='reveal'><summary>{l.split('?')[0]}?</summary><p>{l.split('?')[1]}</p></details>" for l in faq_data.split('\n') if "?" in l])
    return f"""<section id="faq" style="background:rgba(0,0,0,0.02)"><div class="container" style="max-width:800px;"><div class="section-head reveal"><h2>F.A.Q.</h2></div>{items}</div></section>"""

def gen_footer():
    icons = ""
    if fb_link: icons += f'<a href="{fb_link}"><svg class="social-icon" viewBox="0 0 24 24"><path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"/></svg></a>'
    if ig_link: icons += f'<a href="{ig_link}"><svg class="social-icon" viewBox="0 0 24 24"><path d="M16.98 0a6.9 6.9 0 0 1 5.08 1.98A6.94 6.94 0 0 1 24 7.02v9.96c0 2.08-.68 3.87-1.98 5.13A7.14 7.14 0 0 1 16.94 24H7.06a7.06 7.06 0 0 1-5.03-1.89A6.96 6.96 0 0 1 0 16.94V7.02C0 2.8 2.8 0 7.02 0h9.96zM7.17 2.1c-1.4 0-2.6.48-3.46 1.33c-.85.85-1.33 2.06-1.33 3.46v10.3c0 1.3.47 2.5 1.33 3.36c.86.85 2.06 1.33 3.46 1.33h9.66c1.4 0 2.6-.48 3.46-1.33c.85-.85 1.33-2.06 1.33-3.46V6.89c0-1.4-.47-2.6-1.33-3.46c-.86-.85-2.06-1.33-3.46-1.33H7.17zm11.97 3.33c.77 0 1.4.63 1.4 1.4c0 .77-.63 1.4-1.4 1.4c-.77 0-1.4-.63-1.4-1.4c0-.77.63-1.4 1.4-1.4zM12 5.76c3.39 0 6.14 2.75 6.14 6.14c0 3.39-2.75 6.14-6.14 6.14c-3.39 0-6.14-2.75-6.14-6.14c0-3.39 2.75-6.14 6.14-6.14zm0 2.1c-2.2 0-3.99 1.79-3.99 4.04c0 2.25 1.79 4.04 3.99 4.04c2.2 0 3.99-1.79 3.99-4.04c0-2.25-1.79-4.04-3.99-4.04c0-2.25-1.79-4.04-3.99-4.04c0-2.25-1.79-4.04-3.99-4.04c0-2.25-1.79-4.04-3.99-4.04c0-2.25-1.79-4.04-3.99-4.04c0-2.25-1.79-4.04-3.99-4.04z"/></svg></a>'
    return f"""<footer><div class="container"><div class="footer-grid"><div><h3>{biz_name}</h3><p style="opacity:0.8;">{biz_addr}</p><p style="margin-top:1rem;">{biz_email}</p><div style="margin-top:1.5rem; display:flex; gap:1rem;">{icons}</div></div><div><h4>Explore</h4><a href="index.html">Home</a><a href="about.html">About</a><a href="contact.html">Contact</a></div><div><h4>Legal</h4><a href="privacy.html">Privacy</a><a href="terms.html">Terms</a></div></div><div style="border-top:1px solid rgba(255,255,255,0.1); margin-top:3rem; padding-top:2rem; text-align:center; opacity:0.4;">&copy; {biz_name}. Powered by Titan Engine.</div></div></footer>"""

def gen_wa_widget():
    if not wa_num: return ""
    return f"""<a href="https://wa.me/{wa_num}" style="position:fixed; bottom:30px; right:30px; background:#25d366; color:white; width:60px; height:60px; border-radius:50%; display:flex; align-items:center; justify-content:center; box-shadow:0 10px 30px rgba(37,211,102,0.4); z-index:9999;"><svg style="width:32px;height:32px" viewBox="0 0 24 24"><path fill="currentColor" d="M12.04 2c-5.46 0-9.91 4.45-9.91 9.91 0 1.75.46 3.45 1.32 4.95L2.05 22l5.25-1.38c1.45.79 3.08 1.21 4.74 1.21c5.46 0 9.91-4.45 9.91-9.91c0-2.65-1.03-5.14-2.9-7.01A9.816 9.816 0 0 0 12.04 2m.01 1.67c2.2 0 4.26.86 5.82 2.42a8.225 8.225 0 0 1 2.41 5.83c0 4.54-3.7 8.23-8.24 8.23c-1.48 0-2.93-.39-4.19-1.15l-.3-.17l-3.12.82l.83-3.04l-.2-.32a8.188 8.188 0 0 1-1.26-4.38c.01-4.54 3.7-8.24 8.25-8.24m-3.53 3.16c-.13 0-.35.05-.54.26c-.19.2-.72.7-.72 1.72s.73 2.01.83 2.14c.1.13 1.44 2.19 3.48 3.07c.49.21.87.33 1.16.43c.49.16.94.13 1.29.08c.4-.06 1.21-.5 1.38-.98c.17-.48.17-.89.12-.98c-.05-.09-.18-.13-.37-.23c-.19-.1-.1.13-.1.13s-1.13-.56-1.32-.66c-.19-.1-.32-.15-.45.05c-.13.2-.51.65-.62.78c-.11.13-.23.15-.42.05c-.19-.1-.8-.3-1.53-.94c-.57-.5-1.02-1.12-1.21-1.45c-.11-.19-.01-.29.09-.38c.09-.08.19-.23.29-.34c.1-.11.13-.19.19-.32c.06-.13.03-.24-.01-.34c-.05-.1-.45-1.08-.62-1.48c-.16-.4-.36-.34-.51-.35c-.11-.01-.25-.01-.4-.01Z"/></svg></a>"""

def gen_scripts():
    return """<script>
    window.addEventListener('scroll', () => {
        var reveals = document.querySelectorAll('.reveal');
        for (var i = 0; i < reveals.length; i++) {
            var windowHeight = window.innerHeight;
            var elementTop = reveals[i].getBoundingClientRect().top;
            var elementVisible = 150;
            if (elementTop < windowHeight - elementVisible) { reveals[i].classList.add('active'); }
        }
    });
    window.dispatchEvent(new Event('scroll'));
    </script>"""

def gen_404_content():
    return f"""<section class="hero" style="min-height:70vh;"><div class="container"><h1 style="font-size:6rem;">404</h1><p>Page Not Found</p><a href="index.html" class="btn btn-accent">Return Home</a></div></section>"""

def gen_product_page_content(is_demo=False):
    demo_flag = "const isDemo = true;" if is_demo else "const isDemo = false;"
    return f"""<section style="padding-top:150px;"><div class="container"><div id="product-detail" class="detail-view">Loading...</div></div></section>
    {gen_csv_parser()}<script>{demo_flag}
    function shareWA(url, title) {{ window.open('https://wa.me/?text=' + encodeURIComponent(title + ' ' + url), '_blank'); }}
    async function loadProduct() {{
        const params = new URLSearchParams(window.location.search); let targetName = params.get('item');
        if(isDemo) {{ /* Demo */ }} else if(!targetName) {{ document.getElementById('product-detail').innerHTML = 'Product Not Found'; return; }}
        try {{
            const res = await fetch('{sheet_url}'); const txt = await res.text(); const lines = txt.split(/\\r\\n|\\n/);
            for(let i=1; i<lines.length; i++) {{
                const clean = parseCSVLine(lines[i]);
                if(isDemo) targetName = clean[0];
                if(clean[0] === targetName) {{
                    let img = clean[3] && clean[3].length > 5 ? clean[3] : '{custom_feat}';
                    if(clean[6] && clean[6].length > 5) img = clean[6];
                    document.getElementById('product-detail').innerHTML = `<img src="${{img}}" style="width:100%; border-radius:12px; box-shadow:0 10px 30px rgba(0,0,0,0.1);"><div style="color:var(--txt);"><h1 style="color:var(--p);">${{clean[0]}}</h1><p style="color:var(--s); font-size:1.5rem; font-weight:bold;">${{clean[1]}}</p><p style="opacity:0.9;">${{clean[2]}}</p><a href="https://wa.me/{wa_num}?text=Order ${{encodeURIComponent(clean[0])}}" class="btn-primary btn" style="width:100%; margin-top:2rem;">Order on WhatsApp</a></div>`;
                    break;
                }}
            }}
        }} catch(e) {{}}
    }}
    loadProduct();
    </script>"""

# --- 6. PAGE ASSEMBLY ---
def build_page(title, content, extra_js=""):
    css = get_theme_css()
    schema = gen_schema()
    return f"""<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>{title} | {biz_name}</title><meta name="description" content="{seo_d}">{schema}<style>{css}</style><link href="https://fonts.googleapis.com/css2?family={h_font.replace(' ', '+')}:wght@400;700;900&family={b_font.replace(' ', '+')}:wght@300;400;600&display=swap" rel="stylesheet"></head><body>{gen_nav()}{content}{gen_footer()}{gen_wa_widget()}{gen_scripts()}{extra_js}</body></html>"""

home_content = ""
if show_hero: home_content += gen_hero()
if show_stats: home_content += gen_stats()
if show_features: home_content += gen_features()
if show_magic: home_content += gen_magic()
if show_comparison: home_content += gen_comparison()
if show_inventory: home_content += gen_inventory()
if show_gallery: home_content += gen_about_section()
if show_testimonials: 
    t_cards = "".join([f'<div class="card reveal" style="text-align:center;"><i>"{x.split("|")[1]}"</i><br><br><b>- {x.split("|")[0]}</b></div>' for x in testi_data.split('\n') if "|" in x])
    home_content += f'<section style="background:rgba(0,0,0,0.02)"><div class="container"><div class="section-head reveal"><h2>Client Stories</h2></div><div class="grid-3">{t_cards}</div></div></section>'
if show_faq: home_content += gen_faq_section()
if show_audit: home_content += gen_audit_form()
if show_cta: home_content += f'<section style="background:var(--s); color:white; text-align:center;"><div class="container reveal"><h2>Ready to Start?</h2><p style="margin-bottom:2rem; color:white;">Let us build your future today.</p><a href="contact.html" class="btn" style="background:white; color:var(--s);">Get a Quote</a></div></section>'

# --- 7. PREVIEW & DEPLOY ---
about_content = f"{gen_inner_header('About Us')}<section><div class='container'><div class='about-grid'><div class='legal-text'>{format_text(about_long)}</div><img src='{about_img}' style='width:100%; border-radius:12px; box-shadow:0 10px 30px rgba(0,0,0,0.1);'></div></div></section>"
contact_content = f"{gen_inner_header('Contact Us')}<section><div class='container'><div class='contact-layout'><div><div style='background:var(--card); padding:2rem; border-radius:12px; border:1px solid rgba(100,100,100,0.2);'><h3 style='color:var(--p);'>Get In Touch</h3><p style='margin-top:1rem; color:var(--txt);'><strong>📍 Address:</strong><br>{biz_addr}</p><p style='margin-top:1rem; color:var(--txt);'><strong>📞 Phone:</strong><br><a href='tel:{biz_phone}' style='color:var(--s);'>{biz_phone}</a></p><p style='margin-top:1rem; color:var(--txt);'><strong>📧 Email:</strong><br><a href='mailto:{biz_email}'>{biz_email}</a></p><br><a href='https://wa.me/{wa_num}' target='_blank' class='btn btn-accent' style='width:100%; text-align:center;'>Chat on WhatsApp</a></div></div><div class='card'><h3 style='margin-bottom:1.5rem;'>Send a Message</h3><form action='https://formsubmit.co/{biz_email}' method='POST'><div style='display:grid; grid-template-columns:1fr 1fr; gap:1rem;'><div><label>Name</label><input type='text' name='name' required></div><div><label>Email</label><input type='email' name='email' required></div></div><label>Message</label><textarea name='message' rows='5' required></textarea><button type='submit' class='btn btn-primary' style='width:100%;'>Send Message</button><input type='hidden' name='_captcha' value='false'><input type='hidden' name='_next' value='{prod_url}/contact.html'></form></div></div><br><br><div style='border-radius:12px; overflow:hidden; box-shadow:0 10px 30px rgba(0,0,0,0.1);'>{map_iframe}</div></div></section>"
privacy_content = f"{gen_inner_header('Privacy Policy')}<section><div class='container legal-text'>{format_text(priv_txt)}</div></section>"
terms_content = f"{gen_inner_header('Terms of Service')}<section><div class='container legal-text'>{format_text(term_txt)}</div></section>"

c1, c2 = st.columns([3, 1])
with c1:
    if preview_mode == "Home": st.components.v1.html(build_page("Home", home_content), height=600, scrolling=True)
    elif preview_mode == "About": st.components.v1.html(build_page("About", about_content), height=600, scrolling=True)
    elif preview_mode == "Contact": st.components.v1.html(build_page("Contact", contact_content), height=600, scrolling=True)
    elif preview_mode == "Privacy": st.components.v1.html(build_page("Privacy", privacy_content), height=600, scrolling=True)
    elif preview_mode == "Terms": st.components.v1.html(build_page("Terms", terms_content), height=600, scrolling=True)
    elif preview_mode == "Product Detail (Demo)": st.info("Demo Mode Active"); st.components.v1.html(build_page("Product", gen_product_page_content(is_demo=True)), height=600, scrolling=True)

with c2:
    if st.button("DOWNLOAD WEBSITE ZIP", type="primary"):
        z_b = io.BytesIO()
        with zipfile.ZipFile(z_b, "a", zipfile.ZIP_DEFLATED, False) as zf:
            zf.writestr("index.html", build_page("Home", home_content))
            zf.writestr("about.html", build_page("About", about_content))
            zf.writestr("contact.html", build_page("Contact", contact_content))
            zf.writestr("privacy.html", build_page("Privacy Policy", privacy_content))
            zf.writestr("terms.html", build_page("Terms of Service", terms_content))
            zf.writestr("product.html", build_page("Product Details", gen_product_page_content(is_demo=False)))
            zf.writestr("404.html", build_page("404 Not Found", gen_404_content()))
            zf.writestr("robots.txt", f"User-agent: *\nAllow: /\nSitemap: {prod_url}/sitemap.xml")
            sitemap_xml = f"""<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"><url><loc>{prod_url}/</loc></url></urlset>"""
            zf.writestr("sitemap.xml", sitemap_xml)
        st.download_button("📥 Click to Save", z_b.getvalue(), f"{biz_name.lower().replace(' ','_')}_site.zip", "application/zip")

import streamlit as st
import zipfile
import io
import json
import datetime
import re  # <--- REQUIRED for the Text Formatter

# --- 1. APP CONFIGURATION ---
st.set_page_config(
    page_title="Titan v30.5 | Strategy Core", 
    layout="wide", 
    page_icon="🛡️",
    initial_sidebar_state="expanded"
)

# --- 2. ADVANCED UI SYSTEM (CSS FOR BUILDER) ---
st.markdown("""
    <style>
    /* UI Reset & Variables */
    :root { --primary: #0f172a; --accent: #3b82f6; }
    .stApp { background-color: #f8fafc; color: #1e293b; font-family: 'Inter', sans-serif; }
    
    /* Sidebar Styling */
    [data-testid="stSidebar"] { background-color: #ffffff; border-right: 1px solid #e2e8f0; }
    [data-testid="stSidebar"] h1 { 
        background: linear-gradient(90deg, #0f172a, #3b82f6);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 900 !important;
        font-size: 1.8rem !important;
    }
    
    /* Modern Inputs */
    .stTextInput input, .stTextArea textarea, .stSelectbox div[data-baseweb="select"] {
        background-color: #ffffff !important;
        border: 1px solid #cbd5e1 !important;
        border-radius: 8px !important;
        color: #0f172a !important;
        transition: all 0.2s ease;
    }
    .stTextInput input:focus, .stTextArea textarea:focus {
        border-color: #3b82f6 !important;
        box-shadow: 0 0 0 4px rgba(59, 130, 246, 0.1) !important;
    }
    
    /* Action Buttons */
    .stButton>button {
        width: 100%; border-radius: 8px; height: 3.5rem;
        background: linear-gradient(135deg, #0f172a 0%, #2563eb 100%);
        color: white; font-weight: 800; border: none;
        box-shadow: 0 4px 15px rgba(37, 99, 235, 0.3);
        text-transform: uppercase; letter-spacing: 1px;
        transition: transform 0.2s;
    }
    .stButton>button:hover { transform: translateY(-2px); }
    
    /* Preview Frame */
    iframe { border-radius: 12px; border: 1px solid #e2e8f0; box-shadow: 0 20px 40px -10px rgba(0,0,0,0.1); }
    </style>
    """, unsafe_allow_html=True)

# --- 3. SIDEBAR: THE CONTROL CENTER ---
with st.sidebar:
    st.title("Titan Architect")
    st.caption("v30.5 | Strategy Edition")
    st.divider()
    
    # 3.1 VISUAL DNA
    with st.expander("🎨 Visual DNA", expanded=True):
        theme_mode = st.selectbox("Base Theme", [
            "Midnight SaaS (Dark)", 
            "Clean Corporate (Light)", 
            "Glassmorphism (Blur)",
            "Cyberpunk Neon",
            "Luxury Gold",
            "Forest Eco",
            "Ocean Breeze",
            "Stark Minimalist"
        ])
        c1, c2 = st.columns(2)
        p_color = c1.color_picker("Primary Brand", "#3B82F6") 
        s_color = c2.color_picker("Action (CTA)", "#10B981")  
        
        st.markdown("**Typography**")
        h_font = st.selectbox("Headings", ["Space Grotesk", "Montserrat", "Playfair Display", "Oswald", "Clash Display"])
        b_font = st.selectbox("Body Text", ["Inter", "Open Sans", "Roboto", "Satoshi", "Lora"])
        
        st.markdown("**UI Physics**")
        border_rad = st.select_slider("Corner Roundness", ["0px", "4px", "12px", "24px", "40px"], value="12px")
        anim_type = st.selectbox("Animation Style", ["Fade Up", "Zoom In", "Slide Right", "None"])

    # 3.2 MODULE MANAGER
    with st.expander("🧩 Section Manager", expanded=False):
        st.caption("Toggle sections to include:")
        show_hero = st.checkbox("Hero Carousel", value=True)
        show_stats = st.checkbox("Trust Stats/Logos", value=True)
        show_features = st.checkbox("Feature Grid", value=True)
        show_magic = st.checkbox("✨ Magic Section (Sheets CMS)", value=True) # NEW
        show_comparison = st.checkbox("📊 Comparison Table", value=True)     # NEW
        show_inventory = st.checkbox("Inventory / Portfolio", value=True)
        show_gallery = st.checkbox("About Section", value=True)
        show_testimonials = st.checkbox("Testimonials", value=True)
        show_faq = st.checkbox("F.A.Q.", value=True)
        show_audit = st.checkbox("📝 Audit Form (Lead Gen)", value=True)     # NEW
        show_cta = st.checkbox("Final Call to Action", value=False)

    # 3.3 TECHNICAL
    with st.expander("⚙️ SEO & Analytics", expanded=False):
        st.markdown("**Targeting**")
        seo_area = st.text_input("Service Area (City/Region)", "Global / Online")
        seo_kw = st.text_area("SEO Keywords (Comma Separated)", "software, scripts, automation, web development, saas")
        
        st.markdown("**Verification**")
        gsc_tag = st.text_input("Google Verification ID")
        ga_tag = st.text_input("Google Analytics ID (G-XXXX)")
        og_image = st.text_input("Social Share Image URL")

# --- 4. MAIN WORKSPACE ---
st.title("🏗️ Site Content Builder")

tabs = st.tabs(["1. Identity", "2. Copy & Content", "3. Strategy & Pricing", "4. Inventory", "5. Legal"])

with tabs[0]: # IDENTITY
    c1, c2 = st.columns(2)
    with c1:
        biz_name = st.text_input("Business Name", "StopWebRent")
        biz_tagline = st.text_input("Tagline", "Stop Paying 'Web Rent' Forever.")
        biz_phone = st.text_input("Phone", "+966 57 256 2151")
        biz_email = st.text_input("Email (For Forms)", "deploy@stopwebrent.com")
    with c2:
        prod_url = st.text_input("Website URL", "https://stopwebrent.com")
        biz_addr = st.text_area("Address", "Kaydiem Script Lab, Kolkata Innovation Node.", height=100)
        map_iframe = st.text_area("Map/Footer Code", placeholder='<iframe src="..."></iframe>', height=100)
        seo_d = st.text_area("Meta Description", "We build ultra-fast static websites for local businesses. Pay once, own it forever.", height=100)
        logo_url = st.text_input("Logo URL (PNG/SVG)")
        
    st.subheader("Social Links")
    sc1, sc2, sc3 = st.columns(3)
    fb_link = sc1.text_input("Facebook URL")
    ig_link = sc2.text_input("Instagram URL")
    x_link = sc3.text_input("X (Twitter) URL")
    
    sc4, sc5, sc6 = st.columns(3)
    li_link = sc4.text_input("LinkedIn URL")
    yt_link = sc5.text_input("YouTube URL")
    wa_num = sc6.text_input("WhatsApp Number (No +)", "966572562151")

with tabs[1]: # CONTENT BLOCKS
    st.subheader("Hero Carousel")
    hero_h = st.text_input("Hero Headline", "Stop Renting Your Website.")
    hero_sub = st.text_input("Hero Subtext", "The Titan Engine is the world’s first 0.1s website architecture that runs on $0 monthly fees. Pay once. Own it forever.")
    
    hc1, hc2, hc3 = st.columns(3)
    hero_img_1 = hc1.text_input("Slide 1 Image", "https://images.unsplash.com/photo-1550751827-4bd374c3f58b?q=80&w=1600")
    hero_img_2 = hc2.text_input("Slide 2 Image", "https://images.unsplash.com/photo-1497366216548-37526070297c?q=80&w=1600")
    hero_img_3 = hc3.text_input("Slide 3 Image", "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?q=80&w=1600")
    
    st.divider()
    
    st.subheader("Trust Stats Data")
    col_s1, col_s2, col_s3 = st.columns(3)
    stat_1 = col_s1.text_input("Stat 1", "$1,491")
    label_1 = col_s1.text_input("Label 1", "5-Year Savings")
    
    stat_2 = col_s2.text_input("Stat 2", "0.1s")
    label_2 = col_s2.text_input("Label 2", "Load Speed")
    
    stat_3 = col_s3.text_input("Stat 3", "100%")
    label_3 = col_s3.text_input("Label 3", "Ownership")

    st.divider()
    
    st.subheader("Feature Grid")
    st.info("Keywords: shield, water, bolt, database, lock, truck")
    f_title = st.text_input("Features Title", "The 4 Pillars")
    feat_data = st.text_area("Features List", 
                             "water | 0.1s Speed | Google demands speed. Titan sites load instantly (0.1s). This boosts your Google Rank immediately.\nshield | Zero Monthly Fees | No hosting bills. No maintenance fees. No surprise costs. You own the code 100%.\ndatabase | Google Sheets CMS | Update prices and photos using a simple Google Sheet. If you can use Excel, you can run your site.\nlock | Bank-Grade Security | We removed the database, which means we removed the hackers' entry point. Virtually unhackable.",
                             height=150)
    
    st.subheader("About Content")
    about_h = st.text_input("About Title", "Restoring Logic")
    about_img = st.text_input("About Side Image", "https://images.unsplash.com/photo-1555099962-4199c345e5dd?q=80&w=1600")
    c_a1, c_a2 = st.columns(2)
    about_short = c_a1.text_area("Short Summary", "Traditional agencies and builders like Wix/Shopify charge you 'rent' every month. If you stop paying, they delete your business. We changed the rules.", height=200)
    about_long = c_a2.text_area("Long Content", "**The Death of the Subscription Model**\nFor too long, agencies have forced local businesses into 'forever-payments'. At StopWebRent, we view a website as a structural asset.", height=200)

with tabs[2]: # STRATEGY & PRICING (NEW)
    st.subheader("✨ Magic Section (Google Sheets CMS)")
    magic_h = st.text_input("Magic Headline", "Control Your Empire from a Spreadsheet")
    magic_desc = st.text_area("Magic Description", "No WordPress dashboard. No plugins to update. Just open your private Google Sheet, change a text, and watch your site update globally in seconds.")
    magic_img = st.text_input("Magic Image/GIF URL", "https://images.unsplash.com/photo-1460925895917-afdab827c52f?q=80&w=1600")
    
    st.divider()
    st.subheader("📊 Cost Comparison Table")
    comp_h = st.text_input("Table Headline", "The 'Cost of Ownership' Calculator")
    c1, c2, c3 = st.columns(3)
    comp_my_price = c1.text_input("Your Setup Fee", "$249")
    comp_wix_price = c2.text_input("Competitor 5-Year Cost", "$1,815")
    comp_save = c3.text_input("Total Savings Amount", "$1,491")

with tabs[3]: # INVENTORY & LEGAL
    st.info("⚡ Power your inventory with a Google Sheet")
    sheet_url = st.text_input("Google Sheet CSV Link", placeholder="https://docs.google.com/spreadsheets/d/e/.../pub?output=csv")
    custom_feat = st.text_input("Default Product Image URL (Fallback)", "https://images.unsplash.com/photo-1460925895917-afdab827c52f?q=80&w=800")
    
    st.divider()
    
    st.subheader("Trust & Legal")
    testi_data = st.text_area("Testimonials (Name | Quote)", "Joe S. | I was paying $40/month for Wix. StopWebRent saved me $480 this year.\nLakshmi Builders | The Google Sheets integration is magic.", height=100)
    faq_data = st.text_area("FAQ Data (Q? ? A)", "Do I really pay $0 for hosting? ? Yes. We use static architecture that fits within the free tiers of enterprise CDNs.\nWhat about my Domain Name? ? You pay ~$15/year directly to the registrar.", height=100)
    
    l1, l2 = st.columns(2)
    priv_txt = l1.text_area("Privacy Policy Text", "**Digital Sovereignty**\nWe respect your data...", height=200)
    term_txt = l2.text_area("Terms of Service Text", "**Ownership**\nYou own the code upon payment...", height=200)

# --- 5. COMPILER ENGINE (V30.5 COMPLETE) ---

def format_text(text):
    """Advanced Text Formatter v30.4 (Regex)"""
    if not text: return ""
    processed_text = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', text)
    lines = processed_text.split('\n')
    html_out = ""
    in_list = False
    
    for line in lines:
        clean_line = line.strip()
        if not clean_line: continue
        
        if clean_line.startswith("* "):
            if not in_list:
                html_out += '<ul style="margin-bottom:1rem; padding-left:1.5rem;">'
                in_list = True
            content = clean_line[2:] 
            html_out += f'<li style="margin-bottom:0.5rem; opacity:0.9; color:inherit;">{content}</li>'
        elif clean_line.startswith("<strong>") and clean_line.endswith("</strong>"):
            if in_list: html_out += "</ul>"; in_list = False
            header_text = clean_line.replace("<strong>", "").replace("</strong>", "")
            html_out += f"<h3 style='margin-top:1.5rem; margin-bottom:0.5rem; color:var(--p); font-size:1.25rem;'>{header_text}</h3>"
        else:
            if in_list: html_out += "</ul>"; in_list = False
            html_out += f"<p style='margin-bottom:1rem; opacity:0.9; color:inherit;'>{clean_line}</p>"
            
    if in_list: html_out += "</ul>"
    return html_out

def gen_schema():
    schema = {
        "@context": "https://schema.org",
        "@type": "LocalBusiness",
        "name": biz_name,
        "image": logo_url or hero_img_1,
        "telephone": biz_phone,
        "email": biz_email,
        "areaServed": seo_area,
        "address": {"@type": "PostalAddress", "streetAddress": biz_addr},
        "url": prod_url,
        "description": seo_d
    }
    return f'<script type="application/ld+json">{json.dumps(schema)}</script>'

def get_theme_css():
    bg = "#0f172a" if "Midnight" in theme_mode else "#ffffff"
    txt = "#f8fafc" if "Midnight" in theme_mode else "#0f172a"
    card = "#1e293b" if "Midnight" in theme_mode else "#ffffff"
    glass = "rgba(15, 23, 42, 0.9)" if "Midnight" in theme_mode else "rgba(255, 255, 255, 0.95)"
    
    anim_css = ""
    if anim_type == "Fade Up": anim_css = ".reveal { opacity: 0; transform: translateY(30px); transition: all 0.8s ease-out; } .reveal.active { opacity: 1; transform: translateY(0); }"
    elif anim_type == "Zoom In": anim_css = ".reveal { opacity: 0; transform: scale(0.95); transition: all 0.8s cubic-bezier(0.175, 0.885, 0.32, 1.275); } .reveal.active { opacity: 1; transform: scale(1); }"
    
    hero_css = """
    .hero { position: relative; min-height: 90vh; overflow: hidden; display: flex; align-items: center; justify-content: center; text-align: center; color: white; padding-top: 80px; background-color: var(--p); }
    .carousel-slide { position: absolute; top: 0; left: 0; width: 100%; height: 100%; background-size: cover; background-position: center; opacity: 0; transition: opacity 1.5s ease-in-out; z-index: 0; }
    .carousel-slide.active { opacity: 1; }
    .hero-overlay { background: rgba(0,0,0,0.5); position: absolute; top: 0; left: 0; width: 100%; height: 100%; z-index: 1; }
    .hero-content { z-index: 2; position: relative; animation: slideUp 1s ease-out; }
    @keyframes slideUp { from { opacity:0; transform: translateY(30px); } to { opacity:1; transform: translateY(0); } }
    """

    return f"""
    :root {{
        --p: {p_color}; --s: {s_color}; --bg: {bg}; --txt: {txt}; --card: {card};
        --radius: {border_rad}; --nav: {glass};
        --h-font: '{h_font}', sans-serif; --b-font: '{b_font}', sans-serif;
    }}
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
    
    /* GRIDS */
    .grid-3 {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 2rem; }}
    .contact-layout {{ display: grid; grid-template-columns: 1fr 2fr; gap: 3rem; }}
    .about-grid, .magic-grid {{ display: grid; grid-template-columns: 1fr 1fr; gap: 4rem; align-items: center; }}
    
    .card {{ background: var(--card); padding: 2rem; border-radius: var(--radius); border: 1px solid rgba(100,100,100,0.1); transition: 0.3s; height: 100%; display: flex; flex-direction: column; }}
    .card:hover {{ transform: translateY(-5px); box-shadow: 0 20px 40px -10px rgba(0,0,0,0.1); border-color: var(--s); }}
    
    .prod-img {{ width: 100%; height: 250px; object-fit: cover; border-radius: calc(var(--radius) - 4px); margin-bottom: 1.5rem; background: #f1f5f9; }}
    
    /* FAQ Styling */
    details {{ background: var(--card); border: 1px solid rgba(100,100,100,0.1); border-radius: 8px; margin-bottom: 1rem; padding: 1rem; cursor: pointer; color: var(--txt); }}
    details summary {{ font-weight: bold; font-size: 1.1rem; color: var(--txt); }}
    details p {{ margin-top: 1rem; margin-bottom: 0; opacity: 0.9; color: var(--txt); }}

    /* Footer & Social Icons */
    footer {{ background: var(--p); color: white; padding: 4rem 0; margin-top: auto; }}
    .footer-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 3rem; }}
    .footer a, footer a {{ color: rgba(255,255,255,0.8) !important; text-decoration: none; display: block; margin-bottom: 0.5rem; transition: 0.3s; }}
    .footer a:hover, footer a:hover {{ color: #ffffff !important; text-decoration: underline; }}
    
    .social-icon {{ width: 24px; height: 24px; fill: rgba(255,255,255,0.7); transition: 0.3s; }}
    .social-icon:hover {{ fill: #ffffff; transform: scale(1.1); }}

    /* Tables & Strategy Elements */
    .comp-table {{ width: 100%; border-collapse: collapse; margin: 20px 0; background: var(--card); border-radius: var(--radius); overflow: hidden; }}
    .comp-table th, .comp-table td {{ padding: 20px; text-align: left; border-bottom: 1px solid rgba(128,128,128,0.1); }}
    .comp-table th {{ background: var(--p); color: white; }}
    .savings-box {{ background: var(--s); color: white; padding: 2rem; border-radius: var(--radius); text-align: center; margin-top: 2rem; }}

    /* Real Brand Share Buttons */
    .share-btn {{ width: 42px; height: 42px; border-radius: 50%; display: flex; align-items: center; justify-content: center; border: none; cursor: pointer; transition: 0.3s; color: white; }}
    .share-btn:hover {{ transform: scale(1.1); filter: brightness(1.1); }}
    .share-btn svg {{ width: 20px; height: 20px; fill: currentColor; }}
    .share-wa {{ background: #25D366; }} .share-fb {{ background: #1877F2; }} .share-x {{ background: #000000; }} .share-li {{ background: #0A66C2; }} .share-cp {{ background: #64748b; }}
    
    .detail-view {{ display: grid; grid-template-columns: 1fr 1fr; gap: 4rem; align-items: start; }}
    .legal-text h1 {{ font-size: 3rem; margin-bottom: 2rem; color: var(--p); }} .legal-text h3 {{ margin-top: 2rem; font-size: 1.5rem; color: var(--p); }} .legal-text p {{ color: var(--txt); opacity: 0.9; }}

    {anim_css}
    
    @media (max-width: 768px) {{
        .nav-links {{ position: fixed; top: 70px; left: -100%; width: 100%; height: calc(100vh - 70px); background: var(--bg); flex-direction: column; padding: 2rem; transition: 0.3s; align-items: flex-start; justify-content: flex-start; border-top: 1px solid rgba(0,0,0,0.1); }}
        .nav-links.active {{ left: 0; }}
        .nav-links a {{ margin-left: 0; margin-bottom: 1.5rem; font-size: 1.1rem; }}
        .mobile-menu {{ display: block; }}
        .hero {{ min-height: 70vh; }}
        .contact-layout, .detail-view, .about-grid, .magic-grid {{ grid-template-columns: 1fr !important; gap: 2rem; }}
        .about-grid img {{ order: 2; margin-top: 1rem; }} .about-grid div {{ order: 1; }}
    }}
    """

def gen_nav():
    logo_display = f'<img src="{logo_url}" height="40" alt="{biz_name} Logo">' if logo_url else f'<span style="font-weight:900; font-size:1.5rem; color:var(--p)">{biz_name}</span>'
    return f"""
    <nav><div class="container nav-flex">
        <a href="index.html" style="text-decoration:none">{logo_display}</a>
        <div class="mobile-menu" onclick="document.querySelector('.nav-links').classList.toggle('active')">☰</div>
        <div class="nav-links">
            <a href="index.html" onclick="document.querySelector('.nav-links').classList.remove('active')">Home</a>
            {'<a href="index.html#features" onclick="document.querySelector(\'.nav-links\').classList.remove(\'active\')">Features</a>' if show_features else ''}
            {'<a href="index.html#inventory" onclick="document.querySelector(\'.nav-links\').classList.remove(\'active\')">Products</a>' if show_inventory else ''}
            <a href="about.html" onclick="document.querySelector('.nav-links').classList.remove('active')">About</a>
            <a href="contact.html" onclick="document.querySelector('.nav-links').classList.remove('active')">Contact</a>
            {f'<a href="#audit" class="btn-accent" style="padding:0.6rem 1.5rem; margin-left:1.5rem; margin-bottom:0; border-radius:50px; color:white !important;">Free Audit</a>' if show_audit else f'<a href="tel:{biz_phone}" class="btn-accent" style="padding:0.6rem 1.5rem; margin-left:1.5rem; margin-bottom:0; border-radius:50px; color:white !important;">Call Now</a>'}
        </div>
    </div></nav>
    """

def gen_hero():
    return f"""
    <section class="hero">
        <div class="hero-overlay"></div>
        <div class="carousel-slide active" style="background-image: url('{hero_img_1}')"></div>
        <div class="carousel-slide" style="background-image: url('{hero_img_2}')"></div>
        <div class="carousel-slide" style="background-image: url('{hero_img_3}')"></div>
        <div class="container hero-content">
            <h1>{hero_h}</h1>
            <p>{hero_sub}</p>
            <div style="display:flex; gap:1rem; justify-content:center; flex-wrap:wrap;">
                {f'<a href="#audit" class="btn btn-accent">Get Free Audit</a>' if show_audit else '<a href="#inventory" class="btn btn-accent">Explore Now</a>'}
                <a href="#features" class="btn" style="background:rgba(255,255,255,0.2); backdrop-filter:blur(10px); color:white;">How It Works</a>
            </div>
        </div>
    </section>
    <script>let slides = document.querySelectorAll('.carousel-slide'); let currentSlide = 0; setInterval(() => {{ slides[currentSlide].classList.remove('active'); currentSlide = (currentSlide + 1) % slides.length; slides[currentSlide].classList.add('active'); }}, 4000);</script>
    """

def get_simple_icon(name):
    # UPGRADED ICON LIBRARY V30.4
    name = name.lower().strip()
    if "code" in name: return '<svg viewBox="0 0 24 24" width="32" height="32" fill="currentColor"><path d="M9.4 16.6L4.8 12l4.6-4.6L8 6l-6 6 6 6 1.4-1.4zm5.2 0l4.6-4.6-4.6-4.6L16 6l6 6-6 6-1.4-1.4z"/></svg>'
    if "database" in name: return '<svg viewBox="0 0 24 24" width="32" height="32" fill="currentColor"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm1 15h-2v-6h2v6zm0-8h-2V7h2v2z"/></svg>'
    if "layers" in name: return '<svg viewBox="0 0 24 24" width="32" height="32" fill="currentColor"><path d="M11.99 18.54l-7.37-5.73L3 14.07l9 7 9-7-1.63-1.27-7.38 5.74zM12 16l7.36-5.73L21 9l-9-7-9 7 1.63 1.27L12 16z"/></svg>'
    if "truck" in name or "logistics" in name: return '<svg viewBox="0 0 24 24" width="32" height="32" fill="currentColor"><path d="M20 8h-3V4H3c-1.1 0-2 .9-2 2v11h2c0 1.66 1.34 3 3 3s3-1.34 3-3h6c0 1.66 1.34 3 3 3s3-1.34 3-3h2v-5l-3-4zM6 18.5c-.83 0-1.5-.67-1.5-1.5s.67-1.5 1.5-1.5 1.5.67 1.5 1.5-.67 1.5-1.5 1.5zm13.5-9l1.96 2.5H17V9.5h2.5zm-1.5 9c-.83 0-1.5-.67-1.5-1.5s.67-1.5 1.5-1.5 1.5.67 1.5 1.5-.67 1.5-1.5 1.5z"/></svg>'
    if "shield" in name or "secure" in name or "lock" in name: return '<svg viewBox="0 0 24 24" width="32" height="32" fill="currentColor"><path d="M12 1L3 5v6c0 5.55 3.84 10.74 9 12 5.16-1.26 9-6.45 9-12V5l-9-4zm0 10.99h7c-.53 4.12-3.28 7.79-7 8.94V12H5V6.3l7-3.11v8.8z"/></svg>'
    if "hammer" in name or "build" in name: return '<svg viewBox="0 0 24 24" width="32" height="32" fill="currentColor"><path d="M22.11 11.26l-1.41-1.41c-.55-.56-1.43-.6-2.03-.1L15 6.6V3c0-.55-.45-1-1-1H9c-.55 0-1 .45-1 1v7h2v-2h2v4l-6.88 5.73c-.78.65-1.95.65-2.73 0-.78-.65-.78-1.71 0-2.36L8.53 10.2l-1.27-1.27c-.78-.78-.78-2.05 0-2.83.78-.78 2.05-.78 2.83 0l1.27 1.27 5.14-4.28c.15-.12.33-.19.51-.19.18 0 .37.07.51.19l1.41 1.41c.29.29.29.77 0 1.06L14 10.53l6.59 5.49c1.56-1.56 1.56-4.09 1.52-4.76z"/></svg>'
    if "water" in name or "plumb" in name or "drop" in name: return '<svg viewBox="0 0 24 24" width="32" height="32" fill="currentColor"><path d="M12 22c4.97 0 9-4.03 9-9 0-4.97-9-13-9-13S3 8.03 3 13c0 4.97 4.03 9 9 9zm0-11c1.66 0 3 1.34 3 3s-1.34 3-3 3-3-1.34-3-3 1.34-3 3-3z"/></svg>'
    if "home" in name or "roof" in name: return '<svg viewBox="0 0 24 24" width="32" height="32" fill="currentColor"><path d="M10 20v-6h4v6h5v-8h3L12 3 2 12h3v8z"/></svg>'
    if "bolt" in name or "electric" in name: return '<svg viewBox="0 0 24 24" width="32" height="32" fill="currentColor"><path d="M11 21h-1l1-7H7.5c-.58 0-.57-.32-.38-.66.19-.34.05-.08.07-.12C8.48 10.94 10.42 7.54 13 3h1l-1 7h3.5c.49 0 .56.33.47.51l-.07.15C12.96 17.55 11 21 11 21z"/></svg>'
    if "star" in name: return '<svg viewBox="0 0 24 24" width="32" height="32" fill="currentColor"><path d="M12 17.27L18.18 21l-1.64-7.03L22 9.24l-7.19-.61L12 2 9.19 8.63 2 9.24l5.46 4.73L5.82 21z"/></svg>'
    if "heart" in name: return '<svg viewBox="0 0 24 24" width="32" height="32" fill="currentColor"><path d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z"/></svg>'
    return '<svg viewBox="0 0 24 24" width="32" height="32" fill="currentColor"><path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-2 15l-5-5 1.41-1.41L10 14.17l7.59-7.59L19 8l-9 9z"/></svg>'

def gen_features():
    cards = ""
    lines = [x for x in feat_data.split('\n') if x.strip()]
    for line in lines:
        if "|" in line:
            parts = line.split('|')
            if len(parts) >= 3:
                icon_code = get_simple_icon(parts[0])
                # FIXED: Text color inheritance
                cards += f"""<div class="card reveal"><div style="color:var(--s); margin-bottom:1rem;">{icon_code}</div><h3 style="color:var(--p); font-size:1.2rem; text-transform:uppercase; letter-spacing:1px;">{parts[1].strip()}</h3><div style="opacity:0.9; color:var(--txt); font-size:0.95rem;">{format_text(parts[2].strip())}</div></div>"""
            elif len(parts) == 2:
                cards += f"""<div class="card reveal"><h3 style="color:var(--s); font-size:1.2rem; text-transform:uppercase; letter-spacing:1px;">{parts[0].strip()}</h3><div style="opacity:0.9; color:var(--txt); font-size:0.95rem;">{format_text(parts[1].strip())}</div></div>"""
    return f"""<section id="features"><div class="container"><div class="section-head reveal"><h2>{f_title}</h2></div><div class="grid-3">{cards}</div></div></section>"""

def gen_magic():
    return f"""<section id="magic" style="background:rgba(0,0,0,0.02);"><div class="container">
        <div class="magic-grid">
            <div class="reveal">
                <h2 style="font-size:2.5rem;">{magic_h}</h2>
                <p style="font-size:1.1rem; opacity:0.8; margin:1.5rem 0;">{magic_desc}</p>
            </div>
            <img src="{magic_img}" class="reveal" style="width:100%; border-radius:var(--radius); box-shadow:0 20px 50px -20px rgba(0,0,0,0.2);">
        </div></div></section>"""

def gen_comparison():
    return f"""<section id="pricing"><div class="container">
        <div class="section-head reveal" style="text-align:center;"><h2>{comp_h}</h2></div>
        <table class="comp-table reveal">
            <tr><th>Expense Category</th><th>Titan Engine</th><th>Wix / Shopify</th></tr>
            <tr><td>Initial Setup Fee</td><td>{comp_my_price} (One-time)</td><td>$0 (DIY)</td></tr>
            <tr><td>Annual Hosting</td><td><strong>$0</strong></td><td>$348 ($29/mo)</td></tr>
            <tr><td>Technical Maintenance</td><td><strong>$0</strong></td><td>Time or Money</td></tr>
            <tr><td><strong>5-Year Total Cost</strong></td><td><strong>{comp_my_price}</strong></td><td><strong>{comp_wix_price}</strong></td></tr>
        </table>
        <div class="savings-box reveal"><h2>Your 5-Year Savings: {comp_save}</h2><p>Stop bleeding cash. Start owning your asset.</p></div>
    </div></section>"""

def gen_stats():
    return f"""<div style="background:var(--p); color:white; padding:3rem 0; text-align:center;">
        <div class="container grid-3">
            <div class="reveal"><h3>{stat_1}</h3><p>{label_1}</p></div>
            <div class="reveal"><h3>{stat_2}</h3><p>{label_2}</p></div>
            <div class="reveal"><h3>{stat_3}</h3><p>{label_3}</p></div>
        </div></div>"""

def gen_audit_form():
    return f"""<section id="audit" style="background:var(--p); color:white;"><div class="container" style="max-width:600px; text-align:center;">
        <div class="reveal"><h2 style="color:white;">Get Your Free "Digital Rent" Audit</h2><p style="color:white; opacity:0.8; margin-bottom:2rem;">Send us your details. We will show you exactly how much speed and money you are losing.</p>
        <form action="https://formsubmit.co/{biz_email}" method="POST" style="text-align:left;">
            <label style="color:white;">Your Name</label><input type="text" name="name" required>
            <label style="color:white;">Current Website (Optional)</label><input type="text" name="website">
            <label style="color:white;">WhatsApp Number</label><input type="text" name="phone" required>
            <button type="submit" class="btn-accent" style="width:100%; border:none; margin-top:1rem;">REQUEST AUDIT</button>
        </form></div></div></section>"""

def gen_csv_parser():
    return """<script>
    function parseCSVLine(str) { const res = []; let cur = ''; let inQuote = false; for (let i = 0; i < str.length; i++) { const c = str[i]; if (c === '"') { if (inQuote && str[i+1] === '"') { cur += '"'; i++; } else { inQuote = !inQuote; } } else if (c === ',' && !inQuote) { res.push(cur.trim()); cur = ''; } else { cur += c; } } res.push(cur.trim()); return res; }
    </script>"""

def gen_inventory_js(is_demo=False):
    demo_flag = "const isDemo = true;" if is_demo else "const isDemo = false;"
    return f"""{gen_csv_parser()}<script>{demo_flag}
    async function loadInv() {{
        try {{
            const res = await fetch('{sheet_url}'); const txt = await res.text();
            const lines = txt.split(/\\r\\n|\\n/); const box = document.getElementById('inv-grid');
            if(!box) return; box.innerHTML = '';
            for(let i=1; i<lines.length; i++) {{
                if(!lines[i].trim()) continue; const clean = parseCSVLine(lines[i]);
                let img = clean[3] && clean[3].length > 5 ? clean[3] : '{custom_feat}';
                if(clean[6] && clean[6].length > 5) img = clean[6];
                if(clean.length > 1) {{
                    const prodName = encodeURIComponent(clean[0]);
                    box.innerHTML += `<div class="card reveal" style="color:var(--txt);">
                        <img src="${{img}}" class="prod-img" loading="lazy" onerror="this.onerror=null;this.src='{custom_feat}';">
                        <div style="flex-grow:1; display:flex; flex-direction:column; justify-content:space-between;">
                            <div><h3 style="color:var(--p);">${{clean[0]}}</h3><p style="color:var(--s); font-weight:bold;">${{clean[1]}}</p><p style="opacity:0.9;">${{clean[2]}}</p></div>
                            <div style="margin-top:1rem; display:grid; grid-template-columns:1fr 1fr; gap:0.5rem;">
                                <a href="product.html?item=${{prodName}}" class="btn" style="background:#e2e8f0; color:#0f172a !important; padding:0.8rem; font-size:0.8rem;">Details</a>
                                <a href="https://wa.me/{wa_num}?text=Interested in ${{prodName}}" class="btn-primary btn" style="padding:0.8rem; font-size:0.8rem;">WhatsApp</a>
                            </div>
                        </div></div>`;
                }}
            }}
        }} catch(e) {{ console.log(e); }}
    }}
    if(document.getElementById('inv-grid')) window.addEventListener('load', loadInv);
    </script>"""

def gen_inventory():
    if not show_inventory: return ""
    return f"""<section id="inventory" style="background:rgba(0,0,0,0.02)"><div class="container"><div class="section-head reveal"><h2>Live Inventory</h2><p>Real-time availability directly from our warehouse.</p></div><div id="inv-grid" class="grid-3"><div style="grid-column:1/-1; text-align:center; padding:4rem; color:var(--s);">Loading Database...</div></div></div></section>{gen_inventory_js(is_demo=False)}"""

def gen_about_section():
    return f"""<section id="about"><div class="container"><div class="about-grid"><div class="reveal"><h2 style="font-size:2.5rem; margin-bottom:1.5rem;">{about_h}</h2><div style="font-size:1.1rem; opacity:0.9; margin-bottom:2rem; color:var(--txt);">{format_text(about_short)}</div><a href="about.html" class="btn btn-primary" style="padding:0.8rem 2rem; font-size:0.9rem;">Read Our Full Story</a></div><img src="{about_img}" class="reveal" loading="lazy" style="width:100%; border-radius:var(--radius); box-shadow:0 20px 50px -20px rgba(0,0,0,0.2);"></div></div></section>"""

def gen_faq_section():
    items = ""
    for line in faq_data.split('\n'):
        if "?" in line and not line.strip() == "":
            parts = line.split('?', 1)
            if len(parts) == 2:
                items += f"<details class='reveal'><summary>{parts[0].strip()}?</summary><p>{parts[1].strip()}</p></details>"
    return f"""<section id="faq" style="background:rgba(0,0,0,0.02)"><div class="container" style="max-width:800px;"><div class="section-head reveal"><h2>Frequently Asked Questions</h2></div>{items}</div></section>"""

def gen_product_page_content(is_demo=False):
    demo_flag = "const isDemo = true;" if is_demo else "const isDemo = false;"
    return f"""<section style="padding-top:150px;"><div class="container"><div id="product-detail" class="detail-view"><div style="background:#eee; height:400px; border-radius:12px; display:flex; align-items:center; justify-content:center; color:#333;">Loading Product...</div></div></div></section>
    {gen_csv_parser()}<script>{demo_flag}
    function shareWA(url, title) {{ window.open('https://wa.me/?text=' + encodeURIComponent(title + ' ' + url), '_blank'); }}
    function shareFB(url) {{ window.open('https://www.facebook.com/sharer/sharer.php?u=' + encodeURIComponent(url), '_blank'); }}
    function shareX(url, title) {{ window.open('https://twitter.com/intent/tweet?text=' + encodeURIComponent(title) + '&url=' + encodeURIComponent(url), '_blank'); }}
    function shareLI(url) {{ window.open('https://www.linkedin.com/sharing/share-offsite/?url=' + encodeURIComponent(url), '_blank'); }}
    function copyLink(url) {{ navigator.clipboard.writeText(url); alert('Link copied!'); }}
    
    async function loadProduct() {{
        const params = new URLSearchParams(window.location.search); let targetName = params.get('item');
        const currentUrl = window.location.href;
        if(isDemo) {{ /* Demo Logic */ }} else if(!targetName) {{ document.getElementById('product-detail').innerHTML = '<h2>Product not found</h2>'; return; }}
        try {{
            const res = await fetch('{sheet_url}'); const txt = await res.text(); const lines = txt.split(/\\r\\n|\\n/);
            for(let i=1; i<lines.length; i++) {{
                const clean = parseCSVLine(lines[i]);
                if(isDemo) targetName = clean[0];
                if(clean[0] === targetName) {{
                    let img = clean[3] && clean[3].length > 5 ? clean[3] : '{custom_feat}';
                    if(clean[6] && clean[6].length > 5) img = clean[6];
                    document.getElementById('product-detail').innerHTML = `
                    <img src="${{img}}" style="width:100%; border-radius:12px; box-shadow:0 10px 30px rgba(0,0,0,0.1);">
                    <div style="color:var(--txt);">
                        <h1 style="color:var(--p);">${{clean[0]}}</h1>
                        <p style="color:var(--s); font-size:1.5rem; font-weight:bold;">${{clean[1]}}</p>
                        <p style="opacity:0.9;">${{clean[2]}}</p>
                        <a href="https://wa.me/{wa_num}?text=Order ${{encodeURIComponent(clean[0])}}" class="btn-primary btn" style="width:100%; margin-top:2rem;">Order on WhatsApp</a>
                        <div style="margin-top:2rem;">
                            <p style="font-size:0.9rem; font-weight:bold; opacity:0.7;">SHARE THIS:</p>
                            <div style="display:flex; gap:0.8rem;">
                                <button onclick="shareWA('${{currentUrl}}', '${{clean[0]}}')" class="share-btn share-wa"><svg viewBox="0 0 24 24"><path d="M12.04 2c-5.46 0-9.91 4.45-9.91 9.91c0 1.75.46 3.45 1.32 4.95L2.05 22l5.25-1.38c1.45.79 3.08 1.21 4.74 1.21c5.46 0 9.91-4.45 9.91-9.91c0-2.65-1.03-5.14-2.9-7.01A9.816 9.816 0 0 0 12.04 2m.01 1.67c2.2 0 4.26.86 5.82 2.42a8.225 8.225 0 0 1 2.41 5.83c0 4.54-3.7 8.23-8.24 8.23c-1.48 0-2.93-.39-4.19-1.15l-.3-.17l-3.12.82l.83-3.04l-.2-.32a8.188 8.188 0 0 1-1.26-4.38c.01-4.54 3.7-8.24 8.25-8.24m-3.53 3.16c-.13 0-.35.05-.54.26c-.19.2-.72.7-.72 1.72s.73 2.01.83 2.14c.1.13 1.44 2.19 3.48 3.07c.49.21.87.33 1.16.43c.49.16.94.13 1.29.08c.4-.06 1.21-.5 1.38-.98c.17-.48.17-.89.12-.98c-.05-.09-.18-.13-.37-.23c-.19-.1-.1.13-.1.13s-1.13-.56-1.32-.66c-.19-.1-.32-.15-.45.05c-.13.2-.51.65-.62.78c-.11.13-.23.15-.42.05c-.19-.1-.8-.3-1.53-.94c-.57-.5-1.02-1.12-1.21-1.45c-.11-.19-.01-.29.09-.38c.09-.08.19-.23.29-.34c.1-.11.13-.19.19-.32c.06-.13.03-.24-.01-.34c-.05-.1-.45-1.08-.62-1.48c-.16-.4-.36-.34-.51-.35c-.11-.01-.25-.01-.4-.01Z"/></svg></button>
                                <button onclick="shareFB('${{currentUrl}}')" class="share-btn share-fb"><svg viewBox="0 0 24 24"><path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"></path></svg></button>
                                <button onclick="shareX('${{currentUrl}}', '${{clean[0]}}')" class="share-btn share-x"><svg viewBox="0 0 24 24"><path d="M18.901 1.153h3.68l-8.04 9.19L24 22.846h-7.406l-5.8-7.584l-6.638 7.584H.474l8.6-9.83L0 1.154h7.594l5.243 6.932ZM17.61 20.644h2.039L6.486 3.24H4.298Z"></path></svg></button>
                                <button onclick="shareLI('${{currentUrl}}')" class="share-btn share-li"><svg viewBox="0 0 24 24"><path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2a2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6zM2 9h4v12H2zM4 2a2 2 0 1 1-2 2a2 2 0 0 1 2-2z"></path></svg></button>
                                <button onclick="copyLink('${{currentUrl}}')" class="share-btn share-cp"><svg viewBox="0 0 24 24"><path d="M3.9 12c0-1.71 1.39-3.1 3.1-3.1h4V7H7c-2.76 0-5 2.24-5 5s2.24 5 5 5h4v-1.9H7c-1.71 0-3.1-1.39-3.1-3.1zM8 13h8v-2H8v2zm9-6h-4v1.9h4c1.71 0 3.1 1.39 3.1 3.1s-1.39 3.1-3.1 3.1h-4V17h4c2.76 0 5-2.24 5-5s-2.24-5-5-5z"></path></svg></button>
                            </div>
                        </div>
                    </div>`;
                    break;
                }}
            }}
        }} catch(e) {{}}
    }}
    loadProduct();
    </script>"""

# --- 6. PAGE CONTENT GENERATION ---
home_content = ""
if show_hero: home_content += gen_hero()
if show_stats: home_content += gen_stats()
if show_features: home_content += gen_features()
if show_magic: home_content += gen_magic() # NEW
if show_comparison: home_content += gen_comparison() # NEW
if show_inventory: home_content += gen_inventory()
if show_gallery: home_content += gen_about_section()
if show_testimonials: 
    t_cards = "".join([f'<div class="card reveal" style="text-align:center;"><i>"{x.split("|")[1]}"</i><br><br><b>- {x.split("|")[0]}</b></div>' for x in testi_data.split('\n') if "|" in x])
    home_content += f'<section style="background:rgba(0,0,0,0.02)"><div class="container"><div class="section-head reveal"><h2>Client Stories</h2></div><div class="grid-3">{t_cards}</div></div></section>'
if show_faq: home_content += gen_faq_section()
if show_audit: home_content += gen_audit_form() # NEW
if show_cta: home_content += f'<section style="background:var(--s); color:white; text-align:center;"><div class="container reveal"><h2>Ready to Start?</h2><p style="margin-bottom:2rem; color:white;">Let us build your future today.</p><a href="contact.html" class="btn" style="background:white; color:var(--s);">Get a Quote</a></div></section>'

# --- 7. RENDER & DEPLOY ---
st.divider()
st.subheader("🚀 Launchpad")

preview_mode = st.radio("Preview Page:", ["Home", "About", "Contact", "Privacy", "Terms", "Product Detail (Demo)"], horizontal=True)

# HELPER: Function to generate a header for inner pages
def gen_inner_header(title):
    return f"""
    <section class="hero" style="min-height: 40vh; background-image: linear-gradient(rgba(0,0,0,0.6), rgba(0,0,0,0.6)), url('{hero_img_1}'); background-size: cover; background-position: center;">
        <div class="container">
            <h1 style="font-size: 3.5rem; margin-bottom: 0;">{title}</h1>
        </div>
    </section>
    """

# GENERATE INNER PAGES
about_content = f"{gen_inner_header('About Us')}<section><div class='container'><div class='about-grid'><div class='legal-text'>{format_text(about_long)}</div><img src='{about_img}' style='width:100%; border-radius:12px; box-shadow:0 10px 30px rgba(0,0,0,0.1);'></div></div></section>"
contact_content = f"{gen_inner_header('Contact Us')}<section><div class='container'><div class='contact-layout'><div><div style='background:var(--card); padding:2rem; border-radius:12px; border:1px solid rgba(100,100,100,0.2);'><h3 style='color:var(--p);'>Get In Touch</h3><p style='margin-top:1rem; color:var(--txt);'><strong>📍 Address:</strong><br>{biz_addr}</p><p style='margin-top:1rem; color:var(--txt);'><strong>📞 Phone:</strong><br><a href='tel:{biz_phone}' style='color:var(--s);'>{biz_phone}</a></p><p style='margin-top:1rem; color:var(--txt);'><strong>📧 Email:</strong><br><a href='mailto:{biz_email}'>{biz_email}</a></p><br><a href='https://wa.me/{wa_num}' target='_blank' class='btn btn-accent' style='width:100%; text-align:center;'>Chat on WhatsApp</a></div></div><div class='card'><h3 style='margin-bottom:1.5rem;'>Send a Message</h3><form action='https://formsubmit.co/{biz_email}' method='POST'><div style='display:grid; grid-template-columns:1fr 1fr; gap:1rem;'><div><label>Name</label><input type='text' name='name' required></div><div><label>Email</label><input type='email' name='email' required></div></div><label>Message</label><textarea name='message' rows='5' required></textarea><button type='submit' class='btn btn-primary' style='width:100%;'>Send Message</button><input type='hidden' name='_captcha' value='false'><input type='hidden' name='_next' value='{prod_url}/contact.html'></form></div></div><br><br><div style='border-radius:12px; overflow:hidden; box-shadow:0 10px 30px rgba(0,0,0,0.1);'>{map_iframe}</div></div></section>"
privacy_content = f"{gen_inner_header('Privacy Policy')}<section><div class='container legal-text'>{format_text(priv_txt)}</div></section>"
terms_content = f"{gen_inner_header('Terms of Service')}<section><div class='container legal-text'>{format_text(term_txt)}</div></section>"

# PREVIEW LOGIC
def build_page(title, content, extra_js=""):
    css = get_theme_css()
    schema = gen_schema()
    return f"""<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>{title} | {biz_name}</title><meta name="description" content="{seo_d}">{schema}<style>{css}</style><link href="https://fonts.googleapis.com/css2?family={h_font.replace(' ', '+')}:wght@400;700;900&family={b_font.replace(' ', '+')}:wght@300;400;600&display=swap" rel="stylesheet"></head><body>{gen_nav()}{content}{gen_footer()}{gen_wa_widget()}{gen_scripts()}{extra_js}</body></html>"""

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

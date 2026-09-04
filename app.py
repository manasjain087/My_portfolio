import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Manas Jain | Portfolio",
    page_icon="💻",
    layout="wide",
)

# Remove Streamlit's default padding/chrome so the site fills the page
st.markdown(
    """
    <style>
        .block-container { padding: 0 !important; max-width: 100% !important; }
        header[data-testid="stHeader"] { display: none; }
        #MainMenu, footer { visibility: hidden; }
        iframe { width: 100% !important; }
    </style>
    """,
    unsafe_allow_html=True,
)

PORTFOLIO_HTML = """<!DOCTYPE html>
<html lang="en">

<head>
    <link rel="stylesheet"
href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.2/css/all.min.css">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Manas Jain | Portfolio</title>

    <style>
/* =========================================================
   MANAS JAIN — PORTFOLIO
   Palette:
     --bg-base     #0a0f1d  deep navy background
     --bg-panel    #101a2e  card / section panel base
     --accent      #38bdf8  sky blue (signals, links, highlights)
     --accent-warm #fbbf24  amber (stats, small emphasis)
     --text-main   #e6edf5  primary text
     --text-muted  #93a1b8  secondary text
   Type:
     Display / headings : Poppins (already linked in HTML)
     Body                : Inter
     Data / labels       : JetBrains Mono (stat numbers, tags)
========================================================= */

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@500;600&display=swap');

:root {
    --bg-base: #0a0f1d;
    --bg-panel: #101a2e;
    --bg-panel-light: #16223b;
    --accent: #38bdf8;
    --accent-warm: #fbbf24;
    --text-main: #e6edf5;
    --text-muted: #93a1b8;
    --border-soft: rgba(255, 255, 255, 0.08);
    --max-width: 1100px;
}

* {
    box-sizing: border-box;
}

html {
    scroll-behavior: smooth;
}

body {
    margin: 0;
    background: var(--bg-base);
    background-image:
        radial-gradient(circle at 15% 0%, rgba(56, 189, 248, 0.08), transparent 40%),
        radial-gradient(circle at 85% 20%, rgba(56, 189, 248, 0.05), transparent 35%);
    color: var(--text-main);
    font-family: 'Inter', sans-serif;
    line-height: 1.6;
    -webkit-font-smoothing: antialiased;
}

h1, h2, h3, h4 {
    font-family: 'Poppins', sans-serif;
    color: var(--text-main);
    margin: 0;
}

a {
    color: var(--accent);
}

img {
    max-width: 100%;
    display: block;
}

:focus-visible {
    outline: 2px solid var(--accent);
    outline-offset: 3px;
}

@media (prefers-reduced-motion: reduce) {
    * {
        animation: none !important;
        transition: none !important;
    }
}

/* =========================
   NAVBAR
========================= */

.navbar {
    position: sticky;
    top: 0;
    z-index: 100;
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 18px 8%;
    background: rgba(10, 15, 29, 0.75);
    backdrop-filter: blur(14px);
    -webkit-backdrop-filter: blur(14px);
    border-bottom: 1px solid var(--border-soft);
}

.navbar .logo {
    font-family: 'JetBrains Mono', monospace;
    font-weight: 600;
    font-size: 18px;
    color: var(--text-main);
    letter-spacing: 0.5px;
}

.navbar .logo::before {
    content: "</> ";
    color: var(--accent);
}

.nav-links {
    list-style: none;
    display: flex;
    gap: 32px;
    margin: 0;
    padding: 0;
}

.nav-links a {
    color: var(--text-muted);
    text-decoration: none;
    font-size: 15px;
    font-weight: 500;
    transition: color 0.2s ease;
}

.nav-links a:hover {
    color: var(--accent);
}

/* =========================
   HERO
========================= */

.hero {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 60px;
    padding: 100px 8% 80px;
    max-width: var(--max-width);
    margin: 0 auto;
}

.hero-content {
    flex: 1.2;
}

.hero-tag {
    font-family: 'JetBrains Mono', monospace;
    font-size: 13px;
    letter-spacing: 1px;
    text-transform: uppercase;
    color: var(--accent);
    background: rgba(56, 189, 248, 0.1);
    border: 1px solid rgba(56, 189, 248, 0.25);
    display: inline-block;
    padding: 6px 14px;
    border-radius: 999px;
    margin-bottom: 20px;
}

.hero h1 {
    font-size: 48px;
    font-weight: 600;
    line-height: 1.2;
    margin-bottom: 12px;
}

.hero h1 span {
    color: var(--accent);
}

.hero h2 {
    font-size: 20px;
    font-weight: 500;
    color: var(--text-muted);
    margin-bottom: 20px;
}

.hero-description {
    color: var(--text-muted);
    font-size: 16px;
    max-width: 560px;
    margin-bottom: 36px;
}

.hero-stats {
    display: flex;
    gap: 40px;
    margin-bottom: 36px;
}

.stat h3 {
    font-family: 'JetBrains Mono', monospace;
    color: var(--accent-warm);
    font-size: 28px;
    margin-bottom: 4px;
}

.stat p {
    color: var(--text-muted);
    font-size: 14px;
    margin: 0;
}

.buttons {
    display: flex;
    gap: 16px;
    flex-wrap: wrap;
}

.btn {
    display: inline-block;
    padding: 13px 28px;
    border-radius: 10px;
    font-weight: 600;
    font-size: 15px;
    text-decoration: none;
    transition: 0.25s ease;
}

.buttons .btn:not(.btn-secondary) {
    background: var(--accent);
    color: #06121f;
}

.buttons .btn:not(.btn-secondary):hover {
    background: #64d1ff;
    transform: translateY(-2px);
}

.btn-secondary {
    background: transparent;
    color: var(--text-main);
    border: 1px solid var(--border-soft);
}

.btn-secondary:hover {
    border-color: var(--accent);
    color: var(--accent);
    transform: translateY(-2px);
}

.hero-image {
    flex: 1;
    display: flex;
    justify-content: center;
}

.hero-image img {
    width: 320px;
    height: 320px;
    object-fit: cover;
    border-radius: 24px;
    border: 1px solid var(--border-soft);
    box-shadow: 0 20px 50px rgba(0, 0, 0, 0.4);
}

/* =========================
   GENERIC SECTION SHELL
========================= */

.section, #certifications, #contact {
    max-width: var(--max-width);
    margin: 0 auto;
    padding: 80px 8%;
}

.section h2, #certifications h2, #contact h2 {
    font-size: 34px;
    text-align: center;
    margin-bottom: 16px;
}

.section h2::after, #certifications h2::after, #contact h2::after {
    content: "";
    display: block;
    width: 56px;
    height: 3px;
    background: var(--accent);
    margin: 14px auto 0;
    border-radius: 2px;
}

.section-subtitle {
    text-align: center;
    color: var(--text-muted);
    max-width: 620px;
    margin: 0 auto 48px;
}

/* =========================
   ABOUT
========================= */

.about-content {
    max-width: 760px;
    margin: 48px auto 0;
    color: var(--text-muted);
    font-size: 16px;
}

.about-content p {
    margin-bottom: 18px;
}

/* =========================
   SKILLS
========================= */

.skills-container {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(140px, 1fr));
    gap: 20px;
    margin-top: 48px;
}

.skill {
    background: var(--bg-panel);
    border: 1px solid var(--border-soft);
    border-radius: 14px;
    padding: 26px 12px;
    text-align: center;
    transition: 0.25s ease;
}

.skill:hover {
    transform: translateY(-6px);
    border-color: var(--accent);
    box-shadow: 0 12px 24px rgba(56, 189, 248, 0.15);
}

.skill i {
    font-size: 28px;
    color: var(--accent);
    margin-bottom: 10px;
}

.skill span {
    display: block;
    font-size: 14px;
    font-weight: 500;
    color: var(--text-main);
}

/* =========================
   EXPERIENCE
========================= */

.card {
    background: var(--bg-panel);
    border: 1px solid var(--border-soft);
    border-radius: 16px;
    padding: 28px;
    margin: 0 auto 24px;
    max-width: 780px;
    transition: 0.25s ease;
}

.card:hover {
    border-color: var(--accent);
}

.experience-header {
    display: flex;
    align-items: center;
    gap: 18px;
    margin-bottom: 16px;
}

.company-logo {
    width: 56px;
    height: 56px;
    object-fit: contain;
    border-radius: 10px;
    background: #fff;
    padding: 6px;
}

.experience-header h3 {
    font-size: 18px;
    margin-bottom: 2px;
}

.experience-header h4 {
    font-size: 14px;
    font-weight: 500;
    color: var(--accent);
    margin-bottom: 4px;
}

.duration {
    font-family: 'JetBrains Mono', monospace;
    font-size: 12px;
    color: var(--text-muted);
    margin: 0;
}

.card > p {
    color: var(--text-muted);
    font-size: 15px;
    margin: 0;
}

/* =========================
   CERTIFICATIONS
========================= */

.certification-container {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(230px, 1fr));
    gap: 24px;
    margin-top: 48px;
}

.certificate-card {
    background: var(--bg-panel);
    border: 1px solid var(--border-soft);
    border-radius: 16px;
    padding: 28px 20px;
    text-align: center;
    transition: 0.25s ease;
}

.certificate-card:hover {
    transform: translateY(-6px);
    border-color: var(--accent);
    box-shadow: 0 12px 24px rgba(56, 189, 248, 0.15);
}

.certificate-card i {
    font-size: 30px;
    color: var(--accent);
    margin-bottom: 12px;
}

.certificate-logo {
    width: 48px;
    height: 48px;
    object-fit: contain;
    margin: 0 auto 12px;
    background: #fff;
    border-radius: 8px;
    padding: 6px;
}

.certificate-card h3 {
    font-size: 16px;
    margin-bottom: 6px;
}

.certificate-card p {
    color: var(--text-muted);
    font-size: 14px;
    margin: 0 0 4px;
}

.certificate-card span {
    display: block;
    font-family: 'JetBrains Mono', monospace;
    font-size: 12px;
    color: var(--accent-warm);
    margin-bottom: 16px;
}

.certificate-card .btn,
.cert-btn {
    background: transparent;
    border: 1px solid var(--border-soft);
    color: var(--text-main);
    padding: 9px 18px;
    border-radius: 8px;
    font-size: 13px;
    font-weight: 600;
    cursor: pointer;
    text-decoration: none;
    display: inline-block;
    transition: 0.2s ease;
}

.certificate-card .btn:hover,
.cert-btn:hover {
    border-color: var(--accent);
    color: var(--accent);
}

/* =========================
   CONTACT
========================= */

.contact-container {
    display: flex;
    justify-content: center;
    flex-wrap: wrap;
    gap: 20px;
    margin-top: 40px;
}

.contact-item {
    display: flex;
    align-items: center;
    gap: 10px;
    background: var(--bg-panel);
    border: 1px solid var(--border-soft);
    padding: 14px 24px;
    border-radius: 12px;
    text-decoration: none;
    color: var(--text-main);
    font-weight: 500;
    transition: 0.25s ease;
}

.contact-item i {
    color: var(--accent);
    font-size: 18px;
}

.contact-item:hover {
    border-color: var(--accent);
    transform: translateY(-3px);
}

/* =========================
   FOOTER
========================= */

footer {
    text-align: center;
    padding: 28px 8%;
    border-top: 1px solid var(--border-soft);
    color: var(--text-muted);
    font-size: 14px;
}

/* =========================================================
   PROJECT SECTION (existing — kept, lightly integrated)
========================================================= */

#projects {
    padding: 80px 8%;
    text-align: center;
    background: transparent;
    max-width: var(--max-width);
    margin: 0 auto;
}

#projects h2 {
    font-size: 34px;
    margin-bottom: 16px;
    color: var(--text-main);
}

#projects h2::after {
    content: "";
    display: block;
    width: 56px;
    height: 3px;
    background: var(--accent);
    margin: 14px auto 48px;
    border-radius: 2px;
}

.projects-container {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 30px;
}

.project-link {
    text-decoration: none;
    color: inherit;
    display: block;
}

.project-card {
    background: rgba(255, 255, 255, 0.05);
    backdrop-filter: blur(12px);
    -webkit-backdrop-filter: blur(12px);

    border: 1px solid var(--border-soft);

    padding: 20px;
    border-radius: 20px;

    min-height: 400px;

    box-shadow: 0 5px 20px rgba(0, 0, 0, 0.25);

    transition: 0.3s ease;
    text-align: left;
}

.project-card:hover {
    transform: translateY(-10px);
    border-color: var(--accent);

    box-shadow:
        0 10px 30px rgba(56, 189, 248, 0.25);
}

.project-card img {
    width: 100%;
    height: 190px;
    object-fit: cover;
    border-radius: 10px;
    margin-bottom: 15px;
}

.project-card h3 {
    color: var(--accent);
    font-size: 21px;
    margin: 10px 0;
}

.project-card p {
    color: var(--text-muted);
    font-size: 14.5px;
}

/* Project Buttons / Links */

.project-card a {
    color: var(--accent);
    text-decoration: none;
    font-weight: 600;
}

/* ================================
   MOBILE
================================ */

@media (max-width: 900px) {
    .hero {
        flex-direction: column-reverse;
        text-align: center;
        padding-top: 60px;
    }

    .hero-description {
        margin-left: auto;
        margin-right: auto;
    }

    .hero-stats {
        justify-content: center;
    }

    .buttons {
        justify-content: center;
    }

    .hero-image img {
        width: 220px;
        height: 220px;
    }
}

@media (max-width: 768px) {

    .navbar {
        flex-direction: column;
        gap: 14px;
        padding: 16px 6%;
    }

    .nav-links {
        gap: 18px;
        flex-wrap: wrap;
        justify-content: center;
    }

    #projects {
        padding: 60px 5%;
    }

    .projects-container {
        grid-template-columns: 1fr;
    }

    .project-card {
        min-height: auto;
    }

    .section, #certifications, #contact {
        padding: 60px 5%;
    }
}
</style>

    <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap"
        rel="stylesheet">
</head>

<body>

    <!-- Navbar -->
    <nav class="navbar">
        <div class="logo">Manas Jain</div>

        <ul class="nav-links">
            <li><a href="#home">Home</a></li>
            <li><a href="#about">About</a></li>
            <li><a href="#skills">Skills</a></li>
            <li><a href="#experience">Experience</a></li>
            <li><a href="#projects">Projects</a></li>
            <li><a href="#contact">Contact</a></li>
        </ul>
    </nav>

    <section id="home" class="hero">

    <div class="hero-content">

        <p class="hero-tag">
            Final Year B.Tech Computer Science Student
        </p>

        <h1>
            Hi, I'm <span>Manas Jain</span>
        </h1>

        <h2>
            Data Science Intern | Machine Learning Engineer | AWS Cloud Enthusiast
        </h2>

        <p class="hero-description">
            Passionate about transforming data into actionable insights and building
            intelligent solutions through Machine Learning, Data Science, and Cloud Technologies.
            Experienced in developing data-driven applications, exploring AWS services,
            and solving complex problems using Data Structures & Algorithms.
            Currently focused on creating scalable solutions, continuously learning emerging
            technologies, and contributing to impactful real-world projects.
        </p>

        <div class="hero-stats">

            <div class="stat">
                <h3>2+</h3>
                <p>Internships</p>
            </div>

            <div class="stat">
                <h3>10+</h3>
                <p>Projects Built</p>
            </div>

            <div class="stat">
                <h3>500+</h3>
                <p>DSA Problems</p>
            </div>

        </div>

        <div class="buttons">
            <a href="#projects" class="btn">View Projects</a>

            <a href="Manas_Jain_Resume.pdf"
               download
               class="btn btn-secondary">
                Download Resume
            </a>
        </div>

    </div>

    <div class="hero-image">
        <img src="images/profile.jpeg" alt="Manas Jain">
    </div>

 <!-- About section -->

</section>

  <section id="about" class="section">

    <h2>About Me</h2>

    <div class="about-content">

        <p>
            My journey into Computer Science began with curiosity rather than expertise. After completing my 12th grade, I chose to pursue a Bachelor's degree in Computer Science, inspired by my family's engineering background. What started as a career choice soon evolved into a genuine passion for technology and innovation.
        </p>

        <p>
            Throughout my B.Tech journey, I discovered a deep interest in programming, software development, cloud computing, machine learning, and data science. Every new concept felt like an opportunity to explore something exciting, and learning gradually became more than an academic requirement—it became a hobby and a way of life.
        </p>

        <p>
            My curiosity led me to work on real-world projects, solve coding challenges, and gain hands-on experience through internships in Data Science and AWS Machine Learning. These experiences strengthened my technical foundation while helping me understand how technology can be used to solve practical business problems and create meaningful impact.
        </p>

        <p>
            Beyond academics, I have actively participated in college events, extracurricular activities, and sports. These experiences have helped me develop leadership, teamwork, communication, and problem-solving skills while creating memorable experiences throughout my college life.
        </p>

        <p>
            Today, as a final-year Computer Science student, I am passionate about leveraging Data Science, Machine Learning, AWS Cloud Technologies, and Software Development to build scalable and impactful solutions. I am continuously learning, exploring emerging technologies, and preparing myself to contribute effectively in a professional environment while growing both personally and technically.
        </p>

    </div>

</section>

    <!-- Skills -->
   <section id="skills" class="section">

    <h2>Technical Skills</h2>

    <div class="skills-container">

        <div class="skill">
            <i class="fa-brands fa-python"></i>
            <span>Python</span>
        </div>

        <div class="skill">
            <i class="fa-solid fa-brain"></i>
            <span>Machine Learning</span>
        </div>

        <div class="skill">
            <i class="fa-solid fa-chart-line"></i>
            <span>Data Science</span>
        </div>

        <div class="skill">
            <i class="fa-brands fa-aws"></i>
            <span>AWS</span>
        </div>

        <div class="skill">
            <i class="fa-solid fa-database"></i>
            <span>SQL</span>
        </div>

        <div class="skill">
            <i class="fa-solid fa-server"></i>
            <span>Flask</span>
        </div>

        <div class="skill">
            <i class="fa-brands fa-git-alt"></i>
            <span>Git</span>
        </div>

        <div class="skill">
            <i class="fa-brands fa-github"></i>
            <span>GitHub</span>
        </div>

        <div class="skill">
            <i class="fa-solid fa-code"></i>
            <span>DSA</span>
        </div>

        <div class="skill">
            <i class="fa-solid fa-table"></i>
            <span>Pandas</span>
        </div>

        <div class="skill">
            <i class="fa-solid fa-calculator"></i>
            <span>NumPy</span>
        </div>

        <div class="skill">
            <i class="fa-solid fa-robot"></i>
            <span>Scikit-Learn</span>
        </div>

    </div>

</section>

    <!-- Experience -->
<section id="experience" class="section">

    <h2>Experience</h2>

    <!-- AWS Machine Learning Internship -->

    <div class="card">

        <div class="experience-header">
            <img src="images/grras_solutions_p_ltd_logo.jpg"
                 alt="Grras Solutions Logo"
                 class="company-logo">

            <div>
                <h3>AWS Machine Learning Intern</h3>
                <h4>Grras Solutions Private Limited</h4>
                <p class="duration">May 2026 - Present</p>
            </div>
        </div>

        <p>
            Working on Machine Learning models, data preprocessing,
            feature engineering, model evaluation, and deployment.
            Leveraging AWS cloud services to build scalable machine
            learning solutions while gaining hands-on experience with
            real-world datasets and cloud-based workflows.
        </p>

    </div>

    <!-- Data Science Internship -->

    <div class="card">

        <div class="experience-header">
            <img src="images/clover_it_services_pvt_ltd__logo.jpg"
                 alt="Clover IT Services Logo"
                 class="company-logo">

            <div>
                <h3>Data Science Intern</h3>
                <h4>Clover IT Services Pvt. Ltd.</h4>
                <p class="duration">June 2025 - July 2025</p>
            </div>
        </div>

        <p>
            Worked on data cleaning, preprocessing, exploratory data
            analysis (EDA), data visualization, and predictive modeling.
            Utilized Python, Pandas, NumPy, Matplotlib, and Scikit-learn
            to analyze datasets and generate actionable insights for
            data-driven decision making.
        </p>

    </div>

</section>

    

    <!-- Projects -->

  <!-- Projects Section -->
<section id="projects">
    <h2>My Projects</h2>

    <div class="projects-container">

        <!-- Project 1 -->
        <a href="https://manasjain087-customers-segmentation-using-kmeans-app-2hscmu.streamlit.app/"
           target="_blank"
           rel="noopener noreferrer"
           class="project-link">

            <div class="project-card">

                <img src="images/customer_segmentation.png"
                     alt="Customer Segmentation">

                <h3>📊 Customer Segmentation </h3>

                <p>
                    Developed an end-to-end customer segmentation system using RFM analysis on an online retail transaction dataset.
                     Performed data cleaning, feature engineering, scaling, optimal cluster selection using Elbow and Silhouette methods,
                    and K-Means clustering to identify customer segments. Built an interactive Streamlit dashboard for customer analysis, segment visualization, and customer-level insights.
                </p>

            </div>

        </a>




        <!-- Project 2 -->
        <a href="https://manasjain087-house-price-prediction-app-pgkvgf.streamlit.app/"
           target="_blank"
           rel="noopener noreferrer"
           class="project-link">

            <div class="project-card">

                <img src="images/House_Price.jpg"
                     alt="House Price Prediction">

                <h3>🏠 House Price Prediction</h3>

                <p>
                    Developed a Machine Learning regression model to
                    predict house prices using Python and Scikit-learn.
                    Implemented data preprocessing, exploratory data
                    analysis, feature engineering and model evaluation.
                </p>

            </div>

        </a>



        



        <!-- Project 3 -->
        <a href="https://movierecommendation-g3s2pdwz2x3rf4yappixmj4.streamlit.app/"
           target="_blank"
           rel="noopener noreferrer"
           class="project-link">

            <div class="project-card">

                <img src="images/Movie_recomm_system.jpeg"
                     alt="Movie Recommendation System">

                <h3>🎬 Movie Recommendation System</h3>

                <p>
                    Developed a Movie Recommendation System using
                    Python, Pandas, NumPy and Scikit-learn to recommend
                    movies based on similarity between movie features.
                    Deployed the application using Streamlit.
                </p>

            </div>

        </a>


        <!-- Project 4 -->
        <a href="https://manasjain087.github.io/Live_Cricket_Dashboard/"
           target="_blank"
           rel="noopener noreferrer"
           class="project-link">

            <div class="project-card">

                <img src="images/Live_dashboard.jpeg"
                     alt="Live Cricket Dashboard">

                <h3>🏏 Live Cricket Score Dashboard</h3>

                <p>
                    Developed a real-time cricket dashboard using
                    Cricket APIs, HTML, CSS, JavaScript and Python.
                    The application displays live scores, match status,
                    team information and dynamic cricket updates.
                </p>

            </div>

        </a>

        <!-- Project 5 -->

        <a href="https://manasjain087-email-spam-detection-app-xdgqzg.streamlit.app/"
           target="_blank"
           rel="noopener noreferrer"
           class="project-link">

            <div class="project-card">

                <img src="images/Email_Spam_Detection.png"
                     alt="Email Spam Detection">

                <h3>🏏 Email Spam Detection</h3>

                <p>
                    Email Spam Detection is a Machine Learning + Natural Language Processing (NLP) project,
                     that automatically classifies a message as either Spam or Ham (Not Spam).
                </p>

            </div>

        </a>

        <!-- Project 6 -->

         <a href="https://manasjain087-animal-health-symptom-to-urgency-triage-app-u6zp1o.streamlit.app/"
           target="_blank"
           rel="noopener noreferrer"
           class="project-link">

            <div class="project-card">

                <img src="images/Animal-Health-Symptoms-Urgency.jpg"
                     alt="Animal-Health-Symptoms-Urgency">

                <h3>📊 Animal-Health-Symptoms-Urgency-Classifier </h3>

                <p>
                    A small machine learning project that predicts how urgently an animal needs veterinary care based on reported symptoms
                     — Low, Medium, or Emergency — similar in spirit to the kind of triage logic behind conversational animal health assistants
                      (e.g. teletriage tools for farmers, pet parents, and poultry owners).
                </p>

            </div>

        </a>





    </div>

</section>

    <!-- certification -->

    </section>

    <section id="certifications" class="section">

    <h2>Certifications</h2>

    <p class="section-subtitle">
        Professional certifications and training programs completed to strengthen my expertise in Cloud Computing, Data Science, and Machine Learning.
    </p>

    <div class="certification-container">

        <div class="certificate-card">
    <i class="fa-brands fa-aws"></i>
    <h3>AWS Machine Learning Internship</h3>
    <p>Grras Solutions Pvt. Ltd.</p>
    <span>2026</span>

    <button class="cert-btn">View Certificate</button>
</div>
      <div class="certificate-card">
    <i class="fa-brands fa-aws"></i>
    <h3>Data Science Internship</h3>
    <p>Grras Solutions Pvt. Ltd.</p>
    <span>2026</span>

    <a href="Certificates/Manas Jain Internship Certificate_CloverIT Services (2) (1).pdf"
       target="_blank"
       class="btn">
       View Certificate
    </a>
</div>

       <div class="certificate-card">

    <img src="images/nptel_logo.jpg"
         alt="NPTEL Logo"
         class="certificate-logo">

    <h3>NPTEL Certificate</h3>
    <p>Data Analytics with Python</p>
    <span>2026</span>

    <a href="Certificates/NPTEL_data_analytics_with_python.pdf"
       target="_blank"
       class="btn">
       View Certificate
    </a>

</div>

        <div class="certificate-card">
            <i class="fa-solid fa-brain"></i>
            <h3>Machine Learning Certification</h3>
            <p>Machine Learning Fundamentals</p>
            <span>2026</span>

            <a href="Certificates/The_Ultimate_Job_Ready_Data_Science_Course_Certificate.pdf"
       target="_blank"
       class="btn">
       View Certificate
    </a>
        </div>

    </div>

</section>

    <!-- Contact -->
    <section id="contact">

    <h2>Contact Me</h2>

    <div class="contact-container">

        <a href="mailto:manasjain0704@gmail.com" class="contact-item">
            <i class="fa-solid fa-envelope"></i>
            <span>manasjain0704@gmail.com</span>
        </a>

        <a href="https://github.com/manasjain087" target="_blank" class="contact-item">
            <i class="fa-brands fa-github"></i>
            <span>GitHub</span>
        </a>

        <a href="https://www.linkedin.com/in/manasjain0704/" target="_blank" class="contact-item">
            <i class="fa-brands fa-linkedin"></i>
            <span>LinkedIn</span>
        </a>

    </div>

</section>
    <!-- Footer -->
    <footer>

        <p>
            © 2026 Manas Jain. All Rights Reserved.
        </p>

    </footer>

<script>
function searchSection() {

    let input = document
        .getElementById("searchInput")
        .value
        .toLowerCase();

    let section = document.getElementById(input);

    if(section){
        section.scrollIntoView({
            behavior: "smooth"
        });
    }
    else{
        alert("Section not found!");
    }
}
</script></body>

</html>
"""

components.html(PORTFOLIO_HTML, height=4200, scrolling=True)

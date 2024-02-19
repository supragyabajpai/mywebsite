import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image

st.set_page_config(page_title="Supragya Bajpai", layout="wide")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

# ---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
img_transpo = Image.open("images\TranspoLogo_1.jpg")
img_lottie_animation = Image.open("images\playlist_1.jpg")


# ---- HEADER SECTION ----
with st.container():
    st.subheader("Hi, I am Supragya Bajpai :wave:")
    st.title("A curious problem-solver, always eager to learn.")
    st.write(
        "A Master's student specializing in business analytics with over two years of practical experience, holding the position of Senior Analyst at Capgemini. Additionally, has gained valuable entrepreneurial experience by successfully running a startup called TRANSPO for a year and a half, achieving exceptional return on investment. Possesses a deep passion for utilizing problem-solving abilities and recognizing patterns to effectively contribute to the growth and prosperity of businesses."
    )
    st.write("[Read my blogs >](https://medium.com/@supragya.vajpai)")

# ---- WHAT I DO ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
            """
            My journey is fueled by a diverse range of passions:
            - Problem Solving: Embracing challenges and finding innovative solutions.
            - Artificial Intelligence: Exploring the realms of intelligent systems.
            - Human-Machine Interaction: Navigating the intersection of technology and human experience.
            - Digitalization: Harnessing the power of technology for transformative change.
            - Strategy Building: Crafting effective plans for success.
            - Business Analysis: Analyzing data to derive meaningful insights.

            You can contact me on LinkedIn or via email (details below). I am always open to new opportunities.
            """
        )
        st.write("[LinkedIn >](https://www.linkedin.com/in/supragya-bajpai/)")
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")

# ---- PROJECTS ----
with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((0.75, 2))
    with image_column:
        st.image(img_lottie_animation,width=250)
    with text_column:
        st.subheader("Playlist Recommendation")
        st.write(
            """
            Role: Developer

            Description: Predict if a song is going to be popular or not, Generate a playlist based on a song the listener likes.

            Skills Developed:

            Data Analysis, Feature Engineering, Model Development, Model Evaluation, Data Visualization, Hyperparameter Tuning, Machine Learning Algorithms

            """
        )
        st.markdown("[Read in detail...](https://github.com/supragyabajpai/Playlist_Recommendation)")

st.write("  ")
st.write("  ")
st.write("  ")

with st.container():
    text_column,image_column = st.columns((2, 1))
    with text_column:
        st.subheader("TRANSPO")
        st.write(
        """
        Role: Founder | COO

        Description: TRANSPO emerged as a company aimed at resolving transportation hurdles for Manipal University Jaipur students in a remote location. Our mobile app connected students with local drivers, providing a regional alternative to mainstream ride-sharing services. The project progressed from pre-launch market analysis to post-launch success, achieving recognition and profitability. Throughout this entrepreneurial journey, I gained insights into market research, collaboration with local stakeholders, app development, and team management. Valuable lessons were learned in addressing user feedback, strategic expansions, and navigating market dynamics. The transformation from a two-person team to a recognized company highlighted the critical importance of adaptability, customer-centricity, and effective team collaboration in the entrepreneurial landscape.

        Skills Developed:

        Market Research, Collaboration and Stakeholder Management, App Development, Team Management, Customer Feedback and Service Improvement, Strategic Expansions, Adaptability, Entrepreneurial Mindset, Communication Skills, Data Science and Analysis, Risk Management
        """
         )
    st.markdown("[Read in detail......](https://github.com/supragyabajpai/TRANSPO)")
    with image_column:
        st.image(img_transpo)



# --- More Projects ---#
with st.container():
    st.write("---")
    st.markdown("[Click here to check out my GitHub repository for more projects](https://github.com/supragyabajpai/Portfolio)")

# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

    contact_form = """
    <form action="https://formsubmit.co/supragya.vajpai@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()


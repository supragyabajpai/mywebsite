import requests
import streamlit as st
from PIL import Image
from streamlit_lottie import st_lottie

st.set_page_config(page_title="Supragya Bajpai", layout="wide", page_icon=":file_cabinet:")

# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")



# Load static assets
lottie_coding = requests.get("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json").json()
img_transpo = Image.open("images/TranspoLogo_1.jpg")
img_lottie_animation = Image.open("images/playlist_1.jpg")
img_lottie_animation2 = Image.open("images/ARWhiz_screenshot.jpg")


# ---- HEADER SECTION ----
with st.container():
    st.subheader("Hi, I am Supragya Bajpai :wave:")
    st.title("A curious problem-solver, always eager to learn.")
    st.write(
        "A Master's student specializing in business analytics with over two years of practical experience, holding the position of Senior Analyst at Capgemini. Additionally, has gained valuable entrepreneurial experience by successfully running a startup called TRANSPO for a year and a half, achieving exceptional return on investment. Possesses a deep passion for utilizing problem-solving abilities and recognizing patterns to effectively contribute to the growth and prosperity of businesses."
    )
    st.write("[Read my blogs >](https://medium.com/@supragya.vajpai)")

# ---- WHAT I DO ----
with st.expander(label="What I do"):
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        #st.header("What I do")
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
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_lottie_animation2, width=400)
    with text_column:
        st.subheader("AR_Whiz")
        st.write(
            """
            Role: Developer

            Description: After banks release their Annual Review documents, they often compare their strategies with those of other banks. Currently, if they use any LLM model to analyze, they might hallucinate. But by using a RAG model, we can make sure that the insights come directly from the documents, avoiding mistakes.

            Also, there are many rules about compliance from organizations like the Bank for International Settlements (BIS) and the Office of the Superintendent of Financial Institutions (OFSI). By checking their current approach against these new rules quickly, banks can save a lot of time and effort to make sure they follow the rules.

            Skills Developed:

            Genrative AI, RAG modelling, Risk Analysis, Embedding
            """
        )
        st.markdown("[Watch Video...](https://youtu.be/-hGAPAkxZ88)")
        st.markdown("")

with st.container():
    st.write("---")
    image_column, text_column = st.columns((0.6, 2))
    with image_column:
        st.image(img_lottie_animation, width=250)
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
        st.markdown("[Check out the app...](https://sb-playlist.onrender.com)")

with st.container():
    st.write("---")
    text_column, image_column = st.columns((2, 1))
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
    st.write("---")

with st.expander(label="More Projects"):
    st.write("---")
    st.markdown("[GitHub repository](https://github.com/supragyabajpai/Portfolio)")

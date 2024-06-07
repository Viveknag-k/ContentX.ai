import streamlit as st
import os

from PIL import Image
from langchain.chains import LLMChain
#from langchain.utilities import WikipediaAPIWrapper 
from langchain.prompts import PromptTemplate


from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper
wiki = WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper())
img=Image.open("src/images/Page_Icon.png")

st.set_page_config(page_title="ContentX.ai: Generate content with Gemini",page_icon=img)
st.title('ContentX:violet[.]ai')
st.caption("🚀 Effortless Creativity powered by Gemini")

tab1,tab2,tab3=st.tabs(['Home','Get Started','About us'])

with st.sidebar:
    st.subheader("How to use")
    st.markdown("""<span ><font size=2>1. Start by entering your Google API key.</font></span>""",unsafe_allow_html=True)
    st.markdown("""<span ><font size=2>2. Now start generating content for your topic with :violet[ContentX.ai]</font></span>""",unsafe_allow_html=True)
    google_api_key = st.text_input("Google API Key", key="chatbot_api_key", type="password")
    "[Get an Google API key](https://makersuite.google.com/app/apikey)"
    
    
    st.divider()
    st.markdown("""<span ><font size=2>Lets Connect!</font></span>""",unsafe_allow_html=True)
    "[Linkedin](https://www.linkedin.com/in/vivek-nag-kanuri-648901228/)" "  \n"  "[GitHub](https://github.com/Viveknag-k)" "\n[Tableau Public](https://public.tableau.com/app/profile/kanuri.vivek.nag/vizzes)"
    st.markdown("---")
    img1=Image.open("src/images/s1.png")
    st.image(img1,use_column_width=True,width=400)
    st.link_button("🔗 Source Code", "https://github.com/SSK-14/WizSearch", use_container_width=True)


with tab1:
    st.write("""ContentX:violet[.]ai is an AI-powered content creation tool that can help you level up your YouTube channel.\n\nWith :violet[ContentX.ai], you can generate high-quality content in minutes, including titles, descriptions and scripts.Whether you\'re a beginner or a seasoned YouTuber, ContentX.ai can help you take your channel to the next level.""")
    img=Image.open("src/images/cont2.jpg")
    st.image(img,use_column_width=True,width=400)
    st.write('If you\'re looking for a way to create engaging and informative YouTube videos quickly and easily, then ContentX.ai is the perfect tool for you. :violet[Sign up] for a free trial today and see how ContentX:violet[.]ai can help you grow your channel.')
    
    st.write('Here are some of the benefits of using ContentX:violet[.]ai:')
    
    st.success('''

 :violet[Save time and effort]: ContentX.ai can help you generate content quickly and easily, so you can focus on other aspects of your YouTube channel.

:violet[Improve your content quality]: ContentX.ai uses AI to understand your audience and create content that is both engaging and informative.

:violet[Stand out from the competition]: ContentX.ai can help you create unique and original content that will help you stand out from the competition.

''')
    
    
    
    
with tab2:
    st.image("https://t4.ftcdn.net//jpg/06/28/92/31/360_F_628923101_7kRxzUAnUMd6EHR9m2M5ymqkEdo7aKE8.jpg")
    title_template = PromptTemplate(
        input_variables = ['topic'], 
        template='write me a youtube video title about {topic}'
    )
    script_template = PromptTemplate(
        input_variables = ['title','wikipedia_research'], 
        template='write me a youtube video script based on this title: {title} while leveraging this wikipedia research {wikipedia_research}'
        
    )
    description_template=PromptTemplate(
        input_variables=['script'],
        template='Write me a description for youtube video in three lines based on this content:{script}'
    )
    hashtags_template=PromptTemplate(
        input_variables=['script'],
        template='write me five best hashtags for youtube video based on this content:{script}'
    )
    thumbnail_tempalte=PromptTemplate(
        input_variables=['title'],
        template='write me an eye-catching text on thumbnail for youtube video on this title: {title}'
    )
    
    if google_api_key:
        os.environ['GOOGLE_API_KEY']=google_api_key
        llm = ChatGoogleGenerativeAI(model="gemini-pro")
    
        title_chain = LLMChain(llm=llm, prompt=title_template, verbose=True, output_key='title')
        script_chain = LLMChain(llm=llm, prompt=script_template, verbose=True, output_key='script')
        description_chain = LLMChain(llm=llm, prompt=description_template, verbose=True, output_key='description')
        hashtags_chain = LLMChain(llm=llm, prompt=hashtags_template, verbose=True, output_key='hashtags')
        thumbnail_chain = LLMChain(llm=llm, prompt=thumbnail_tempalte, verbose=True, output_key='thumbnail')

        
    
    if prompt := st.text_input("Enter a prompt here "):
            if not google_api_key:
                st.info("🗝️Please add your Google API key to continue.")
                st.stop()
             
            title = title_chain.run(prompt)
            wiki_research = wiki.run(prompt)

            script = script_chain.run(title=title, wikipedia_research=wiki_research)
            description = description_chain.run(script=script)
            hashtags=hashtags_chain.run(script=script)
            thumbnail=thumbnail_chain.run(title)
            with st.expander('Title'):
                st.info(title)
            with st.expander('Script'):
                st.info(script)
            with st.expander('Description'):
                st.info(description)
            with st.expander('Hashtags'):
                st.info(hashtags)
            with st.expander('Thumbnail'):
                st.info(thumbnail)
            with st.expander('Wikipedia Research'): 
                st.info(wiki_research)
                
                
with tab3:
    st.title("What is ContentX:violet[.]ai?")
    st.write("ContentX.ai is a cutting-edge tool designed to streamline and enhance content creation for YouTube. It offers an all-in-one solution for generating engaging titles, detailed descriptions, compelling scripts, and eye-catching thumbnails, ensuring your videos stand out in a crowded marketplace. With advanced algorithms and user-friendly interfaces, ContentX.ai simplifies the creative process, saving time and maximizing productivity. Whether you're a seasoned creator or a newcomer to the platform, this tool helps you craft professional-quality content with ease. Additionally, ContentX.ai optimizes your video hashtags, boosting visibility and audience engagement. Transform your YouTube channel with ContentX.ai and elevate your content to new heights.")
    
    st.write("\n\n\n")
    col1,col2=st.columns(2)
    img2=Image.open("src/images/st6.jpg")
    with col1:
        st.write("At ContentX.ai, we understand the challenges of producing high-quality content consistently. That's why we've harnessed advanced algorithms and crafted a user-friendly interface to simplify the creative process, save time, and maximize productivity. Whether you're a seasoned creator or a newcomer to the platform, our tool is designed to help you craft professional-quality content with ease.",use_column_width=True)
    with col2:
            st.image(img2,use_column_width=True)
            
    st.title("Boost Your Visibility")
    st.write("ContentX.ai doesn't stop at content creation. Our tool also optimizes your video hashtags, boosting your video's visibility and audience engagement. By leveraging our platform, you can ensure that your content reaches a wider audience and achieves greater impact.")
    st.title("Transform Your Channel")
    st.write("\n\n\n")
    col3,col4=st.columns(2)
    img3=Image.open("src/images/st7.jpg")
    with col3:
        st.image(img3,use_column_width=True)
    with col4:
        st.write("""Join the growing community of creators who have transformed their YouTube channels with ContentX.ai. Elevate your content to new heights and experience the difference that a streamlined, efficient, and innovative content creation process can make.""")
        
    st.write("Ready to take your YouTube channel to the next level? Start using :violet[ContentX.ai] today and see how easy and effective content creation can be.")

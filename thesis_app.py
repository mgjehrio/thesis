import streamlit as st
import base64


st.set_page_config(page_title="Matthew Jehrio Poster App")




state = st.sidebar.selectbox('Page', ['Poster', 'Paper', 'Presentation'])


def st_display_pdf(pdf_file):
    with open(pdf_file, "rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="800" height="800" type="application/pdf"></iframe>'
    st.markdown(pdf_display, unsafe_allow_html=True)



    
if state == "Presentation":
    
    presentation_page_number = st.number_input('Page Number', 1, 40)
    presentation_string = "Thesis_Presentation_git1024_" + str(presentation_page_number) + ".jpg"
    st.image(presentation_string)
    
    
if state == "Poster":
       
        st.image('old_format_poster.jpg')
        
elif state == "Paper":
    paper_page_number = st.number_input('Page Number', 1, 40)
    paper_string = "thesis_git1024_" + str(paper_page_number) + ".jpg"
    st.image(paper_string)

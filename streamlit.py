import torch
import streamlit as st
import pytorch_lightning
import transformers
import datasets
import wandb

#model = torch.load(PATH)
#model.eval()

def predict(name, skills, exp, job):
        prediction = model.predict(name, skills, exp, job)
        return prediction

st.title('Génération de lettre de motivation')
st.image("""https://rodriguedemeuse.be/wp-content/uploads/2022/02/image-from-rawpixel-id-3285747-jpeg-1024x684-1.jpg""")
st.header('Entrez les informations requises')
name = st.text_input('Name : ex Nicholas McGregor')
skills = st.text_input('Skills: ex excellent customer service skills and am familiar with SQL')
exp = st.text_input('Experiences : ex Wrote numerous unit and API tests')
job = st.text_input('Job: ex Full Stack Developper')

if st.button('Génération'):
        lettre = predict(name, skills, exp, job)
        st.success(lettre)                                

import streamlit as st
from transformers import T5ForConditionalGeneration, T5Tokenizer

tokenizer = T5Tokenizer.from_pretrained('t5-small')
model_test = T5ForConditionalGeneration.from_pretrained('.')


def inference(row, model):
    inputs = ['Writte cover letter with this information: name: ' + row['name'] + ', skill: ' + row['skills'] + ', experience: ' + row['exp'] + ', job: ' + row['job']]
    inputs_ids = tokenizer(inputs, max_length=256, truncation=True, return_tensors='pt').input_ids
    print('hello')
    outputs = model.generate(inputs_ids, num_beams=8, do_sample=True, min_length=512, max_new_tokens=2048)
    print("xx")
    return tokenizer.decode(outputs[0], skip_special_tokens=True)


st.title('Génération de lettre de motivation')
st.image("""https://rodriguedemeuse.be/wp-content/uploads/2022/02/image-from-rawpixel-id-3285747-jpeg-1024x684-1.jpg""")
st.header('Entrez vos informations requises')
name = st.text_input("Votre nom :")
skills = st.text_input('Vos compétences: ')
exp = st.text_input('Vos Expériences ')
job = st.text_input("L'intitulé de poste:")

payload = {'name': name, 'skills': skills, 'exp': exp, 'job': job}

if st.button('Générer la Lettre de motivation'):
    with st.spinner('Wait for it...'):
        output = inference(payload, model_test)
        print("here")

    st.text_area('Your Cover letter', output)
    st.success('Done!')

import torch
import streamlit as st
#import pytorch-lightning
#import transformers
#import datasets
#import wandb

#model = torch.load(PATH)
#model.eval()

def predict(entree_fonction):
	liste_entree = entree_fonction.split(";")
	#prediction = model.predict(liste_entree)
	#return prediction

st.title('Génération de lettre de motivation')
st.image("""https://rodriguedemeuse.be/wp-content/uploads/2022/02/image-from-rawpixel-id-3285747-jpeg-1024x684-1.jpg""")
st.header('Entrez les informations requises')
entree = st.text_input('Paramètre')

if st.button('Génération'):
	#lettre = predict(entree)
	st.success(lettre)
	#st.write('hello')

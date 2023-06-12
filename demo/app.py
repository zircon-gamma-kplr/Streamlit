import streamlit as st
import numpy as np
import time
import datetime

# Titre
st.title("Mon application Streamlit avec Markdown")
st.subheader("Example d'utilisation du Markdown")
st.markdown("voici un **texte en gras** et un *texte en italique*.")
st.markdown("""
Voici une liste à puces:
- élément 1
- élément 2
- élément 3
""")
st.markdown("""
Voici une liste à puces:
1. élément 1
2. élément 2
3. élément 3
""")
st.markdown(">Voici une citation.")
st.markdown("---")

st.markdown("![Alt texte](https://img.freepik.com/photos-premium/adorable-mignon-chat-potele-rendu-3d_784625-1053.jpg)")
st.markdown("[Cliquez ici pour aller sur Google](https://www.google.com)")

st.button("Click me")

st.slider('valeur',0,50,10)
st.selectbox('Valeur à choisir?',('1','2','3', 'Ne rien choisir'))
st.multiselect(
    'What are your favorite colors',
    ['Green', 'Yellow', 'Red', 'Blue'],
    ['Yellow', 'Red'])

st.text_input("écrire votre résumé")
st.number_input("entrer une valeur",10,60,step=1)
st.text_area("Entrer votre résumé")
st.date_input("choose a date", datetime.date(2023,6,12))
st.time_input("entrer l'heure",datetime.time(0,00))

st.file_uploader("Upload your file",)

st.checkbox('check the boxs')

progress_bar = st.sidebar.progress(0)
status_text = st.sidebar.empty()
last_rows = np.random.randn(1, 1)
chart = st.line_chart(last_rows)

for i in range(1, 101):
    new_rows = last_rows[-1, :] + np.random.randn(5, 1).cumsum(axis=0)
    status_text.text("%i%% Complete" % i)
    chart.add_rows(new_rows)
    progress_bar.progress(i)
    last_rows = new_rows
    time.sleep(0.05)

progress_bar.empty()

# Streamlit widgets automatically run the script from top to bottom. Since
# this button is not connected to any other logic, it just causes a plain
# rerun.
st.button("Re-run")
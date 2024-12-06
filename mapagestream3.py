import streamlit as st
from streamlit_authenticator import Authenticate
import streamlit_authenticator as stauth
from streamlit_option_menu import option_menu

# Nos données utilisateurs doivent respecter ce format
lesDonneesDesComptes = {'usernames': {'utilisateur': {'name': 'utilisateur',
   'password': 'utilisateurMDP',
   'email': 'utilisateur@gmail.com',
   'failed_login_attemps': 0, # Sera géré automatiquement
   'logged_in': False, # Sera géré automatiquement
   'role': 'utilisateur'},
  'root': {'name': 'root',
   'password': 'rootMDP',
   'email': 'admin@gmail.com',
   'failed_login_attemps': 0, # Sera géré automatiquement
   'logged_in': False, # Sera géré automatiquement
   'role': 'administrateur'}}}

authenticator = Authenticate(
    lesDonneesDesComptes, # Les données des comptes
    "cookie name", # Le nom du cookie, un str quelconque
    "cookie key", # La clé du cookie, un str quelconque
    0, # Le nombre de jours avant que le cookie expire 
)
authenticator.login()

def accueil():
      st.title("Bienvenue sur ma page")

if 'authentication_status' in st.session_state:
    if st.session_state["authentication_status"]: 
        ""
        
        # Création du menu qui va afficher les choix qui se trouvent dans la variable options.
        with st.sidebar:
            st.write('Bienvenue')
            selection = option_menu(
                menu_title='Menu',
                options = ["🏠 Accueil", "🐶 Mon chien"]
            )
            selection
            authenticator.logout("Déconnexion")
      
        # On indique au programme quoi faire en fonction du choix
        if selection == "🏠 Accueil":
            accueil()
            st.image("artifices.jpg", width=1000)

        elif selection == "🐶 Mon chien":
            st.title("Bienvenue sur l'album de Boomie !")

            col1, col2, col3 = st.columns(3)
            with col1:
                st.image("20230601_171202.png", caption="Mimi !")

            with col2:
                st.image("20230728_175006.jpg", caption="Je me cache, avec mon copain !")

            with col3:
                st.image("IMG-20230709-WA0000.jpg", caption="Salut les copains !")

elif st.session_state["authentication_status"] is False:
    st.error("L'username ou le password est/sont incorrect")
elif st.session_state["authentication_status"] is None:
    st.warning('Les champs username et mot de passe doivent être remplie')

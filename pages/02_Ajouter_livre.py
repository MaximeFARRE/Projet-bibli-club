import streamlit as st
from src.services.livre_service import ajouter_nouveau_livre
from src.services.isbn_service import fetch_book_info_by_isbn

st.set_page_config(page_title="Ajouter un livre",    page_icon="assets/logo_icone.png",
)

st.title("Ajouter un livre")
st.write("Remplis les informations ci-dessous pour ajouter un livre à la bibliothèque du club.")

# Recherche par ISBN
st.subheader("Remplissage automatique")
col1, col2 = st.columns([3, 1])
with col1:
    isbn_input = st.text_input("ISBN du livre (optionnel)", help="Exemple : 9782253010216")
with col2:
    st.write("")
    st.write("")
    if st.button("Rechercher"):
        if isbn_input:
            with st.spinner("Recherche en cours..."):
                book_info = fetch_book_info_by_isbn(isbn_input)
                if book_info:
                    st.session_state["autofill_titre"] = book_info.get("titre", "")
                    st.session_state["autofill_auteur"] = book_info.get("auteur", "")
                    st.session_state["autofill_resume"] = book_info.get("resume", "")
                    st.session_state["autofill_couverture"] = book_info.get("couverture", "")
                    st.success("Informations récupérées !")
                else:
                    st.error("Aucun livre trouvé pour cet ISBN.")
        else:
            st.warning("Veuillez saisir un ISBN.")

# Valeurs par défaut depuis session_state
def_titre = st.session_state.get("autofill_titre", "")
def_auteur = st.session_state.get("autofill_auteur", "")
def_resume = st.session_state.get("autofill_resume", "")
def_couverture = st.session_state.get("autofill_couverture", "")

st.divider()

with st.form("ajout_livre_form"):

    titre = st.text_input("Titre du livre", value=def_titre)
    auteur = st.text_input("Auteur", value=def_auteur)
    categorie = st.selectbox(
        "Catégorie",
        ["Business", "Mindset", "Finance", "Marketing", "Management", "Développement personnel", "Autre"]
    )
    proprietaire = st.text_input("Propriétaire (ton nom)")
    proprietaire_email = st.text_input("Email DeVinci du propriétaire")
    resume = st.text_area("Résumé (optionnel)", value=def_resume)
    couverture = st.text_input("URL de couverture (optionnel)", value=def_couverture)

    submitted = st.form_submit_button("Ajouter le livre")

    if submitted:
        if not titre or not proprietaire or not proprietaire_email:
            st.error("Le titre, le propriétaire et l'email du propriétaire sont obligatoires.")
        else:
            # Optionnel : vérifier le domaine
            if not proprietaire_email.endswith("@edu.devinci.fr"):
                 st.error("Merci d'utiliser ton email de l'école (@edu.devinci.fr).")
            else:
                ajouter_nouveau_livre(titre, auteur, categorie, proprietaire, proprietaire_email, resume, couverture)
                st.success(f"Le livre **{titre}** a été ajouté avec succès.")
                # Nettoyer le state
                for key in ["autofill_titre", "autofill_auteur", "autofill_resume", "autofill_couverture"]:
                    if key in st.session_state:
                        del st.session_state[key]

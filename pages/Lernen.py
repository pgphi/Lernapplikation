import streamlit as st
from module.quizLogik import quiz_logik


class Lernapplikation():

    """
    Konfiguriert die Struktur und den Inhalt für die Quizseite.
    """

    def __init__(self):
        pass
    
    # Konfiguriere die Informationsseite
    def inhalt(self):

        # Konfiguriere die Metadaten
        st.set_page_config(
            page_title='Lernapplikation',
            page_icon="🎓",
            initial_sidebar_state="expanded"
        )

        # Konfiguriere die Lernapplikation
        st.title("Quiz")
        quiz_logik()


if __name__ == "__main__":

    # Initialisiere Lernapplikation
    app = Lernapplikation()
    app.inhalt()

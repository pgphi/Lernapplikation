import streamlit as st


class Home():

    """
    Konfiguriere die Struktur und den Inhalt der Homepage.
    """

    def __init__(self):
        pass


    def inhalt(self):

        # Konfiguriere die Metadaten
        st.set_page_config(
            page_title='Lernapplikation',
            page_icon="🎓",
            initial_sidebar_state="expanded"
        )

        # Konfiguriere den Inhalt
        st.title("Python Lernapplikation")
        st.markdown("") # Füge leerer Raum hinzu
        st.header("Hier lernst Du die Grundlagen von Python")
        st.markdown("") # Füge leerer Raum hinzu
        st.image("images/python-hero.jpg")
        st.markdown("") # Füge leerer Raum hinzu
        st.subheader("Welche Grundlagen Du lernst:")
        st.markdown("") # Füge leerer Raum hinzu
        st.info("1. Du kennst die Industriestandards der Python-Programmierung.")
        st.info("2. Du kannst eine for-Schleife in Python programmieren.")
        st.info("3. Du weißt wie eine Funktion in Python initialisiert wird.")
        


if __name__ == "__main__":

    # Initialisiere die Homepage
    home = Home()
    home.inhalt()
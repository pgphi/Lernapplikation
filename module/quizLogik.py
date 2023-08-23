import streamlit as st

def quiz_logik():

    """
    Konfiguriere den Aufbau und die Logik der Lernapplikation.
    """
    
    # Konfiguriere den Inhalt für Frage 1
    st.subheader("Frage 1: Industriestandard Funktionen")
    antwort1 = st.radio("", ["Wähle die richtige Antwort aus","Meine-Funktion", "meineFunktion","meine_funktion"], key="frage1")


    # Konfiguriere die Quizlogik für Frage 1
    if antwort1 == "meine_funktion":
        st.success("Korrekt!")
    
    elif antwort1 == "Wähle die richtige Antwort aus":
        st.info("Wähle eine Antwort aus!")

    else:
        st.error("Ups - versuche es nochmal!")

    st.markdown("") # Füge leerer Raum hinzu
    st.markdown("***")
    st.markdown("") # Füge leerer Raum hinzu


    # Konfiguriere den Inhalt für Frage 2
    st.subheader("Frage 2: For-Schleife")
    st.code("Du hast folgende Liste gegeben: [1,2,3,4,5]. Gebe jede zweite Zahl aus.")
    st.markdown("") # Füge leerer Raum hinzu
    antwort2 = st.text_input("Schreibe hier Deinen Lösungsvorschlag hinein:", key="frage2") # Variable gibt True zurück wenn eine Antwort gegeben wurde andernfalls False.


    # Konfiguriere die Quizlogik für Frage 2
    if antwort2:
        st.info("Deine Antwort lautet:")
        st.code(antwort2)
        st.success("Die richtige Antwort lautet:")
        st.code("liste = [1,2,3,4,5] \n for i in range(1, len(liste)+1,2): \n print(i) # output 1,3,5")
    
    else:
        st.info("Bitte eine Antwort eingeben!")

    st.markdown("") # Füge leerer Raum hinzu
    st.markdown("***")
    st.markdown("") # Füge leerer Raum hinzu


    # Konfiguriere den Inhalt für Frage 3
    st.subheader("Frage 3: Python Funktion")
    st.code("Initialisiere eine beliebige Funktion in Python.")
    st.markdown("") # Füge leerer Raum hinzu
    antwort3 = st.text_input("Schreibe hier Deinen Lösungsvorschlag hinein:", key="frage3") # Variable gibt True zurück wenn eine Antwort gegeben wurde andernfalls False.


    # Konfiguriere die Quizlogik für Frage 3
    if antwort3:
        st.info("Deine Antwort lautet:")
        st.code(antwort3)
        st.success("eine mögliche Antwort lautet wie folgt:")
        st.code("def meine_funktion(a,b): \n'''\n kalkuliere die b-te wurzel von a z.B. a hoch b. \n''' \n result = a ** b \n return result \n meine_funktion(2,2) # output 4 \n ")
    
    else:
        st.info("Bitte geben eine Antwort ein")
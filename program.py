import os 
from openai import OpenAI

def generuj_html_z_artykulu( sciezka_do_pliku,temperature,max_tokens):
    # Ustaw klucz API
    client=OpenAI(
      api_key=os.environ.get("OPENAI_API_KEY")
    )
 
    # Wczytaj treść artykułu z pliku tekstowego
    with open(sciezka_do_pliku, 'r', encoding='utf-8') as plik:
        artykul = plik.read()

    # Prompt dla modelu
    prompt = (
        "Przetwórz poniższy artykuł i wygeneruj kod HTML, który używa odpowiednich tagów HTML "
        "do strukturyzacji treści. Dodaj tagi <img> z atrybutem src='image_placeholder.jpg' i "
        "alt z dokładnym opisem obrazu tam, gdzie warto wstawić grafikę. Umieść podpisy pod "
        "grafikami za pomocą odpowiedniego tagu. Nie dołączaj CSS ani JavaScript, zwróć tylko "
        "zawartość między <body> i </body>. Artykuł:\n\n" + artykul
    )

     # Wysłanie żądania do API OpenAI za pomocą ChatCompletion
    odpowiedz = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Jesteś asystentem tworzącym kod HTML."},
            {"role": "user", "content": prompt}
        ],
        temperature=temperature,
        max_tokens=max_tokens
    )

    # Pobranie wygenerowanego HTML-a
    html_content = odpowiedz.choices[0].message.content.strip()

    # Zapisz wynik do pliku artykul.html
    with open("artykul.html", "w", encoding='utf-8') as plik_html:
        plik_html.write(html_content)

    print("Plik artykul.html został wygenerowany.")

sciezka_do_pliku = "zadanie.txt"
generuj_html_z_artykulu(sciezka_do_pliku,temperature=0.7, max_tokens=2500)

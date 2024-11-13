# Generowanie HTML z Artykułu za pomocą OpenAI API

## Opis projektu

Ta aplikacja Python służy do generowania kodu HTML na podstawie treści artykułu znajdującego się w pliku tekstowym. Wykorzystuje model językowy GPT-4 udostępniany przez OpenAI, aby przetworzyć treść artykułu i wygenerować kod HTML o odpowiedniej strukturze. Kod zawiera placeholdery dla grafik z przypisanymi opisami, a także podpisy pod grafikami, ale nie zawiera żadnego stylu CSS ani JavaScript.

Wynikowy kod HTML jest zapisywany w pliku `artykul.html`.

### Cechy aplikacji:
- Wczytuje artykuł z pliku tekstowego.
- Generuje strukturalny kod HTML zawierający placeholdery dla grafik.
- Zapisuje kod HTML do pliku `artykul.html`.

## Wymagania

Przed uruchomieniem aplikacji należy upewnić się, że środowisko posiada:
- Python 3.7 lub nowszy,
- Zainstalowany pakiet `openai`oraz `python-dotenv`
- Plik `.env` zawierający klucz API OpenAI.

Należy utworzyć plik `.env` zawierający komendę OPENAI_API_KEY="klucz do API_openai" , plik ten nie jest dołączony automatycznie ze względów bezpieczenśtwa i braku chęci udostępniania klucza w publicznym repozytorium github

## Przykładowe użycie funkcji 
    sciezka_do_pliku = "zadanie.txt"
    generuj_html_z_artykulu(sciezka_do_pliku, temperature=0.7, max_tokens=2500)
    Parametry modelu można dobrać indywidualnie , po kilku testach przy tak ustawionych parametrach kreatywności oraz tokenów otrzymano zadowalający wynik. 

## Instrukcja instalacji

1. **Klonowanie repozytorium**  
   Skopiuj kod repozytorium do swojego komputera:
   ```bash
   git clone <URL-do-Repozytorium>
   cd <Nazwa-Repozytorium>

## Repozytorium 
├── klucz.env               # Plik z kluczem API OpenAI
├── README.md          # Ten plik z opisem projektu
├── zadanie.txt        # Plik z artykułem do przetworzenia
├── artykul.html       # Wygenerowany plik HTML
└── program.py # Skrypt Pythona generujący HTML
# Asteroids
### Drugi projekt z boot.dev -> backend developer path
(Pierwszy był bookbot, ale nie ma go w moich repozytoriach)

(prawdopodobnie) Ciekawe rzeczy z którymi nie miałem wcześniej do czynienia (lub o których chcę się więcej dowiedzieć):
    - uv
    - pygame
    - ``__name__ == "__main__"``  

##### 11.05.2026
Dzisiaj tak:
    1. Klasa CircleShape, w której znajduje się warunkowa inicjalizacja kontenerów. Jest to klasa abstrakcyjna
    2. Klasa Player: dziedziczy po CircleShape i dziedziczy po niej metody:
        - draw - rysuje wielokąt (tutaj akurat trójkąt) na okręgu (obiekcie Player)
        - update - aktualizuje stan (pozycje, strone w ktora jest zwrocony trojkat):
        metody charakterystyczne dla Player:
        - triangle - definiuje trójkąt
        - rotate - to rotacji self dodaje stałą obracania pomnożoną przez odstęp czasowy pomiędzy klatkami
        - move - do pozycji self dodaje wektor przesunięcia (wektor jednostkowy obrócony o rotację i pomnożony przez prędkość rotacji pomiędzy klatkami
    3. Dodałem kilka stałych do constants.py
    4. Wygenerowanie obiektu gracza (kształt trójkąta, ale narysowany na okręgu), poruszanie się poza mapą

Trzeba ograniczyć gracza, bo obecnie może wyjść poza okienko - niewskazane

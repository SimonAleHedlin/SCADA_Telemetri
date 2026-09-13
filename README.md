Funktionalitet (CRUD)
    Create: Lägger till nya sensorer med eget ID, var de är placerade och tillhörande larmgränser.
    Read: Läser in och kollar på sparad historik, räknar ut medelvärden och visar data över valda tidsintervall.
    Update: Uppdaterar befintliga sensorer om man flyttar på dem eller behöver ändra tröskelvärdena.
    Delete: Tar bort sensorer helt ur systemet när de plockas bort eller inte längre används.

Arkitektur
    Koden är uppdelad i moduler för att hålla isär gränssnitt och logik:
        main.py: Huvudfilen som styr gränssnittet, menyer, listor och skapar instanser av sensorerna.
        sensor_node.py: Själva komponentmodulen som innehåller klassen Sensor och logiken för att hantera datastrukturerna.

Felhantering och Stabilitet
    Programmet använder try/except-block för att inte krascha om användaren matar in fel saker (till exempel bokstäver istället för siffror, vilket ger ValueError) eller om det skulle dyka upp en noll-division (ZeroDivisionError). Det gör att systemet rullar på stabilt utan att dö.
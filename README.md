# OBS2Discord
Pythonscript to send a POST request to a webhook URL on OBS action "start streaming"

# Anleitung

## Erstellen des Discord Webhooks

Discord-Webhooks können zur einfachen Nachrichtenweitergabe verwendet werden. Das Feature wird vom kostenlosen Basisserver angeboten.

    1. Gehe zu Servereinstellungen -> Integration
    2. Klicke auf 'Webhooks'
    3. Erstelle einen neuen Webhook. Dieser sollte nun in der Liste sichtbar sein.
    4. Klicke auf den neuen Webhook. Hier kann man den Kanal wählen, in welchem die Nachrichten ausgegeben werden sollen und dem Bot einen Namen geben.
    5. Über den Klick auf 'copy webhook url' erhält man den Link, welchen man später im Script einfügen muss.
    6. Fertig

## Nutzen des Scripts

Von dem Script sind zwei Versionen bereitgestellt:

 - [obs2discord.py](https://github.com/sc2de/OBS2Discord/blob/main/obs2discord.py) liefert die Basisfunktion
 - [obs2discord_multichannel.py](https://github.com/sc2de/OBS2Discord/blob/main/obs2discord_multichannel.py) Basisscript für 2 Kanäle, welches beliebig erweitert werden kann


Vorgehen(weitere Hinweise ebenfalls in den Script-Dateien selbst):

    1. Lade das Script an einen beliebigen Ort auf deiner Festplatte herunter.
    2. Öffne die Datei mit einem beliebigen Texteditor.
    3. Füge die URL des Discord-Webhooks an die richtige Stelle ein.
    4. Editiere die Nachricht, welche versendet werden soll nach belieben.
    5. Achte darauf, dass Anführungszeichen und Klammern bleiben wo Sie sind. Tausche nur DISCORD_URL_HIER und EURE_NACHRICHT_HIER aus.
    6. Passe ggf. den Profilnamen an. Welches Profil du in OBS verwendest, wird von OBS Studio in der Titelleiste angezeigt.
    7. Speichere die Datei.
    8. Gehe in OBS-Studio zu Werkzeuge->Scripte und füge die Datei hinzu.
    9. Fertig. Sobald du nun auf "Starte Stream" drückst, wird die Aktion ausgelöst.
    10. Sollte alles passen, sollte die versendete Nachricht fast sofort im gewählten Discordkanal zu sehen sein.

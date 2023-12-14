#########################################################
# Einfaches Script zum versenden einer Nachricht an     #
# z.B. einen Discord-Webhook durch das Auslösen der     #
# Aktion "Starte Stream" in OBS Studio.                 #
#                                                       #
# Einfache Anleitung auf:                               #
# https://github.com/sc2de/OBS2Discord/                 #
#########################################################

import obspython as S
import requests

# Headers Regeln den MIME-Type, einfach so lassen wie es ist. Egal ob du hier bist und nicht.
headers = {'content-type': 'application/json'}

# Die Variable url wird mit dem Webhook-Link den man von Discord erhält befüllt.
url_a = 'DISCORD_URL_HIER'

# Die Variable body enthält einen JSON-Körper der innerhalb des Schlüssels "content" die Nachricht enthält. Ein Beispiel dazu folgt unten
body_a = { "content":"EURE_NACHRICHT_HIER" }

# URL des Webhooks und Body für einen zweiten Kanal
url_b = 'DISCORD_URL_HIER'
body_b = { "content":"EURE_NACHRICHT_HIER" }

############# Beispiel #############
# url = 'https://discord.com/api/webhooks/1180420648623951902/ihui645gh54&5634654gjkh54i6h54ui6hh2ui23gj8gj3u3489u-123zh3h945h3999'
# body = { "content":"<@&1180416336153813005> IMoC hat soeben den Stream gestartet. Schau vorbei auf https://www.twitch.tv/imoclol" }
#
# Um Rollen oder Nutzer anzupingen, muss dies über die Rollen-ID oder Nutzer-ID erfolgen. Die RollenID-Syntax erfordert zusätzlich ein & nach dem @ <@&RoleID> bzw. <@UserID>.
####################################

# Der Name eures OBS - Profils in welchem die Aktion ausgelöst werden soll.
profilename_a = "sc2de"
profilename_b = "imoclol"

# Ab hier passieren Dinge, die man wie folgt zusammenfassen kann: Es wurde ein Event abgefangen und nachgesehen ob es "stream starten" war.
# Dann wird geschaut, ob der Profilname passt.
# Wenn der passt, wird die Nachricht einmalig losgeschickt.
# Man kann so viele Profile aka. Kanäle auswählen wie man lustig ist, lul.
def on_event(event):
    if event == S.OBS_FRONTEND_EVENT_STREAMING_STARTING:
        if S.obs_frontend_get_current_profile() == profilename_a:
            req = requests.post(url_a, headers=headers, json=body_a)

            print(req.status_code)
            print(req.headers)
            print(req.text)

        if S.obs_frontend_get_current_profile() == profilename_b:
            req = requests.post(url_b, headers=headers, json=body_b)

            print(req.status_code)
            print(req.headers)
            print(req.text)


def script_load(settings):
    S.obs_frontend_add_event_callback(on_event)


def script_description():
    "Trigger a POST request when pressing the start streaming button in OBS."





# Zeug für Troubleshooting(Event oben kann hiermit  getauscht werden, um die Trigger-Aktion mit einem Szenenwechsel auszulösen(für testzwecke)
# if event == S.OBS_FRONTEND_EVENT_SCENE_CHANGED:
#     print("lul")

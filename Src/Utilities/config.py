import json
import logging

# LOAD CONFIG
with open('config.json') as f:
    config = json.load(f)

SITE = config["Siti"]

# ⭐ FUNZIONE SAFE-GET — mettila QUI
def get(site, key, default=None):
    return SITE.get(site, {}).get(key, default)

# Ora puoi leggere i parametri in modo sicuro
SC_DOMAIN = get("StreamingCommunity", "url")
SW_DOMAIN = get("StreamingWatch", "url")
AW_DOMAIN = get("AnimeWorld", "url")
CB_DOMAIN = get("CB01", "url")
GS_DOMAIN = get("Guardaserie", "url")
GHD_DOMAIN = get("GuardaHD", "url")
ES_DOMAIN = get("Eurostreaming", "url")
GF_DOMAIN = get("Guardaflix", "url")
GO_DOMAIN = get("Guardoserie", "url")
RT_DOMAIN = get("Realtime", "url")  # non crasha più se non esiste

SC = get("StreamingCommunity", "enabled", "0")
SW = get("StreamingWatch", "enabled", "0")
AW = get("AnimeWorld", "enabled", "0")
CB = get("CB01", "enabled", "0")
GS = get("Guardaserie", "enabled", "0")
GHD = get("GuardaHD", "enabled", "0")
ES = get("Eurostreaming", "enabled", "0")
GF = get("Guardaflix", "enabled", "0")
GO = get("Guardoserie", "enabled", "0")
RT = get("Realtime", "enabled", "0")

SC_ForwardProxy = get("StreamingCommunity", "SC_ForwardProxy", "0")
GS_ForwardProxy = get("Guardaserie", "GS_ForwardProxy", "0")
GH_ForwardProxy = get("GuardaHD", "GH_ForwardProxy", "0")
VX_ForwardProxy = get("StreamingCommunity", "VX_ForwardProxy", "0")
AW_ForwardProxy = get("AnimeWorld", "AW_ForwardProxy", "0")
MX_ForwardProxy = get("CB01", "MX_ForwardProxy", "0")
CB_ForwardProxy = get("CB01", "CB_ForwardProxy", "0")
ES_ForwardProxy = get("Eurostreaming", "ES_ForwardProxy", "0")
GF_ForwardProxy = get("Guardaflix", "GF_ForwardProxy", "0")
GO_ForwardProxy = get("Guardoserie", "GO_ForwardProxy", "0")
SW_ForwardProxy = get("StreamingWatch", "SW_ForwardProxy", "0")
RT_ForwardProxy = get("Realtime", "RT_ForwardProxy", "0")

GS_PROXY = get("Guardaserie", "GS_PROXY", "0")
GH_PROXY = get("GuardaHD", "GH_PROXY", "0")
CB_PROXY = get("CB01", "CB_PROXY", "0")
SC_PROXY = get("StreamingCommunity", "SC_PROXY", "0")
VX_PROXY = get("StreamingCommunity", "VX_PROXY", "0")
AW_PROXY = get("AnimeWorld", "AW_PROXY", "0")
MX_PROXY = get("CB01", "MX_PROXY", "0")
ES_PROXY = get("Eurostreaming", "ES_PROXY", "0")
GF_PROXY = get("Guardaflix", "GF_PROXY", "0")
GO_PROXY = get("Guardoserie", "GO_PROXY", "0")
SW_PROXY = get("StreamingWatch", "SW_PROXY", "0")
RT_PROXY = get("Realtime", "RT_PROXY", "0")

# GENERAL
GENERAL = config['General']
dotenv = GENERAL.get("load_env", "0")
HOST = GENERAL.get("HOST", "0.0.0.0")
PORT = GENERAL.get("PORT", 8080)
Icon = GENERAL.get("Icon", "")
Name = GENERAL.get("Name", "")
LEVEL = GENERAL.get("level", "info")
Global_Proxy = GENERAL.get("Global_Proxy", "0")

def setup_logging(LEVEL):
    LEVEL = LEVEL.upper()
    level = getattr(logging, LEVEL, logging.DEBUG)
    logging.basicConfig(level=level, format='%(message)s')
    logger = logging.getLogger(__name__)
    return logger

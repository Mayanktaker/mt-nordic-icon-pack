# © Mayanktaker Computers & Web Development | https://mayanktaker.com
# KDE fluent-edition app tiles, batch 1: Tier-1 KDE application artwork.
# Stage A ships dolphin/konsole/systemsettings; the remaining 19 tiles join in stage B.

try:
    from apps_popular_common import tile, ACCENT, ACCENT2, SNOW, GREEN, BASE, TILE_FILL
except ImportError:
    from tools.icons.apps_popular_common import tile, ACCENT, ACCENT2, SNOW, GREEN, BASE, TILE_FILL


KDE_APP_ICONS = {
    # Dolphin — folder with a leaping glacier dolphin
    "dolphin": tile("dolphin", f'''
<rect x="15" y="14" width="14" height="8" rx="2.5" fill="{ACCENT}"/>
<rect x="14" y="18" width="36" height="27" rx="4" fill="{TILE_FILL}" stroke="{ACCENT}" stroke-width="2"/>
<path d="M 18 44 C 26 26 44 22 48 26 C 44 27 40 30 38 34 C 34 41 26 44 18 44 Z" fill="{ACCENT2}"/>
<path d="M 33 24.5 C 34 20.5 38 19 41 20 C 38.5 21.5 37 24 37 26.5 Z" fill="{ACCENT2}"/>
<circle cx="43.5" cy="28.5" r="1.3" fill="{BASE}"/>'''),

    # Konsole — terminal window with prompt chevron and cursor
    "konsole": tile("konsole", f'''
<rect x="14" y="15" width="36" height="34" rx="3" fill="{TILE_FILL}" stroke="{ACCENT}" stroke-width="2"/>
<line x1="15.5" y1="23" x2="48.5" y2="23" stroke="{ACCENT}" stroke-width="1.6"/>
<path d="M 20 31 L 25 36 L 20 41" stroke="{GREEN}" stroke-width="2.6" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
<line x1="29" y1="41" x2="43" y2="41" stroke="{SNOW}" stroke-width="2.6" stroke-linecap="round"/>'''),

    # System Settings — large and small gear in the core-suite ring+teeth style
    "systemsettings": tile("systemsettings", f'''
<circle cx="26" cy="38" r="11" fill="none" stroke="{ACCENT}" stroke-width="2.4"/>
<rect x="24" y="23" width="4" height="7" rx="1.5" fill="{ACCENT}"/>
<rect x="24" y="46" width="4" height="7" rx="1.5" fill="{ACCENT}"/>
<rect x="11" y="36" width="7" height="4" rx="1.5" fill="{ACCENT}"/>
<rect x="34" y="36" width="7" height="4" rx="1.5" fill="{ACCENT}"/>
<circle cx="26" cy="38" r="3.5" fill="{ACCENT}"/>
<circle cx="44" cy="22" r="6.5" fill="none" stroke="{ACCENT2}" stroke-width="2.2"/>
<rect x="42" y="13.5" width="4" height="4.5" rx="1.2" fill="{ACCENT2}"/>
<rect x="42" y="26" width="4" height="4.5" rx="1.2" fill="{ACCENT2}"/>
<rect x="35.5" y="20" width="4.5" height="4" rx="1.2" fill="{ACCENT2}"/>
<rect x="48" y="20" width="4.5" height="4" rx="1.2" fill="{ACCENT2}"/>
<circle cx="44" cy="22" r="2" fill="{ACCENT2}"/>'''),
}

# Desktop ids whose target tiles exist today; the remaining 19 org.kde.* ids ship
# together with their tiles in stage B so no alias ever dangles.
KDE_APP_ALIASES = {
    "org.kde.dolphin": "dolphin",
    "org.kde.konsole": "konsole",
    "org.kde.systemsettings": "systemsettings",
    "org.kde.gwenview": "gwenview",
    "org.kde.elisa": "elisa",
    "org.kde.okular": "okular",
    "org.kde.partitionmanager": "partitionmanager",
}

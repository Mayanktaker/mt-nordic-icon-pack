# © Mayanktaker Computers & Web Development | https://mayanktaker.com
# KDE fluent-edition app tiles: Tier-1 KDE application artwork (22 canonical tiles).
# Vocabulary per approved checkpoint: tile() chrome + accent tokens, ≤~15 elements per body.

try:
    from apps_popular_common import tile, ACCENT, ACCENT2, SNOW, GREEN, GOLD, BASE, TILE_FILL
except ImportError:
    from tools.icons.apps_popular_common import tile, ACCENT, ACCENT2, SNOW, GREEN, GOLD, BASE, TILE_FILL


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

    # Yakuake — drop-down terminal pulled from the top edge
    "yakuake": tile("yakuake", f'''
<path d="M 32 9 L 32 16" stroke="{ACCENT2}" stroke-width="2.2" stroke-linecap="round"/>
<path d="M 27 13 L 32 18 L 37 13" stroke="{ACCENT2}" stroke-width="2.2" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
<rect x="15" y="21" width="34" height="27" rx="3" fill="{TILE_FILL}" stroke="{ACCENT}" stroke-width="2"/>
<path d="M 21 30 L 25 34 L 21 38" stroke="{GREEN}" stroke-width="2.4" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
<line x1="29" y1="38" x2="41" y2="38" stroke="{SNOW}" stroke-width="2.4" stroke-linecap="round"/>'''),

    # Discover — Plasma globe with a download badge
    "discover": tile("discover", f'''
<circle cx="29" cy="32" r="14" fill="none" stroke="{ACCENT}" stroke-width="2.2"/>
<ellipse cx="29" cy="32" rx="14" ry="5.5" fill="none" stroke="{ACCENT2}" stroke-width="1.6"/>
<ellipse cx="29" cy="32" rx="5.5" ry="14" fill="none" stroke="{ACCENT2}" stroke-width="1.6"/>
<circle cx="45" cy="45" r="7" fill="{GREEN}"/>
<path d="M 45 41.5 L 45 48 M 42 45.5 L 45 48.5 L 48 45.5" stroke="{SNOW}" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round"/>'''),

    # Ark — archive chest with zipper seam
    "ark": tile("ark", f'''
<rect x="14" y="17" width="36" height="8" rx="2.5" fill="{ACCENT}"/>
<rect x="16" y="25" width="32" height="23" rx="3" fill="{TILE_FILL}" stroke="{ACCENT}" stroke-width="2"/>
<line x1="32" y1="25" x2="32" y2="48" stroke="{ACCENT2}" stroke-width="2" stroke-dasharray="4 3"/>
<circle cx="32" cy="42" r="2.5" fill="{GOLD}"/>'''),

    # Spectacle — screenshot camera with flash
    "spectacle": tile("spectacle", f'''
<rect x="26" y="16" width="12" height="8" rx="2" fill="{ACCENT}"/>
<rect x="14" y="22" width="36" height="24" rx="4" fill="{TILE_FILL}" stroke="{ACCENT}" stroke-width="2"/>
<circle cx="31" cy="34" r="7" fill="none" stroke="{GOLD}" stroke-width="2.4"/>
<circle cx="31" cy="34" r="2.5" fill="{GOLD}"/>
<circle cx="44" cy="27" r="2" fill="{SNOW}"/>'''),

    # KDE Connect — phone paired over radio waves
    "kdeconnect": tile("kdeconnect", f'''
<rect x="17" y="14" width="16" height="32" rx="3.5" fill="{TILE_FILL}" stroke="{ACCENT}" stroke-width="2"/>
<circle cx="25" cy="41" r="1.5" fill="{ACCENT2}"/>
<path d="M 38 25 C 43 29 43 35 38 39" stroke="{ACCENT2}" stroke-width="2.4" fill="none" stroke-linecap="round"/>
<path d="M 43 20 C 50 26 50 38 43 44" stroke="{ACCENT}" stroke-width="2.4" fill="none" stroke-linecap="round"/>'''),

    # KCalc — calculator with display and key grid
    "kcalc": tile("kcalc", f'''
<rect x="18" y="14" width="28" height="36" rx="4" fill="{TILE_FILL}" stroke="{ACCENT}" stroke-width="2"/>
<rect x="22" y="18" width="20" height="8" rx="2" fill="{ACCENT2}" fill-opacity="0.4"/>
<circle cx="24" cy="32" r="2" fill="{ACCENT2}"/><circle cx="32" cy="32" r="2" fill="{ACCENT2}"/><circle cx="40" cy="32" r="2" fill="{ACCENT2}"/>
<circle cx="24" cy="38" r="2" fill="{ACCENT2}"/><circle cx="32" cy="38" r="2" fill="{ACCENT2}"/><circle cx="40" cy="38" r="2" fill="{ACCENT2}"/>
<circle cx="24" cy="44" r="2" fill="{ACCENT2}"/><circle cx="32" cy="44" r="2" fill="{ACCENT2}"/><circle cx="40" cy="44" r="2" fill="{GOLD}"/>'''),

    # KClock — clock face with hands and cardinal ticks
    "kclock": tile("kclock", f'''
<circle cx="32" cy="34" r="15" fill="none" stroke="{ACCENT}" stroke-width="2.4"/>
<path d="M 32 19 L 32 21 M 32 47 L 32 49 M 17 34 L 19 34 M 45 34 L 47 34" stroke="{ACCENT2}" stroke-width="1.6" stroke-linecap="round"/>
<line x1="32" y1="34" x2="32" y2="24" stroke="{SNOW}" stroke-width="2.2" stroke-linecap="round"/>
<line x1="32" y1="34" x2="39" y2="38" stroke="{ACCENT2}" stroke-width="2.2" stroke-linecap="round"/>
<circle cx="32" cy="34" r="2.2" fill="{ACCENT}"/>'''),

    # KFind — magnifier with sparkle
    "kfind": tile("kfind", f'''
<circle cx="28" cy="31" r="11" fill="none" stroke="{ACCENT}" stroke-width="2.6"/>
<path d="M 21 29 C 21 24 24 21 28 21" stroke="{ACCENT2}" stroke-width="2" fill="none" stroke-linecap="round"/>
<line x1="36" y1="39" x2="46" y2="49" stroke="{ACCENT}" stroke-width="3" stroke-linecap="round"/>
<path d="M 44 19 L 44 25 M 41 22 L 47 22" stroke="{GOLD}" stroke-width="2" stroke-linecap="round"/>'''),

    # Filelight — radial disk-usage rings with free-space gaps
    "filelight": tile("filelight", f'''
<circle cx="32" cy="33" r="13" fill="none" stroke="{ACCENT}" stroke-width="4.5" stroke-dasharray="61 21" transform="rotate(-90 32 33)"/>
<circle cx="32" cy="33" r="7.5" fill="none" stroke="{ACCENT2}" stroke-width="4" stroke-dasharray="40 8" transform="rotate(-90 32 33)"/>'''),

    # Printer Manager — printer with progress bar and paper flow
    "printer-manager": tile("printer-manager", f'''
<rect x="24" y="13" width="16" height="11" rx="1.5" fill="{SNOW}"/>
<rect x="16" y="24" width="32" height="15" rx="3" fill="{TILE_FILL}" stroke="{ACCENT}" stroke-width="2"/>
<rect x="20" y="34" width="24" height="3" rx="1.5" fill="{GREEN}"/>
<rect x="24" y="42" width="16" height="9" rx="1.5" fill="{SNOW}"/>'''),

    # KGpg — gold key with bitting teeth
    "kgpg": tile("kgpg", f'''
<circle cx="22" cy="31" r="8" fill="none" stroke="{GOLD}" stroke-width="3"/>
<line x1="30" y1="31" x2="49" y2="31" stroke="{GOLD}" stroke-width="3" stroke-linecap="round"/>
<path d="M 42 31 L 42 37 M 47 31 L 47 36" stroke="{GOLD}" stroke-width="3" stroke-linecap="round"/>'''),

    # Skanpage — flatbed scanner with green scan bar
    "skanpage": tile("skanpage", f'''
<rect x="13" y="13" width="38" height="6" rx="2.5" fill="{ACCENT}"/>
<rect x="13" y="21" width="38" height="24" rx="3" fill="{TILE_FILL}" stroke="{ACCENT}" stroke-width="2"/>
<rect x="17" y="33" width="30" height="4.5" rx="2.25" fill="{GREEN}" fill-opacity="0.85"/>
<line x1="17" y1="28" x2="47" y2="28" stroke="{ACCENT2}" stroke-width="1.4"/>'''),

    # Krfb — desktop sharing: monitor casting outward
    "krfb": tile("krfb", f'''
<rect x="14" y="18" width="28" height="20" rx="3" fill="{TILE_FILL}" stroke="{ACCENT}" stroke-width="2"/>
<path d="M 28 24 L 28 32 L 35 28 Z" fill="{ACCENT2}"/>
<path d="M 28 38 L 28 43 M 22 45 L 34 45" stroke="{ACCENT}" stroke-width="2.2" stroke-linecap="round"/>
<path d="M 46 20 C 51 25 51 31 46 36" stroke="{ACCENT2}" stroke-width="2.4" fill="none" stroke-linecap="round"/>
<circle cx="45" cy="28" r="2" fill="{ACCENT2}"/>'''),

    # KRdc — remote desktop: two linked monitors
    "krdc": tile("krdc", f'''
<rect x="14" y="15" width="26" height="18" rx="3" fill="{TILE_FILL}" stroke="{ACCENT}" stroke-width="2"/>
<path d="M 24 38 C 27 39 29 39 32 40 M 27 36 L 31.5 40 L 26.5 41" stroke="{ACCENT2}" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
<rect x="33" y="31" width="18" height="14" rx="2.5" fill="{TILE_FILL}" stroke="{ACCENT2}" stroke-width="2"/>'''),

    # Dragon Player — media player with flame lick
    "dragonplayer": tile("dragonplayer", f'''
<circle cx="30" cy="34" r="13" fill="none" stroke="{ACCENT}" stroke-width="2.4"/>
<path d="M 26 27 L 26 41 L 38 34 Z" fill="{ACCENT2}"/>
<path d="M 43 17 C 48 19 48 25 43 27 C 45.5 23.5 45 20 41 20 Z" fill="{GOLD}"/>'''),

    # Juk — jukebox arch with a gold note
    "juk": tile("juk", f'''
<path d="M 20 46 L 20 24 C 20 17 44 17 44 24 L 44 46 Z" fill="{TILE_FILL}" stroke="{ACCENT}" stroke-width="2"/>
<path d="M 24 46 L 24 27 C 24 22 40 22 40 27 L 40 46" fill="none" stroke="{ACCENT2}" stroke-width="1.6"/>
<circle cx="33" cy="39" r="3" fill="{GOLD}"/>
<path d="M 36 39 L 36 28 C 38.5 28.5 40 30.5 39.5 33" stroke="{GOLD}" stroke-width="2" fill="none" stroke-linecap="round"/>'''),

    # KMail — envelope with unread badge
    "kmail": tile("kmail", f'''
<rect x="15" y="20" width="34" height="24" rx="3" fill="{TILE_FILL}" stroke="{ACCENT}" stroke-width="2"/>
<path d="M 16 24 L 32 36 L 48 24" stroke="{ACCENT2}" stroke-width="2.2" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
<circle cx="46" cy="21" r="4.5" fill="{GREEN}"/>'''),

    # Kontact — PIM hub linking mail, contacts and calendar
    "kontact": tile("kontact", f'''
<path d="M 32 32 L 17 20 M 32 32 L 47 20 M 32 32 L 32 49" stroke="{ACCENT2}" stroke-width="1.8"/>
<circle cx="17" cy="20" r="4.5" fill="{TILE_FILL}" stroke="{ACCENT2}" stroke-width="2"/>
<circle cx="47" cy="20" r="4.5" fill="{TILE_FILL}" stroke="{ACCENT2}" stroke-width="2"/>
<circle cx="32" cy="49" r="4.5" fill="{TILE_FILL}" stroke="{ACCENT2}" stroke-width="2"/>
<circle cx="32" cy="32" r="5.5" fill="{ACCENT}"/>'''),

    # KAddressBook — address card with contact portrait
    "kaddressbook": tile("kaddressbook", f'''
<rect x="15" y="18" width="34" height="27" rx="3" fill="{TILE_FILL}" stroke="{ACCENT}" stroke-width="2"/>
<circle cx="25" cy="27" r="3" fill="{ACCENT2}"/>
<path d="M 20 38 C 20 32.5 30 32.5 30 38 Z" fill="{ACCENT2}"/>
<path d="M 36 26 L 45 26 M 36 31 L 43 31" stroke="{ACCENT2}" stroke-width="1.8" stroke-linecap="round"/>'''),
}

# Desktop ids for every Tier-1 name; targets all exist in this module or in
# apps_popular_5/6, so no alias ever dangles.
KDE_APP_ALIASES = {
    "org.kde.dolphin": "dolphin",
    "org.kde.konsole": "konsole",
    "org.kde.systemsettings": "systemsettings",
    "org.kde.yakuake": "yakuake",
    "org.kde.discover": "discover",
    "org.kde.ark": "ark",
    "org.kde.spectacle": "spectacle",
    "org.kde.kdeconnect": "kdeconnect",
    "org.kde.kdeconnect.app": "kdeconnect",
    "org.kde.kcalc": "kcalc",
    "org.kde.kclock": "kclock",
    "org.kde.kfind": "kfind",
    "org.kde.filelight": "filelight",
    "org.kde.print-manager": "printer-manager",
    "org.kde.kgpg": "kgpg",
    "org.kde.skanpage": "skanpage",
    "org.kde.krfb": "krfb",
    "org.kde.krdc": "krdc",
    "org.kde.dragonplayer": "dragonplayer",
    "org.kde.juk": "juk",
    "org.kde.kmail": "kmail",
    "org.kde.kontact": "kontact",
    "org.kde.kaddressbook": "kaddressbook",
    "org.kde.gwenview": "gwenview",
    "org.kde.elisa": "elisa",
    "org.kde.okular": "okular",
    "org.kde.partitionmanager": "partitionmanager",
}

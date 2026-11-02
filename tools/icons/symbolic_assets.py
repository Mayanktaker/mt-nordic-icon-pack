# © Mayanktaker Computers & Web Development | https://mayanktaker.com
# Extended symbolic icons for MT-Nordic-Blue-Icons suite.
# High-contrast filled silhouette paths (strictly no fill="none" with strokes,
# ensuring GTK4's symbolic shader never fills outlined shapes into solid discs).

EXTENDED_SYMBOLIC_ICONS = {
    # ---------------------------------------------------------------------
    # GNOME Interactive Screenshot & Screencast Suite (Filled Path Geometry)
    # ---------------------------------------------------------------------
    "camera-photo-symbolic": '''<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16">
  <path fill="currentColor" fill-rule="evenodd" d="M 5.5 2 L 6.5 3 L 9.5 3 L 10.5 2 Z M 2 4 C 1.45 4 1 4.45 1 5 L 1 12 C 1 12.55 1.45 13 2 13 L 14 13 C 14.55 13 15 12.55 15 12 L 15 5 C 15 4.45 14.55 4 14 4 Z M 8 6 C 9.66 6 11 7.34 11 9 C 11 10.66 9.66 12 8 12 C 6.34 12 5 10.66 5 9 C 5 7.34 6.34 6 8 6 Z M 8 7.3 C 7.06 7.3 6.3 8.06 6.3 9 C 6.3 9.94 7.06 10.7 8 10.7 C 8.94 10.7 9.7 9.94 9.7 9 C 9.7 8.06 8.94 7.3 8 7.3 Z"/>
</svg>''',

    "camera-video-symbolic": '''<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16">
  <path fill="currentColor" fill-rule="evenodd" d="M 2 4 C 1.45 4 1 4.45 1 5 L 1 11 C 1 11.55 1.45 12 2 12 L 9.5 12 C 10.05 12 10.5 11.55 10.5 11 L 10.5 9.5 L 14.2 11.7 C 14.6 11.9 15 11.7 15 11.2 L 15 4.8 C 15 4.3 14.6 4.1 14.2 4.3 L 10.5 6.5 L 10.5 5 C 10.5 4.45 10.05 4 9.5 4 Z"/>
</svg>''',

    "screenshot-ui-area-symbolic": '''<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16">
  <path fill="currentColor" d="M 2 2 L 6 2 L 6 3.5 L 3.5 3.5 L 3.5 6 L 2 6 Z M 10 2 L 14 2 L 14 6 L 12.5 6 L 12.5 3.5 L 10 3.5 Z M 2 10 L 3.5 10 L 3.5 12.5 L 6 12.5 L 6 14 L 2 14 Z M 12.5 10 L 14 10 L 14 14 L 10 14 L 10 12.5 L 12.5 12.5 Z"/>
  <circle cx="8" cy="8" r="1.3" fill="currentColor"/>
</svg>''',

    "screenshot-ui-display-symbolic": '''<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16">
  <path fill="currentColor" fill-rule="evenodd" d="M 2 2 C 1.45 2 1 2.45 1 3 L 1 10 C 1 10.55 1.45 11 2 11 L 6.5 11 L 5.5 13.5 L 4 13.5 L 4 14.5 L 12 14.5 L 12 13.5 L 10.5 13.5 L 9.5 11 L 14 11 C 14.55 11 15 10.55 15 10 L 15 3 C 15 2.45 14.55 2 14 2 Z M 2.5 3.5 L 13.5 3.5 L 13.5 9.5 L 2.5 9.5 Z"/>
</svg>''',

    "screenshot-ui-window-symbolic": '''<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16">
  <path fill="currentColor" fill-rule="evenodd" d="M 2 2 C 1.45 2 1 2.45 1 3 L 1 13 C 1 13.55 1.45 14 2 14 L 14 14 C 14.55 14 15 13.55 15 13 L 15 3 C 15 2.45 14.55 2 14 2 Z M 2.5 5.5 L 13.5 5.5 L 13.5 12.5 L 2.5 12.5 Z M 3 3.8 C 3 4.2 3.3 4.5 3.7 4.5 C 4.1 4.5 4.4 4.2 4.4 3.8 C 4.4 3.4 4.1 3.1 3.7 3.1 C 3.3 3.1 3 3.4 3 3.8 Z M 5.2 3.8 C 5.2 4.2 5.5 4.5 5.9 4.5 C 6.3 4.5 6.6 4.2 6.6 3.8 C 6.6 3.4 6.3 3.1 5.9 3.1 C 5.5 3.1 5.2 3.4 5.2 3.8 Z M 7.4 3.8 C 7.4 4.2 7.7 4.5 8.1 4.5 C 8.5 4.5 8.8 4.2 8.8 3.8 C 8.8 3.4 8.5 3.1 8.1 3.1 C 7.7 3.1 7.4 3.4 7.4 3.8 Z"/>
</svg>''',

    # ---------------------------------------------------------------------
    # CCTV & Security Camera Symbolic
    # ---------------------------------------------------------------------
    "security-camera-symbolic": '''<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16">
  <!-- Body + lens ring as one evenodd path: the ring stays transparent, so it reads on light and dark. -->
  <path fill="currentColor" fill-rule="evenodd" d="M 2 4 C 1.4 4 1 4.4 1 5 L 1 11 C 1 11.6 1.4 12 2 12 L 10 12 L 14.5 14.5 C 14.8 14.7 15 14.5 15 14.2 L 15 5.8 C 15 5.5 14.8 5.3 14.5 5.5 L 10 8 L 10 5 C 10 4.4 9.6 4 9 4 Z M 5 6 A 2 2 0 1 0 5 10 A 2 2 0 1 0 5 6 Z M 5 7 A 1 1 0 1 0 5 9 A 1 1 0 1 0 5 7 Z"/>
</svg>''',

    "cctv-symbolic": '''<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16">
  <!-- Body + lens ring as one evenodd path: the ring stays transparent, so it reads on light and dark. -->
  <path fill="currentColor" fill-rule="evenodd" d="M 2 4 C 1.4 4 1 4.4 1 5 L 1 11 C 1 11.6 1.4 12 2 12 L 10 12 L 14.5 14.5 C 14.8 14.7 15 14.5 15 14.2 L 15 5.8 C 15 5.5 14.8 5.3 14.5 5.5 L 10 8 L 10 5 C 10 4.4 9.6 4 9 4 Z M 5 6 A 2 2 0 1 0 5 10 A 2 2 0 1 0 5 6 Z M 5 7 A 1 1 0 1 0 5 9 A 1 1 0 1 0 5 7 Z"/>
</svg>''',

    # ---------------------------------------------------------------------
    # Nautilus & GNOME Headerbar Actions & Navigation (High-Contrast Frost)
    # ---------------------------------------------------------------------
    "sidebar-show-symbolic": '''<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16">
  <path fill="currentColor" class="ColorScheme-Text" fill-rule="evenodd" d="M 2 2 C 1.45 2 1 2.45 1 3 L 1 13 C 1 13.55 1.45 14 2 14 L 14 14 C 14.55 14 15 13.55 15 13 L 15 3 C 15 2.45 14.55 2 14 2 Z M 2.5 3.5 L 6 3.5 L 6 12.5 L 2.5 12.5 Z M 7.5 3.5 L 13.5 3.5 L 13.5 12.5 L 7.5 12.5 Z"/>
</svg>''',

    "sidebar-show-symbolic-rtl": '''<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16">
  <path fill="currentColor" class="ColorScheme-Text" fill-rule="evenodd" d="M 2 2 C 1.45 2 1 2.45 1 3 L 1 13 C 1 13.55 1.45 14 2 14 L 14 14 C 14.55 14 15 13.55 15 13 L 15 3 C 15 2.45 14.55 2 14 2 Z M 2.5 3.5 L 8.5 3.5 L 8.5 12.5 L 2.5 12.5 Z M 10 3.5 L 13.5 3.5 L 13.5 12.5 L 10 12.5 Z"/>
</svg>''',

    "sidebar-show-right-symbolic": '''<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16">
  <path fill="currentColor" class="ColorScheme-Text" fill-rule="evenodd" d="M 2 2 C 1.45 2 1 2.45 1 3 L 1 13 C 1 13.55 1.45 14 2 14 L 14 14 C 14.55 14 15 13.55 15 13 L 15 3 C 15 2.45 14.55 2 14 2 Z M 2.5 3.5 L 8.5 3.5 L 8.5 12.5 L 2.5 12.5 Z M 10 3.5 L 13.5 3.5 L 13.5 12.5 L 10 12.5 Z"/>
</svg>''',

    "sidebar-show-right-symbolic-rtl": '''<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16">
  <path fill="currentColor" class="ColorScheme-Text" fill-rule="evenodd" d="M 2 2 C 1.45 2 1 2.45 1 3 L 1 13 C 1 13.55 1.45 14 2 14 L 14 14 C 14.55 14 15 13.55 15 13 L 15 3 C 15 2.45 14.55 2 14 2 Z M 2.5 3.5 L 6 3.5 L 6 12.5 L 2.5 12.5 Z M 7.5 3.5 L 13.5 3.5 L 13.5 12.5 L 7.5 12.5 Z"/>
</svg>''',

    "adw-sidebar-symbolic": '''<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16">
  <path fill="currentColor" class="ColorScheme-Text" fill-rule="evenodd" d="M 2 2 C 1.45 2 1 2.45 1 3 L 1 13 C 1 13.55 1.45 14 2 14 L 14 14 C 14.55 14 15 13.55 15 13 L 15 3 C 15 2.45 14.55 2 14 2 Z M 2.5 3.5 L 6 3.5 L 6 12.5 L 2.5 12.5 Z M 7.5 3.5 L 13.5 3.5 L 13.5 12.5 L 7.5 12.5 Z"/>
</svg>''',

    "adw-sidebar-symbolic-rtl": '''<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16">
  <path fill="currentColor" class="ColorScheme-Text" fill-rule="evenodd" d="M 2 2 C 1.45 2 1 2.45 1 3 L 1 13 C 1 13.55 1.45 14 2 14 L 14 14 C 14.55 14 15 13.55 15 13 L 15 3 C 15 2.45 14.55 2 14 2 Z M 2.5 3.5 L 8.5 3.5 L 8.5 12.5 L 2.5 12.5 Z M 10 3.5 L 13.5 3.5 L 13.5 12.5 L 10 12.5 Z"/>
</svg>''',

    "folder-new-symbolic": '''<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16">
  <path fill="currentColor" class="ColorScheme-Text" fill-rule="evenodd" d="M 2 2 C 1.45 2 1 2.45 1 3 L 1 13 C 1 13.55 1.45 14 2 14 L 8 14 L 8 12.5 L 2.5 12.5 L 2.5 5.5 L 13.5 5.5 L 13.5 8 L 15 8 L 15 5 C 15 4.45 14.55 4 14 4 L 8 4 L 6.5 2 Z M 12 9.5 L 12 11.5 L 10 11.5 L 10 13 L 12 13 L 12 15 L 13.5 15 L 13.5 13 L 15.5 13 L 15.5 11.5 L 13.5 11.5 L 13.5 9.5 Z"/>
</svg>''',

    "view-grid-symbolic": '''<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16">
  <rect x="2" y="2" width="5" height="5" rx="1" fill="currentColor" class="ColorScheme-Text"/>
  <rect x="9" y="2" width="5" height="5" rx="1" fill="currentColor" class="ColorScheme-Text"/>
  <rect x="2" y="9" width="5" height="5" rx="1" fill="currentColor" class="ColorScheme-Text"/>
  <rect x="9" y="9" width="5" height="5" rx="1" fill="currentColor" class="ColorScheme-Text"/>
</svg>''',

    "view-list-symbolic": '''<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16">
  <rect x="2" y="2" width="3" height="3" rx="0.8" fill="currentColor" class="ColorScheme-Text"/>
  <rect x="6.5" y="2.5" width="7.5" height="2" rx="0.8" fill="currentColor" class="ColorScheme-Text"/>
  <rect x="2" y="6.5" width="3" height="3" rx="0.8" fill="currentColor" class="ColorScheme-Text"/>
  <rect x="6.5" y="7" width="7.5" height="2" rx="0.8" fill="currentColor" class="ColorScheme-Text"/>
  <rect x="2" y="11" width="3" height="3" rx="0.8" fill="currentColor" class="ColorScheme-Text"/>
  <rect x="6.5" y="11.5" width="7.5" height="2" rx="0.8" fill="currentColor" class="ColorScheme-Text"/>
</svg>''',

    "view-list-bullet-symbolic": '''<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16">
  <circle cx="3.5" cy="3.5" r="1.5" fill="currentColor" class="ColorScheme-Text"/>
  <rect x="6.5" y="2.5" width="7.5" height="2" rx="0.8" fill="currentColor" class="ColorScheme-Text"/>
  <circle cx="3.5" cy="8" r="1.5" fill="currentColor" class="ColorScheme-Text"/>
  <rect x="6.5" y="7" width="7.5" height="2" rx="0.8" fill="currentColor" class="ColorScheme-Text"/>
  <circle cx="3.5" cy="12.5" r="1.5" fill="currentColor" class="ColorScheme-Text"/>
  <rect x="6.5" y="11.5" width="7.5" height="2" rx="0.8" fill="currentColor" class="ColorScheme-Text"/>
</svg>''',

    "view-list-ordered-symbolic": '''<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16">
  <rect x="2" y="2" width="3" height="3" rx="0.8" fill="currentColor" class="ColorScheme-Text"/>
  <rect x="6.5" y="2.5" width="7.5" height="2" rx="0.8" fill="currentColor" class="ColorScheme-Text"/>
  <rect x="2" y="6.5" width="3" height="3" rx="0.8" fill="currentColor" class="ColorScheme-Text"/>
  <rect x="6.5" y="7" width="7.5" height="2" rx="0.8" fill="currentColor" class="ColorScheme-Text"/>
  <rect x="2" y="11" width="3" height="3" rx="0.8" fill="currentColor" class="ColorScheme-Text"/>
  <rect x="6.5" y="11.5" width="7.5" height="2" rx="0.8" fill="currentColor" class="ColorScheme-Text"/>
</svg>''',

    "view-more-symbolic": '''<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16">
  <circle cx="8" cy="3" r="1.8" fill="currentColor" class="ColorScheme-Text"/>
  <circle cx="8" cy="8" r="1.8" fill="currentColor" class="ColorScheme-Text"/>
  <circle cx="8" cy="13" r="1.8" fill="currentColor" class="ColorScheme-Text"/>
</svg>''',

    "view-more-horizontal-symbolic": '''<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16">
  <circle cx="3" cy="8" r="1.8" fill="currentColor" class="ColorScheme-Text"/>
  <circle cx="8" cy="8" r="1.8" fill="currentColor" class="ColorScheme-Text"/>
  <circle cx="13" cy="8" r="1.8" fill="currentColor" class="ColorScheme-Text"/>
</svg>''',

    "pan-down-symbolic": '''<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16">
  <path fill="currentColor" class="ColorScheme-Text" fill-rule="evenodd" d="M 3.3 6.3 C 3.7 5.9 4.3 5.9 4.7 6.3 L 8 9.6 L 11.3 6.3 C 11.7 5.9 12.3 5.9 12.7 6.3 C 13.1 6.7 13.1 7.3 12.7 7.7 L 8.7 11.7 C 8.3 12.1 7.7 12.1 7.3 11.7 L 3.3 7.7 C 2.9 7.3 2.9 6.7 3.3 6.3 Z"/>
</svg>''',

    "pan-up-symbolic": '''<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16">
  <path fill="currentColor" class="ColorScheme-Text" fill-rule="evenodd" d="M 3.3 9.7 C 3.7 10.1 4.3 10.1 4.7 9.7 L 8 6.4 L 11.3 9.7 C 11.7 10.1 12.3 10.1 12.7 9.7 C 13.1 9.3 13.1 8.7 12.7 8.3 L 8.7 4.3 C 8.3 3.9 7.7 3.9 7.3 4.3 L 3.3 8.3 C 2.9 8.7 2.9 9.3 3.3 9.7 Z"/>
</svg>''',

    "pan-start-symbolic": '''<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16">
  <path fill="currentColor" class="ColorScheme-Text" fill-rule="evenodd" d="M 9.7 3.3 C 10.1 3.7 10.1 4.3 9.7 4.7 L 6.4 8 L 9.7 11.3 C 10.1 11.7 10.1 12.3 9.7 12.7 C 9.3 13.1 8.7 13.1 8.3 12.7 L 4.3 8.7 C 3.9 8.3 3.9 7.7 4.3 7.3 L 8.3 3.3 C 8.7 2.9 9.3 2.9 9.7 3.3 Z"/>
</svg>''',

    "pan-end-symbolic": '''<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16">
  <path fill="currentColor" class="ColorScheme-Text" fill-rule="evenodd" d="M 6.3 3.3 C 6.7 2.9 7.3 2.9 7.7 3.3 L 11.7 7.3 C 12.1 7.7 12.1 8.3 11.7 8.7 L 7.7 12.7 C 7.3 13.1 6.7 13.1 6.3 12.7 C 5.9 12.3 5.9 11.7 6.3 11.3 L 9.6 8 L 6.3 4.7 C 5.9 4.3 5.9 3.7 6.3 3.3 Z"/>
</svg>''',

    "go-previous-symbolic": '''<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16">
  <path fill="currentColor" class="ColorScheme-Text" fill-rule="evenodd" d="M 9.7 2.3 C 10.1 2.7 10.1 3.3 9.7 3.7 L 5.4 8 L 9.7 12.3 C 10.1 12.7 10.1 13.3 9.7 13.7 C 9.3 14.1 8.7 14.1 8.3 13.7 L 3.3 8.7 C 2.9 8.3 2.9 7.7 3.3 7.3 L 8.3 2.3 C 8.7 1.9 9.3 1.9 9.7 2.3 Z"/>
</svg>''',

    "go-next-symbolic": '''<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16">
  <path fill="currentColor" class="ColorScheme-Text" fill-rule="evenodd" d="M 6.3 2.3 C 6.7 1.9 7.3 1.9 7.7 2.3 L 12.7 7.3 C 13.1 7.7 13.1 8.3 12.7 8.7 L 7.7 13.7 C 7.3 14.1 6.7 14.1 6.3 13.7 C 5.9 13.3 5.9 12.7 6.3 12.3 L 10.6 8 L 6.3 3.7 C 5.9 3.3 5.9 2.7 6.3 2.3 Z"/>
</svg>''',

    # ---------------------------------------------------------------------
    # Window Controls Suite (Crisp High-Definition Vectors)
    # ---------------------------------------------------------------------
    "window-minimize-symbolic": '''<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16">
  <rect x="3" y="7.2" width="10" height="1.6" rx="0.8" fill="currentColor" class="ColorScheme-Text"/>
</svg>''',

    "window-maximize-symbolic": '''<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16">
  <path fill="currentColor" class="ColorScheme-Text" fill-rule="evenodd" d="M 3.5 3 C 2.67 3 2 3.67 2 4.5 L 2 11.5 C 2 12.33 2.67 13 3.5 13 L 12.5 13 C 13.33 13 14 12.33 14 11.5 L 14 4.5 C 14 3.67 13.33 3 12.5 3 Z M 3.8 4.8 L 12.2 4.8 L 12.2 11.2 L 3.8 11.2 Z"/>
</svg>''',

    "window-restore-symbolic": '''<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16">
  <path fill="currentColor" class="ColorScheme-Text" fill-rule="evenodd" d="M 5 2 C 4.45 2 4 2.45 4 3 L 4 4 L 3 4 C 2.45 4 2 4.45 2 5 L 2 13 C 2 13.55 2.45 14 3 14 L 11 14 C 11.55 14 12 13.55 12 13 L 12 12 L 13 12 C 13.55 12 14 11.55 14 11 L 14 3 C 14 2.45 13.55 2 13 2 Z M 3.6 5.6 L 10.4 5.6 L 10.4 12.4 L 3.6 12.4 Z M 12.4 3.6 L 12.4 10.4 L 11.8 10.4 L 11.8 5 C 11.8 4.45 11.35 4 10.8 4 L 5.4 4 L 5.4 3.6 Z"/>
</svg>''',

    "window-close-symbolic": '''<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16">
  <path fill="currentColor" class="ColorScheme-Text" d="M 3.7 2.3 C 3.3 1.9 2.7 1.9 2.3 2.3 C 1.9 2.7 1.9 3.3 2.3 3.7 L 6.6 8 L 2.3 12.3 C 1.9 12.7 1.9 13.3 2.3 13.7 C 2.7 14.1 3.3 14.1 3.7 13.7 L 8 9.4 L 12.3 13.7 C 12.7 14.1 13.3 14.1 13.7 13.7 C 14.1 13.3 14.1 12.7 13.7 12.3 L 9.4 8 L 13.7 3.7 C 14.1 3.3 14.1 2.7 13.7 2.3 C 13.3 1.9 12.7 1.9 12.3 2.3 L 8 6.6 Z"/>
</svg>''',

    # ---------------------------------------------------------------------
    # Nautilus Search, Progress & Menu Actions (High-Contrast Frost)
    # ---------------------------------------------------------------------
    "cancel-operation-symbolic": '''<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16">
  <path fill="currentColor" class="ColorScheme-Text" d="M 3.7 2.3 C 3.3 1.9 2.7 1.9 2.3 2.3 C 1.9 2.7 1.9 3.3 2.3 3.7 L 6.6 8 L 2.3 12.3 C 1.9 12.7 1.9 13.3 2.3 13.7 C 2.7 14.1 3.3 14.1 3.7 13.7 L 8 9.4 L 12.3 13.7 C 12.7 14.1 13.3 14.1 13.7 13.7 C 14.1 13.3 14.1 12.7 13.7 12.3 L 9.4 8 L 13.7 3.7 C 14.1 3.3 14.1 2.7 13.7 2.3 C 13.3 1.9 12.7 1.9 12.3 2.3 L 8 6.6 Z"/>
</svg>''',

    "process-stop-symbolic": '''<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16">
  <path fill="currentColor" class="ColorScheme-Text" d="M 3.7 2.3 C 3.3 1.9 2.7 1.9 2.3 2.3 C 1.9 2.7 1.9 3.3 2.3 3.7 L 6.6 8 L 2.3 12.3 C 1.9 12.7 1.9 13.3 2.3 13.7 C 2.7 14.1 3.3 14.1 3.7 13.7 L 8 9.4 L 12.3 13.7 C 12.7 14.1 13.3 14.1 13.7 13.7 C 14.1 13.3 14.1 12.7 13.7 12.3 L 9.4 8 L 13.7 3.7 C 14.1 3.3 14.1 2.7 13.7 2.3 C 13.3 1.9 12.7 1.9 12.3 2.3 L 8 6.6 Z"/>
</svg>''',

    "edit-find-symbolic": '''<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16">
  <path fill="currentColor" class="ColorScheme-Text" fill-rule="evenodd" d="M 6.5 1.5 C 3.74 1.5 1.5 3.74 1.5 6.5 C 1.5 9.26 3.74 11.5 6.5 11.5 C 7.74 11.5 8.87 11.05 9.76 10.3 L 13.23 13.77 C 13.62 14.16 14.25 14.16 14.64 13.77 C 15.03 13.38 15.03 12.75 14.64 12.36 L 11.17 8.89 C 11.38 8.16 11.5 7.35 11.5 6.5 C 11.5 3.74 9.26 1.5 6.5 1.5 Z M 3 6.5 C 3 4.57 4.57 3 6.5 3 C 8.43 3 10 4.57 10 6.5 C 10 8.43 8.43 10 6.5 10 C 4.57 10 3 8.43 3 6.5 Z"/>
</svg>''',

    "nautilus-folder-search-symbolic": '''<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16">
  <path fill="currentColor" class="ColorScheme-Text" fill-rule="evenodd" d="M 2 2 C 1.45 2 1 2.45 1 3 L 1 13 C 1 13.55 1.45 14 2 14 L 14 14 C 14.55 14 15 13.55 15 13 L 15 5 C 15 4.45 14.55 4 14 4 L 8 4 L 6.5 2 Z M 2.5 5.5 L 13.5 5.5 L 13.5 12.5 L 2.5 12.5 Z M 7.5 6.5 C 6.4 6.5 5.5 7.4 5.5 8.5 C 5.5 9.6 6.4 10.5 7.5 10.5 C 7.9 10.5 8.3 10.4 8.6 10.1 L 10.5 12 L 11.5 11 L 9.6 9.1 C 9.8 8.8 10 8.4 10 8.5 C 10 7.4 9.1 6.5 8 6.5 Z M 7.5 7.5 C 8.05 7.5 8.5 7.95 8.5 8.5 C 8.5 9.05 8.05 9.5 7.5 9.5 C 6.95 9.5 6.5 9.05 6.5 8.5 C 6.5 7.95 6.95 7.5 7.5 7.5 Z"/>
</svg>''',

    "open-menu-symbolic": '''<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16">
  <path fill="currentColor" class="ColorScheme-Text" d="M 2 3 C 1.45 3 1 3.45 1 4 C 1 4.55 1.45 5 2 5 L 14 5 C 14.55 5 15 4.55 15 4 C 15 3.45 14.55 3 14 3 Z M 2 7.5 C 1.45 7.5 1 7.95 1 8.5 C 1 9.05 1.45 9.5 2 9.5 L 14 9.5 C 14.55 9.5 15 9.05 15 8.5 C 15 7.95 14.55 7.5 14 7.5 Z M 2 12 C 1.45 12 1 12.45 1 13 C 1 13.55 1.45 14 2 14 L 14 14 C 14.55 14 15 13.55 15 13 C 15 12.45 14.55 12 14 12 Z"/>
</svg>''',

    "org.gnome.Nautilus-symbolic": '''<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16">
  <path fill="currentColor" class="ColorScheme-Text" fill-rule="evenodd" d="M 2 2 C 1.45 2 1 2.45 1 3 L 1 13 C 1 13.55 1.45 14 2 14 L 14 14 C 14.55 14 15 13.55 15 13 L 15 5 C 15 4.45 14.55 4 14 4 L 8 4 L 6.5 2 Z M 2.5 5.5 L 13.5 5.5 L 13.5 12.5 L 2.5 12.5 Z"/>
</svg>''',

    "system-file-manager-symbolic": '''<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16">
  <path fill="currentColor" class="ColorScheme-Text" fill-rule="evenodd" d="M 2 2 C 1.45 2 1 2.45 1 3 L 1 13 C 1 13.55 1.45 14 2 14 L 14 14 C 14.55 14 15 13.55 15 13 L 15 5 C 15 4.45 14.55 4 14 4 L 8 4 L 6.5 2 Z M 2.5 5.5 L 13.5 5.5 L 13.5 12.5 L 2.5 12.5 Z"/>
</svg>''',

    "bookmark-new-symbolic": '''<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16">
  <path fill="currentColor" class="ColorScheme-Text" fill-rule="evenodd" d="M 3 2 C 2.45 2 2 2.45 2 3 L 2 14 L 7 11.5 L 12 14 L 12 7 L 10.5 7 L 10.5 11.7 L 7 9.9 L 3.5 11.7 L 3.5 3.5 L 8 3.5 L 8 2 Z M 11.5 1 L 11.5 3 L 9.5 3 L 9.5 4.5 L 11.5 4.5 L 11.5 6.5 L 13 6.5 L 13 4.5 L 15 4.5 L 15 3 L 13 3 L 13 1 Z"/>
</svg>''',

    "folder-documents-symbolic": '''<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16">
  <path fill="currentColor" class="ColorScheme-Text" fill-rule="evenodd" d="M 3 1 C 2.45 1 2 1.45 2 2 L 2 14 C 2 14.55 2.45 15 3 15 L 13 15 C 13.55 15 14 14.55 14 14 L 14 5 L 10 1 Z M 3.5 2.5 L 9 2.5 L 9 5.5 L 12.5 5.5 L 12.5 13.5 L 3.5 13.5 Z M 5 7 L 11 7 L 11 8.2 L 5 8.2 Z M 5 9.5 L 11 9.5 L 11 10.7 L 5 10.7 Z M 5 12 L 9 12 L 9 13.2 L 5 13.2 Z"/>
</svg>''',

    "folder-download-symbolic": '''<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16">
  <path fill="currentColor" class="ColorScheme-Text" fill-rule="evenodd" d="M 2 2 C 1.45 2 1 2.45 1 3 L 1 13 C 1 13.55 1.45 14 2 14 L 14 14 C 14.55 14 15 13.55 15 13 L 15 5 C 15 4.45 14.55 4 14 4 L 8 4 L 6.5 2 Z M 2.5 5.5 L 13.5 5.5 L 13.5 12.5 L 2.5 12.5 Z M 8 6 L 8 9.5 L 6.5 9.5 L 8.5 11.5 L 10.5 9.5 L 9 9.5 L 9 6 Z"/>
</svg>''',

    "folder-music-symbolic": '''<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16">
  <path fill="currentColor" class="ColorScheme-Text" fill-rule="evenodd" d="M 2 2 C 1.45 2 1 2.45 1 3 L 1 13 C 1 13.55 1.45 14 2 14 L 14 14 C 14.55 14 15 13.55 15 13 L 15 5 C 15 4.45 14.55 4 14 4 L 8 4 L 6.5 2 Z M 2.5 5.5 L 13.5 5.5 L 13.5 12.5 L 2.5 12.5 Z M 7 6 L 11 6 L 11 7 L 8.5 7 L 8.5 10.5 C 8.5 11.3 7.8 12 7 12 C 6.2 12 5.5 11.3 5.5 10.5 C 5.5 9.7 6.2 9 7 9 L 7.5 9 L 7.5 7 L 7 7 Z"/>
</svg>''',

    "folder-pictures-symbolic": '''<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16">
  <path fill="currentColor" class="ColorScheme-Text" fill-rule="evenodd" d="M 2 2 C 1.45 2 1 2.45 1 3 L 1 13 C 1 13.55 1.45 14 2 14 L 14 14 C 14.55 14 15 13.55 15 13 L 15 5 C 15 4.45 14.55 4 14 4 L 8 4 L 6.5 2 Z M 2.5 5.5 L 13.5 5.5 L 13.5 12.5 L 2.5 12.5 Z M 5.5 7 C 4.95 7 4.5 7.45 4.5 8 C 4.5 8.55 4.95 9 5.5 9 C 6.05 9 6.5 8.55 6.5 8 C 6.5 7.45 6.05 7 5.5 7 Z M 12 11.5 L 4 11.5 L 6.5 8.5 L 8.5 10.5 L 10 9 Z"/>
</svg>''',

    "folder-videos-symbolic": '''<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16">
  <path fill="currentColor" class="ColorScheme-Text" fill-rule="evenodd" d="M 2 2 C 1.45 2 1 2.45 1 3 L 1 13 C 1 13.55 1.45 14 2 14 L 14 14 C 14.55 14 15 13.55 15 13 L 15 5 C 15 4.45 14.55 4 14 4 L 8 4 L 6.5 2 Z M 2.5 5.5 L 13.5 5.5 L 13.5 12.5 L 2.5 12.5 Z M 6.5 7 L 10.5 9 L 6.5 11 Z"/>
</svg>''',

    "folder-projects-symbolic": '''<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16">
  <path fill="currentColor" class="ColorScheme-Text" fill-rule="evenodd" d="M 2 2 C 1.45 2 1 2.45 1 3 L 1 13 C 1 13.55 1.45 14 2 14 L 14 14 C 14.55 14 15 13.55 15 13 L 15 5 C 15 4.45 14.55 4 14 4 L 8 4 L 6.5 2 Z M 2.5 5.5 L 13.5 5.5 L 13.5 12.5 L 2.5 12.5 Z M 6 7.5 L 4.5 9 L 6 10.5 L 5 11.5 L 2.5 9 L 5 6.5 Z M 10 7.5 L 11.5 9 L 10 10.5 L 11 11.5 L 13.5 9 L 11 6.5 Z"/>
</svg>''',

    "folder-publicshare-symbolic": '''<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16">
  <path fill="currentColor" class="ColorScheme-Text" fill-rule="evenodd" d="M 2 2 C 1.45 2 1 2.45 1 3 L 1 13 C 1 13.55 1.45 14 2 14 L 14 14 C 14.55 14 15 13.55 15 13 L 15 5 C 15 4.45 14.55 4 14 4 L 8 4 L 6.5 2 Z M 2.5 5.5 L 13.5 5.5 L 13.5 12.5 L 2.5 12.5 Z M 8 7 C 7.2 7 6.5 7.7 6.5 8.5 C 6.5 9.3 7.2 10 8 10 C 8.8 10 9.5 9.3 9.5 8.5 C 9.5 7.7 8.8 7 8 7 Z M 5.5 11.5 C 5.5 10.5 7 10 8 10 C 9 10 10.5 10.5 10.5 11.5 L 5.5 11.5 Z"/>
</svg>''',

    "folder-templates-symbolic": '''<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16">
  <path fill="currentColor" class="ColorScheme-Text" fill-rule="evenodd" d="M 2 2 C 1.45 2 1 2.45 1 3 L 1 13 C 1 13.55 1.45 14 2 14 L 14 14 C 14.55 14 15 13.55 15 13 L 15 5 C 15 4.45 14.55 4 14 4 L 8 4 L 6.5 2 Z M 2.5 5.5 L 13.5 5.5 L 13.5 12.5 L 2.5 12.5 Z M 5 7 L 11 7 L 11 8 L 5 8 Z M 5 9 L 9 9 L 9 10 L 5 10 Z"/>
</svg>''',

    "user-desktop-symbolic": '''<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16">
  <path fill="currentColor" class="ColorScheme-Text" fill-rule="evenodd" d="M 2 2 C 1.45 2 1 2.45 1 3 L 1 11 C 1 11.55 1.45 12 2 12 L 6.5 12 L 5.5 14 L 4 14 L 4 15 L 12 15 L 12 14 L 10.5 14 L 9.5 12 L 14 12 C 14.55 12 15 11.55 15 11 L 15 3 C 15 2.45 14.55 2 14 2 Z M 2.5 3.5 L 13.5 3.5 L 13.5 10.5 L 2.5 10.5 Z"/>
</svg>''',

    "user-trash-full-symbolic": '''<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16">
  <path fill="currentColor" class="ColorScheme-Text" d="M 3 4 L 13 4 L 11.5 14 L 4.5 14 Z M 5 2 L 11 2 L 12 3 L 4 3 Z M 6 6 L 7 6 L 7 12 L 6 12 Z M 9 6 L 10 6 L 10 12 L 9 12 Z"/>
</svg>''',

    "non-starred-symbolic": '''<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16">
  <path fill="currentColor" class="ColorScheme-Text" fill-rule="evenodd" d="M 8 2.5 L 9.7 6.2 L 13.7 6.6 L 10.7 9.4 L 11.5 13.3 L 8 11.3 L 4.5 13.3 L 5.3 9.4 L 2.3 6.6 L 6.3 6.2 Z M 8 4.7 L 7 7 L 4.5 7.2 L 6.4 8.9 L 5.8 11.4 L 8 10.1 L 10.2 11.4 L 9.6 8.9 L 11.5 7.2 L 9 7 Z"/>
</svg>''',

    # ---------------------------------------------------------------------
    # Form Controls: Checkbox, Radio, and Selection Indicators
    # ---------------------------------------------------------------------
    "object-select-symbolic": '''<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16">
  <path fill="currentColor" class="ColorScheme-Text" d="M 6.2 12.8 L 1.7 8.3 L 3.1 6.9 L 6.2 10 L 12.9 3.3 L 14.3 4.7 Z"/>
</svg>''',

    "check-plain-symbolic": '''<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16">
  <path fill="currentColor" class="ColorScheme-Text" d="M 6.2 12.8 L 1.7 8.3 L 3.1 6.9 L 6.2 10 L 12.9 3.3 L 14.3 4.7 Z"/>
</svg>''',

    "checkbox-checked-symbolic": '''<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16">
  <path fill="currentColor" class="ColorScheme-Text" fill-rule="evenodd" d="M 2 2 C 1.45 2 1 2.45 1 3 L 1 13 C 1 13.55 1.45 14 2 14 L 14 14 C 14.55 14 15 13.55 15 13 L 15 3 C 15 2.45 14.55 2 14 2 Z M 6.4 11.2 L 3.2 8 L 4.6 6.6 L 6.4 8.4 L 11.4 3.4 L 12.8 4.8 Z"/>
</svg>''',

    "checkbox-symbolic": '''<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16">
  <path fill="currentColor" class="ColorScheme-Text" fill-rule="evenodd" d="M 2 2 C 1.45 2 1 2.45 1 3 L 1 13 C 1 13.55 1.45 14 2 14 L 14 14 C 14.55 14 15 13.55 15 13 L 15 3 C 15 2.45 14.55 2 14 2 Z M 2.5 3.5 L 13.5 3.5 L 13.5 12.5 L 2.5 12.5 Z"/>
</svg>''',

    "checkbox-mixed-symbolic": '''<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16">
  <path fill="currentColor" class="ColorScheme-Text" fill-rule="evenodd" d="M 2 2 C 1.45 2 1 2.45 1 3 L 1 13 C 1 13.55 1.45 14 2 14 L 14 14 C 14.55 14 15 13.55 15 13 L 15 3 C 15 2.45 14.55 2 14 2 Z M 4 7 L 12 7 L 12 9 L 4 9 Z"/>
</svg>''',

    "dash-symbolic": '''<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16">
  <rect x="3" y="7" width="10" height="2" rx="0.8" fill="currentColor" class="ColorScheme-Text"/>
</svg>''',

    "radio-checked-symbolic": '''<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16">
  <path fill="currentColor" class="ColorScheme-Text" fill-rule="evenodd" d="M 8 1 C 4.13 1 1 4.13 1 8 C 1 11.87 4.13 15 8 15 C 11.87 15 15 11.87 15 8 C 15 4.13 11.87 1 8 1 Z M 8 2.5 C 11.04 2.5 13.5 4.96 13.5 8 C 13.5 11.04 11.04 13.5 8 13.5 C 4.96 13.5 2.5 11.04 2.5 8 C 2.5 4.96 4.96 2.5 8 2.5 Z M 8 5 C 6.34 5 5 6.34 5 8 C 5 9.66 6.34 11 8 11 C 9.66 11 11 9.66 11 8 C 11 6.34 9.66 5 8 5 Z"/>
</svg>''',

    "radio-symbolic": '''<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16">
  <path fill="currentColor" class="ColorScheme-Text" fill-rule="evenodd" d="M 8 1 C 4.13 1 1 4.13 1 8 C 1 11.87 4.13 15 8 15 C 11.87 15 15 11.87 15 8 C 15 4.13 11.87 1 8 1 Z M 8 2.5 C 11.04 2.5 13.5 4.96 13.5 8 C 13.5 11.04 11.04 13.5 8 13.5 C 4.96 13.5 2.5 11.04 2.5 8 C 2.5 4.96 4.96 2.5 8 2.5 Z"/>
</svg>''',

    "bullet-symbolic": '''<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16">
  <circle cx="8" cy="8" r="3.5" fill="currentColor" class="ColorScheme-Text"/>
</svg>''',

    # ---------------------------------------------------------------------
    # Shelly Package Manager & Tartube Symbolic
    # ---------------------------------------------------------------------
    "shelly-symbolic": '''<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16">
  <path fill="currentColor" class="ColorScheme-Text" fill-rule="evenodd" d="M 8 1.5 C 5.5 1.5 3.5 3.5 3.5 6 C 3.5 7.8 4.6 9.3 6.1 10 L 5 14 L 8 12.8 L 11 14 L 9.9 10 C 11.4 9.3 12.5 7.8 12.5 6 C 12.5 3.5 10.5 1.5 8 1.5 Z M 8 3 C 9.65 3 11 4.35 11 6 C 11 7.65 9.65 9 8 9 C 6.35 9 5 7.65 5 6 C 5 4.35 6.35 3 8 3 Z"/>
</svg>''',

    "shelly-shell-symbolic": '''<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16">
  <path fill="currentColor" class="ColorScheme-Text" fill-rule="evenodd" d="M 8 1.5 C 5.5 1.5 3.5 3.5 3.5 6 C 3.5 7.8 4.6 9.3 6.1 10 L 5 14 L 8 12.8 L 11 14 L 9.9 10 C 11.4 9.3 12.5 7.8 12.5 6 C 12.5 3.5 10.5 1.5 8 1.5 Z M 8 3 C 9.65 3 11 4.35 11 6 C 11 7.65 9.65 9 8 9 C 6.35 9 5 7.65 5 6 C 5 4.35 6.35 3 8 3 Z"/>
</svg>''',

    "shelly-updates-symbolic": '''<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16">
  <path fill="currentColor" class="ColorScheme-Text" fill-rule="evenodd" d="M 8 1 C 4.13 1 1 4.13 1 8 C 1 11.87 4.13 15 8 15 C 11.87 15 15 11.87 15 8 C 15 4.13 11.87 1 8 1 Z M 8 2.5 C 11.04 2.5 13.5 4.96 13.5 8 C 13.5 11.04 11.04 13.5 8 13.5 C 4.96 13.5 2.5 11.04 2.5 8 C 2.5 4.96 4.96 2.5 8 2.5 Z M 7.2 4.5 L 8.8 4.5 L 8.8 8.5 L 11 8.5 L 8 11.5 L 5 8.5 L 7.2 8.5 Z"/>
</svg>''',

    "tartube-tray": '''<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16">
  <path fill="currentColor" class="ColorScheme-Text" fill-rule="evenodd" d="M 2 3 C 1.45 3 1 3.45 1 4 L 1 12 C 1 12.55 1.45 13 2 13 L 14 13 C 14.55 13 15 12.55 15 12 L 15 4 C 15 3.45 14.55 3 14 3 Z M 6.5 5.5 L 10.5 8 L 6.5 10.5 Z"/>
</svg>''',

    "tartube-download-tray": '''<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16">
  <path fill="currentColor" class="ColorScheme-Text" fill-rule="evenodd" d="M 2 3 C 1.45 3 1 3.45 1 4 L 1 12 C 1 12.55 1.45 13 2 13 L 14 13 C 14.55 13 15 12.55 15 12 L 15 4 C 15 3.45 14.55 3 14 3 Z M 7.2 5 L 8.8 5 L 8.8 8 L 10.5 8 L 8 10.5 L 5.5 8 L 7.2 8 Z"/>
</svg>''',

    "tartube-update-tray": '''<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16">
  <path fill="currentColor" class="ColorScheme-Text" fill-rule="evenodd" d="M 2 3 C 1.45 3 1 3.45 1 4 L 1 12 C 1 12.55 1.45 13 2 13 L 14 13 C 14.55 13 15 12.55 15 12 L 15 4 C 15 3.45 14.55 3 14 3 Z M 7.2 6.5 L 8.8 6.5 L 8.8 10 L 10.5 10 L 8 12.5 L 5.5 10 L 7.2 10 Z"/>
</svg>''',

    "tartube-check-tray": '''<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16">
  <path fill="currentColor" class="ColorScheme-Text" fill-rule="evenodd" d="M 2 3 C 1.45 3 1 3.45 1 4 L 1 12 C 1 12.55 1.45 13 2 13 L 14 13 C 14.55 13 15 12.55 15 12 L 15 4 C 15 3.45 14.55 3 14 3 Z M 6.8 9.5 L 4.5 7.2 L 5.5 6.2 L 6.8 7.5 L 10.5 3.8 L 11.5 4.8 Z"/>
</svg>''',


}

# Core FreeDesktop names that previously fell through to Adwaita. Same filled-silhouette rules:
# currentColor only, no stroked outlines, evenodd used to knock detail out of a solid shape.
EXTENDED_SYMBOLIC_ICONS.update({
    "folder-symbolic": '''<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16">
  <path fill="currentColor" d="M 1.5 3 C 1.22 3 1 3.22 1 3.5 L 1 12.5 C 1 12.78 1.22 13 1.5 13 L 14.5 13 C 14.78 13 15 12.78 15 12.5 L 15 5.5 C 15 5.22 14.78 5 14.5 5 L 8.2 5 L 6.4 3 Z"/>
</svg>''',

    "folder-open-symbolic": '''<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16">
  <path fill="currentColor" d="M 1 3.5 L 6 3.5 L 7.5 5 L 14.5 5 L 14.5 9.5 L 1.5 9.5 Z M 1.5 8.5 L 15 8.5 L 13 13.5 L 0.5 13.5 Z"/>
</svg>''',

    "edit-copy-symbolic": '''<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16">
  <path fill="currentColor" d="M 5 1 C 4.45 1 4 1.45 4 2 L 4 10 C 4 10.55 4.45 11 5 11 L 12 11 C 12.55 11 13 10.55 13 10 L 13 2 C 13 1.45 12.55 1 12 1 Z M 2 4 L 2 12.5 C 2 13.88 3.12 15 4.5 15 L 11 15 L 11 13.5 L 4.5 13.5 C 3.95 13.5 3.5 13.05 3.5 12.5 L 3.5 4 Z"/>
</svg>''',

    "edit-paste-symbolic": '''<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16">
  <path fill="currentColor" fill-rule="evenodd" d="M 6 1 C 5.45 1 5 1.45 5 2 L 5 3 L 3.5 3 C 3.22 3 3 3.22 3 3.5 L 3 14.5 C 3 14.78 3.22 15 3.5 15 L 12.5 15 C 12.78 15 13 14.78 13 14.5 L 13 3.5 C 13 3.22 12.78 3 12.5 3 L 11 3 L 11 2 C 11 1.45 10.55 1 10 1 Z M 5 7 L 11 7 L 11 8.3 L 5 8.3 Z M 5 10 L 11 10 L 11 11.3 L 5 11.3 Z"/>
</svg>''',

    "edit-delete-symbolic": '''<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16">
  <path fill="currentColor" fill-rule="evenodd" d="M 6 1 L 10 1 L 10.8 2.2 L 13.5 2.2 L 13.5 3.7 L 2.5 3.7 L 2.5 2.2 L 5.2 2.2 Z M 3.4 4.8 L 12.6 4.8 L 11.7 14.2 C 11.63 14.68 11.25 15 10.77 15 L 5.23 15 C 4.75 15 4.37 14.68 4.3 14.2 Z M 6 6.6 L 7.2 6.6 L 7.2 13 L 6 13 Z M 8.8 6.6 L 10 6.6 L 10 13 L 8.8 13 Z"/>
</svg>''',

    "document-open-symbolic": '''<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16">
  <path fill="currentColor" fill-rule="evenodd" d="M 3 1 L 9 1 L 13 5 L 13 15 L 3 15 Z M 9 1.6 L 12.4 5 L 9 5 Z M 4.8 9.2 L 8.2 9.2 L 8.2 7.8 L 11.6 10 L 8.2 12.2 L 8.2 10.8 L 4.8 10.8 Z"/>
</svg>''',

    "document-save-symbolic": '''<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16">
  <path fill="currentColor" fill-rule="evenodd" d="M 3 1 L 9 1 L 13 5 L 13 15 L 3 15 Z M 9 1.6 L 12.4 5 L 9 5 Z M 7.1 6.4 L 8.9 6.4 L 8.9 9.6 L 10.6 9.6 L 8 12.2 L 5.4 9.6 L 7.1 9.6 Z M 4.4 13 L 11.6 13 L 11.6 14.4 L 4.4 14.4 Z"/>
</svg>''',

    "view-refresh-symbolic": '''<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16">
  <path fill="currentColor" d="M 8 1.5 C 11.6 1.5 14.5 4.4 14.5 8 L 12.8 8 C 12.8 5.34 10.66 3.2 8 3.2 C 6.6 3.2 5.35 3.8 4.45 4.75 L 6.5 6.8 L 1.5 6.8 L 1.5 1.8 L 3.55 3.85 C 4.7 2.6 6.25 1.5 8 1.5 Z M 3.2 8 C 3.2 10.66 5.34 12.8 8 12.8 C 9.4 12.8 10.65 12.2 11.55 11.25 L 9.5 9.2 L 14.5 9.2 L 14.5 14.2 L 12.45 12.15 C 11.3 13.4 9.75 14.5 8 14.5 C 4.4 14.5 1.5 11.6 1.5 8 Z"/>
</svg>''',

    "emblem-important-symbolic": '''<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16">
  <path fill="currentColor" fill-rule="evenodd" d="M 8 1 C 11.87 1 15 4.13 15 8 C 15 11.87 11.87 15 8 15 C 4.13 15 1 11.87 1 8 C 1 4.13 4.13 1 8 1 Z M 7.1 4 L 8.9 4 L 8.55 9.2 L 7.45 9.2 Z M 7.15 10.6 L 8.85 10.6 L 8.85 12.3 L 7.15 12.3 Z"/>
</svg>''',

    "computer-symbolic": '''<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16">
  <path fill="currentColor" d="M 1.5 2 C 1.22 2 1 2.22 1 2.5 L 1 9.5 C 1 9.78 1.22 10 1.5 10 L 14.5 10 C 14.78 10 15 9.78 15 9.5 L 15 2.5 C 15 2.22 14.78 2 14.5 2 Z M 6 11 L 10 11 L 10 13 L 12.5 13 L 12.5 14.5 L 3.5 14.5 L 3.5 13 L 6 13 Z"/>
</svg>''',

    "audio-volume-high-symbolic": '''<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16">
  <path fill="currentColor" d="M 1.6 6 L 4 6 L 7.4 3 L 7.4 13 L 4 10 L 1.6 10 Z M 9.4 4.6 C 11.2 5.7 12.2 6.8 12.2 8 C 12.2 9.2 11.2 10.3 9.4 11.4 L 8.7 10.2 C 10 9.4 10.7 8.7 10.7 8 C 10.7 7.3 10 6.6 8.7 5.8 Z M 11.6 2.6 C 14 4.1 15.2 6 15.2 8 C 15.2 10 14 11.9 11.6 13.4 L 10.9 12.2 C 12.9 10.9 13.8 9.4 13.8 8 C 13.8 6.6 12.9 5.1 10.9 3.8 Z"/>
</svg>''',

    "audio-volume-muted-symbolic": '''<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16">
  <path fill="currentColor" d="M 1.6 6 L 4 6 L 7.4 3 L 7.4 13 L 4 10 L 1.6 10 Z M 9.3 5.2 L 10.5 4 L 12.1 5.6 L 13.7 4 L 14.9 5.2 L 13.3 6.8 L 14.9 8.4 L 13.7 9.6 L 12.1 8 L 10.5 9.6 L 9.3 8.4 L 10.9 6.8 Z"/>
</svg>''',

    "network-wired-symbolic": '''<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16">
  <path fill="currentColor" d="M 4.2 1.5 L 6.2 1.5 L 6.2 4.6 L 9.8 4.6 L 9.8 1.5 L 11.8 1.5 L 11.8 6.2 C 11.8 7.3 10.9 8.2 9.8 8.2 L 8.8 8.2 L 8.8 11 L 11.2 11 L 11.2 14.5 L 4.8 14.5 L 4.8 11 L 7.2 11 L 7.2 8.2 L 6.2 8.2 C 5.1 8.2 4.2 7.3 4.2 6.2 Z"/>
</svg>''',

    "dialog-information-symbolic": '''<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16">
  <path fill="currentColor" fill-rule="evenodd" d="M 8 1 C 11.87 1 15 4.13 15 8 C 15 11.87 11.87 15 8 15 C 4.13 15 1 11.87 1 8 C 1 4.13 4.13 1 8 1 Z M 7.1 6.8 L 8.9 6.8 L 8.9 12.2 L 7.1 12.2 Z M 7.1 3.8 L 8.9 3.8 L 8.9 5.6 L 7.1 5.6 Z"/>
</svg>''',

    "dialog-warning-symbolic": '''<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16">
  <path fill="currentColor" fill-rule="evenodd" d="M 8 1.4 L 15.2 14.2 L 0.8 14.2 Z M 7.2 5.2 L 8.8 5.2 L 8.45 10.2 L 7.55 10.2 Z M 7.2 11.2 L 8.8 11.2 L 8.8 12.9 L 7.2 12.9 Z"/>
</svg>''',

    "dialog-error-symbolic": '''<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16">
  <path fill="currentColor" fill-rule="evenodd" d="M 8 1 C 11.87 1 15 4.13 15 8 C 15 11.87 11.87 15 8 15 C 4.13 15 1 11.87 1 8 C 1 4.13 4.13 1 8 1 Z M 5.9 4.5 L 8 6.6 L 10.1 4.5 L 11.5 5.9 L 9.4 8 L 11.5 10.1 L 10.1 11.5 L 8 9.4 L 5.9 11.5 L 4.5 10.1 L 6.6 8 L 4.5 5.9 Z"/>
</svg>''',

    "media-playback-start-symbolic": '''<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16">
  <path fill="currentColor" d="M 4.2 2.4 L 13.4 8 L 4.2 13.6 Z"/>
</svg>''',

    "media-eject-symbolic": '''<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16">
  <path fill="currentColor" d="M 8 2.2 L 13.4 9.4 L 2.6 9.4 Z M 2.6 10.8 L 13.4 10.8 L 13.4 13.6 L 2.6 13.6 Z"/>
</svg>''',

    "printer-symbolic": '''<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16">
  <path fill="currentColor" fill-rule="evenodd" d="M 4.4 1 L 11.6 1 L 11.6 4.2 L 4.4 4.2 Z M 2 5.4 C 1.45 5.4 1 5.85 1 6.4 L 1 11 C 1 11.55 1.45 12 2 12 L 4.4 12 L 4.4 15 L 11.6 15 L 11.6 12 L 14 12 C 14.55 12 15 11.55 15 11 L 15 6.4 C 15 5.85 14.55 5.4 14 5.4 Z M 5.4 9 L 10.6 9 L 10.6 13.6 L 5.4 13.6 Z"/>
</svg>''',

    "battery-symbolic": '''<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16">
  <path fill="currentColor" fill-rule="evenodd" d="M 1.6 4.4 C 1.27 4.4 1 4.67 1 5 L 1 11 C 1 11.33 1.27 11.6 1.6 11.6 L 12.4 11.6 C 12.73 11.6 13 11.33 13 11 L 13 9.4 L 15 9.4 L 15 6.6 L 13 6.6 L 13 5 C 13 4.67 12.73 4.4 12.4 4.4 Z M 2.8 6.2 L 4.6 6.2 L 4.6 9.8 L 2.8 9.8 Z M 5.8 6.2 L 7.6 6.2 L 7.6 9.8 L 5.8 9.8 Z"/>
</svg>''',

    "text-x-script-symbolic": '''<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16">
  <path fill="currentColor" fill-rule="evenodd" d="M 3 1 L 9 1 L 13 5 L 13 15 L 3 15 Z M 9 1.6 L 12.4 5 L 9 5 Z M 5.2 7 L 6.9 7 L 8.4 8.5 L 6.9 10 L 5.2 10 L 6.7 8.5 Z M 9 9.2 L 11.4 9.2 L 11.4 10.6 L 9 10.6 Z"/>
</svg>''',

    "image-x-generic-symbolic": '''<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16">
  <path fill="currentColor" fill-rule="evenodd" d="M 3 1 L 9 1 L 13 5 L 13 15 L 3 15 Z M 9 1.6 L 12.4 5 L 9 5 Z M 5 6.2 C 5.9 6.2 6.6 6.9 6.6 7.8 C 6.6 8.7 5.9 9.4 5 9.4 C 4.1 9.4 3.4 8.7 3.4 7.8 C 3.4 6.9 4.1 6.2 5 6.2 Z M 4.2 13 L 7.2 9 L 9.1 11.4 L 10.4 10 L 12.2 13 Z"/>
</svg>''',

    "video-x-generic-symbolic": '''<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16">
  <path fill="currentColor" fill-rule="evenodd" d="M 3 1 L 9 1 L 13 5 L 13 15 L 3 15 Z M 9 1.6 L 12.4 5 L 9 5 Z M 5 7 L 11 10 L 5 13 Z"/>
</svg>''',

    "camera-off-symbolic": '''<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16">
  <path fill="currentColor" fill-rule="evenodd" d="M 6.5 2.6 L 9.5 2.6 L 10.5 4 L 14 4 C 14.55 4 15 4.45 15 5 L 15 12 C 15 12.55 14.55 13 14 13 L 2 13 C 1.45 13 1 12.55 1 12 L 1 5 C 1 4.45 1.45 4 2 4 L 5.5 4 Z M 8 5.6 C 9.6 5.6 10.9 6.9 10.9 8.5 C 10.9 10.1 9.6 11.4 8 11.4 C 6.4 11.4 5.1 10.1 5.1 8.5 C 5.1 6.9 6.4 5.6 8 5.6 Z M 3.3 1.3 L 5.3 1.3 L 13.3 15.3 L 11.3 15.3 Z"/>
</svg>''',

    "audio-x-generic-symbolic": '''<svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16">
  <path fill="currentColor" fill-rule="evenodd" d="M 3 1 L 9 1 L 13 5 L 13 15 L 3 15 Z M 9 1.6 L 12.4 5 L 9 5 Z M 6.4 9.8 C 7.2 9.8 7.8 10.4 7.8 11.1 C 7.8 11.8 7.2 12.4 6.4 12.4 C 5.6 12.4 5 11.8 5 11.1 C 5 10.4 5.6 9.8 6.4 9.8 Z M 7.2 6.4 L 9.4 5.9 L 9.4 11.2 L 7.8 11.5 L 7.8 8.2 L 7.2 8.4 Z"/>
</svg>''',
})

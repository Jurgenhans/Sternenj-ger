# Sternenjäger als APK bauen

Das Spiel liegt in `www/index.html`. Alles andere ist fertig vorbereitet.

Das Spiel ist in 3D: Es nutzt einen eigenen WebGL-Renderer in derselben Datei, es werden keine Bibliotheken nachgeladen. Die Steuerung und alle Spielregeln sind unverändert, nur die Kamera schaut schräg auf die Szene.

Das Spielfeld hat außerdem eine Höhe (Z-Achse, ±60 Einheiten auf der Anzeige): Mit den Tasten ▲ HOCH und ▼ RUNTER am rechten Bildschirmrand (Tastatur: Leertaste / Umschalt) fliegst du nach oben und unten. Gegner, Geschosse und Beute haben ebenfalls eine Höhe, Stationen und Sonnen liegen auf Höhe 0. Dünne Linien zeigen, wie hoch ein Objekt über oder unter der Spielebene schwebt.

## Weg A: Ohne Android Studio, direkt bei GitHub (auch vom Handy)

1. Kostenloses Konto auf github.com anlegen und ein neues Repository erstellen (privat ist ok).
2. Den Inhalt dieses Ordners hochladen. Wichtig: auch der versteckte Ordner `.github` muss mit.
   Am Rechner geht das per „Add file > Upload files“ oder mit `git push`.
3. Im Repository oben auf **Actions** gehen, links „APK bauen“ wählen, dann **Run workflow**.
4. Nach etwa 4 bis 6 Minuten erscheint der Lauf mit grünem Haken. Dort unten unter
   **Artifacts** „Sternenjaeger-APK“ herunterladen und die ZIP entpacken.
5. `app-debug.apk` aufs Handy kopieren und öffnen. Android fragt einmal, ob Apps aus dieser Quelle
   installiert werden dürfen. Das erlauben.

## Weg B: Am Rechner

Voraussetzungen: Node 20 oder neuer, JDK 21, Android Studio (für das Android SDK).

- Mac/Linux: `./build.sh`
- Windows: nacheinander in der Eingabeaufforderung ausführen:
  `npm install`, `npx cap add android`, `npx capacitor-assets generate --android`,
  `python scripts/patch.py`, `npx cap sync android`, dann `cd android` und `gradlew assembleDebug`.

Die APK liegt danach unter `android/app/build/outputs/apk/debug/app-debug.apk`.

## Anpassen

- **Bildschirmlage:** in `scripts/patch.py` oben `ORIENTATION` ändern.
  `sensorLandscape` = quer, `sensorPortrait` = hoch, `fullSensor` = frei drehbar.
- **Name und Paketname:** `capacitor.config.json` (`appName`, `appId`).
- **Icon:** die drei Bilder in `assets/` ersetzen (1024 × 1024 px, PNG).
- **Spiel ändern:** `www/index.html` bearbeiten und neu bauen.

## Hinweise

- Das ist eine Debug-APK, signiert mit einem Standard-Testschlüssel. Für private Nutzung reicht das.
  Für den Play Store brauchst du eine signierte Release-Version.
- Die Schriftart wird beim Start aus dem Internet geladen. Ohne Verbindung greift eine Ersatzschrift,
  das Spiel läuft trotzdem.
- Der Spielstand wird im Speicher der App abgelegt und bleibt bei Updates erhalten, solange der
  Paketname gleich bleibt.

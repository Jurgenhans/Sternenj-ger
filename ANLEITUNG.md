# Sternenjäger als APK bauen

Das Spiel liegt in `www/index.html`. Alles andere ist fertig vorbereitet.

Das Spiel ist in 3D: Es nutzt einen eigenen WebGL-Renderer in derselben Datei, es werden keine Bibliotheken nachgeladen. Die Steuerung und alle Spielregeln sind unverändert, nur die Kamera schaut schräg auf die Szene.

Die Kamera ist eine Verfolgerkamera: Sie sitzt schräg hinter dem Schiff und dreht sich mit ihm, die Nase zeigt immer nach oben im Bild. Gesteuert wird aus Sicht des Schiffs: Joystick links/rechts dreht das Schiff, nach oben gibt Schub, nach unten bremst und fliegt rückwärts (Tastatur: A/D drehen, W/S Schub). Das Radar dreht mit.

Die Kamera lässt sich zoomen: Tasten + und − am linken Bildschirmrand (gedrückt halten), Mausrad oder Tastatur + / − (0 setzt zurück). Die Zoomstufe wird gespeichert.

Das Spielfeld hat außerdem eine Höhe (Z-Achse, ±60 Einheiten auf der Anzeige): Mit den Tasten ▲ HOCH und ▼ RUNTER am rechten Bildschirmrand (Tastatur: Leertaste / Umschalt) fliegst du nach oben und unten. Gegner, Geschosse und Beute haben ebenfalls eine Höhe, Stationen und Sonnen liegen auf Höhe 0. Dünne Linien zeigen, wie hoch ein Objekt über oder unter der Spielebene schwebt.

## Die Welt: 4 Sonnensysteme

- **HELIOS (System 1):** 9 Planeten, 2 Stationen (innen und weiter außen), Asteroidengürtel. Jeder Planet hat die NPC-Schiffe eines der früheren neun Systeme (von innen nach außen immer stärker, Planet IX mit Aliens).
- **NEMESIS (System 2):** 15 Planeten mit stärkeren NPCs als in HELIOS. 2 Stationen, an Planet IV und Planet XI. NPCs lassen **goldene Module der Stufe V** fallen. Sie sind genau doppelt so stark wie Stufe IV (Frostfeld höchstens 95 %), nicht kaufbar, und lassen sich in der Station einbauen und aufwerten.
- **ZENITH (System 3):** das kleine Wächter-System mit Boss, Schwarzem Loch und Abgrund.
- **CRIMSON (System 4):** liegt ganz unten rechts auf der Karte. Dunkelrote Sonne, sehr viel dunkelroter Nebel, 5 sehr große Planeten mit Ringen. Jeder Planet hat genau einen NPC-Spawnpunkt (Nummern 28 bis 32 = die stärksten der Welt). Die **Phantom-Schiffe** dort sind sehr stark, nutzen die Schiffsmodelle des Spielers (Fregatte, Kreuzer, Schlachtschiff, Dreadnought, Raubvogel) in dunklen Rottönen sowie die bekannten NPC-Modelle, und lassen goldene Module der Stufe V fallen. Es gibt dort keine Station.
- **Portale:** In NEMESIS (nahe der Sonne) und in CRIMSON (nahe der Sonne) steht je ein Portal. Hineinfliegen bringt dich zum Portal im anderen System. Beide sind auf der Karte und im Radar markiert. Der Warp endet kurz vor dem Portal.
- **Startguthaben:** Ein neues Spiel beginnt mit 1.000.000 CR (bestehende Spielstände behalten ihr Guthaben).
- Die beiden großen Systeme sind doppelt so groß wie zuvor, die Planeten sind entsprechend weiter verteilt.
- **Planeten:** Es gibt sie in dunklem Rot, Grün, Schwarz, Grau, Lila und Blau. Auf jedem Planeten kann man landen (Knopf LANDEN in der Nähe), aussteigen und im Tresor lagern. Auf HELIOS I (Planet 1, Test) ist der ganze Planet die Spielwelt: schon beim Fliegen im Weltall siehst du Gelände mit dunkelrotem Boden, Bäume, Deckungen, Kuppel und NPCs rund um den ganzen Planeten (6 gekrümmte Flächen). Landen und Abheben auf HELIOS I gehen ohne Bildwechsel: Das Schiff fliegt im Weltall-Bild auf einer Kurve zum Landeplatz auf der nächstgelegenen Seite des Planeten und startet von dort wieder. Auf der Seite zur Sonne ist Tag, auf der Gegenseite Nacht (auch beim Aussteigen, dort mit Sternenhimmel). Nach der Landung siehst du die Planetenoberfläche mit deinem Schiff auf dem Landeplatz (die Kamera kreist langsam um das Schiff). Beim Aussteigen läufst du auf der Oberfläche des Planeten: Die Welt hat keine Grenze mehr, der Horizont ist gekrümmt und du kannst in eine Richtung laufen, bis du den ganzen Planeten umrundet hast (rund 17.900 Einheiten Umfang, du bekommst dann eine Meldung). Das Gelände ist auf allen Planeten dasselbe; Tresor und Munitionskiste gehören je Planet.
- **NPC-Spawnpunkte** liegen weit weg von Planeten, Planeten-Asteroiden, Gürteln und Stationen (rote Kreise im Radar und auf der Karte, rot nummeriert von 1 = schwach bis stark). An etwa 40 % davon liegen viele Asteroiden und Kristalle sowie gemischter Nebel (rot, blau, grün).
- **Titan (Werft):** das größte Schiff mit 30 Modul-Plätzen für 400.000 CR. Er darf bis zu 10 × dieselbe Waffe einbauen (alle anderen Schiffe 5 ×) und macht mit allen Waffen +30 % Schaden. Der Bonus gilt zusätzlich zu Skills, Upgrades und Waffen-Varianten.
- **Upgrades:** Alle Module der Stufe IV und V lassen sich in der Station bis Stufe 100 aufwerten (1.000 CR je Stufe, +1 % Wirkung je Stufe, Triebwerke +3 %). Obergrenzen gelten weiter (Dämpfer 95 %, Frostfeld 95 %, Energiesparen 90 %).

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

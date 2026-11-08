#!/usr/bin/env bash
# APK lokal bauen (Mac/Linux). Voraussetzung: Node 20+, JDK 21, Android SDK (Android Studio).
set -e
npm install
[ -d android ] || npx cap add android
npx capacitor-assets generate --android
python3 scripts/patch.py
npx cap sync android
(cd android && ./gradlew assembleDebug)
echo
echo "Fertig: android/app/build/outputs/apk/debug/app-debug.apk"

#!/usr/bin/env python3
"""Passt das von Capacitor erzeugte Android-Projekt an:
Querformat, Vollbild ohne Systemleisten, Bildschirm bleibt an."""
import pathlib, re, sys

# Bildschirmlage: sensorLandscape (quer, beide Richtungen), sensorPortrait (hoch)
# oder fullSensor (frei drehbar)
ORIENTATION = "sensorLandscape"

root = pathlib.Path("android/app/src/main")
manifest = root / "AndroidManifest.xml"
text = manifest.read_text(encoding="utf-8")
text = re.sub(r'\s+android:screenOrientation="[^"]*"', "", text)
text = text.replace("<activity", '<activity\n            android:screenOrientation="%s"' % ORIENTATION, 1)
manifest.write_text(text, encoding="utf-8")

java_dir = root / "java" / "com" / "sternenjaeger" / "app"
java_dir.mkdir(parents=True, exist_ok=True)
(java_dir / "MainActivity.java").write_text('''package com.sternenjaeger.app;

import android.os.Bundle;
import android.view.View;
import android.view.WindowManager;
import com.getcapacitor.BridgeActivity;

public class MainActivity extends BridgeActivity {
    @Override
    public void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        getWindow().addFlags(WindowManager.LayoutParams.FLAG_KEEP_SCREEN_ON);
    }

    @Override
    public void onWindowFocusChanged(boolean hasFocus) {
        super.onWindowFocusChanged(hasFocus);
        if (hasFocus) {
            getWindow().getDecorView().setSystemUiVisibility(
                View.SYSTEM_UI_FLAG_LAYOUT_STABLE
                | View.SYSTEM_UI_FLAG_LAYOUT_HIDE_NAVIGATION
                | View.SYSTEM_UI_FLAG_LAYOUT_FULLSCREEN
                | View.SYSTEM_UI_FLAG_HIDE_NAVIGATION
                | View.SYSTEM_UI_FLAG_FULLSCREEN
                | View.SYSTEM_UI_FLAG_IMMERSIVE_STICKY);
        }
    }
}
''', encoding="utf-8")
print("Android-Projekt angepasst:", ORIENTATION)

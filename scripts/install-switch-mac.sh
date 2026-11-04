#!/bin/sh
# Install Switch Console 0.40.1 (arm64) on the Mac, detached-safe.
# Log: /tmp/switch-install.log
set -u
URL="https://github.com/sandbox-quantum/switch/releases/download/switch-console-v0.40.1/switch-console-arm64.dmg"
DMG="$HOME/Downloads/switch-console-arm64.dmg"
echo "Downloading $URL"
curl -L --fail -o "$DMG" "$URL" || { echo "DOWNLOAD FAILED"; exit 1; }
echo "Mounting $DMG"
hdiutil attach "$DMG" -nobrowse >/dev/null 2>&1 || { echo "MOUNT FAILED"; exit 1; }
MOUNT=$(ls -d /Volumes/Switch* 2>/dev/null | head -1)
echo "Mounted at: $MOUNT"
if [ -z "$MOUNT" ]; then echo "MOUNT FAILED"; exit 1; fi
APP=$(find "$MOUNT" -maxdepth 2 -name "Switch Console.app" | head -1)
echo "App found: $APP"
if [ -z "$APP" ]; then hdiutil detach "$MOUNT" 2>/dev/null; echo "APP NOT FOUND"; exit 1; fi
cp -R "$APP" /Applications/ || { hdiutil detach "$MOUNT" 2>/dev/null; echo "COPY FAILED"; exit 1; }
hdiutil detach "$MOUNT" 2>/dev/null || true
ls -d "/Applications/Switch Console.app" && echo "SWITCH INSTALL OK"

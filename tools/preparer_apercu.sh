#!/bin/sh
# Télécharge le kit, les polices et les photos du dépôt dans ./base pour faire un aperçu local.
set -e
R=https://raw.githubusercontent.com/Minerve04/vitriz-social/main
mkdir -p base/fonts base/assets
curl -fsSL "$R/tools/kit_vitriz.py" -o kit_vitriz.py
for f in inter-latin-400-normal inter-latin-600-normal inter-latin-700-normal space-grotesk-latin-400-normal space-grotesk-latin-500-normal space-grotesk-latin-700-normal; do
  curl -fsSL "$R/fonts/$f.woff2" -o "base/fonts/$f.woff2"; done
for p in florist phone flowers bakery hairdresser craftsman restaurant boutique; do
  curl -fsSL "$R/assets/$p.webp" -o "base/assets/$p.webp"; done
echo "Aperçu prêt : from kit_vitriz import * ; render(page(affiche(...), 'base'), 'apercu.jpg')"

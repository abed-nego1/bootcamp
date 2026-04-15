#!/bin/bash
# backup.sh — sauvegarde quotidienne avec horodatage

SOURCE="$HOME/Projets"
DEST="/mnt/backup"
DATE=$(date +"%Y-%m-%d_%H-%M")
ARCHIVE="$DEST/backup_$DATE.tar.gz"

# Créer le dossier de destination si besoin
mkdir -p "$DEST"

# Créer l'archive compressée
tar -czf "$ARCHIVE" "$SOURCE"

# Vérifier le succès
if [ $? -eq 0 ]; then
  echo "[OK] Sauvegarde : $ARCHIVE"
else
  echo "[ERREUR] Sauvegarde échouée" >&2
  exit 1
fi

# Garder seulement les 7 dernières sauvegardes
ls -t "$DEST"/backup_*.tar.gz | tail -n +8 | xargs -r rm

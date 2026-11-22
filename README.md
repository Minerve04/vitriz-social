# vitriz-social

Posts automatiques de la page VITRIZ (Facebook « Vitriz (Saint-Omer) » et LinkedIn « Vitriz »).

- `a-publier/<AAAA-MM-JJ>-<rubrique>.html` + `.json` : déposés par la tâche programmée (via le scénario Make « vitriz_depot_fichier_github »).
- GitHub Actions (`publier.yml`) : lundi, mercredi et vendredi à 11 h 30 (Paris), rend l'image 1080×1350, la range dans `publiees/` et appelle le webhook Make qui publie sur les deux pages.
- **Annuler un post** : supprimer ses deux fichiers dans `a-publier/` avant 11 h 30.
- Charte : bleu canard #0E7490, Space Grotesk + Inter (`fonts/`).

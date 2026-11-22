# vitriz-social

Posts automatiques de la page VITRIZ (Facebook « Vitriz (Saint-Omer) » et LinkedIn « Vitriz »).

1. La tâche programmée dépose `a-publier/<AAAA-MM-JJ>.html` (visuel) puis `a-publier/<AAAA-MM-JJ>.json` (textes), via le scénario Make « vitriz_depot_fichier_github ».
2. GitHub Actions (`rendre.yml`) rend `a-publier/<AAAA-MM-JJ>.jpg` (1080×1350).
3. Le scénario Make « VITRIZ — Publication page VITRIZ » tourne lundi, mercredi et vendredi à 11 h 30 (Paris) : s'il trouve le post du jour, il le publie sur les deux pages et écrit `publiees/<AAAA-MM-JJ>.resultat.json`.

**Annuler un post** : supprimer `a-publier/<date>.json` avant 11 h 30.
Charte : bleu canard #0E7490, Space Grotesk + Inter (`fonts/`).

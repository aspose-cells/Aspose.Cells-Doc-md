---
title: Valider toute la feuille de calcul au lieu des cellules mises à jour uniquement
type: docs
weight: 80
url: /fr/java/validate-entire-worksheet-instead-of-only-the-updated-cells/
---

## **Scénarios d'utilisation possibles**
Par défaut, GridWeb ne valide que les cellules mises à jour et ne valide pas toute la feuille de calcul. Cependant, si vous souhaitez valider l'ensemble de la feuille de calcul côté client avant que GridWeb n'envoie une demande au serveur, vous devez définir la variable needValidateall à true dans le fichier acwmain.js.
## **Valider toute la feuille de calcul au lieu des cellules mises à jour uniquement**
La capture d'écran suivante affiche la variable needValidateall dans acwmain.js. Veuillez la définir sur true et maintenant, GridWeb validera l'ensemble de votre feuille de calcul, pas seulement les cellules mises à jour.

![todo:image_alt_text](validate-entire-worksheet-instead-of-only-the-updated-cells_1.png)



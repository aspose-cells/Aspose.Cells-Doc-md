---
title: Validez la feuille de calcul entière au lieu des seules cellules mises à jour
type: docs
weight: 80
url: /fr/java/validate-entire-worksheet-instead-of-only-the-updated-cells/
---
##  **Scénarios d'utilisation possibles**
Par défaut, GridWeb valide uniquement les cellules mises à jour et ne valide pas l'intégralité de la feuille de calcul. Cependant, si vous souhaitez valider l'intégralité de la feuille de calcul côté client avant que GridWeb publie la demande sur le serveur, vous devez définir la variable needValidateall dans acwmain.js sur true.
##  **Validez la feuille de calcul entière au lieu des seules cellules mises à jour**
La capture d'écran suivante affiche la variable needValidateall dans acwmain.js. Veuillez le définir sur true et GridWeb validera désormais l'intégralité de votre feuille de calcul, pas seulement les cellules mises à jour.

![tâche : image_alt_text](validate-entire-worksheet-instead-of-only-the-updated-cells_1.png)



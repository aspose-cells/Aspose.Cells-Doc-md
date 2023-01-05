---
title: Ligne personnalisée et légende de colonne personnalisée de la feuille de calcul GridDesktop
type: docs
weight: 120
url: /fr/net/custom-row-and-custom-column-caption-of-griddesktop-worksheet/
---
## **Scénarios d'utilisation possibles**
Vous pouvez personnaliser la légende des lignes et des colonnes de la feuille de calcul GridDesktop. Normalement, la ligne commence à partir de 1 et la colonne commence à partir de A. Vous pouvez modifier ce comportement et utiliser vos propres légendes pour les lignes et les colonnes de la feuille de calcul GridDesktop. Afin de modifier les légendes des lignes et des colonnes, veuillez implémenter les interfaces ICustomRowCaption et ICustomColumnCaption.
## **Ligne personnalisée et légende de colonne personnalisée de la feuille de calcul GridDesktop**
L'exemple de code suivant implémente les interfaces ICustomRowCaption et ICustomColumnCaption et modifie les légendes des lignes et des colonnes. La capture d'écran montre le résultat de l'exécution de cet exemple de code pour une référence.



![tâche : image_autre_texte](custom-row-and-custom-column-caption-of-griddesktop-worksheet_1.png)

## **Exemple de code**
{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples-GridDesktop-CSharp-WorkingWithRowsandColumns-Form_CustomRowAndCustomColumnCaptionOfGridDesktopWorksheet.cs" >}}

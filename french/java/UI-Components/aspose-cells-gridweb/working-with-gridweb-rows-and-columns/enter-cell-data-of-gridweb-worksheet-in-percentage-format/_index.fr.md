---
title: Entrez les données Cell de la feuille de calcul GridWeb au format pourcentage
type: docs
weight: 1010
url: /fr/java/enter-cell-data-of-gridweb-worksheet-in-percentage-format/
---
##  **Scénarios d'utilisation possibles**
GridWeb permet désormais aux utilisateurs de saisir les données de cellule au format de pourcentage, tel que 3 %, et les données de la cellule seront automatiquement formatées à 3,00 %. Cependant, vous devrez définir le style de cellule sur Format de pourcentage qui est soit GridTableItemStyle.NumberType a 9 ou 10. Le nombre 9 formatera 3 % à 3 %, mais le nombre 10 formatera 3 % à 3,00 %.

{{% alert color="primary" %}} 

Si vous n'avez pas défini le style de cellule sur Format de pourcentage, les données saisies 3 % s'afficheront sous la forme 0,03.

{{% /alert %}} 
##  **Entrez les données Cell de la feuille de calcul GridWeb au format pourcentage**
L'exemple de code suivant définit la cellule A1 GridTableItemStyle.NumberType sur 10, donc les données d'entrée 3 % sont automatiquement formatées à 3,00 %, comme indiqué dans la capture d'écran.

![tâche : image_alt_text](enter-cell-data-of-gridweb-worksheet-in-percentage-format_1.png)
##  **Exemple de code**




{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-EnterCellDataofGridWebWorksheet-EnterCellDataofGridWebWorksheet.jsp" >}}







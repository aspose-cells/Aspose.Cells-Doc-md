---
title: Saisir les données de la cellule de la feuille de calcul GridWeb au format pourcentage
type: docs
weight: 1010
url: /fr/java/enter-cell-data-of-gridweb-worksheet-in-percentage-format/
---

## **Scénarios d'utilisation possibles**
GridWeb prend maintenant en charge la saisie des données de cellule au format pourcentage, comme 3 % et les données dans la cellule seront automatiquement formatées en 3,00 %. Cependant, vous devrez définir le style de la cellule au format pourcentage, qui est soit GridTableItemStyle.NumberType 9 ou 10. Le nombre 9 formatera 3 % en tant que 3 %, mais le nombre 10 formatera 3 % en tant que 3,00 %.

{{% alert color="primary" %}} 

Si vous n'avez pas défini le style de la cellule au format pourcentage, alors les données d'entrée 3 % s'afficheront comme 0,03.

{{% /alert %}} 
## **Saisir les données de cellule de la feuille de calcul GridWeb en format pourcentage**
Le code d'exemple suivant définit la cellule A1 GridTableItemStyle.NumberType comme 10, donc les données d'entrée 3 % seront automatiquement formatées en 3,00 % comme indiqué dans la capture d'écran.

![todo:image_alt_text](enter-cell-data-of-gridweb-worksheet-in-percentage-format_1.png)
## **Code d'exemple**




{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-EnterCellDataofGridWebWorksheet-EnterCellDataofGridWebWorksheet.jsp" >}}







---
title: Entrez les données Cell de la feuille de calcul GridWeb au format pourcentage
type: docs
weight: 80
url: /fr/net/enter-cell-data-of-gridweb-worksheet-in-percentage-format/
---
## **Scénarios d'utilisation possibles**
GridWeb permet désormais aux utilisateurs de saisir des données de cellule au format de pourcentage comme 3 % et les données de la cellule seront automatiquement formatées en 3,00 %. Cependant, vous devrez définir le style de cellule sur Format de pourcentage qui est soit GridTableItemStyle.NumberType a 9 ou 10. Le nombre 9 formatera 3 % en 3 % mais le nombre 10 formatera 3 % en 3,00 %.

{{% alert color="primary" %}} 

Si vous n'avez pas défini le style de cellule sur Format de pourcentage, les données d'entrée 3 % s'afficheront sous la forme 0,03.

{{% /alert %}} 
## **Entrez les données Cell de la feuille de calcul GridWeb au format pourcentage**
L'exemple de code suivant définit la cellule A1 GridTableItemStyle.NumberType sur 10. Par conséquent, les données d'entrée 3 % sont automatiquement formatées en 3,00 %, comme indiqué dans la capture d'écran.

![tâche : image_autre_texte](enter-cell-data-of-gridweb-worksheet-in-percentage-format_1.png)
### **Exemple de code**


{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Articles-SetCellPercentageFormat.aspx-SetCellPercentageFormat.cs" >}}

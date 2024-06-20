---
title: Spécifiez comment croiser une chaîne dans le PDF de sortie et l image
type: docs
weight: 110
url: /fr/java/specify-how-to-cross-string-in-output-pdf-and-image/
---

## **Scénarios d'utilisation possibles**

Lorsqu'une cellule contient du texte ou une chaîne mais qu'elle est plus large que la largeur de la cellule, alors la chaîne dépasse si la cellule suivante dans la colonne suivante est nulle ou vide. Lorsque vous enregistrez votre fichier Excel au format PDF/Image, vous pouvez contrôler ce dépassement en spécifiant le type de croisement en utilisant l'énumération [**TextCrossType**](https://reference.aspose.com/cells/java/com.aspose.cells/TextCrossType). Il a les valeurs suivantes

- [**TextCrossType.DEFAULT**](https://reference.aspose.com/cells/java/com.aspose.cells/textcrosstype#DEFAULT): Affichage comme dans MS Excel, dépend de la cellule suivante. Si la cellule suivante est nulle, la chaîne croisera ou sera tronquée.

- [**TextCrossType. CROSS_KEEP**](https://reference.aspose.com/cells/java/com.aspose.cells/textcrosstype#CROSS_KEEP): Affiche la chaîne comme lors de l'exportation en PDF/Image depuis MS Excel

- [**TextCrossType.CROSS_OVERRIDE**](https://reference.aspose.com/cells/java/com.aspose.cells/textcrosstype#CROSS_OVERRIDE): Affiche tout le texte en croisant d'autres cellules et en remplaçant le texte des cellules croisées

- [**TextCrossType.STRICT_IN_CELL**](https://reference.aspose.com/cells/java/com.aspose.cells/textcrosstype#STRICT_IN_CELL): Affichage uniquement de la chaîne dans la largeur de la cellule

## **Spécifiez comment croiser une chaîne dans le PDF de sortie/une image en utilisant TextCrossType**

Le code d'exemple suivant charge le fichier Excel d'exemple et le sauvegarde au format PDF/Image en spécifiant différents [**TextCrossType**](https://reference.aspose.com/cells/java/com.aspose.cells/TextCrossType). Le fichier Excel d'exemple et les fichiers de sortie peuvent être téléchargés aux liens suivants:

[sampleCrossType.xlsx](sampleCrossType.xlsx)

[outputCrossType.pdf](outputCrossType.pdf)

[outputCrossType.png](outputCrossType.png)

## **Code d'exemple**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Rendering-RenderUsingTextCrossType-1.java" >}}

---
title: Spécifiez comment croiser la chaîne dans le PDF de sortie et l'image
type: docs
weight: 110
url: /fr/java/specify-how-to-cross-string-in-output-pdf-and-image/
---
## **Scénarios d'utilisation possibles**

Lorsqu'une cellule contient du texte ou une chaîne mais qu'elle est plus grande que la largeur de la cellule, la chaîne déborde si la cellule suivante dans la colonne suivante est nulle ou vide. Lorsque vous enregistrez votre fichier Excel en PDF/Image, vous pouvez contrôler ce débordement en spécifiant le type croisé à l'aide de la[**TextCrossType**](https://reference.aspose.com/cells/java/com.aspose.cells/TextCrossType)énumération. Il a les valeurs suivantes

- [**TextCrossType.DEFAULT**](https://reference.aspose.com/cells/java/com.aspose.cells/textcrosstype#DEFAULT): Affichage comme MS Excel, dépend de la cellule suivante. Si la cellule suivante est nulle, la chaîne se croisera ou sera tronquée.

- [**TextCrossType. CROSS_KEEP**](https://reference.aspose.com/cells/java/com.aspose.cells/textcrosstype#CROSS_KEEP): Affiche la chaîne comme MS Excel exportant PDF/Image

- [**TextCrossType.CROSS_OVERRIDE**](https://reference.aspose.com/cells/java/com.aspose.cells/textcrosstype#CROSS_OVERRIDE): Afficher tout le texte en croisant d'autres cellules et remplacer le texte des cellules croisées

- [**TextCrossType.STRICT_IN_CELL**](https://reference.aspose.com/cells/java/com.aspose.cells/textcrosstype#STRICT_IN_CELL): affiche uniquement la chaîne dans la largeur de la cellule.

## **Spécifiez comment croiser la chaîne dans la sortie PDF/Image à l'aide de TextCrossType**

L'exemple de code suivant charge l'exemple de fichier Excel et l'enregistre au format PDF/Image en spécifiant différents[**TextCrossType**](https://reference.aspose.com/cells/java/com.aspose.cells/TextCrossType)L'exemple de fichier Excel et les fichiers de sortie peuvent être téléchargés à partir des liens suivants :

[exempleCrossType.xlsx](sampleCrossType.xlsx)

[outputCrossType.pdf](outputCrossType.pdf)

[outputCrossType.png](outputCrossType.png)

## **Exemple de code**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Rendering-RenderUsingTextCrossType-1.java" >}}

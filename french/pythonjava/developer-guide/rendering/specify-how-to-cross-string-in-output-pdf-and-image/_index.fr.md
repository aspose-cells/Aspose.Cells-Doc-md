---
title: Spécifiez comment croiser la chaîne dans le PDF de sortie et l'image
type: docs
weight: 20
url: /fr/python-java/specify-how-to-cross-string-in-output-pdf-and-image/
---
## **Spécifiez comment croiser la chaîne dans le PDF de sortie et l'image**
 Lorsqu'une cellule contient du texte ou une chaîne plus grande que la largeur de la cellule, la chaîne déborde si la cellule suivante de la colonne suivante est nulle ou vide. Lorsque vous enregistrez votre fichier Excel en PDF/Image, vous pouvez contrôler ce débordement en spécifiant le type croisé à l'aide de la[TextCrossType](https://reference.aspose.com/cells/python/asposecells.api/TextCrossType) énumération. Il a les valeurs suivantes

- [TextCrossType.DEFAULT](https://reference.aspose.com/cells/python/asposecells.api/textcrosstype#DEFAULT): Affichage comme MS Excel, dépend de la cellule suivante. Si la cellule suivante est nulle, la chaîne se croisera ou sera tronquée.
- [TextCrossType. CROSS_KEEP](https://reference.aspose.com/cells/python/asposecells.api/textcrosstype#CROSS_KEEP): Affiche la chaîne similaire à MS Excel exportant PDF/Image
- [TextCrossType.CROSS_OVERRIDE](https://reference.aspose.com/cells/python/asposecells.api/textcrosstype#CROSS_OVERRIDE)Afficher tout le texte en croisant d'autres cellules et remplacer le texte des cellules croisées
- [TextCrossType.STRICT_DANS_CELLULE](https://reference.aspose.com/cells/python/asposecells.api/textcrosstype#STRICT_IN_CELL): affiche uniquement la chaîne dans la largeur de la cellule.

L'exemple de code suivant charge l'exemple de fichier Excel et l'enregistre au format PDF/Image en spécifiant un TextCrossType différent. L'exemple de fichier Excel et les fichiers de sortie peuvent être téléchargés à partir des liens suivants :

[exempleCrossType.xlsx](sampleCrossType.xlsx)

[outputCrossType.pdf](outputCrossType.pdf)

[outputCrossType.png](outputCrossType.png)
## **Exemple de code**
{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Rendering-RenderUsingTextCrossType.py" >}}

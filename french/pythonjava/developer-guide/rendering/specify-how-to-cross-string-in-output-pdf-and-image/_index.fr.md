---
title: Spécifiez comment croiser une chaîne dans le PDF de sortie et l image
type: docs
weight: 20
url: /fr/python-java/specify-how-to-cross-string-in-output-pdf-and-image/
---

## **Spécifiez comment croiser la chaîne dans le PDF de sortie et l'image**
Lorsqu'une cellule contient du texte ou une chaîne plus large que la largeur de la cellule, la chaîne déborde si la cellule suivante dans la colonne suivante est vide ou nulle. Lorsque vous enregistrez votre fichier Excel en PDF/Image, vous pouvez contrôler ce débordement en spécifiant le type de croisement en utilisant l'énumération [TextCrossType](https://reference.aspose.com/cells/python/asposecells.api/TextCrossType). Elle comporte les valeurs suivantes :

- [TextCrossType.DEFAULT](https://reference.aspose.com/cells/python/asposecells.api/textcrosstype#DEFAULT) : Affichage similaire à MS Excel, dépend de la cellule suivante. Si la cellule suivante est vide, la chaîne croisera ou sera tronquée.
- [TextCrossType.CROSS_KEEP](https://reference.aspose.com/cells/python/asposecells.api/textcrosstype#CROSS_KEEP) : Affiche la chaîne de manière similaire à l'exportation en PDF/Image de MS Excel
- [TextCrossType.CROSS_OVERRIDE](https://reference.aspose.com/cells/python/asposecells.api/textcrosstype#CROSS_OVERRIDE) : Affiche tout le texte en croisant d'autres cellules et en remplaçant le texte des cellules croisées
- [TextCrossType.STRICT_IN_CELL](https://reference.aspose.com/cells/python/asposecells.api/textcrosstype#STRICT_IN_CELL) : Affichage uniquement de la chaîne dans la largeur de la cellule.

Le code d'exemple suivant charge le fichier Excel d'exemple et l'enregistre au format PDF/Image en spécifiant différents TextCrossType. Le fichier Excel d'exemple et les fichiers de sortie peuvent être téléchargés à partir des liens suivants :

[sampleCrossType.xlsx](sampleCrossType.xlsx)

[outputCrossType.pdf](outputCrossType.pdf)

[outputCrossType.png](outputCrossType.png)
## **Code d'exemple**
{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Rendering-RenderUsingTextCrossType.py" >}}

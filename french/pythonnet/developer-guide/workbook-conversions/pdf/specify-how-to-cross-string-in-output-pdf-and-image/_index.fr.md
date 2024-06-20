---
title: Spécifiez comment croiser une chaîne dans le PDF de sortie et l image
type: docs
weight: 120
url: /fr/python-net/specify-how-to-cross-string-in-output-pdf-and-image/
description: Apprenez comment croiser une chaîne dans le PDF de sortie et l image avec l API Aspose.Cells pour Python via .NET.
keywords: Croiser une chaîne en PDF de sortie et en image en Python
---

## **Scénarios d'utilisation possibles**

Lorsqu'une cellule contient du texte ou une chaîne mais qu'elle est plus large que la largeur de la cellule, alors la chaîne déborde si la cellule suivante dans la colonne suivante est nulle ou vide. Lorsque vous enregistrez votre fichier Excel au format PDF/Image, vous pouvez contrôler ce débordement en spécifiant le type de croisement à l'aide de l'énumération [**TextCrossType**](https://reference.aspose.com/cells/python-net/aspose.cells/textcrosstype/). Il a les valeurs suivantes

- **TextCrossType.DEFAULT** : Afficher le texte comme dans MS Excel qui dépend de la cellule suivante. Si la cellule suivante est nulle, la chaîne sera croisée ou tronquée.

- **TextCrossType.CROSS_KEEP** : Affiche la chaîne comme avec MS Excel en exportant PDF/Image

- **TextCrossType.CROSS_OVERRIDE** : Affiche tout le texte en croisant d'autres cellules et en remplaçant le texte des cellules croisées

- **TextCrossType.STRICT_IN_CELL** : Affiche uniquement la chaîne dans la largeur de la cellule.

## **Spécifiez comment croiser une chaîne dans le PDF de sortie/une image en utilisant TextCrossType**

Le code d'exemple suivant charge le fichier Excel d'exemple et le sauvegarde au format PDF/Image en spécifiant différents [**TextCrossType**](https://reference.aspose.com/cells/python-net/aspose.cells/textcrosstype/). Le fichier Excel d'exemple et les fichiers de sortie peuvent être téléchargés aux liens suivants:

[sampleCrossType.xlsx](81920905.xlsx)

[outputCrossType.pdf](81920903.pdf)

[outputCrossType.png](81920904.png)

### Code d'exemple

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-RenderUsingTextCrossType-1.py" >}}

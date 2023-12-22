---
title: Spécifiez comment croiser la chaîne dans la sortie PDF et l'image
type: docs
weight: 120
url: /fr/python-net/specify-how-to-cross-string-in-output-pdf-and-image/
description: Apprenez à croiser une chaîne dans la sortie PDF et une image avec Aspose.Cells for Python via .NET API.
keywords: Python Cross String in output PDF and image
---
##  **Scénarios d'utilisation possibles**

Lorsqu'une cellule contient du texte ou une chaîne mais qu'elle est plus grande que la largeur de la cellule, la chaîne déborde si la cellule suivante de la colonne suivante est nulle ou vide. Lorsque vous enregistrez votre fichier Excel dans PDF/Image, vous pouvez contrôler ce débordement en précisant le type de croix à l'aide du[**TextCrossType**](https://reference.aspose.com/cells/python-net/aspose.cells/textcrosstype/)énumération. Il a les valeurs suivantes

- *TextCrossType.DEFAULT** : Afficher le texte comme MS Excel qui dépend de la cellule suivante. Si la cellule suivante est nulle, la chaîne sera croisée ou elle sera tronquée.

- *TextCrossType.CROSS_KEEP** : affiche la chaîne comme MS Excel en exportant PDF/Image

- *TextCrossType.CROSS_OVERRIDE** : Afficher tout le texte en croisant d'autres cellules et remplacer le texte des cellules croisées

- *TextCrossType.STRICT_IN_CELL** : affiche uniquement la chaîne dans la largeur de la cellule.

##  **Spécifiez comment croiser la chaîne dans la sortie PDF/Image à l'aide de TextCrossType**

L'exemple de code suivant charge l'exemple de fichier Excel et l'enregistre au format PDF/Image en spécifiant différents[**TextCrossType**](https://reference.aspose.com/cells/python-net/aspose.cells/textcrosstype/)L'exemple de fichier Excel et les fichiers de sortie peuvent être téléchargés à partir des liens suivants :

[exempleCrossType.xlsx](81920905.xlsx)

[sortieCrossType.pdf](81920903.pdf)

[sortieCrossType.png](81920904.png)

###  Exemple de code

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-RenderUsingTextCrossType-1.py" >}}

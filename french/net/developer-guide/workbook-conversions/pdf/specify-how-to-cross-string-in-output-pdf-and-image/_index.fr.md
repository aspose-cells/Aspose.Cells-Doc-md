---
title: Spécifiez comment traverser la chaîne dans la sortie PDF et l'image
type: docs
weight: 120
url: /fr/net/specify-how-to-cross-string-in-output-pdf-and-image/
---
## **Scénarios d'utilisation possibles**

Lorsqu'une cellule contient du texte ou une chaîne mais qu'elle est plus grande que la largeur de la cellule, la chaîne déborde si la cellule suivante dans la colonne suivante est nulle ou vide. Lorsque vous enregistrez votre fichier Excel dans PDF/Image, vous pouvez contrôler ce débordement en précisant le type croisé à l'aide de la[**TextCrossType**](https://reference.aspose.com/cells/net/aspose.cells/textcrosstype)énumération. Il a les valeurs suivantes

- **TextCrossType.Default**: Affiche du texte comme MS Excel qui dépend de la cellule suivante. Si la cellule suivante est nulle, la chaîne se croisera ou sera tronquée.

- **TextCrossType.CrossKeep**: Affichez la chaîne comme MS Excel exportant PDF/Image

- **TextCrossType.CrossOverrideTextCrossType.CrossOverride**: Afficher tout le texte en croisant d'autres cellules et remplacer le texte des cellules croisées

- **TextCrossType.StrictInCell**: affiche uniquement la chaîne dans la largeur de la cellule.

## **Spécifiez comment croiser la chaîne dans la sortie PDF/Image à l'aide de TextCrossType**

L'exemple de code suivant charge l'exemple de fichier Excel et l'enregistre au format PDF/Image en spécifiant différents[**TextCrossType**](https://reference.aspose.com/cells/net/aspose.cells/textcrosstype). L'exemple de fichier Excel et les fichiers de sortie peuvent être téléchargés à partir des liens suivants :

[exempleCrossType.xlsx](81920905.xlsx)

[outputCrossType.pdf](81920903.pdf)

[outputCrossType.png](81920904.png)

### Exemple de code

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Rendering-RenderUsingTextCrossType-1.cs" >}}

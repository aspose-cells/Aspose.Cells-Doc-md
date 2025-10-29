---
title: Spécifiez comment croiser la chaîne dans le PDF de sortie et l image avec Golang via C++
linktitle: Spécifiez comment croiser une chaîne dans le PDF de sortie et l image
type: docs
weight: 120
url: /fr/go-cpp/specify-how-to-cross-string-in-output-pdf-and-image/
description: Apprenez comment contrôler le débordement du texte dans les sorties PDF et image en utilisant Aspose.Cells for C++.
---

## **Scénarios d'utilisation possibles**

Lorsqu'une cellule contient du texte ou une chaîne plus longue que la largeur de la cellule, la chaîne déborde si la cellule suivante dans la colonne suivante est nulle ou vide. Lors de la sauvegarde de votre fichier Excel en PDF ou Image, vous pouvez contrôler ce débordement en spécifiant le type de traversée à l'aide de l'énumération [**TextCrossType**](https://reference.aspose.com/cells/go-cpp/textcrosstype/). Il possède les valeurs suivantes :

- **TextCrossType.Default** : Affiche le texte comme MS Excel, en dépendant de la cellule suivante. Si la cellule suivante est nulle, la chaîne traversera ou sera tronquée.

- **TextCrossType.CrossKeep** : Affiche la chaîne comme l'exportation PDF/Image de MS Excel.

- **TextCrossType.CrossOverride** : Affiche tout le texte en croisant d'autres cellules et en écrasant le texte des cellules croisées.

- **TextCrossType.StrictInCell**: Affiche uniquement la chaîne dans la largeur de la cellule.

## **Spécifiez comment croiser une chaîne dans le PDF de sortie/une image en utilisant TextCrossType**

Le code d'exemple suivant charge le fichier Excel d'exemple et le sauvegarde au format PDF/Image en spécifiant différents [**TextCrossType**](https://reference.aspose.com/cells/go-cpp/textcrosstype/). Le fichier Excel d'exemple et les fichiers de sortie peuvent être téléchargés depuis les liens suivants :

[sampleCrossType.xlsx](81920905.xlsx)

[outputCrossType.pdf](81920903.pdf)

[outputCrossType.png](81920904.png)

### Code d'exemple

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SpecifyHowToCrossStringInOutputPdfAndImage.go" >}}

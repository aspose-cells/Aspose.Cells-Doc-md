---
title: Extraire du texte de la forme SmartArt de type engrenage via Golang en C++
linktitle: Extraire du texte de la forme SmartArt de type équipement
type: docs
weight: 500
url: /fr/go-cpp/extract-text-from-the-gear-type-smartart-shape/
description: Apprenez comment extraire du texte des formes SmartArt de type Engrenage dans Excel en utilisant Aspose.Cells for C++ avec un guide étape par étape et des exemples de code.
---

## **Scénarios d'utilisation possibles**

Aspose.Cells for C++ peut extraire le texte de la forme SmartArt de type Engrenage. Pour y parvenir, suivez ces étapes :
1. Convertir la forme SmartArt en groupe de formes en utilisant la méthode [**Shape::GetResultOfSmartArt()**](https://reference.aspose.com/cells/go-cpp/).
2. Récupérer toutes les formes individuelles composant le groupe de formes en utilisant la méthode [**GroupShape::GetGroupedShapes()**](https://reference.aspose.com/cells/go-cpp/).
3. Parcourir chaque forme individuelle et en extraire le texte en utilisant la méthode [**GetText()**](https://reference.aspose.com/cells/go-cpp/).

## **Extraire du texte de la forme SmartArt de type équipement**

Le code d'exemple suivant charge un [fichier Excel d'exemple](67338483.xlsx) contenant une forme SmartArt de type Engrenage et en extrait le texte de ses formes individuelles. Consultez la sortie de la console ci-dessous pour voir les résultats.

## **Code d'exemple**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ExtractTextFromTheGearTypeSmartartShape.go" >}}
## **Sortie console**

{{< highlight java >}}
Gear Type Shape Text: Nice
Gear Type Shape Text: Good
Gear Type Shape Text: Excellent
{{< /highlight >}}

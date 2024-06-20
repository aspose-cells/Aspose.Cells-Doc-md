---
title: Extraire du texte de la forme SmartArt de type équipement
type: docs
weight: 130
url: /fr/java/extract-text-from-the-gear-type-smartart-shape/
---

## **Scénarios d'utilisation possibles**

Aspose.Cells peut extraire le texte de la forme Smart Art Type d'engrenage. Pour ce faire, vous devez d'abord convertir la forme Smart Art en forme de groupe en utilisant la méthode [**Shape.getResultOfSmartArt()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#getResultOfSmartArt--). Ensuite, vous devez obtenir le tableau de toutes les formes individuelles formant la forme de groupe en utilisant la méthode [**GroupShape.getGroupedShapes()**](https://reference.aspose.com/cells/java/com.aspose.cells/groupshape#getGroupedShapes--). Enfin, vous pouvez parcourir toutes les formes individuelles une par une dans une boucle et extraire leur texte en utilisant la propriété [**Shape.Text**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#Text).

## **Extraire du texte de la forme SmartArt de type équipement**

Le code d'exemple suivant charge le [fichier Excel d'exemple](67338510.xlsx) qui contient une forme SmartArt de type engrenage. Il extrait ensuite le texte de ses formes individuelles comme discuté ci-dessus. Veuillez consulter la sortie de la console du code ci-dessous pour une référence.

## **Code d'exemple**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "DrawingObjects-ExtractTextFromGearTypeSmartArtShape.java" >}}

## **Sortie console**

{{< highlight java >}}

Gear Type Shape Text: Nice Gear Type Shape Text: Good Gear Type Shape Text: Excellent

{{< /highlight >}}

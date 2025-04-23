---
title: Extraire du texte de la forme SmartArt de type équipement
type: docs
weight: 500
url: /fr/net/extract-text-from-the-gear-type-smartart-shape/
---

## **Scénarios d'utilisation possibles**

Aspose.Cells peut extraire du texte de la forme SmartArt de type équipement. Pour ce faire, vous devez d'abord convertir la forme SmartArt en forme de groupe en utilisant la méthode [**Shape.GetResultOfSmartArt()**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/methods/getresultofsmartart). Ensuite, vous devriez obtenir le tableau de toutes les formes individuelles formant la forme de groupe en utilisant la méthode [**GroupShape.GetGroupedShapes()**](https://reference.aspose.com/cells/net/aspose.cells.drawing/groupshape/methods/getgroupedshapes). Enfin, vous pouvez itérer toutes les formes individuelles une par une dans une boucle et extraire leur texte en utilisant la propriété [**Shape.Text**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/text).

## **Extraire du texte de la forme SmartArt de type équipement**

Le code d'exemple suivant charge le [fichier Excel d'exemple](67338483.xlsx) qui contient une forme SmartArt de type équipement. Ensuite, il extrait le texte de ses formes individuelles comme discuté ci-dessus. Veuillez consulter la sortie de console du code ci-dessous à titre de référence.

## **Code d'exemple**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "DrawingObjects-ExtractTextFromGearTypeSmartArtShape.cs" >}}

## **Sortie console**

{{< highlight java >}}

Gear Type Shape Text: Nice

Gear Type Shape Text: Good

Gear Type Shape Text: Excellent

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}

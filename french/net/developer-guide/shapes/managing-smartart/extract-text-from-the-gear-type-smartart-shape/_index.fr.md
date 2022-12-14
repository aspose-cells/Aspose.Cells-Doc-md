---
title: Extraire le texte de la forme SmartArt du type d'engrenage
type: docs
weight: 500
url: /fr/net/extract-text-from-the-gear-type-smartart-shape/
---
## **Scénarios d'utilisation possibles**

 Aspose.Cells peut extraire du texte de la forme d'art intelligente Gear Type. Pour ce faire, vous devez d'abord convertir la forme d'art intelligent en forme de groupe à l'aide de la[**Forme.GetResultOfSmartArt()**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/methods/getresultofsmartart) méthode. Ensuite, vous devriez obtenir le tableau de toutes les formes individuelles formant la forme de groupe en utilisant le[**GroupShape.GetGroupedShapes()**](https://reference.aspose.com/cells/net/aspose.cells.drawing/groupshape/methods/getgroupedshapes) méthode. Enfin, vous pouvez parcourir toutes les formes individuelles une par une dans une boucle et extraire leur texte à l'aide de la[**Forme.Texte**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/text)propriété.

## **Extraire le texte de la forme SmartArt du type d'engrenage**

 L'exemple de code suivant charge le[exemple de fichier Excel](67338483.xlsx) qui contient Gear Type Smart Art Shape. Il extrait ensuite le texte de ses formes individuelles, comme indiqué ci-dessus. Veuillez consulter la sortie de la console du code ci-dessous pour une référence.

## **Exemple de code**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "DrawingObjects-ExtractTextFromGearTypeSmartArtShape.cs" >}}

## **Sortie console**

{{< highlight "java" >}}

Gear Type Shape Text: Nice

Gear Type Shape Text: Good

Gear Type Shape Text: Excellent

{{< /highlight >}}

---
title: Extrahera text från Gear Type SmartArt Shape
type: docs
weight: 500
url: /sv/net/extract-text-from-the-gear-type-smartart-shape/
---
## **Möjliga användningsscenarier**

 Aspose.Cells kan extrahera text från Gear Type Smart Art Shape. För att göra det bör du först konvertera Smart Art Shape till Group Shape med hjälp av[**Shape.GetResultOfSmartArt()**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/methods/getresultofsmartart) metod. Då bör du få samlingen av alla individuella former som bildar gruppformen med hjälp av[**GroupShape.GetGroupedShapes()**](https://reference.aspose.com/cells/net/aspose.cells.drawing/groupshape/methods/getgroupedshapes) metod. Slutligen kan du iterera alla individuella former en efter en i en slinga och extrahera deras text med hjälp av[**Shape.Text**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/text)fast egendom.

## **Extrahera text från Gear Type SmartArt Shape**

 Följande exempelkod laddar[exempel på Excel-fil](67338483.xlsx) som innehåller Gear Type Smart Art Shape. Den extraherar sedan texten från dess individuella former som diskuterats ovan. Se konsolutgången för koden nedan för en referens.

## **Exempelkod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "DrawingObjects-ExtractTextFromGearTypeSmartArtShape.cs" >}}

## **Konsolutgång**

{{< highlight "java" >}}

Gear Type Shape Text: Nice

Gear Type Shape Text: Good

Gear Type Shape Text: Excellent

{{< /highlight >}}

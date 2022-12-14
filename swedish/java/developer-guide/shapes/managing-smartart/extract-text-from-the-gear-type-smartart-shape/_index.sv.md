---
title: Extrahera text från Gear Type SmartArt Shape
type: docs
weight: 130
url: /sv/java/extract-text-from-the-gear-type-smartart-shape/
---
## **Möjliga användningsscenarier**

Aspose.Cells kan extrahera text från Gear Type Smart Art Shape. För att göra det bör du först konvertera Smart Art Shape till Group Shape med hjälp av[**Shape.getResultOfSmartArt()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#getResultOfSmartArt()) metod. Då bör du få samlingen av alla individuella former som bildar gruppformen med hjälp av[**GroupShape.getGroupedShapes()**](https://reference.aspose.com/cells/java/com.aspose.cells/groupshape#getGroupedShapes()) metod. Slutligen kan du iterera alla individuella former en efter en i en slinga och extrahera deras text med hjälp av[**Shape.Text**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#Text)fast egendom.

## **Extrahera text från Gear Type SmartArt Shape**

Följande exempelkod laddar[exempel på Excel-fil](67338510.xlsx)som innehåller Gear Type Smart Art Shape. Den extraherar sedan texten från dess individuella former som diskuterats ovan. Se konsolutgången för koden nedan för en referens.

## **Exempelkod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "DrawingObjects-ExtractTextFromGearTypeSmartArtShape.java" >}}

## **Konsolutgång**

{{< highlight "java" >}}

Gear Type Shape Text: Nice Gear Type Shape Text: Good Gear Type Shape Text: Excellent

{{< /highlight >}}

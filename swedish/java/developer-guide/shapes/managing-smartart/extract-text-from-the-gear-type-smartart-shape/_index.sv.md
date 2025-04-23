---
title: Extrahera text från SmartArt figurer av typen Gear
type: docs
weight: 130
url: /sv/java/extract-text-from-the-gear-type-smartart-shape/
---

## **Möjliga användningsscenario**

Aspose.Cells kan extrahera text från Gear Type Smart Art Shape. För att göra det bör du först konvertera Smart Art Shape till Group Shape med [**Shape.getResultOfSmartArt()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#getResultOfSmartArt--)-metoden. Sedan bör du få arrayen av alla Individual Shapes som bildar Group Shape med [**GroupShape.getGroupedShapes()**](https://reference.aspose.com/cells/java/com.aspose.cells/groupshape#getGroupedShapes--)-metoden. Slutligen kan du iterera alla Individual Shapes en efter en i en loop och extrahera deras text med hjälp av [**Shape.Text**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#Text)-egenskapen.

## **Extrahera text från SmartArt-form med tandhjulstyp**

Följande exempelkod laddar in den [exempel Excel-filen](67338510.xlsx) som innehåller Gear Type Smart Art Shape. Sedan extraherar den texten från dess individuella former som diskuterats ovan. Se utförseln till konsolen i koden nedan för referens.

## **Exempelkod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "DrawingObjects-ExtractTextFromGearTypeSmartArtShape.java" >}}

## **Konsoloutput**

{{< highlight java >}}

Gear Type Shape Text: Nice Gear Type Shape Text: Good Gear Type Shape Text: Excellent

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}

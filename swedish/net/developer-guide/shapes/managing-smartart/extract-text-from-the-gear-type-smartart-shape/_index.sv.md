---
title: Extrahera text från SmartArt figurer av typen Gear
type: docs
weight: 500
url: /sv/net/extract-text-from-the-gear-type-smartart-shape/
---

## **Möjliga användningsscenario**

Aspose.Cells kan extrahera text från Geartyp Smart konstform. För att göra det ska du först konvertera Smart konstform till gruppkonstform med hjälp av [**Shape.GetResultOfSmartArt()**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/methods/getresultofsmartart) metoden. Sedan ska du få arrayen av alla individuella former som bildar gruppkonstformen med hjälp av [**GroupShape.GetGroupedShapes()**](https://reference.aspose.com/cells/net/aspose.cells.drawing/groupshape/methods/getgroupedshapes) metoden. Slutligen kan du iterera alla individuella former en efter en i en loop och extrahera deras text med hjälp av [**Shape.Text**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/text) egenskapen.

## **Extrahera text från SmartArt-form med tandhjulstyp**

Följande kodexempel laddar [exempel Excel-filen](67338483.xlsx) som innehåller Geartyp Smart Art Shape. Den extraherar sedan texten från dess individuella former enligt ovanstående. Se konsoloutputen från det angivna kodexemplet nedan för en referens.

## **Exempelkod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "DrawingObjects-ExtractTextFromGearTypeSmartArtShape.cs" >}}

## **Konsoloutput**

{{< highlight java >}}

Gear Type Shape Text: Nice

Gear Type Shape Text: Good

Gear Type Shape Text: Excellent

{{< /highlight >}}

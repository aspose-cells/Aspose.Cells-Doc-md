---
title: Extrahera text från SmartArt figurer av typen Gear
type: docs
weight: 500
url: /sv/python-net/extract-text-from-the-gear-type-smartart-shape/
---

## **Möjliga användningsscenario**

Aspose.Cells kan extrahera text från Geartyp Smart konstform. För att göra det ska du först konvertera Smart konstform till gruppkonstform med hjälp av [**Shape.get_result_of_smart_art()**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/get_result_of_smart_art) metoden. Sedan ska du få arrayen av alla individuella former som bildar gruppkonstformen med hjälp av [**GroupShape.get_grouped_shapes()**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/groupshape/get_grouped_shapes) metoden. Slutligen kan du iterera alla individuella former en efter en i en loop och extrahera deras text med hjälp av [**Shape.text**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/text) egenskapen.

## **Extrahera text från SmartArt-form med tandhjulstyp**

Följande kodexempel laddar [exempel Excel-filen](67338483.xlsx) som innehåller Geartyp Smart Art Shape. Den extraherar sedan texten från dess individuella former enligt ovanstående. Se konsoloutputen från det angivna kodexemplet nedan för en referens.

## **Exempelkod**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-ExtractTextFromGearTypeSmartArtShape.py" >}}

## **Konsoloutput**

{{< highlight java >}}

Gear Type Shape Text: Nice

Gear Type Shape Text: Good

Gear Type Shape Text: Excellent

{{< /highlight >}}

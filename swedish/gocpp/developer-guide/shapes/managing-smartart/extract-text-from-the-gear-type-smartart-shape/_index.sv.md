---
title: Extrahera text från Gear typ SmartArt form med Golang via C++
linktitle: Extrahera text från SmartArt figurer av typen Gear
type: docs
weight: 500
url: /sv/go-cpp/extract-text-from-the-gear-type-smartart-shape/
description: Lär dig hur man extraherar text från Gear typ SmartArt former i Excel med Aspose.Cells for C++ med steg för steg guidning och kodexempel.
---

## **Möjliga användningsscenario**

Aspose.Cells for C++ kan extrahera text från Gear-typ SmartArt Shape. Följ dessa steg för att göra det:
1. Konvertera SmartArt Shape till Gruppform med [**Shape::GetResultOfSmartArt()**](https://reference.aspose.com/cells/go-cpp/) metoden.
2. Hämta alla enskilda former som bildar Gruppformen med [**GroupShape::GetGroupedShapes()**](https://reference.aspose.com/cells/go-cpp/) metoden.
3. Loop igenom varje enskild form och extrahera text med [**GetText()**](https://reference.aspose.com/cells/go-cpp/) metoden.

## **Extrahera text från SmartArt-form med tandhjulstyp**

Följande exempel kod laddar en [exempel-Excelfil](67338483.xlsx) som innehåller en Gear-typ SmartArt Shape och extraherar text från dess enskilda former. Se resultaten i konsolutmatningen nedan.

## **Exempelkod**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ExtractTextFromTheGearTypeSmartartShape.go" >}}
## **Konsoloutput**

{{< highlight java >}}
Gear Type Shape Text: Nice
Gear Type Shape Text: Good
Gear Type Shape Text: Excellent
{{< /highlight >}}

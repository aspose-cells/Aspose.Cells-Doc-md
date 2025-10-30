---
title: Skicka form framåt eller bakåt inne i Arbetsbladet
type: docs
weight: 3400
url: /sv/python-net/send-shape-front-or-back-inside-the-worksheet/
---

## **Möjliga användningsscenario**

När flera former finns på samma plats avgörs synligheten av deras z-ordningspositioner. Aspose.Cells för Python via .NET tillhandahåller [**Shape.to_front_or_back()**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/to_front_or_back)-metoden som ändrar z-ordningspositionen för formen. Om du vill skicka formen till bakgrunden använder du ett negativt tal som -1, -2, -3, etc., och om du vill föra formen till fronten använder du ett positivt tal som 1, 2, 3, etc.

## **Skicka form framåt eller bakåt inne i Arbetsbladet**

Följande exempelkod förklarar användningen av [**Shape.to_front_or_back()**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/to_front_or_back) metoden. Se [exempel Excel-filen](50528330.xlsx) som används i koden och [utmatnings Excel-filen](50528331.xlsx) som genereras av den. Skärmdumpen visar effekten av koden på exempel Excel-filen vid utförandet.

![todo:image_alt_text](send-shape-front-or-back-inside-the-worksheet_1.png)

## **Exempelkod**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-SendShapeFrontOrBackInWorksheet.py" >}}
{{< app/cells/assistant language="python-net" >}}

---
title: Ta fram former till fronten eller bakgrunden i ett arbetsblad
type: docs
weight: 3400
url: /sv/python-java/send-shape-front-or-back-inside-the-worksheet/
---

## **Möjliga användningsscenario**

När det finns flera former på samma plats bestäms deras synlighet av deras z-ordningspositioner. Aspose.Cells tillhandahåller [**Shape.toFrontOrBack()**](https://reference.aspose.com/cells/python-java/asposecells.api/shape#toFrontOrBack(int)) metoden som ändrar formens z-ordningsposition. Om du vill skicka formen bakåt använder du ett negativt nummer som -1, -2, -3, osv. och om du vill skicka formen framåt använder du ett positivt nummer som 1, 2, 3, osv.

## **Ta fram form till fronten eller bakgrunden i arbetsbladet**

Följande exempel kod förklarar användningen av [**Shape.toFrontOrBack()**](https://reference.aspose.com/cells/python-java/asposecells.api/shape#toFrontOrBack(int)) metoden. Vänligen se den [exempelfil i Excel](sampleToFrontOrBack.xlsx) som används i koden och [utdata-excelfilen](50528331.xlsx) som genererats av den. Skärmdumpen visar effekten av koden på exempelfilen vid körning.

![todo:image_alt_text](send-shape-front-or-back-inside-the-worksheet_1.png)

## **Exempelkod**

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Examples-pythonjava-Shapes-BringShapeFrontOrBackInWorksheet.py" >}}
{{< app/cells/assistant language="csharp" >}}

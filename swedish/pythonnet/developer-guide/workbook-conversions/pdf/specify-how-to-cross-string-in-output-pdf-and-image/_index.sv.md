---
title: Ange hur strängen ska korsas i utgång PDF och bild
type: docs
weight: 120
url: /sv/python-net/specify-how-to-cross-string-in-output-pdf-and-image/
description: Lär dig hur du korsar strängen i utgång PDF och bild med Aspose.Cells for Python via .NET API.
keywords: Python Cross String in output PDF and image
---
##  **Möjliga användningsscenarier**

När en cell innehåller text eller sträng men den är större än cellens bredd, svämmar strängen över om nästa cell i nästa kolumn är null eller tom. När du sparar din Excel-fil i PDF/Image kan du kontrollera detta överflöde genom att ange korstypen med hjälp av[**TextCrossType**](https://reference.aspose.com/cells/python-net/aspose.cells/textcrosstype/)uppräkning. Den har följande värden

- *TextCrossType.DEFAULT**: Visa text som MS Excel som beror på nästa cell. Om nästa cell är null kommer strängen att korsas eller trunkeras.

- *TextCrossType.CROSS_KEEP**: Visa strängen som MS Excel som exporterar PDF/Bild

- *TextCrossType.CROSS_OVERRIDE**: Visa all text genom att korsa andra celler och åsidosätta texten i korsade celler

- *TextCrossType.STRICT_IN_CELL**: Visa endast strängen inom cellens bredd.

##  **Ange hur strängen ska korsas i utdata PDF/Bild med TextCrossType**

Följande exempelkod laddar exemplet i Excel-filen och sparar den i PDF/bildformat genom att ange olika[**TextCrossType**](https://reference.aspose.com/cells/python-net/aspose.cells/textcrosstype/)Exemplet på Excel-filen och utdatafilerna kan laddas ner från följande länkar:

[sampleCrossType.xlsx](81920905.xlsx)

[outputCrossType.pdf](81920903.pdf)

[outputCrossType.png](81920904.png)

###  Exempelkod

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-RenderUsingTextCrossType-1.py" >}}

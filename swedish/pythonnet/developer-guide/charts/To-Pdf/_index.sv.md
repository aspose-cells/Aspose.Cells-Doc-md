---
title: Diagram till PDF 
description: Lär dig hur du använder Aspose.Cells för Python via .NET för att konvertera ett diagram till en PDF dokument. Vår guide visar hur man exporterar ett diagram från Microsoft Excel och sparar det som en PDF för vidare distribution och arkivering.
keywords: Aspose.Cells för Python via .NET, Diagram till PDF, Microsoft Excel, PDF konvertering, Export, Distribution, Arkivering.
type: docs
weight: 47
url: /sv/python-net/chart-to-pdf/
---

## **Rendera diagram till PDF**

För att kunna rendera diagrammet till PDF-format har Aspose.Cells för Python via .NET exponerat [**Chart.to_pdf**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/chart/to_pdf) metoden med möjlighet att lagra den resulterande PDF:en på diskväg eller Stream.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-ChartRenderingChartToPDF.py" >}}

## **Skapa diagram-PDF med önskad sidstorlek**
Du kan skapa diagram-PDF med önskad sidstorlek med Aspose.Cells för Python via .NET och ange hur du vill justera diagrammet på sidan, exempelvis topp, botten, centrum, vänster, höger etc. Dessutom kan utdata-diagrammet skapas i ström eller på disk. Se följande exempel som laddar [exempel-Excelfil](64716906.xlsx), får åtkomst till det första diagrammet i kalkylbladet och konverterar det till [utgångs-PDF](64716907.pdf) med önskad sidstorlek. Följande skärmbild visar att sidstorleken i utdata-PDF är 7x7 som specificerat i koden och diagrammet är centrumjusterat både horisontellt och vertikalt. 

![todo:image_alt_text](create-chart-pdf-with-desired-page-size_1.png)
## **Exempelkod**
{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-CreateChartPDFWithDesiredPageSize.py" >}}

{{< app/cells/assistant language="python-net" >}}

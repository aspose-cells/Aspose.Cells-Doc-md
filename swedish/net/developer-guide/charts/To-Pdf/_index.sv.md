---
title:  Diagram till PDF
type: docs
weight: 47
url: /sv/net/chart-to-pdf/
---
##  **Återgivningsdiagram till PDF**

 För att återge diagrammet till PDF-formatet har API:erna Aspose.Cells exponerat[**Chart.ToPdf**](https://reference.aspose.com/cells/net/aspose.cells.charts/chart/methods/topdf/index)metod med förmågan att lagra den resulterande PDF på skivväg eller Stream.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ChartRendering-ChartRenderingChartToPDF.cs" >}}

##  **Skapa diagram PDF med önskad sidstorlek**
 Du kan skapa diagram-Pdf med önskad sidstorlek med hjälp av Aspose.Cells och ange hur du vill anpassa diagrammet inuti sidan som topp, botten, mitten, vänster, höger etc. Dessutom kan utdatadiagrammet skapas i stream eller på disk. Se följande exempelkod som laddar[exempel på Excel-fil](64716906.xlsx) , kommer åt det första diagrammet i kalkylbladet och konverterar det sedan till[utgång pdf](64716907.pdf)med önskad sidstorlek. Följande skärmdump visar att sidstorleken i utdata Pdf är 7x7 som specificerats i koden och diagrammet är mittjusterat både horisontellt och vertikalt.

![todo:image_alt_text](create-chart-pdf-with-desired-page-size_1.png)
##  **Exempelkod**
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Charts-CreateChartPDFWithDesiredPageSize.cs" >}}


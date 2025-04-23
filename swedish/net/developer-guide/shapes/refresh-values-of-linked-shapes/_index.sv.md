---
title: Uppdatera värdena för länkade former
type: docs
weight: 3200
url: /sv/net/refresh-values-of-linked-shapes/
---

{{% alert color="primary" %}}

Ibland har du en länkad form i din Excel-fil som är länkad till någon cell. I Microsoft Excel ändrar ändra värdet i den länkade cellen även värdet för den länkade formen. Det fungerar också bra med Aspose.Cells om du vill spara din arbetsbok i XLS- eller XLSX-format. Om du dock vill spara din arbetsbok i PDF- eller HTML-format måste du ringa [**Worksheet.Shapes.UpdateSelectedValue()**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/updateselectedvalue)-metoden för att uppdatera värdet för den länkade formen.

{{% /alert %}}

## Exempel

Följande skärmbild visar den käll-Excel-fil som används i provkoden nedan. Den har en länkad bild som är länkad till cellerna A1 till E4. Vi kommer att ändra värdet i cell B4 med Aspose.Cells och sedan ringa [**Worksheet.Shapes.UpdateSelectedValue()**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/updateselectedvalue)-metoden för att uppdatera värdet för bilden och spara den i PDF-format.

![todo:image_alt_text](refresh-values-of-linked-shapes_1.jpg)

Du kan ladda ner [käll-Excel-filen](95584291.xlsx) och [utmatnings-PDF-filen](95584292.pdf) från de angivna länkarna.

### C#-kod för att uppdatera värdena för länkade former

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-RefreshValueOfLinkedShapes-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}

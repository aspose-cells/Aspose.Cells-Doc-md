---
title: Uppdatera värden för länkade former
type: docs
weight: 3200
url: /sv/net/refresh-values-of-linked-shapes/
---
{{% alert color="primary" %}}

Ibland har du en länkad form i din Excel-fil som är länkad till någon cell. I Microsoft Excel ändras värdet på den länkade cellen också värdet på den länkade formen. Detta fungerar också bra med Aspose.Cells om du vill spara din arbetsbok i XLS- eller XLSX-format. Men om du vill spara din arbetsbok i PDF- eller HTML-format måste du ringa[**Worksheet.Shapes.UpdateSelectedValue()**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/updateselectedvalue) metod för att uppdatera värdet på den länkade formen.

{{% /alert %}}

## Exempel

 Följande skärmdump visar källfilen för Excel som används i exempelkoden nedan. Den har en länkad bild kopplad till cellerna A1 till E4. Vi ändrar värdet på cell B4 med Aspose.Cells och ringer sedan[**Worksheet.Shapes.UpdateSelectedValue()**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/updateselectedvalue)metod för att uppdatera bildens värde och spara den i PDF-format.

![todo:image_alt_text](refresh-values-of-linked-shapes_1.jpg)

Du kan ladda ner[käll Excel-fil](95584291.xlsx) och den[mata ut PDF](95584292.pdf) från de angivna länkarna.

### C# kod för att uppdatera värdena för länkade former

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageChartsAndShapes-RefreshValueOfLinkedShapes-1.cs" >}}

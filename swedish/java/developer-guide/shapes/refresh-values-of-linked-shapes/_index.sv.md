---
title: Uppdatera värdena för länkade former
type: docs
weight: 3000
url: /sv/java/refresh-values-of-linked-shapes/
---

{{% alert color="primary" %}}

Ibland har du en länkad form i din Excel-fil som är länkad till någon cell. I Microsoft Excel ändrar en ändring av värdet för den länkade cellen också värdet för den länkade formen. Detta fungerar också bra med Aspose.Cells om du vill spara din arbetsbok i XLS- eller XLSX-format. Men om du vill spara din arbetsbok i PDF- eller HTML-format, måste du anropa [**Worksheet.getShapes().updateSelectedValue()**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection/#updateSelectedValue--) -metoden för att uppdatera värdet för den länkade formen.

{{% /alert %}}

## Exempel

Följande skärmbild visar käll-Excel-filen som används i koden nedan. Den har en länkad **Bild 1** länkad till cell A1. Vi kommer att ändra värdet för cell A1 med Aspose.Cells och sedan anropa [**Worksheet.getShapes().updateSelectedValue()**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection/#updateSelectedValue--) -metoden för att uppdatera värdet för **Bild 1** och spara den i PDF-format.

![todo:image_alt_text](refresh-values-of-linked-shapes_1.png)

Du kan ladda ner den [käll-Excel-filen](5472956.xlsx) och den [utdata PDF](5472955.pdf) från de angivna länkarna.

### Java-kod för att uppdatera värdena för länkade former

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-RefreshValuesOfLinkedShapes-RefreshValuesOfLinkedShapes.java" >}}

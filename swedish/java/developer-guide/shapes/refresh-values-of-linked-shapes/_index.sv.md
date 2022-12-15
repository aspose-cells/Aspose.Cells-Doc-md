---
title: Uppdatera värden för länkade former
type: docs
weight: 3000
url: /sv/java/refresh-values-of-linked-shapes/
---
{{% alert color="primary" %}}

Ibland har du en länkad form i din Excel-fil som är länkad till någon cell. I Microsoft Excel ändras värdet på den länkade cellen också värdet på den länkade formen. Detta fungerar också bra med Aspose.Cells om du vill spara din arbetsbok i XLS- eller XLSX-format. Men om du vill spara din arbetsbok i PDF- eller HTML-format måste du ringa[**Worksheet.getShapes().updateSelectedValue()**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#updateSelectedValue()) metod för att uppdatera värdet på den länkade formen.

{{% /alert %}}

## Exempel

 Följande skärmdump visar källfilen för Excel som används i exempelkoden nedan. Den har en länkad**Bild 1** kopplad till cell A1. Vi ändrar värdet på cell A1 med Aspose.Cells och ringer sedan[**Worksheet.getShapes().updateSelectedValue()**](https://reference.aspose.com/cells/java/com.aspose.cells/shapecollection#updateSelectedValue() ) metod för att uppdatera värdet på**Bild 1** och spara den i PDF-format.

![todo:image_alt_text](refresh-values-of-linked-shapes_1.png)

Du kan ladda ner[käll Excel-fil](5472956.xlsx) och den[mata ut PDF](5472955.pdf) från de angivna länkarna.

### Java kod för att uppdatera värdena för länkade former

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-RefreshValuesOfLinkedShapes-RefreshValuesOfLinkedShapes.java" >}}

---
title: Exportera intervallet Cells i ett kalkylblad till bild
type: docs
weight: 130
url: /sv/java/export-range-of-cells-in-a-worksheet-to-image/
---
{{% alert color="primary" %}}

Du kan skapa en bild av ett kalkylblad med Aspose.Cells. Men ibland behöver du bara exportera ett cellintervall i ett kalkylblad till en bild. Den här artikeln förklarar hur du uppnår detta.

{{% /alert %}}

 För att ta en bild av ett område, ställ in utskriftsområdet till önskat område och ställ sedan in alla marginaler till 0. Ställ även in[**ImageOrPrintOptions.setOnePagePerSheet()**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#OnePagePerSheet) till**Sann**.

Följande kod tar en bild av området E8:H10. Nedan finns en skärmdump av källarbetsboken som används i koden. Du kan prova koden med vilken arbetsbok som helst.

**Indatafil**

![todo:image_alt_text](export-range-of-cells-in-a-worksheet-to-image_1.png)

Genom att köra koden skapas endast en bild av området E8:H10.

**Utdatabild**

![todo:image_alt_text](export-range-of-cells-in-a-worksheet-to-image_2.jpg)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-ExportRangeofCells-1.java" >}}

 Du kan också hitta artikeln[Konvertera arbetsblad till olika bildformat](/cells/sv/java/converting-worksheet-to-different-image-formats/) hjälpsam.

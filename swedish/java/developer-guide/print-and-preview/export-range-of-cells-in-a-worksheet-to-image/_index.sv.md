---
title: Exportera område av celler i en arbetsbok till bild
type: docs
weight: 130
url: /sv/java/export-range-of-cells-in-a-worksheet-to-image/
---

{{% alert color="primary" %}}

Du kan skapa en bild av en arbetsbok med hjälp av Aspose.Cells. Ibland behöver du dock exportera endast ett område av celler i en arbetsbok till en bild. Den här artikeln förklarar hur du åstadkommer detta.

{{% /alert %}}

För att ta en bild av ett område, ställ in utskriftsområdet till det önskade området och ställ sedan in alla marginaler till 0. Ställ också in [**ImageOrPrintOptions.setOnePagePerSheet()**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#OnePagePerSheet) till **sant**.

Följande kod tar en bild av området E8:H10. Nedan visas en skärmbild av den källarbetsbok som används i koden. Du kan prova koden med vilken arbetsbok som helst.

**Ingångsfil**

![todo:image_alt_text](export-range-of-cells-in-a-worksheet-to-image_1.png)

Att utföra koden skapar en bild av området E8:H10 endast.

**Utmatningsbild**

![todo:image_alt_text](export-range-of-cells-in-a-worksheet-to-image_2.jpg)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-ExportRangeofCells-1.java" >}}

Du kan också hitta artikeln [Konvertera arbetsblad till olika bildformat](/cells/sv/java/converting-worksheet-to-different-image-formats/) hjälpsam.

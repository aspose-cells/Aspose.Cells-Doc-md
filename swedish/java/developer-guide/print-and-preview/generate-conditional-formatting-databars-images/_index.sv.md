---
title: Generera bilder för betingad formatering DataBars
type: docs
weight: 170
url: /sv/java/generate-conditional-formatting-databars-images/
---

{{% alert color="primary" %}}

Ibland behöver du generera bilder på DataBars för betingad formatering. Du kan använda Aspose.Cells [**DataBar.toImage()**](https://reference.aspose.com/cells/java/com.aspose.cells/databar#toImage-com.aspose.cells.Cell-com.aspose.cells.ImageOrPrintOptions-)-metod för att generera dessa bilder. Denna artikel visar hur man genererar en DataBar-bild med hjälp av Aspose.Cells.

{{% /alert %}}

## **Exempel**

Följande kodexempel genererar DataBar-bilden av cell C1. Först får den åtkomst till cellens formatvillkor-objekt, och sedan från det objektet får det tillgång till DataBar-objektet och använder dess [**DataBar.toImage()**](https://reference.aspose.com/cells/java/com.aspose.cells/databar#toImage-com.aspose.cells.Cell-com.aspose.cells.ImageOrPrintOptions-) metod för att generera bilden av cellen. Slutligen sparar den bilden på disk.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-GenerateDatabarImage-1.java" >}}
{{< app/cells/assistant language="java" >}}

---
title: Infoga tidslinje
linktitle: Tidslinjer
type: docs
weight: 170
url: /sv/net/create-timeline/
description: Lär dig hur du skapar en tidslinje med Aspose.Cells.
---
## **Möjliga användningsscenarier**

Istället för att justera filter för att visa datum kan du använda en PivotTable Timeline——ett dynamiskt filteralternativ som låter dig enkelt filtrera efter datum/tid och zooma in på den period du vill med en skjutreglage. Microsoft Excel låter dig skapa tidslinje genom att välja en pivottabell och sedan klicka på*Infoga > Tidslinje*. Aspose.Cells låter dig också skapa tidslinje med hjälp av[**Worksheet.Timelines.Add()**](https://reference.aspose.com/cells/net/aspose.cells.timelines/timelinecollection/methods/index)metod.

## **Skapa tidslinje till en pivottabell**

 Se följande exempelkod. Den laddar[exempel på Excel-fil](input.xlsx) som innehåller pivottabellen. Den skapar sedan tidslinjen baserat på det första baspivotfältet. Slutligen sparar den arbetsboken[utgång XLSX](output.xlsx) formatera. Följande skärmdump visar tidslinjen skapad av Aspose.Cells i utdata Excel-filen.

![todo:image_alt_text](create-timeline-to-a-pivot-table_1.png)

### **Exempelkod**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Timelines-CreateTimelineToPivotTable.cs" >}}


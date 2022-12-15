---
title: Infoga tidslinje
linktitle: Tidslinjer
type: docs
weight: 170
url: /sv/java/create-timeline/
description: Lär dig hur du skapar en tidslinje med Aspose.Cells för java.
---
## **Möjliga användningsscenarier**

 Istället för att justera filter för att visa datum kan du använda en PivotTable Timeline——ett dynamiskt filteralternativ som låter dig enkelt filtrera efter datum/tid och zooma in på den period du vill med en skjutreglage. Microsoft Excel låter dig skapa en tidslinje genom att välja en pivottabell och sedan klicka på*Infoga > Tidslinje*. Aspose.Cells för java låter dig också skapa tidslinje med metoden [**Worksheet.getTimelines.add()**].

## **Skapa tidslinje till en pivottabell**

 Se följande exempelkod. Den laddar[exempel på Excel-fil](input.xlsx) som innehåller pivottabellen. Den skapar sedan tidslinjen baserat på det första baspivotfältet. Slutligen sparar den arbetsboken[utgång XLSX](output.xlsx) formatera. Följande skärmdump visar tidslinjen skapad av Aspose.Cells i utdata Excel-filen.

<img src="create-timeline-to-a-pivot-table_1.png" width="60%">

### **Exempelkod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Timelines-CreateTimelineToPivotTable.java" >}}


---
title: Infoga tidslinje
linktitle: Tidslinjer
type: docs
weight: 170
url: /sv/python-net/create-timeline/
description: Lär dig hur du skapar en tidslinje med Aspose.Cells for Python via .NET.
---
##  **Möjliga användningsscenarier**

Istället för att justera filter för att visa datum kan du använda en PivotTable Timeline——ett dynamiskt filteralternativ som låter dig enkelt filtrera efter datum/tid och zooma in på den period du vill med en skjutreglage. Microsoft Excel låter dig skapa tidslinje genom att välja en pivottabell och sedan klicka på *Infoga > Tidslinje*. Aspose.Cells for Python via .NET låter dig också skapa tidslinje med hjälp av[**Worksheet.timelines.add()**](https://reference.aspose.com/cells/python-net/aspose.cells.timelines/timelinecollection/#methods)metod.

##  **Skapa tidslinje till en pivottabell**

 Se följande exempelkod. Den laddar[exempel på Excel-fil](input.xlsx)som innehåller pivottabellen. Den skapar sedan tidslinjen baserat på det första baspivotfältet. Slutligen sparar den arbetsboken[utgång XLSX](output.xlsx) formatera. Följande skärmdump visar tidslinjen skapad av Aspose.Cells for Python via .NET i utdata Excel-filen.

![todo:image_alt_text](create-timeline-to-a-pivot-table_1.png)

###  **Exempelkod**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Timelines-CreateTimelineToPivotTable.py" >}}


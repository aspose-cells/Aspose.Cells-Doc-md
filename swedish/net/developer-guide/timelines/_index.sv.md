---
title: Infoga Tidslinje
linktitle: Tidslinjer
type: docs
weight: 170
url: /sv/net/create-timeline/
description: Lär dig hur man skapar en tidslinje med Aspose.Cells.
---

## **Möjliga användningsscenario**

Istället för att anpassa filter för att visa datum kan du använda en pivottabelltidslinje - en dynamisk filteralternativ som låter dig enkelt filtrera efter datum/tid och zooma in på den period du vill med en skjutreglagekontroll. Microsoft Excel tillåter dig att skapa en tidslinje genom att välja en pivottabell och sedan klicka på *Infoga > Tidslinje*. Aspose.Cells tillåter också att skapa tidslinje med hjälp av [**Worksheet.Timelines.Add()**](https://reference.aspose.com/cells/net/aspose.cells.timelines/timelinecollection/methods/index)-metoden.

## **Skapa tidslinje till en Pivot-tabell**

Se följande exempelkod. Den laddar den [provs Excel-fil](input.xlsx) som innehåller pivot-tabellen. Den skapar sedan tidslinjen baserad på det första baspivot-fältet. Slutligen sparar den arbetsboken i [output XLSX](output.xlsx) format. Följande skärmbild visar tidslinjen skapad av Aspose.Cells i den slutliga Excel-filen.

![todo:image_alt_text](create-timeline-to-a-pivot-table_1.png)

### **Exempelkod**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Timelines-CreateTimelineToPivotTable.cs" >}}


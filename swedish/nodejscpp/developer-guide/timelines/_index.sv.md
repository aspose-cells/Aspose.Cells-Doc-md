---
title: Infoga Tidslinje
linktitle: Tidslinjer
type: docs
weight: 170
url: /sv/nodejs-cpp/create-timeline/
description: Lär dig skapa en tidslinje med Aspose.Cells for Node.js via C++.
---

## **Möjliga användningsscenario**

Istället för att justera filter för att visa datum kan du använda en pivottabelltidslinje—ett dynamiskt filteralternativ som låter dig enkelt filtrera efter datum/tid och zooma in på den period du vill ha med en skjutreglagekontroll. Microsoft Excel tillåter dig att skapa tidslinje genom att välja en pivottabell och klicka på *Infoga > Tidslinje*. Aspose.Cells for Node.js via C++ tillåter också att du skapar tidslinje med hjälp av [**Worksheet.getTimelines().add()**](https://reference.aspose.com/cells/nodejs-cpp/timelinecollection/#add-pivottable-number-number-string-)-metoden.

## **Skapa tidslinje till en Pivot-tabell**

Se följande exempel. Det laddar [exempel Excel-fil](input.xlsx) som innehåller pivottabellen. Sedan skapas tidslinjen baserat på det första baspivåfältet. Slutligen sparas arbetsboken i [utdata XLSX](output.xlsx) format. Följande skärmdump visar tidslinjen som skapats av Aspose.Cells for Node.js via C++ i utdata Excel-fil.

![todo:image_alt_text](create-timeline-to-a-pivot-table_1.png)

### **Exempelkod**

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Timelines-CreateTimelineToPivotTable.js" >}}

{{< app/cells/assistant language="nodejs-cpp" >}}

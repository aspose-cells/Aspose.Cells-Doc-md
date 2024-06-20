---
title: Infoga Tidslinje
linktitle: Tidslinjer
type: docs
weight: 170
url: /sv/python-net/create-timeline/
description: Lär dig hur du skapar en tidslinje med Aspose.Cells för Python via .NET.
keywords: Aspose.Cells för Python Excel, Excel Python bibliotek, Skapa tidslinje utan Excel i Python, Lägg till tidslinje via Aspose.Cells för Python, Infoga tidslinje med Aspose.Cells för Python.
---

## **Möjliga användningsscenario**

Istället för att justera filter för att visa datum kan du använda en PivotTable-tidslinje - ett dynamiskt filteralternativ som låter dig enkelt filtrera efter datum/tid och zooma in på den period du vill med en skjutreglage. Microsoft Excel gör det möjligt att skapa tidslinje genom att välja en pivot-tabell och sedan klicka på *Infoga > Tidslinje*. Aspose.Cells för Python via .NET tillåter även att du skapar tidslinje med hjälp av metoden [**Worksheet.timelines.add()**](https://reference.aspose.com/cells/python-net/aspose.cells.timelines/timelinecollection/#methods).

## **Så här skapar du en tidslinje för en pivot-tabell med hjälp av Aspose.Cells för Python Excel-bibliotek**

Se följande provkod. Den laddar [exempel-Excel-filen](input.xlsx) som innehåller pivot-tabellen. Sedan skapar den tidslinjen baserad på det första baspivotfältet. Slutligen sparar den arbetsboken i formatet [output XLSX](output.xlsx). Följande skärmbild visar tidslinjen skapad av Aspose.Cells för Python via .NET i den resulterande Excel-filen.

![todo:image_alt_text](create-timeline-to-a-pivot-table_1.png)

### **Exempelkod**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Timelines-CreateTimelineToPivotTable.py" >}}


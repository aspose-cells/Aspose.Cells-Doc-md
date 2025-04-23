---
title: Infoga Tidslinje
linktitle: Tidslinjer
type: docs
weight: 170
url: /sv/java/create-timeline/
description: Lär dig hur man skapar en tidslinje med Aspose.Cells för java.
---

## **Möjliga användningsscenario**

Istället för att justera filter för att visa datum kan du använda en PivotTable-tidslinje - ett dynamiskt filteralternativ som gör att du enkelt kan filtrera efter datum/tid och zooma in på den period du vill med en skjutreglage. Microsoft Excel låter dig skapa tidslinje genom att välja en pivot-tabell och sedan klicka på *Infoga > Tidslinje*. Aspose.Cells för java låter dig också skapa tidslinje med hjälp av metoden [**Worksheet.getTimelines.add()**].

## **Skapa tidslinje till en Pivot-tabell**

Se följande exempelkod. Den laddar den [provs Excel-fil](input.xlsx) som innehåller pivot-tabellen. Den skapar sedan tidslinjen baserad på det första baspivot-fältet. Slutligen sparar den arbetsboken i [output XLSX](output.xlsx) format. Följande skärmbild visar tidslinjen skapad av Aspose.Cells i den slutliga Excel-filen.

<img src="create-timeline-to-a-pivot-table_1.png" width="60%">

### **Exempelkod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Timelines-CreateTimelineToPivotTable.java" >}}

{{< app/cells/assistant language="java" >}}

---
title: Infoga tidslinje med Golang via C++
linktitle: Tidslinjer
type: docs
weight: 170
url: /sv/go-cpp/create-timeline/
description: Lär dig hur man skapar en tidslinje med Aspose.Cells med C++.
---

## **Möjliga användningsscenario**

Istället för att justera filter för att visa datum kan du använda en pivottabell-tidslinje — ett dynamiskt filteralternativ som låter dig enkelt filtrera efter datum/tid och zooma in på den period du vill ha med en skjutreglagen. Microsoft Excel låter dig skapa en tidslinje genom att välja en pivottabell och sedan klicka på *Infoga > Tidslinje*. Aspose.Cells låter dig också skapa en tidslinje med hjälp av [**Worksheet.Timelines.Add()**](https://reference.aspose.com/cells/go-cpp/timelinecollection/add_pivottable_int_int_string/) metoden.

## **Skapa tidslinje till en Pivot-tabell**

Se följande exempelkod. Den laddar den [provs Excel-fil](input.xlsx) som innehåller pivot-tabellen. Den skapar sedan tidslinjen baserad på det första baspivot-fältet. Slutligen sparar den arbetsboken i [output XLSX](output.xlsx) format. Följande skärmbild visar tidslinjen skapad av Aspose.Cells i den slutliga Excel-filen.

![todo:image_alt_text](create-timeline-to-a-pivot-table_1.png)

### **Exempelkod**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-Timelines.go" >}}

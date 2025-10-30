---
title: Olika sätt att öppna filer
linktitle: Olika sätt att öppna filer
type: docs
weight: 10
url: /sv/cpp/different-ways-to-open-files/
---

{{% alert color="primary" %}} 

Med Aspose.Cells är det möjligt att öppna filer, till exempel för att hämta data eller använda en designer mall för att påskynda utvecklingsprocessen. Aspose.Cells kan öppna olika typer av filer, som Microsoft Excel kalkylblad (XLS, XLSX, XLSM, XLSB), CSV eller Tabulator-avgränsade filer.

{{% /alert %}} 
## **Öppna en fil via en sökväg**
Utvecklare kan öppna en Microsoft Excel-fil med hjälp av dess sökväg på den lokala datorn genom att specificera det i konstruktorn för [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)klassen. Skicka helt enkelt sökvägen i konstruktorn som en sträng. Aspose.Cells kommer automatiskt att upptäcka filformatet.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-LoadingSavingAndConverting-OpeningFiles-OpeningExcelFileUsingPath-new.cpp" >}}

## **Öppna en fil med hjälp av en ström**
Det är också möjligt att öppna en Excel-fil som en ström. För att göra det, använd en överlagrad version av konstruktorn som tar emot *Stream*objektet som innehåller filen.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-LoadingSavingAndConverting-OpeningFiles-OpeningExcelFileUsingStream-new.cpp" >}}

{{< app/cells/assistant language="cpp" >}}

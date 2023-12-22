---
title: Olika sätt att öppna filer
linktitle: Olika sätt att öppna filer
type: docs
weight: 10
url: /sv/cpp/different-ways-to-open-files/
---
{{% alert color="primary" %}} 

Med Aspose.Cells är det möjligt att öppna filer, till exempel för att hämta data, eller att använda en designermall för att påskynda utvecklingsprocessen. Aspose.Cells kan öppna en rad olika filer, till exempel Microsoft Excel-kalkylblad (XLS, XLSX, XLSM, XLSB), CSV eller 071618344.

{{% /alert %}} 
##  **Öppna en fil via en sökväg**
 Utvecklare kan öppna en Microsoft Excel-fil med dess sökväg på den lokala datorn genom att ange den i[Arbetsbok](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)klass konstruktör. Skicka bara sökvägen i konstruktorn som sträng. Aspose.Cells kommer automatiskt att upptäcka filformatstypen.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-LoadingSavingAndConverting-OpeningFiles-OpeningExcelFileUsingPath-new.cpp" >}}

##  **Öppna en fil med en Stream**
 Det är också möjligt att öppna en Excel-fil som en stream. För att göra det, använd en överbelastad version av konstruktorn som tar*Ström*objekt som innehåller filen.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-LoadingSavingAndConverting-OpeningFiles-OpeningExcelFileUsingStream-new.cpp" >}}


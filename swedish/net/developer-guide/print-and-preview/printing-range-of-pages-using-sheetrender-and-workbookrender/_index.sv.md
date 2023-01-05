---
title: Skriva ut omfång av sidor med SheetRender och WorkbookRender
type: docs
weight: 250
url: /sv/net/printing-range-of-pages-using-sheetrender-and-workbookrender/
---
{{% alert color="primary" %}} 

Microsoft Excel låter dig skriva ut ett antal sidor i arbetsbok eller kalkylblad. Följande skärmdump visar Microsoft Excel-gränssnittet för att specificera sidorna.

Aspose.Cells tillhandahåller metoderna WorkbookRender.ToPrinter(string PrinterName, int PrintPageIndex, int PrintPageCount) och SheetRender.ToPrinter(string PrinterName, int PrintPageIndex, int PrintPageCount) för detta ändamål.

{{% /alert %}} 
## **Microsoft Excel-gränssnitt för att ange intervallet för sidor som ska skrivas ut**
Följande exempelkod illustrerar användningen av metoderna WorkbookRender.ToPrinter(string PrinterName, int PrintPageIndex, int PrintPageCount) och SheetRender.ToPrinter(string PrinterName, int PrintPageIndex, int PrintPageCount). Den skriver ut sidorna 2-5 i arbetsboken och arbetsbladet.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-PrintingRangeOfPages-PrintingSpecificRangeOfPages.cs" >}}

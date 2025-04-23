---
title: Utskrift av sidområde med hjälp av SheetRender och WorkbookRender
type: docs
weight: 250
url: /sv/net/printing-range-of-pages-using-sheetrender-and-workbookrender/
---

{{% alert color="primary" %}} 

Microsoft Excel ger dig möjlighet att skriva ut sidområdet av arbetsbok eller arbetsblad. I följande skärmbild visas gränssnittet i Microsoft Excel för att ange sidområdet.

Aspose.Cells tillhandahåller metoderna WorkbookRender.ToPrinter(string PrinterName, int PrintPageIndex, int PrintPageCount) och SheetRender.ToPrinter(string PrinterName, int PrintPageIndex, int PrintPageCount) för detta ändamål.

{{% /alert %}} 
## **Microsoft Excel-gränssnitt för att ange sidområdet att skriva ut**
Följande kodexempel illustrerar användningen av metoderna WorkbookRender.ToPrinter(string PrinterName, int PrintPageIndex, int PrintPageCount) och SheetRender.ToPrinter(string PrinterName, int PrintPageIndex, int PrintPageCount). Den skriver ut sidorna 2-5 från arbetsboken och arbetsbladet.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderingAndPrinting-PrintingRangeOfPages-PrintingSpecificRangeOfPages.cs" >}}
{{< app/cells/assistant language="csharp" >}}

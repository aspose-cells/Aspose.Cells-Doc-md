---
title: Förhandsvisning av arbetsbok och arbetsblad
type: docs
weight: 130
url: /sv/java/workbook-and-worksheet-print-preview/
---
## **Användningsscenario**

Det kan finnas fall där Excel-filer med miljontals sidor behöver konverteras till PDF eller bilder. Att bearbeta sådana filer kommer att ta mycket tid och resurser. I sådana fall kan funktionen för förhandsgranskning av arbetsbok och arbetsblad visa sig vara användbar. Innan sådana filer konverteras kan användaren kontrollera det totala antalet sidor och sedan bestämma om filen ska konverteras eller inte. Den här artikeln fokuserar på att använda[**WorkbookPrintingPreview**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookPrintingPreview)och[**SheetPrintingPreview**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetPrintingPreview)klasser för att ta reda på det totala antalet sidor.

## **Förhandsvisning av arbetsbok och arbetsblad**

Aspose.Cells tillhandahåller förhandsgranskningsfunktionen. För detta tillhandahåller API[**WorkbookPrintingPreview**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookPrintingPreview)och[**SheetPrintingPreview**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetPrintingPreview)klasser. För att skapa förhandsvisningen av hela arbetsboken skapar du en instans av[**WorkbookPrintingPreview**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookPrintingPreview)klass genom att passera[**Arbetsbok**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)och[**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions)objekt till konstruktören. De[**WorkbookPrintingPreview**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookPrintingPreview)klass ger en[**EvaluatedPageCount**](https://reference.aspose.com/cells/java/com.aspose.cells/workbookprintingpreview#EvaluatedPageCount)metod som returnerar antalet sidor i den genererade förhandsvisningen. Liknande[**WorkbookPrintingPreview**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookPrintingPreview)klass, den[**SheetPrintingPreview**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetPrintingPreview)klass används för att generera en förhandsgranskning för ett specifikt kalkylblad. För att skapa förhandsvisningen av ett kalkylblad, skapa en instans av[**SheetPrintingPreview**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetPrintingPreview)klass genom att passera[**Arbetsblad**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet)och[**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions)objekt till konstruktören. De[**SheetPrintingPreview**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetPrintingPreview)klass ger också en[**EvaluatedPageCount**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetprintingpreview#EvaluatedPageCount)metod som returnerar antalet sidor i den genererade förhandsvisningen.

Följande kodavsnitt visar användningen av båda[**WorkbookPrintingPreview**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookPrintingPreview)och[**SheetPrintingPreview**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetPrintingPreview)klasser genom att använda[exempel på excel-fil](Book1.xlsx).

### **Exempelkod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-PrintPreview-1.java" >}}

Följande är utdata som genereras genom att exekvera ovanstående kod.

### **Konsolutgång**

Antal sidor i arbetsboken: 1</br>
Antal sidor i arbetsbladet: 1

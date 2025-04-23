---
title: Utskriftsgranskning av arbetsbok och kalkylblad
type: docs
weight: 130
url: /sv/java/workbook-and-worksheet-print-preview/
---

## **Användningsscenarie**

Det kan hända att Excel-filer med miljontals sidor behöver konverteras till PDF eller bilder. Att behandla sådana filer kommer att kräva mycket tid och resurser. I sådana fall kan arbetsbok- och kalkylbladsutskriftsgranskningsfunktionen vara användbar. Innan sådana filer konverteras kan användaren kontrollera det totala antalet sidor och sedan bestämma om filen ska konverteras eller inte. Denna artikel fokuserar på att använda klasserna [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookPrintingPreview) och [**SheetPrintingPreview**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetPrintingPreview) för att ta reda på det totala antalet sidor.

## **Utskriftsgranskning av arbetsbok och kalkylblad**

Aspose.Cells tillhandahåller utskriftsgranskningsfunktionen. För detta tillhandahåller API:et klasserna [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookPrintingPreview) och [**SheetPrintingPreview**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetPrintingPreview). För att skapa utskriftsgranskningen av hela arbetsboken, skapa en instans av klassen [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookPrintingPreview) genom att skicka [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook) och [**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions) objekt till konstruktören. Klassen [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookPrintingPreview) tillhandahåller en metod [**EvaluatedPageCount**](https://reference.aspose.com/cells/java/com.aspose.cells/workbookprintingpreview#EvaluatedPageCount) som returnerar antalet sidor i den genererade granskningen. Liknande klass [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookPrintingPreview) används för att generera en utskriftsgranskning för ett specifikt kalkylblad. För att skapa utskriftsgranskningen av ett kalkylblad, skapa en instans av klassen [**SheetPrintingPreview**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetPrintingPreview) genom att skicka [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) och [**ImageOrPrintOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/ImageOrPrintOptions) objekt till konstruktören. Klassen [**SheetPrintingPreview**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetPrintingPreview) tillhandahåller också en metod [**EvaluatedPageCount**](https://reference.aspose.com/cells/java/com.aspose.cells/sheetprintingpreview#EvaluatedPageCount) som returnerar antalet sidor i den genererade granskningen.

Följande kodsnutt demonstrerar användningen av både klasserna [**WorkbookPrintingPreview**](https://reference.aspose.com/cells/java/com.aspose.cells/WorkbookPrintingPreview) och [**SheetPrintingPreview**](https://reference.aspose.com/cells/java/com.aspose.cells/SheetPrintingPreview) genom att använda [provexcelfilen](Book1.xlsx).

### **Exempelkod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-PrintPreview-1.java" >}}

Följande är utdatan som genereras genom att köra ovanstående kod.

### **Konsoloutput**

{{< highlight java >}}

Workbook page count: 1</br>
Worksheet page count: 1

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}

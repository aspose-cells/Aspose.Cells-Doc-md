---
title: Kontrollera laddning av externa resurser i MS Excel arbetsbok vid rendering till PDF
type: docs
weight: 40
url: /sv/java/control-loading-of-external-resources-in-ms-excel-workbook-while-rendering-to-pdf/
---

## **Möjliga användningsscenario**

Din Excelfil kan innehålla externa resurser, t.ex. länkade bilder eller objekt. När du konverterar din Excelfil till PDF, hämtar Aspose.Cells dessa externa resurser och renderar dem till PDF. Men ibland vill du inte ladda dessa externa resurser och dessutom vill du manipulera dem. Det kan du göra med [**PdfSaveOptions.StreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#StreamProvider) som implementerar [**IStreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/IStreamProvider)-gränssnittet.

## **Kontrollera inläsning av externa resurser i MS Excel Arbetsbok vid rendering till PDF**

Följande exempelkod förklarar hur man använder [**PdfSaveOptions.StreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#StreamProvider) för att kontrollera laddningen av externa resurser och manipulera dem. Var vänlig kontrollera den [exempel Excelfil](50528353.xlsx) som används inuti koden och den [utdatan PDF-filen](50528354.pdf) som genererats av koden. [Skärmdumpen](50528357.png) visar hur [den gamla externa bilden](50528356.png) i den exempel Excelfilen ersattes med en [ny bild](50528355.png) i utdatan PDF.

![todo:image_alt_text](control-loading-of-external-resources-in-ms-excel-workbook-while-rendering-to-pdf_1.png)

## **Exempelkod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Rendering-ControlLoadingOfExternalResourcesInExcelToPDF.java" >}}

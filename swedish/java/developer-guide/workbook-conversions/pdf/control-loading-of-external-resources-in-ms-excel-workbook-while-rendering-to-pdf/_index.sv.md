---
title: Kontrollera laddningen av externa resurser i MS Excel Workbook under rendering till PDF
type: docs
weight: 40
url: /sv/java/control-loading-of-external-resources-in-ms-excel-workbook-while-rendering-to-pdf/
---
## **Möjliga användningsscenarier**

Din Excel-fil kan innehålla externa resurser, t.ex. länkade bilder eller objekt. När du konverterar din Excel-fil till PDF, hämtar Aspose.Cells dessa externa resurser och renderar dem till PDF. Men ibland vill du inte ladda dessa externa resurser och mer än så vill du manipulera dem. Du kan göra detta med hjälp av[**PdfSaveOptions.StreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#StreamProvider)som implementerar[**IStreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/IStreamProvider)gränssnitt.

## **Kontrollera laddningen av externa resurser i MS Excel Workbook under rendering till PDF**

Följande exempelkod förklarar hur du använder[**PdfSaveOptions.StreamProvider**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#StreamProvider)att kontrollera belastningen av externa resurser och manipulera dem. Vänligen kontrollera[exempel på Excel-fil](50528353.xlsx)används i koden och[utgång PDF](50528354.pdf)genereras av koden. De[skärmdump](50528357.png)visar hur[gammal extern bild](50528356.png)i exemplet Excel-filen ersattes med en[ny bild](50528355.png)i utgången PDF.

![todo:image_alt_text](control-loading-of-external-resources-in-ms-excel-workbook-while-rendering-to-pdf_1.png)

## **Exempelkod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Rendering-ControlLoadingOfExternalResourcesInExcelToPDF.java" >}}

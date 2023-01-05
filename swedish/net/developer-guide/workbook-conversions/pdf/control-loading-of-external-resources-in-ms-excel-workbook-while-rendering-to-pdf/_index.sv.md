---
title: Kontrollera laddningen av externa resurser i MS Excel Workbook under rendering till PDF
type: docs
weight: 40
url: /sv/net/control-loading-of-external-resources-in-ms-excel-workbook-while-rendering-to-pdf/
---
## **Möjliga användningsscenarier**

Din Excel-fil kan innehålla externa resurser, t.ex. länkade bilder eller objekt. När du konverterar din Excel-fil till PDF, hämtar Aspose.Cells dessa externa resurser och renderar dem till PDF. Men ibland vill du inte ladda dessa externa resurser och mer än så vill du manipulera dem. Du kan göra detta med hjälp av[**WorkbookSettings.StreamProvider**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/streamprovider)som implementerar[**IStreamProvider**](https://reference.aspose.com/cells/net/aspose.cells/istreamprovider)gränssnitt.

## **Kontrollera laddningen av externa resurser i MS Excel Workbook under rendering till PDF**

 Följande exempelkod förklarar hur du använder[**WorkbookSettings.StreamProvider**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/streamprovider) att kontrollera belastningen av externa resurser och manipulera dem. Vänligen kontrollera[exempel på Excel-fil](50528322.xlsx) används i koden och[utgång PDF](50528325.pdf) genereras av koden. De[skärmdump](50528326.png) visar hur[gammal extern bild](50528324.png) i exemplet Excel-filen ersattes med en[ny bild](50528323.png) i utgången PDF.

![todo:image_alt_text](control-loading-of-external-resources-in-ms-excel-workbook-while-rendering-to-pdf_1.png)

## **Exempelkod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Rendering-ControlLoadingOfExternalResourcesInExcelToPDF-1.cs" >}}

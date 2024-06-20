---
title: Kontrollera laddning av externa resurser i MS Excel arbetsbok vid rendering till PDF
type: docs
weight: 40
url: /sv/net/control-loading-of-external-resources-in-ms-excel-workbook-while-rendering-to-pdf/
---

## **Möjliga användningsscenario**

Din Excel-fil kan innehålla externa resurser t.ex. länkade bilder eller objekt. När du konverterar din Excel-fil till PDF hämtar Aspose.Cells dessa externa resurser och renderar dem till PDF. Men ibland vill du inte ladda in dessa externa resurser och dessutom vill du manipulera dem. Det kan du göra med hjälp av [**WorkbookSettings.StreamProvider**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/streamprovider) som implementerar [**IStreamProvider**](https://reference.aspose.com/cells/net/aspose.cells/istreamprovider) gränssnitt.

## **Kontrollera inläsning av externa resurser i MS Excel Arbetsbok vid rendering till PDF**

Följande kodexempel förklarar hur man använder [**WorkbookSettings.StreamProvider**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/streamprovider) för att kontrollera laddningen av externa resurser och manipulera dem. Kolla in den [exempel-Excel-filen](50528322.xlsx) som används i koden och den [genererade PDF:en](50528325.pdf) skapad av koden. [Skärmbilden](50528326.png) visar hur den [gamla externa bilden](50528324.png) i den exemplariska Excel-filen ersattes med en [ny bild](50528323.png) i utdata-PDF:en.

![todo:image_alt_text](control-loading-of-external-resources-in-ms-excel-workbook-while-rendering-to-pdf_1.png)

## **Exempelkod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Rendering-ControlLoadingOfExternalResourcesInExcelToPDF-1.cs" >}}

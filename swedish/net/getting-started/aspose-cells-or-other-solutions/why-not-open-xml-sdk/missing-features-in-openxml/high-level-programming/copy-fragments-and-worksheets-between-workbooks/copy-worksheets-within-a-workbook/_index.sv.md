---
title: Kopiera kalkylblad inom en arbetsbok
type: docs
weight: 20
url: /sv/net/copy-worksheets-within-a-workbook/
---

**Aspose.Cells** tillhandahåller en överlagrad metod, **Aspose.Cells.WorksheetCollection.AddCopy()**, som används för att lägga till ett kalkylblad i samlingen och kopiera data från ett befintligt kalkylblad. En version av metoden tar index för källkalkylbladet som parameter. Den andra versionen tar namnet på källkalkylbladet som parameter.

Det följande exemplet visar hur man kopierar ett befintligt kalkylblad inom en arbetsbok.

{{< highlight csharp >}}

 //Create a new Workbook.

//Open an existing Excel file.

Workbook wb = new Workbook("ResultedBook.xls");

//Create a Worksheets object with reference to

//the sheets of the Workbook.

WorksheetCollection sheets = wb.Worksheets;

//Copy data to a new sheet from an existing

//sheet within the Workbook.

sheets.AddCopy("MySheet");

//Save the Excel file.

wb.Save("Copy Worksheet.xls");

{{< /highlight >}}
## **Ladda ned provkoden**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Copy%20Worksheet%20%28Aspose.Cells%29.zip)

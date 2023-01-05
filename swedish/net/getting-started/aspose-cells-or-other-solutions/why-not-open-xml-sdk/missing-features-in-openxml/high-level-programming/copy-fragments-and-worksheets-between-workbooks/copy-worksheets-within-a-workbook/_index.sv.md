---
title: Kopiera arbetsblad i en arbetsbok
type: docs
weight: 20
url: /sv/net/copy-worksheets-within-a-workbook/
---
**Aspose.Cells** ger en överbelastad metod,**Aspose.Cells.WorksheetCollection.AddCopy()**, som används för att lägga till ett kalkylblad till samlingen och kopierar data från ett befintligt kalkylblad. En version av metoden tar källarkets index som en parameter. Den andra versionen tar namnet på källarbetsbladet som parameter.

Följande exempel visar hur man kopierar ett befintligt kalkylblad i en arbetsbok.

{{< highlight "csharp" >}}

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
## **Ladda ner provkod**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
- [Bit hink](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Copy%20Worksheet%20%28Aspose.Cells%29.zip)

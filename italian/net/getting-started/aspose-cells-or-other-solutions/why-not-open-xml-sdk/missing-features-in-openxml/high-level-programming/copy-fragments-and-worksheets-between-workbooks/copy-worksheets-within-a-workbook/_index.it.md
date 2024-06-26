---
title: Copia i fogli all interno del workbook
type: docs
weight: 20
url: /it/net/copy-worksheets-within-a-workbook/
---

**Aspose.Cells** fornisce un metodo sovraccaricato, **Aspose.Cells.WorksheetCollection.AddCopy()**, che viene utilizzato per aggiungere un foglio di lavoro alla collezione e copia i dati da un foglio di lavoro esistente. Una versione del metodo prende l'indice del foglio di lavoro sorgente come parametro. L'altra versione prende il nome del foglio di lavoro sorgente come parametro.

Nell'esempio seguente viene mostrato come copiare un foglio di lavoro esistente all'interno di un libro.

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
## **Scarica il codice di esempio**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Copy%20Worksheet%20%28Aspose.Cells%29.zip)

---
title: Copia i fogli di lavoro all'interno di una cartella di lavoro
type: docs
weight: 20
url: /it/net/copy-worksheets-within-a-workbook/
---
**Aspose.Cells** fornisce un metodo sovraccarico,**Aspose.Cells.WorksheetCollection.AddCopy()**, utilizzato per aggiungere un foglio di lavoro alla raccolta e copiare i dati da un foglio di lavoro esistente. Una versione del metodo accetta l'indice del foglio di lavoro di origine come parametro. L'altra versione prende il nome del foglio di lavoro di origine come parametro.

L'esempio seguente mostra come copiare un foglio di lavoro esistente all'interno di una cartella di lavoro.

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
## **Scarica il codice di esempio**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Copy%20Worksheet%20%28Aspose.Cells%29.zip)

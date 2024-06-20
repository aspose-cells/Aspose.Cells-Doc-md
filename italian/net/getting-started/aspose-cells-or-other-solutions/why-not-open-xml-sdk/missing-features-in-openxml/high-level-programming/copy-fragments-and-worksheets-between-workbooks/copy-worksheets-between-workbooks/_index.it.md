---
title: Copia i fogli tra i workbook
type: docs
weight: 10
url: /it/net/copy-worksheets-between-workbooks/
---

Aspose.Cells fornisce un metodo, Aspose.Cells.Worksheet.Copy(), utilizzato per copiare dati e formattazione da un foglio di lavoro sorgente a un altro foglio di lavoro all'interno o tra i workbook. Il metodo prende l'oggetto foglio di lavoro sorgente come parametro.

L'esempio seguente mostra come copiare un foglio di lavoro da un libro di lavoro a un altro libro di lavoro.

{{< highlight csharp >}}

 string FilePath = @"..\..\..\Sample Files\";

string FileName = FilePath + "Copy Sheet between Workbook.xlsx";

//Create a new Workbook.

Workbook excelWorkbook0 = new Workbook();

//Get the first worksheet in the book.

Worksheet ws0 = excelWorkbook0.Worksheets[0];

//Put some data into header rows (A1:A4)

for (int i = 0; i < 5; i++)

{

    ws0.Cells[i, 0].PutValue(string.Format("Header Row {0}", i));

}

//Put some detail data (A5:A999)

for (int i = 5; i < 1000; i++)

{

    ws0.Cells[i, 0].PutValue(string.Format("Detail Row {0}", i));

}

//Define a pagesetup object based on the first worksheet.

PageSetup pagesetup = ws0.PageSetup;

//The first five rows are repeated in each page...

//It can be seen in print preview.

pagesetup.PrintTitleRows = "$1:$5";

//Create another Workbook.

Workbook excelWorkbook1 = new Workbook();

//Get the first worksheet in the book.

Worksheet ws1 = excelWorkbook1.Worksheets[0];

//Name the worksheet.

ws1.Name = "MySheet";

//Copy data from the first worksheet of the first workbook into the

//first worksheet of the second workbook.

ws1.Copy(ws0);

//Save the excel file.

excelWorkbook1.Save(FileName);

{{< /highlight >}}
## **Scarica il codice di esempio**
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Copy%20between%20Workbooks%20%28Aspose.Cells%29.zip)

L'esempio seguente mostra come copiare un foglio di lavoro da un libro di lavoro a un altro libro di lavoro.

{{< highlight csharp >}}

 //Create a new Workbook.

Workbook excelWorkbook0 = new Workbook();

//Get the first worksheet in the book.

Worksheet ws0 = excelWorkbook0.Worksheets[0];

//Put some data into header rows (A1:A4)

for (int i = 0; i < 5; i++)

{

	ws0.Cells[i, 0].PutValue(string.Format("Header Row {0}", i));

}

//Put some detail data (A5:A999)

for (int i = 5; i < 1000; i++)

{

	ws0.Cells[i, 0].PutValue(string.Format("Detail Row {0}", i));

}

//Define a pagesetup object based on the first worksheet.

PageSetup pagesetup = ws0.PageSetup;

//The first five rows are repeated in each page...

//It can be seen in print preview.

pagesetup.PrintTitleRows = "$1:$5";

//Create another Workbook.

Workbook excelWorkbook1 = new Workbook();

//Get the first worksheet in the book.

Worksheet ws1 = excelWorkbook1.Worksheets[0];

//Name the worksheet.

ws1.Name = "MySheet";

//Copy data from the first worksheet of the first workbook into the

//first worksheet of the second workbook.

ws1.Copy(ws0);

//Save the excel file.

excelWorkbook1.Save("copyworksheet.xls");


{{< /highlight >}}
## **Scarica il codice di esempio**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Copy%20Sheet%20between%20Workbook%20%28Aspose.Cells%29.zip)

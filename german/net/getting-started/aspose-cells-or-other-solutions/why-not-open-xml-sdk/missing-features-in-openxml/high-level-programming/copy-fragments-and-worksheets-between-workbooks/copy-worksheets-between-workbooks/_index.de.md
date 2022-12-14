---
title: Arbeitsblätter zwischen Arbeitsmappen kopieren
type: docs
weight: 10
url: /de/net/copy-worksheets-between-workbooks/
---
Aspose.Cells stellt eine Methode bereit, Aspose.Cells.Worksheet.Copy(), die verwendet wird, um Daten und Formatierungen von einem Quellarbeitsblatt in ein anderes Arbeitsblatt innerhalb oder zwischen Arbeitsmappen zu kopieren. Die Methode nimmt das Quellarbeitsblattobjekt als Parameter.

Das folgende Beispiel zeigt, wie Sie ein Arbeitsblatt von einer Arbeitsmappe in eine andere Arbeitsmappe kopieren.

{{< highlight "csharp" >}}

string FilePath = @"..\..\..\Beispieldateien\";

string FileName = FilePath + "Blatt zwischen Workbook.xlsx kopieren";

//Eine neue Arbeitsmappe erstellen.

Arbeitsmappe excelWorkbook0 = neue Arbeitsmappe();

//Erstes Arbeitsblatt im Buch holen.

Arbeitsblatt ws0 = excelWorkbook0.Worksheets[0];

//Einige Daten in Kopfzeilen einfügen (A1:A4)

 für (int i = 0; i< 5; i++)

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
## **Beispielcode herunterladen**
- [Bit Bucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Copy%20between%20Workbooks%20%28Aspose.Cells%29.zip)

Das folgende Beispiel zeigt, wie Sie ein Arbeitsblatt von einer Arbeitsmappe in eine andere Arbeitsmappe kopieren.

{{< highlight "csharp" >}}

 //Eine neue Arbeitsmappe erstellen.

Arbeitsmappe excelWorkbook0 = neue Arbeitsmappe();

//Erstes Arbeitsblatt im Buch holen.

Arbeitsblatt ws0 = excelWorkbook0.Worksheets[0];

//Einige Daten in Kopfzeilen einfügen (A1:A4)

 für (int i = 0; i< 5; i++)

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
## **Beispielcode herunterladen**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
- [Bit Bucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Copy%20Sheet%20between%20Workbook%20%28Aspose.Cells%29.zip)

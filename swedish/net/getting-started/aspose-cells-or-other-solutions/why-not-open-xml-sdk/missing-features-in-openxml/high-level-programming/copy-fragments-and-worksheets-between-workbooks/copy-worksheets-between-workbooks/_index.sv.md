---
title: Kopiera arbetsblad mellan arbetsböcker
type: docs
weight: 10
url: /sv/net/copy-worksheets-between-workbooks/
---
Aspose.Cells tillhandahåller en metod, Aspose.Cells.Worksheet.Copy() som används för att kopiera data och formatering från ett källkalkylblad till ett annat kalkylblad inom eller mellan arbetsböcker. Metoden tar källarksobjektet som en parameter.

Följande exempel visar hur man kopierar ett kalkylblad från en arbetsbok till en annan arbetsbok.

{{< highlight "csharp" >}}

string FilePath = @"..\..\..\Sample Files\";

string FileName = FilePath + "Kopiera ark mellan Workbook.xlsx";

//Skapa en ny arbetsbok.

Workbook excelWorkbook0 = new Workbook();

//Hämta det första kalkylbladet i boken.

Arbetsblad ws0 = excelWorkbook0.Worksheets[0];

//Sätt in lite data i rubrikrader (A1:A4)

 för (int i = 0; i< 5; i++)

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
## **Ladda ner provkod**
- [Bit hink](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Copy%20between%20Workbooks%20%28Aspose.Cells%29.zip)

Följande exempel visar hur man kopierar ett kalkylblad från en arbetsbok till en annan arbetsbok.

{{< highlight "csharp" >}}

 //Skapa en ny arbetsbok.

Workbook excelWorkbook0 = new Workbook();

//Hämta det första kalkylbladet i boken.

Arbetsblad ws0 = excelWorkbook0.Worksheets[0];

//Sätt in lite data i rubrikrader (A1:A4)

 för (int i = 0; i< 5; i++)

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
## **Ladda ner provkod**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
- [Bit hink](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Copy%20Sheet%20between%20Workbook%20%28Aspose.Cells%29.zip)

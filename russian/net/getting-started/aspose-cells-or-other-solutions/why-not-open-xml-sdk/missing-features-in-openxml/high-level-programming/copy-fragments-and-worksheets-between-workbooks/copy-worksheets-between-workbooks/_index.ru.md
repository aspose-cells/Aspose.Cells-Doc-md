---
title: Копировать рабочие листы между рабочими книгами
type: docs
weight: 10
url: /ru/net/copy-worksheets-between-workbooks/
---
Aspose.Cells предоставляет метод Aspose.Cells.Worksheet.Copy(), используемый для копирования данных и форматирования с исходного рабочего листа на другой рабочий лист внутри или между рабочими книгами. Метод принимает исходный объект рабочего листа в качестве параметра.

В следующем примере показано, как скопировать лист из одной книги в другую книгу.

{{< highlight "csharp" >}}

string FilePath = @"..\..\..\Sample Files\";

string FileName = FilePath + "Копировать лист между Workbook.xlsx";

//Создать новую книгу.

Рабочая книга excelWorkbook0 = новая рабочая книга();

//Получить первый рабочий лист в книге.

Рабочий лист ws0 = excelWorkbook0.Worksheets[0];

//Помещаем некоторые данные в строки заголовков (A1:A4)

 для (целое я = 0; я< 5; i++)

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
## **Скачать пример кода**
- [Битбакет](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Copy%20between%20Workbooks%20%28Aspose.Cells%29.zip)

В следующем примере показано, как скопировать лист из одной книги в другую книгу.

{{< highlight "csharp" >}}

 //Создать новую книгу.

Рабочая книга excelWorkbook0 = новая рабочая книга();

//Получить первый рабочий лист в книге.

Рабочий лист ws0 = excelWorkbook0.Worksheets[0];

//Помещаем некоторые данные в строки заголовков (A1:A4)

 для (целое я = 0; я< 5; i++)

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
## **Скачать пример кода**
- [Гитхаб](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
- [Битбакет](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Copy%20Sheet%20between%20Workbook%20%28Aspose.Cells%29.zip)

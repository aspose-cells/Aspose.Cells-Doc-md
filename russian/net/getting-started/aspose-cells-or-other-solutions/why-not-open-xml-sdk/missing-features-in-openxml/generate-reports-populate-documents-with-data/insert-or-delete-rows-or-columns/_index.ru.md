---
title: Вставка или удаление строк или столбцов
type: docs
weight: 20
url: /ru/net/insert-or-delete-rows-or-columns/
---
Независимо от того, создаем ли мы новый рабочий лист с нуля или работаем с существующим рабочим листом, нам может потребоваться добавить дополнительные строки или столбцы в рабочий лист, чтобы разместить больше данных или по какой-либо другой причине. И наоборот, также может потребоваться удалить строки или столбцы из указанных позиций рабочего листа.
## **Управление строками/столбцами**
**Aspose.Cells** предоставляет класс Workbook, представляющий файл Excel. Класс Workbook содержит коллекцию Worksheets, которая позволяет получить доступ к каждому рабочему листу в файле Excel. Рабочий лист представлен классом Worksheet. Класс Worksheet предоставляет коллекцию Cells, которая представляет все ячейки на листе.

**Cells**collection предоставляет несколько методов для управления строками или столбцами на листе, некоторые из них более подробно обсуждаются ниже.
## **Вставка строки**
 Разработчики могут вставить строку в лист в любом месте, вызвав метод InsertRow коллекции Cells.**Вставить строку** Метод принимает индекс строки, в которую будет вставлена новая строка.

{{< highlight "csharp" >}}

 //Creating a file stream containing the Excel file to be opened

FileStream fstream = new FileStream(MyDir + "Row and Column Operation.xls", FileMode.Open);

//Instantiating a Workbook object

//Opening the Excel file through the file stream

Workbook workbook = new Workbook(fstream);

//Accessing the first worksheet in the Excel file

Worksheet worksheet = workbook.Worksheets[0];

//Inserting a row into the worksheet at 3rd position

worksheet.Cells.InsertRow(2);

//Saving the modified Excel file

workbook.Save(MyDir + "Inserting Row.xls");

//Closing the file stream to free all resources

fstream.Close();

{{< /highlight >}}
## **Вставка нескольких строк**
Иногда разработчикам может потребоваться вставить в рабочий лист несколько строк. Это можно сделать, вызвав метод InsertRows коллекции Cells. Метод InsertRows принимает два параметра:

- **Индекс строки**, индекс строки, из которой будут вставлены новые строки
- **Количество рядов**, общее количество строк, которые необходимо вставить

{{< highlight "csharp" >}}

 //Creating a file stream containing the Excel file to be opened

FileStream fstream = new FileStream(MyDir + "Row and Column Operation.xls", FileMode.Open);

//Instantiating a Workbook object

//Opening the Excel file through the file stream

Workbook workbook = new Workbook(fstream);

//Accessing the first worksheet in the Excel file

Worksheet worksheet = workbook.Worksheets[0];

//Inserting 10 rows into the worksheet starting from 3rd row

worksheet.Cells.InsertRows(2, 10);

//Saving the modified Excel file

workbook.Save(MyDir + "Inserting Mutiple Rows.xls");

//Closing the file stream to free all resources

fstream.Close();

{{< /highlight >}}
## **Удаление строки**
 Разработчики могут удалить строку из рабочего листа в любом месте, вызвав метод**УдалитьРов** метод коллекции Cells.**УдалитьРов** Метод принимает индекс строки, которую нужно удалить.

{{< highlight "csharp" >}}

 //Creating a file stream containing the Excel file to be opened

FileStream fstream = new FileStream(MyDir + "Row and Column Operation.xls", FileMode.Open);

//Instantiating a Workbook object

//Opening the Excel file through the file stream

Workbook workbook = new Workbook(fstream);

//Accessing the first worksheet in the Excel file

Worksheet worksheet = workbook.Worksheets[0];

//Deleting 3rd row from the worksheet

worksheet.Cells.DeleteRow(2);

//Saving the modified Excel file

workbook.Save(MyDir + "Deleting Rows.xls");

//Closing the file stream to free all resources

fstream.Close();

{{< /highlight >}}
## **Удаление нескольких строк**
Если разработчикам необходимо удалить несколько строк из листа, это также можно сделать, вызвав метод DeleteRows коллекции Cells. Метод DeleteRows принимает два параметра:

- **Индекс строки**, индекс строки, из которой строки будут удалены.
- **Количество рядов**, общее количество строк, которые необходимо удалить.

{{< highlight "csharp" >}}

 //Creating a file stream containing the Excel file to be opened

FileStream fstream = new FileStream(MyDir + "Row and Column Operation.xls", FileMode.Open);

//Instantiating a Workbook object

//Opening the Excel file through the file stream

Workbook workbook = new Workbook(fstream);

//Accessing the first worksheet in the Excel file

Worksheet worksheet = workbook.Worksheets[0];

//Deleting 10 rows from the worksheet starting from 3rd row

worksheet.Cells.DeleteRows(2, 10);

//Saving the modified Excel file

workbook.Save(MyDir + "Deleting Mutiple Rows.xls");

//Closing the file stream to free all resources

fstream.Close();

{{< /highlight >}}
## **Вставка столбца**
Разработчики также могут вставить столбец на лист в любом месте, вызвав метод InsertColumn коллекции Cells. Метод InsertColumn принимает индекс столбца, в который будет вставлен новый столбец.

{{< highlight "csharp" >}}

 //Creating a file stream containing the Excel file to be opened

FileStream fstream = new FileStream(MyDir + "Row and Column Operation.xls", FileMode.Open);

//Instantiating a Workbook object

//Opening the Excel file through the file stream

Workbook workbook = new Workbook(fstream);

//Accessing the first worksheet in the Excel file

Worksheet worksheet = workbook.Worksheets[0];

//Inserting a column into the worksheet at 2nd position

worksheet.Cells.InsertColumn(1);

//Saving the modified Excel file

workbook.Save(MyDir + "Inserting Column.xls");

//Closing the file stream to free all resources

fstream.Close();

{{< /highlight >}}
## **Удаление столбца**
Чтобы удалить столбец с листа в любом месте, разработчики могут вызвать метод DeleteColumn коллекции Cells. Метод DeleteColumn принимает индекс удаляемого столбца.

{{< highlight "csharp" >}}

 //Creating a file stream containing the Excel file to be opened

FileStream fstream = new FileStream(MyDir + "Row and Column Operation.xls", FileMode.Open);

//Instantiating a Workbook object

//Opening the Excel file through the file stream

Workbook workbook = new Workbook(fstream);

//Accessing the first worksheet in the Excel file

Worksheet worksheet = workbook.Worksheets[0];

//Deleting a column from the worksheet at 2nd position

worksheet.Cells.DeleteColumn(1);

//Saving the modified Excel file

workbook.Save(MyDir + "Deleting Column.xls");

//Closing the file stream to free all resources

fstream.Close();

{{< /highlight >}}
## **Скачать пример кода**
- [Гитхаб](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
- [Битбакет](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Work%20with%20Rows%20n%20Columns%20%28Aspose.Cells%29.zip)

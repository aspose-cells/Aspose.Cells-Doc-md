---
title: Вставить или удалить строки или столбцы
type: docs
weight: 20
url: /ru/net/insert-or-delete-rows-or-columns/
---

Независимо от того, создаём ли мы новый рабочий лист с нуля или работаем с существующим листом, может потребоваться добавить дополнительные строки или столбцы в лист, чтобы вместить больше данных или по какой-то другой причине. Наоборот, также может потребоваться удалить строки или столбцы из указанных позиций листа.
## **Управление строками/столбцами**
**Aspose.Cells** предоставляет класс Workbook, который представляет собой файл Excel. Класс Workbook содержит коллекцию Worksheets, которая позволяет получить доступ к каждому рабочему листу в файле Excel. Рабочий лист представлен классом Worksheet. Класс Worksheet предоставляет коллекцию Cells, которая представляет все ячейки в рабочем листе.

Коллекция **Cells** предоставляет несколько методов для управления строками или столбцами в рабочем листе, некоторые из которых обсуждаются ниже более подробно.
## **Вставка строки**
Разработчики могут вставить строку в рабочий лист в любом месте, вызвав метод InsertRow коллекции Cells. Метод **InsertRow** принимает индекс строки, куда будет вставлена новая строка.

{{< highlight csharp >}}

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
Иногда разработчикам может понадобиться вставить несколько строк в рабочий лист. Это можно сделать, вызвав метод InsertRows коллекции Cells. Метод **InsertRows** принимает два параметра:

- **Индекс строки**, индекс строки, откуда будут вставлены новые строки
- **Количество строк**, общее количество строк, которые нужно вставить

{{< highlight csharp >}}

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
Разработчики могут удалить строку из рабочего листа на любом месте, вызвав метод **DeleteRow** коллекции Cells. Метод **DeleteRow** принимает индекс строки, которая должна быть удалена.

{{< highlight csharp >}}

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
Если разработчикам нужно удалить несколько строк из рабочего листа, это также можно сделать, вызвав метод DeleteRows коллекции Cells. Метод DeleteRows принимает два параметра:

- **Индекс строки**, индекс строки, откуда будут удаляться строки.
- **Количество строк**, общее количество строк, которые нужно удалить.

{{< highlight csharp >}}

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
Разработчики также могут вставлять столбец в листе, вызывая метод InsertColumn коллекции Cells. Метод InsertColumn принимает индекс столбца, куда будет вставлен новый столбец.

{{< highlight csharp >}}

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
Для удаления столбца из листа в любом месте разработчики могут вызывать метод DeleteColumn коллекции Cells. Метод DeleteColumn принимает индекс столбца для удаления.

{{< highlight csharp >}}

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
## **Загрузить образец кода**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Work%20with%20Rows%20n%20Columns%20%28Aspose.Cells%29.zip)

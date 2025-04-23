---
title: 行または列の挿入または削除
type: docs
weight: 20
url: /ja/net/insert-or-delete-rows-or-columns/
---

新しいワークシートをゼロから作成している場合、または既存のワークシートで作業している場合、追加の行や列をワークシートに追加してデータを追加したり、他の理由でワークシートから行や列を削除する必要が生じることがあります。逆に、指定された位置から行または列を削除する必要があることもあります。
## **行/列の管理**
**Aspose.Cells**は、Excelファイルを表すWorkbookクラスを提供します。Workbookクラスには、Excelファイル内の各ワークシートにアクセスできるWorksheetsコレクションが含まれています。ワークシートはWorksheetクラスで表されます。Worksheetクラスは、ワークシート内のすべてのセルを表すCellsコレクションを提供します。

**Cells**コレクションには、ワークシート内の行や列を管理するためのいくつかのメソッドが用意されており、そのうちいくつかについて以下で詳しく説明します。
## **行の挿入**
開発者は、CellsコレクションのInsertRowメソッドを呼び出すことで、ワークシートに行を任意の場所に挿入することができます。**InsertRow**メソッドは、新しい行が挿入される行のインデックスを取ります。

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
## **複数の行の挿入**
時には、開発者はワークシートに複数の行を挿入する必要があります。これは、CellsコレクションのInsertRowsメソッドを呼び出すことで行うことができます。InsertRowsメソッドは、2つのパラメータを取ります：

- **行のインデックス**、新しい行が挿入される行のインデックス
- **行数**、挿入する必要がある行の総数

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
## **行の削除**
開発者は、Cellsコレクションの**DeleteRow**メソッドを呼び出すことで、ワークシートから任意の位置の行を削除することができます。**DeleteRow**メソッドは、削除する行のインデックスを取ります。

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
## **複数の行の削除**
開発者がワークシートから複数の行を削除する必要がある場合、CellsコレクションのDeleteRowsメソッドを呼び出すことでも行うことができます。DeleteRowsメソッドは、2つのパラメータを取ります：

- **行のインデックス**、削除する行のインデックス
- **行数**、削除する必要がある行の総数

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
## **列の挿入**
開発者は、CellsコレクションのInsertColumnメソッドを呼び出すことで、ワークシートに列を任意の場所に挿入することができます。**InsertColumn**メソッドは、新しい列が挿入される列のインデックスを取ります。

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
## **列の削除**
開発者は、CellsコレクションのDeleteColumnメソッドを呼び出すことで、ワークシートから任意の位置の列を削除することができます。**DeleteColumn**メソッドは、削除する列のインデックスを取ります。

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
## **サンプルコードをダウンロード**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Work%20with%20Rows%20n%20Columns%20%28Aspose.Cells%29.zip)
{{< app/cells/assistant language="csharp" >}}

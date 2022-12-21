---
title: 行または列の挿入または削除
type: docs
weight: 20
url: /ja/net/insert-or-delete-rows-or-columns/
---
新しいワークシートをゼロから作成する場合でも、既存のワークシートで作業する場合でも、より多くのデータを収容するため、またはその他の理由で、ワークシートに余分な行または列を追加する必要がある場合があります。逆に、ワークシートの指定された位置から行または列を削除する必要がある場合もあります。
## **行/列の管理**
**Aspose.Cells** Excel ファイルを表すクラス Workbook を提供します。 Workbook クラスには、Excel ファイル内の各ワークシートにアクセスできる Worksheets コレクションが含まれています。ワークシートは Worksheet クラスによって表されます。 Worksheet クラスは、ワークシート内のすべてのセルを表す Cells コレクションを提供します。

**Cells**collection は、ワークシートの行または列を管理するためのいくつかの方法を提供します。これらのいくつかについては、以下で詳しく説明します。
## **行の挿入**
開発者は、Cells コレクションの InsertRow メソッドを呼び出して、ワークシートの任意の場所に行を挿入できます。**行の挿入**メソッドは、新しい行が挿入される行のインデックスを取ります。

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
## **複数行の挿入**
開発者は、ワークシートに複数の行を挿入する必要がある場合があります。これは、Cells コレクションの InsertRows メソッドを呼び出すことで実行できます。 InsertRows メソッドは、次の 2 つのパラメーターを取ります。

- **行インデックス**、新しい行が挿入される行のインデックス
- **行の数**、挿入する必要がある行の総数

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
## **行の削除**
開発者は、を呼び出して、ワークシートの任意の場所から行を削除できます。**行の削除** Cells コレクションのメソッド。**行の削除**メソッドは、削除する必要がある行のインデックスを取得します。

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
## **複数行の削除**
開発者がワークシートから複数の行を削除する必要がある場合は、Cells コレクションの DeleteRows メソッドを呼び出して行うこともできます。 DeleteRows メソッドは、次の 2 つのパラメーターを取ります。

- **行インデックス**、行が削除される行のインデックス。
- **行の数**、削除する必要がある行の総数。

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
## **列の挿入**
開発者は、Cells コレクションの InsertColumn メソッドを呼び出して、ワークシートの任意の場所に列を挿入することもできます。 InsertColumn メソッドは、新しい列が挿入される列のインデックスを取得します。

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
## **列の削除**
ワークシートの任意の場所から列を削除するには、開発者は Cells コレクションの DeleteColumn メソッドを呼び出すことができます。 DeleteColumn メソッドは、削除する列のインデックスを受け取ります。

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
## **サンプルコードをダウンロード**
- [ギットハブ](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
- [ビットバケット](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Work%20with%20Rows%20n%20Columns%20%28Aspose.Cells%29.zip)

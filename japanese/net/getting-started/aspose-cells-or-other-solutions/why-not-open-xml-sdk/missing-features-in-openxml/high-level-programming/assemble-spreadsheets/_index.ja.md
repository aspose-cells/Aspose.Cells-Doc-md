---
title: スプレッドシートの組み立て
type: docs
weight: 10
url: /ja/net/assemble-spreadsheets/
---

このセクションでは、次の方法について説明します：

新しいExcelファイルを作成し、それにワークシートを追加します。

- デザイナースプレッドシートにワークシートを追加します。
- シート名を使用してワークシートにアクセスします。
- シート名を使用してExcelファイルからワークシートを削除します。
- シートインデックスを使用してExcelファイルからワークシートを削除します。
- Aspose.Cellsには、Excelファイルを表すWorkbookクラスを提供します。Workbookクラスには、Excelファイル内の各ワークシートにアクセスできるWorksheetsコレクションが含まれています。

ワークシートはWorksheetクラスで表されます。Worksheetクラスは、ワークシートを管理するための幅広いプロパティとメソッドを提供します。
## **新しいExcelファイルにワークシートを追加する**
プログラムで新しいExcelファイルを作成するには：

- Workbookクラスのオブジェクトを作成します。
- WorksheetsコレクションのAddメソッドを呼び出します。空のワークシートがExcelファイルに自動的に追加されます。新しいワークシートのシートインデックスをWorksheetsコレクションに渡すことで、参照できます。
- ワークシートの参照を取得します。
- ワークシートで作業を実行します。
- WorkbookクラスのSaveメソッドを呼び出して、新しいワークシートが追加されたExcelファイルを保存します。

{{< highlight csharp >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook();

//Adding a new worksheet to the Workbook object

int i = workbook.Worksheets.Add();

//Obtaining the reference of the newly added worksheet by passing its sheet index

Worksheet worksheet = workbook.Worksheets[i];

//Setting the name of the newly added worksheet

worksheet.Name = "My Worksheet";

//Saving the Excel file

workbook.Save("Adding Worksheet.xls");

{{< /highlight >}}
## **デザイナースプレッドシートにワークシートを追加する**
デザイナースプレッドシートにワークシートを追加するプロセスは、新しいワークシートを追加するのと同じですが、既存のExcelファイルが既に存在するため、ワークシートを追加する前に開いておく必要があります。Workbookクラスによってデザイナースプレッドシートを開くことができます。

{{< highlight csharp >}}

 //Creating a file stream containing the Excel file to be opened

FileStream fstream = new FileStream("book1.xls", FileMode.Open);

//Instantiating a Workbook object

//Opening the Excel file through the file stream

Workbook workbook = new Workbook(fstream);

//Adding a new worksheet to the Workbook object

int i = workbook.Worksheets.Add();

//Obtaining the reference of the newly added worksheet by passing its sheet index

Worksheet worksheet = workbook.Worksheets[i];

//Setting the name of the newly added worksheet

worksheet.Name = "My Worksheet";

//Saving the Excel file

workbook.Save("Designer Spreadsheet.xls");

//Closing the file stream to free all resources

fstream.Close();

{{< /highlight >}}
## **シート名を使用してワークシートにアクセスする**
名前またはインデックスを指定して任意のワークシートにアクセスまたは取得します。

{{< highlight csharp >}}

 //Creating a file stream containing the Excel file to be opened

FileStream fstream = new FileStream("WorksHeet Operations.xls", FileMode.Open);

//Instantiating a Workbook object

//Opening the Excel file through the file stream

Workbook workbook = new Workbook(fstream);

//Accessing a worksheet using its sheet name

Worksheet worksheet = workbook.Worksheets["Sheet1"];

{{< /highlight >}}
## **シート名を使用してワークシートを削除する**
ファイルからワークシートを削除するには、WorksheetsコレクションのRemoveAtメソッドを呼び出します。特定のワークシートを削除するには、そのワークシートのシート名をRemoveAtメソッドに渡します。

{{< highlight csharp >}}

 //Creating a file stream containing the Excel file to be opened

FileStream fstream = new FileStream("WorksHeet Operations.xls", FileMode.Open);

//Instantiating a Workbook object

//Opening the Excel file through the file stream

Workbook workbook = new Workbook(fstream);

//Removing a worksheet using its sheet name

workbook.Worksheets.RemoveAt("Sheet3");

workbook.Save("WorksHeet Operations.xls");

{{< /highlight >}}
## **Sheet Indexを使用してワークシートを削除する**
ワークシートの名前を知っている場合は、ワークシートを削除することもできます。ワークシートの名前がわからない場合は、削除するワークシートのシートインデックスを渡す、RemoveAtメソッドのオーバーロードバージョンを使用します。

{{< highlight csharp >}}

 //creating a file stream containing the Excel file to be opened

FileStream fstream = new FileStream("WorksHeet Operations.xls", FileMode.Open);

//Instantiating a Workbook object

//Opening the Excel file through the file stream

Workbook workbook = new Workbook(fstream);

//Removing a worksheet using its sheet index

workbook.Worksheets.RemoveAt(1);

workbook.Save("WorksHeet Operations.xls");

{{< /highlight >}}
## **サンプルコードをダウンロード**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Assemble%20Worksheet%20%28Aspose.Cells%29.zip)
{{< app/cells/assistant language="csharp" >}}

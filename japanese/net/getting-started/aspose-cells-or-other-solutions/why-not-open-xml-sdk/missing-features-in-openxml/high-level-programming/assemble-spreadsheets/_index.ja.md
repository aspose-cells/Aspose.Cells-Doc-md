---
title: スプレッドシートを組み立てる
type: docs
weight: 10
url: /ja/net/assemble-spreadsheets/
---
このセクションでは、次の方法について説明します。

新しい Excel ファイルを最初から作成し、それにワークシートを追加します。

- ワークシートをデザイナー スプレッドシートに追加します。
- シート名を使用してワークシートにアクセスします。
- シート名を使用して Excel ファイルからワークシートを削除します。
- シート インデックスを使用して Excel ファイルからワークシートを削除します。
- Aspose.Cells は、Excel ファイルを表すクラス Workbook を提供します。 Workbook クラスには、Excel ファイル内の各ワークシートにアクセスできる Worksheets コレクションが含まれています。

ワークシートは Worksheet クラスによって表されます。 Worksheet クラスは、ワークシートを管理するための幅広いプロパティとメソッドを提供します。
## **新しい Excel ファイルへのワークシートの追加**
プログラムで新しい Excel ファイルを作成するには:

- Workbook クラスのオブジェクトを作成します。
- Worksheets コレクションの Add メソッドを呼び出します。空のワークシートが Excel ファイルに * 自動的に追加されます。新しいワークシートのシート インデックスを Worksheets コレクションに渡すことで参照できます。
- ワークシート参照を取得します。
- ワークシートで作業を行います。
- Workbook クラスの Save メソッドを呼び出して、新しいワークシートを含む新しい Excel ファイルを保存します。

{{< highlight "csharp" >}}

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
## **Designer スプレッドシートへのワークシートの追加**
ワークシートをデザイナー スプレッドシートに追加するプロセスは、新しいワークシートを追加するプロセスと同じですが、Excel ファイルが既に存在するため、ワークシートを追加する前に開く必要があります。デザイナー スプレッドシートは Workbook クラスで開くことができます。

{{< highlight "csharp" >}}

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
名前またはインデックスを指定して、任意のワークシートにアクセスまたは取得します。

{{< highlight "csharp" >}}

 //Creating a file stream containing the Excel file to be opened

FileStream fstream = new FileStream("WorksHeet Operations.xls", FileMode.Open);

//Instantiating a Workbook object

//Opening the Excel file through the file stream

Workbook workbook = new Workbook(fstream);

//Accessing a worksheet using its sheet name

Worksheet worksheet = workbook.Worksheets["Sheet1"];

{{< /highlight >}}
## **シート名を使用してワークシートを削除する**
ファイルからワークシートを削除するには、Worksheets コレクションの RemoveAt メソッドを呼び出します。特定のワークシートを削除するには、シート名を RemoveAt メソッドに渡します。

{{< highlight "csharp" >}}

 //Creating a file stream containing the Excel file to be opened

FileStream fstream = new FileStream("WorksHeet Operations.xls", FileMode.Open);

//Instantiating a Workbook object

//Opening the Excel file through the file stream

Workbook workbook = new Workbook(fstream);

//Removing a worksheet using its sheet name

workbook.Worksheets.RemoveAt("Sheet3");

workbook.Save("WorksHeet Operations.xls");

{{< /highlight >}}
## **シート インデックスを使用してワークシートを削除する**
名前によるワークシートの削除は、ワークシートの名前がわかっている場合にうまく機能します。ワークシートの名前がわからない場合は、シート名の代わりにワークシートのシート インデックスを取得するオーバーロードされたバージョンの RemoveAt メソッドを使用します。

{{< highlight "csharp" >}}

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
- [ギットハブ](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
- [ビットバケット](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Assemble%20Worksheet%20%28Aspose.Cells%29.zip)

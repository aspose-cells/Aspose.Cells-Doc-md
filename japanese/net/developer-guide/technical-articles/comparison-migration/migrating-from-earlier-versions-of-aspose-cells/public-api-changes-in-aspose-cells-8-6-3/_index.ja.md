---
title: パブリック API Aspose.Cells の変更点 8.6.3
type: docs
weight: 220
url: /ja/net/public-api-changes-in-aspose-cells-8-6-3/
---
{{% alert color="primary" %}} 

このドキュメントでは、モジュール/アプリケーション開発者にとって興味深い、バージョン 8.6.2 から 8.6.3 への Aspose.Cells API への変更について説明します。新規および更新されたパブリック メソッド、追加されたクラスだけでなく、Aspose.Cells の舞台裏での動作の変更の説明も含まれています。

{{% /alert %}} 
## **追加された API**
### **データのインポート中の HTML 解析のサポート**
Aspose.Cells for .NET API のこのリリースでは、ImportTableOptions.IsHtmlString プロパティが公開されています。このプロパティは、API がワークシートにデータをインポートする際に HTML タグを解析し、解析結果をセル値として設定するように指示します。 Aspose.Cells API は、単一セルに対してこのタスクを実行するために Cell.HtmlString を既に提供していますが、DataTable などからデータを一括でインポートしている間、ImportTableOptions.IsHtmlString プロパティ (true に設定されている場合) は、サポートされているすべてのHTML タグを付けて、解析結果を対応するセルに設定します。

これが最も単純な使用シナリオです。

**C#**

{{< highlight "csharp" >}}

 //create an instance of ImportTableOptions

var importOptions = new ImportTableOptions();

//Set IsHtmlString to true so that the API can parse the HTML

importOptions.IsHtmlString = true;

//Import data from DataTable while passing instance of ImportTableOptions

cells.ImportData(table, 0, 0, importOptions);

{{< /highlight >}}


### **メソッド Workbook.CreateBuiltinStyle が追加されました**
Aspose.Cells for .NET 8.6.3 は Workbook.CreateBuiltinStyle メソッドを公開しました。このメソッドを使用して、次のいずれかに対応する Style クラスのオブジェクトを作成できます。[Excel アプリケーションによって提供される組み込みスタイル](/cells/ja/net/using-built-in-styles/)Workbook.CreateBuiltinStyle メソッドは、列挙型 BuiltinStyleType から定数を受け取ります。 Aspose.Cells API の以前のリリースでは、StyleCollection.CreateBuiltinStyle メソッドを介して同じタスクを実行できましたが、Aspose.Cells API の最近のリリースでは StyleCollection クラスが削除されたため、新しく公開された Workbook.CreateBuiltinStyle メソッドを別の方法と見なすことができます。同じことを達成します。

以下は、簡単な使用シナリオです。

**C#**

{{< highlight "csharp" >}}

 //Create an instance of Workbook

//Optionally load a spreadsheet

var book = new Workbook();

//Create a built-in style of type Title

var style = book.CreateBuiltinStyle(BuiltinStyleType.Title);

{{< /highlight >}}


### **メソッド Cells.ImportGridView が追加されました**
Aspose.Cells for .NET 8.6.3 は Cells.ImportGridView のオーバーロードされたバージョンを公開し、ImportTableOptions のインスタンスを受け入れて、インポート プロセスをより詳細に制御できるようになりました。

以下は、簡単な使用シナリオです。

**C#**

{{< highlight "csharp" >}}

 //Create an instance of Workbook

//Optionally load a spreadsheet

var book = new Workbook();

//Retrieve the Cells collection of first Worksheet in Workbook

var cells = book.Worksheets[0].Cells;

//create an instance of ImportTableOptions & set its various properties

var importOptions = new ImportTableOptions();

importOptions.IsHtmlString = true;

importOptions.IsFieldNameShown = true;

//Import data from GridView while passing instance of ImportTableOptions

cells.ImportGridView(gridView, 0, 0, importOptions);

{{< /highlight >}}


### **プロパティ ImportTableOptions.ConvertGridStyle が追加されました**
上記の機能強化を参照して、Aspose.Cells for .NET API の最新バージョンでは、ImportTableOptions.ConvertGridStyle プロパティも公開されています。このブール型のプロパティにより、開発者はインポートされたデータの外観を制御できます。ImportTableOptions.ConvertGridStyle プロパティを true に設定すると、データがインポートされたセルに API が GridView のスタイルを適用することを示します。

以下は、簡単な使用シナリオです。

**C#**

{{< highlight "csharp" >}}

 //Create an instance of Workbook

//Optionally load a spreadsheet

var book = new Workbook();

//Retrieve the Cells collection of first Worksheet in Workbook

var cells = book.Worksheets[0].Cells;

//create an instance of ImportTableOptions

var importOptions = new ImportTableOptions();

//Set ConvertGridStyle property to true

importOptions.ConvertGridStyle = true;



//Import data from GridView while passing instance of ImportTableOptions

cells.ImportGridView(gridView, 0, 0, importOptions);

{{< /highlight >}}


### **プロパティ LoadDataOption.OnlyVisibleWorksheet が追加されました**
 Aspose.Cells for .NET 8.6.3 は LoadDataOption.OnlyVisibleWorksheet プロパティを公開しました。このプロパティを true に設定すると、Aspose.Cells for .NET API の読み込みメカニズムに影響を与えます。その結果、特定のスプレッドシートから表示されているワークシートのみが読み込まれます。を確認してください[詳細記事](/cells/ja/net/different-ways-to-open-files/)この教科では。

以下は、簡単な使用シナリオです。

**C#**

{{< highlight "csharp" >}}

 //Create an instance of LoadDataOption

var loadDataOptions = new LoadDataOption();

//Set OnlyVisibleWorksheet property to true

loadDataOptions.OnlyVisibleWorksheet = true;

//Create an instance of LoadOptions

var loadOptions = new LoadOptions();

//Set LoadDataOptions property to the instance of LoadDataOption created earlier

loadOptions.LoadDataOptions = loadDataOptions;



//Create an instance of Workbook & load an existing spreadsheet

//while passing the instance of LoadOptions created earlier

var book = new Workbook(inputFilePath, loadOptions);

{{< /highlight >}}
## **廃止された API**
### **メソッド Worksheet.CopyConditionalFormatting 廃止されました**
Worksheet.CopyConditionalFormatting メソッドの代わりに、Cells.CopyRows または Range.Copy メソッドのいずれかを使用することをお勧めします。
### **プロパティ Cells.End 廃止**
Cells.End プロパティの代わりに Cells.LastCell プロパティを使用してください。

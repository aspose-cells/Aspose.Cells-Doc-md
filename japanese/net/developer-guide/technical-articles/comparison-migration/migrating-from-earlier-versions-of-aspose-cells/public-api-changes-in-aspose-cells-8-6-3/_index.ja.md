---
title: Aspose.Cells 8.6.3の公開API変更
type: docs
weight: 220
url: /ja/net/public-api-changes-in-aspose-cells-8-6-3/
---

{{% alert color="primary" %}} 

このドキュメントは、Aspose.Cells APIの8.6.2から8.6.3への変更について記載しており、モジュール／アプリケーション開発者に関心がある可能性のある変更を説明しています。新しいおよび更新された公開メソッド、追加されたクラスだけでなく、Aspose.Cellsの裏側の挙動に変更がある場合も含まれています。

{{% /alert %}} 
## **APIの追加**
### **データをインポートする際のHTMLパースのサポート**
このバージョンのAspose.Cells for .NET APIでは、ImportTableOptions.IsHtmlStringプロパティが公開され、APIをワークシートにデータをインポートする際にHTMLタグを解析し、解析結果をセルの値として設定するように指示します。Aspose.Cells APIはすでにCell.HtmlStringを提供しており、単一のセルでこのタスクを実行できますが、DataTableなどからデータを大量にインポートする場合、ImportTableOptions.IsHtmlStringプロパティ（trueに設定されている場合）はサポートされているすべてのHTMLタグを解析し、解析結果を対応するセルに設定しようとします。

以下は最もシンプルな使用シナリオです。

**C#**

{{< highlight csharp >}}

 //create an instance of ImportTableOptions

var importOptions = new ImportTableOptions();

//Set IsHtmlString to true so that the API can parse the HTML

importOptions.IsHtmlString = true;

//Import data from DataTable while passing instance of ImportTableOptions

cells.ImportData(table, 0, 0, importOptions);

{{< /highlight >}}


### **Workbook.CreateBuiltinStyleメソッドを追加**
Aspose.Cells for .NET 8.6.3では、Workbook.CreateBuiltinStyleメソッドが公開されました。このメソッドを使用して、Excelアプリケーションが提供する[組み込みスタイル](/cells/ja/net/using-built-in-styles/)に対応するStyleクラスのオブジェクトを作成できます。Workbook.CreateBuiltinStyleメソッドは、列挙型BuiltinStyleTypeからの定数を受け入れます。以前のバージョンのAspose.Cells APIでは、同じタスクはStyleCollection.CreateBuiltinStyleメソッドを使用して実行できましたが、最近のAspose.Cells APIのリリースでは、StyleCollectionクラスが削除されたため、新しく公開されたWorkbook.CreateBuiltinStyleメソッドは同じことを達成するための代替手段として考えられます。

以下はシンプルな使用シナリオです。

**C#**

{{< highlight csharp >}}

 //Create an instance of Workbook

//Optionally load a spreadsheet

var book = new Workbook();

//Create a built-in style of type Title

var style = book.CreateBuiltinStyle(BuiltinStyleType.Title);

{{< /highlight >}}


### **Cells.ImportGridViewメソッドを追加**
Aspose.Cells for .NET 8.6.3では、Cells.ImportGridViewのオーバーロードバージョンが公開され、ImportTableOptionsのインスタンスを受け入れるようになり、インポートプロセスをさらに制御できるようになりました。

以下はシンプルな使用シナリオです。

**C#**

{{< highlight csharp >}}

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


### **ImportTableOptions.ConvertGridStyleプロパティを追加**
上記の拡張機能に関連して、最新バージョンのAspose.Cells for .NET APIでは、ImportTableOptions.ConvertGridStyleプロパティも公開されています。このブーリアン型のプロパティを設定すると、インポートされたデータの外観を制御でき、ImportTableOptions.ConvertGridStyleプロパティをtrueに設定すると、APIはGridViewのスタイルをインポートされたデータがあるセルに適用します。

以下はシンプルな使用シナリオです。

**C#**

{{< highlight csharp >}}

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


### **LoadDataOption.OnlyVisibleWorksheetプロパティを追加**
Aspose.Cells for .NET 8.6.3では、LoadDataOption.OnlyVisibleWorksheetプロパティが公開され、これをtrueに設定すると、Aspose.Cells for .NET APIのロードメカニズムに影響を与え、結果として与えられたスプレッドシートからの可視のワークシートのみがロードされます。この件については、[詳細な記事](/cells/ja/net/different-ways-to-open-files/)をご確認ください。

以下はシンプルな使用シナリオです。

**C#**

{{< highlight csharp >}}

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
## **非推奨API**
### **Worksheet.CopyConditionalFormattingメソッドが非推奨になりました**
Worksheet.CopyConditionalFormattingメソッドの代わりとして、Cells.CopyRowsまたはRange.Copyメソッドのいずれかを使用することをお勧めします。
### **Cells.Endプロパティの廃止**
Cells.Endプロパティの代わりにCells.LastCellプロパティを使用してください。
{{< app/cells/assistant language="csharp" >}}

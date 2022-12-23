---
title: パブリック API Aspose.Cells の変更点 8.6.3
type: docs
weight: 230
url: /ja/java/public-api-changes-in-aspose-cells-8-6-3/
---
{{% alert color="primary" %}} 

このドキュメントでは、モジュール/アプリケーション開発者にとって興味深い、バージョン 8.6.2 から 8.6.3 への Aspose.Cells API への変更について説明します。新規および更新されたパブリック メソッド、追加されたクラスだけでなく、Aspose.Cells の舞台裏での動作の変更の説明も含まれています。

{{% /alert %}} 
## **追加された API**
### **データのインポート中の HTML 解析のサポート**
Aspose.Cells for Java API のこのリリースでは、ImportTableOptions.setHtmlString 属性が公開されています。この属性は、API がワークシートにデータをインポートする際に HTML タグを解析し、解析結果をセル値として設定するように指示します。 Aspose.Cells API は、単一のセルに対してこのタスクを実行するために、Cell.setHtmlString 属性を既に提供していますが、データを一括でインポートしている間、ImportTableOptions.setHtmlString 属性 (true に設定されている場合) は、サポートされているすべての HTML タグとセットを解析しようとします。解析された結果を対応するセルに。

これが最も単純な使用シナリオです。

**Java**

{{< highlight "csharp" >}}

 //create an instance of ImportTableOptions

ImportTableOptions importOptions = new ImportTableOptions();

//Set IsHtmlString to true so that the API can parse the HTML

importOptions.setHtmlString(true);

//Import data from DataTable while passing instance of ImportTableOptions

cells.importData(iTable, 0, 0, importOptions);

{{< /highlight >}}
### **メソッド Workbook.createBuiltinStyle が追加されました**
Aspose.Cells for Java 8.6.3 は Workbook.createBuiltinStyle メソッドを公開しました。このメソッドを使用して、Style クラスのオブジェクトを作成できます。[Excel アプリケーションによって提供される組み込みスタイル](/cells/ja/java/using-built-in-styles/)Workbook.createBuiltinStyle メソッドは、列挙型 BuiltinStyleType から定数を受け取ります。 Aspose.Cells API の以前のリリースでは、StyleCollection.createBuiltinStyle メソッドを使用して同じタスクを実行できましたが、Aspose.Cells API の最近のリリースでは StyleCollection クラスが削除されたため、新しく公開された Workbook.createBuiltinStyle メソッドを別の方法と見なすことができます。同じことを達成します。

以下は、簡単な使用シナリオです。

**Java**

{{< highlight "csharp" >}}

 //Create an instance of Workbook

//Optionally load a spreadsheet

Workbook book = new Workbook();

//Create a built-in style of type Title

Style style = book.createBuiltinStyle(BuiltinStyleType.TITLE);

{{< /highlight >}}
### **プロパティ LoadDataOption.OnlyVisibleWorksheet が追加されました**
Aspose.Cells for Java 8.6.3 は LoadDataOption.OnlyVisibleWorksheet プロパティを公開しました。このプロパティを true に設定すると、Aspose.Cells for Java API の読み込みメカニズムに影響を与えます。その結果、特定のスプレッドシートから表示されているワークシートのみが読み込まれます。

以下は、簡単な使用シナリオです。

**Java**

{{< highlight "csharp" >}}

 //Create an instance of LoadDataOption

LoadDataOption loadDataOptions = new LoadDataOption();

//Set OnlyVisibleWorksheet property to true

loadDataOptions.setOnlyVisibleWorksheet(true);

//Create an instance of LoadOptions

LoadOptions loadOptions = new LoadOptions();

//Set LoadDataOptions property to the instance of LoadDataOption created earlier

loadOptions.setLoadDataOptions(loadDataOptions);

//Create an instance of Workbook & load an existing spreadsheet

//while passing the instance of LoadOptions created earlier

Workbook book = new Workbook(inputFilePath, loadOptions);

{{< /highlight >}}
## **廃止された API**
### **メソッド Worksheet.copyConditionalFormatting 廃止されました**
Worksheet.copyConditionalFormatting メソッドの代わりに、Cells.copyRows または Range.copy メソッドのいずれかを使用することをお勧めします。
### **プロパティ Cells.End 廃止**
Cells.End プロパティの代わりに Cells.LastCell プロパティを使用してください。

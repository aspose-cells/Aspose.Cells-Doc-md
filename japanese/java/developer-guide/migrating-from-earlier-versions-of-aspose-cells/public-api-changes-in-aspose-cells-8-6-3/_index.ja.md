---
title: Aspose.Cells 8.6.3の公開API変更
type: docs
weight: 230
url: /ja/java/public-api-changes-in-aspose-cells-8-6-3/
---

{{% alert color="primary" %}} 

このドキュメントは、Aspose.Cells APIの8.6.2から8.6.3への変更について記載しており、モジュール／アプリケーション開発者に関心がある可能性のある変更を説明しています。新しいおよび更新された公開メソッド、追加されたクラスだけでなく、Aspose.Cellsの裏側の挙動に変更がある場合も含まれています。

{{% /alert %}} 
## **APIの追加**
### **データをインポートする際のHTMLパースのサポート**
Aspose.Cells for Java APIのこのリリースでは、ImportTableOptions.setHtmlString属性が公開され、この属性をtrueに設定するとAPIはワークシートにデータをインポートする際にHTMLタグを解析し、解析結果をセルの値として設定します。Aspose.Cells APIは既にCell.setHtmlString属性を提供しており、単一のセルでこのタスクを実行できますが、大量のデータをインポートする際には、ImportTableOptions.setHtmlString属性を使用することで（trueに設定した場合）、サポートされているすべてのHTMLタグを解析し、解析結果を対応するセルに設定しようとします。

以下は最もシンプルな使用シナリオです。

**Java**

{{< highlight csharp >}}

 //create an instance of ImportTableOptions

ImportTableOptions importOptions = new ImportTableOptions();

//Set IsHtmlString to true so that the API can parse the HTML

importOptions.setHtmlString(true);

//Import data from DataTable while passing instance of ImportTableOptions

cells.importData(iTable, 0, 0, importOptions);

{{< /highlight >}}
### **Workbook.createBuiltinStyleメソッドの追加**
Aspose.Cells for Java 8.6.3では、Workbook.createBuiltinStyleメソッドが公開されました。このメソッドは、Excelアプリケーションによって提供される[組み込みスタイル](/cells/ja/java/using-built-in-styles/)の一つに対応するStyleクラスのオブジェクトを作成するために使用できます。Workbook.createBuiltinStyleメソッドは、列挙型BuiltinStyleTypeの定数を受け入れます。以前のAspose.Cells APIのリリースでは、同じタスクはStyleCollection.createBuiltinStyleメソッドを使用して実行できましたが、最近のAspose.Cells APIのリリースではStyleCollectionクラスが削除されたため、新しく公開されたWorkbook.createBuiltinStyleメソッドは同じ目的を達成するための代替アプローチとして考えられます。

以下はシンプルな使用シナリオです。

**Java**

{{< highlight csharp >}}

 //Create an instance of Workbook

//Optionally load a spreadsheet

Workbook book = new Workbook();

//Create a built-in style of type Title

Style style = book.createBuiltinStyle(BuiltinStyleType.TITLE);

{{< /highlight >}}
### **LoadDataOption.OnlyVisibleWorksheetプロパティの追加**
Aspose.Cells for Java 8.6.3では、LoadDataOption.OnlyVisibleWorksheetプロパティが公開されました。これをtrueに設定すると、指定されたスプレッドシートからのみ表示されるワークシートがロードされます。

以下はシンプルな使用シナリオです。

**Java**

{{< highlight csharp >}}

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
## **非推奨API**
### **Worksheet.copyConditionalFormattingメソッドの廃止**
Worksheet.copyConditionalFormattingメソッドの代替として、Cells.copyRowsまたはRange.copyのいずれかを使用することが推奨されています。
### **Cells.Endプロパティの廃止**
Cells.Endプロパティの代わりにCells.LastCellプロパティを使用してください。

---
title: Aspose.Cells 8.1.0 におけるパブリックAPIの変更
type: docs
weight: 40
url: /ja/net/public-api-changes-in-aspose-cells-8-1-0/
---

{{% alert color="primary" %}} 

このドキュメントでは、Aspose.Cellsのバージョン8.0.2から8.1.0へのAPIの変更について、モジュール/アプリケーション開発者に関心がある可能性のあるものを説明しています。新しいおよび更新されたパブリックメソッドだけでなく、Aspose.Cellsの裏側の挙動の変更の説明も含まれています。

{{% /alert %}} 
## **HtmlSaveOptions.ExportHiddenWorksheetプロパティの追加**
HtmlSaveOptionsクラスにはExportHiddenWorksheetプロパティが公開されており、非表示のワークシートがHTML形式にエクスポートされるかどうかを指定するために使用できます。デフォルト値はtrueです。falseに設定すると、Aspose.Cellsは非表示のワークシートの内容をエクスポートしません。

{{% alert color="primary" %}} 

[非表示ワークシートのエクスポートを防止する](/cells/ja/net/prevent-exporting-hidden-worksheet-contents-on-saving-to/)の詳細な記事をご確認ください

{{% /alert %}}
## **Cell.StringValueWithoutFormatプロパティの追加**
CellValueWithoutFormatプロパティがCellクラスに追加され、開発者が書式を適用せずにセルの値を取得することを容易にするために追加されました。

以下に示すコードスニペットでは、スプレッドシートをゼロから作成し、1つのセルに数値形式を適用することで、Cell.StringValueWithoutFormat プロパティの使用方法を示しています。

**C#**

{{< highlight csharp >}}

 //Create an instance of Workbook

Workbook book = new Workbook();

//Access first worksheet

Worksheet sheet = book.Worksheets[0];

//Access A1 cell

Cell cell = sheet.Cells["A1"];

//Put a value cell and convert it to number

cell.PutValue("123456", true);

//Create a new Style object and add it to Workbook's Style Collection

Style style = book.Styles[book.Styles.Add()];

//Set Number format for Style object

style.Number = 3;

//Set the style of A1 cell

cell.SetStyle(style, new StyleFlag() { NumberFormat = true });

//Get formatted string value 

string formatted = cell.DisplayStringValue;

Console.WriteLine(formatted);

//Get un-formatted string value

string unformatted = cell.StringValueWithoutFormat;

Console.WriteLine(unformatted);

{{< /highlight >}}

{{% alert color="primary" %}} 

上記のコードの出力は以下の通りです

123,456

123456

{{% /alert %}}
## **廃止されたBytes、Characters、CharactersWithSpaces、Lines、Paragraphsプロパティ**
BuiltInDocumentPropertyCollectionクラスの多くのプロパティがバージョン Aspose.Cells for .NET 8.1.0 から非推奨となりました。これらのプロパティにはBytes、Characters、CharactersWithSpaces、Lines、Paragraphsが含まれています。これらのプロパティはExcelスプレッドシートの保存において利用されないためです。元々これらのプロパティはWord文書やPowerPointプレゼンテーション向けに記述されていました。

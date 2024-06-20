---
title: Aspose.Cells 8.1.0 におけるパブリックAPIの変更
type: docs
weight: 50
url: /ja/java/public-api-changes-in-aspose-cells-8-1-0/
---

{{% alert color="primary" %}} 

このドキュメントでは、Aspose.Cellsのバージョン8.0.2から8.1.0へのAPIの変更について、モジュール/アプリケーション開発者に関心がある可能性のあるものを説明しています。新しいおよび更新されたパブリックメソッドだけでなく、Aspose.Cellsの裏側の挙動の変更の説明も含まれています。

{{% /alert %}} 
## **HtmlSaveOptions.ExportHiddenWorksheetプロパティの追加**
HtmlSaveOptionsクラスにはExportHiddenWorksheetプロパティが公開されており、非表示のワークシートがHTML形式にエクスポートされるかどうかを指定するために使用できます。デフォルト値はtrueです。falseに設定すると、Aspose.Cellsは非表示のワークシートの内容をエクスポートしません。

{{% alert color="primary" %}} 

[非表示のワークシートのエクスポートを防止](/cells/ja/java/prevent-exporting-hidden-worksheet-contents-on-saving-to/)の詳細記事をご覧ください

{{% /alert %}}
## **Cell.StringValueWithoutFormatプロパティの追加**
CellValueWithoutFormatプロパティがCellクラスに追加され、開発者が書式を適用せずにセルの値を取得することを容易にするために追加されました。 

以下に提供されるコードスニペットは、スプレッドシートを作成し、セルの値のフォーマットを適用せずにセル.getStringValueWithoutFormatメソッドをCell.getDisplayStringValueと比較する方法を示しています。 

**Java**

{{< highlight csharp >}}

 //Create an instance of Workbook

Workbook book = new Workbook();

//Access first worksheet

Worksheet sheet = book.getWorksheets().get(0);

//Access A1 cell

Cell cell = sheet.getCells().get("A1");

//Put a value cell and convert it to number

cell.putValue("123456", true);

//Create a new Style object and add it to Workbook's Style Collection

int index = book.getStyles().add();

Style style = book.getStyles().get(index);

//Set Number format for Style object

style.setNumber(3);

//Create an instance of StyleFlag class

//and set NumberFormat to true

StyleFlag flag = new StyleFlag();

flag.setNumberFormat(true);

//Set the style of A1 cell

cell.setStyle(style, flag);

//Get formatted string value 

String formatted = cell.getDisplayStringValue();

System.out.println("Formatted String Value: " +formatted);

//Get un-formatted string value

String unformatted = cell.getStringValueWithoutFormat();

System.out.println("Un-formatted String Value: " + unformatted);

{{< /highlight >}}

{{% alert color="primary" %}} 

上記のコードの出力は以下の通りです

フォーマットされた文字列の値: 123,456
フォーマットされていない文字列の値: 123456

{{% /alert %}}
## **廃止されたBytes、Characters、CharactersWithSpaces、Lines、Paragraphsプロパティ**
BuiltInDocumentPropertyCollectionクラスの多くのプロパティがバージョン Aspose.Cells for .NET 8.1.0 から非推奨となりました。これらのプロパティにはBytes、Characters、CharactersWithSpaces、Lines、Paragraphsが含まれています。これらのプロパティはExcelスプレッドシートの保存において利用されないためです。元々これらのプロパティはWord文書やPowerPointプレゼンテーション向けに記述されていました。 

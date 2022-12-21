---
title: パブリック API Aspose.Cells 8.1.0 の変更点
type: docs
weight: 50
url: /ja/java/public-api-changes-in-aspose-cells-8-1-0/
---
{{% alert color="primary" %}} 

このドキュメントでは、バージョン 8.0.2 から 8.1.0 への Aspose.Cells API の変更について説明します。これは、モジュール/アプリケーション開発者にとって興味深いものです。これには、新規および更新されたパブリック メソッドだけでなく、Aspose.Cells の舞台裏での動作の変更の説明も含まれています。

{{% /alert %}} 
## **HtmlSaveOptions.ExportHiddenWorksheet プロパティを追加**
HtmlSaveOptions クラスには、非表示のワークシートを HTML 形式でエクスポートするかどうかを指定するために使用できる ExportHiddenWorksheet プロパティが公開されています。デフォルト値は true です。一方、false に設定すると、Aspose.Cells は非表示のワークシート コンテンツをエクスポートしません。

{{% alert color="primary" %}} 

の詳細記事をご確認ください[非表示のワークシートのエクスポートを防止](/cells/ja/java/prevent-exporting-hidden-worksheet-contents-on-saving-to/)

{{% /alert %}}
## **Cell.StringValueWithoutFormat プロパティを追加**
StringValueWithoutFormat プロパティが Cell クラスに追加され、開発者がフォーマットを適用せずにセル値を簡単に取得できるようになりました。

以下のコード スニペットは、ゼロからスプレッドシートを作成し、セルの 1 つに数値形式を適用することにより、cell.getDisplayStringValue と比較して Cell.getStringValueWithoutFormat メソッドの使用法を示しています。

**Java**

{{< highlight "csharp" >}}

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

上記のコードの出力は次のとおりです

フォーマットされた文字列値: 123,456
フォーマットされていない文字列値: 123456

{{% /alert %}}
## **廃止された Bytes、Characters、CharactersWithSpaces、Lines、Paragraphs のプロパティ**
BuiltInDocumentPropertyCollection クラスの多くのプロパティは、Aspose.Cells for .NET 8.1.0 から廃止されました。これらのプロパティには、Bytes、Characters、CharactersWithSpaces、Lines & Paragraphs が含まれます。理由は、前述のプロパティは、Excel がそれらを省略しているため、Excel スプレッドシートの防腐剤としては役に立たないからです。これらのプロパティは、もともと Word ドキュメントと PowerPoint プレゼンテーション用に作成されたものです。

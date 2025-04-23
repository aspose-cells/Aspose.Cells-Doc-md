---
title: Aspose.Cells 8.0.2での公開API変更
type: docs
weight: 40
url: /ja/java/public-api-changes-in-aspose-cells-8-0-2/
---

{{% alert color="primary" %}} 

このドキュメントは、Aspose.Cellsのバージョン8.0.1から8.0.2への変更点を記載しており、モジュール/アプリケーション開発者に興味を持たれる可能性があるものです。新しいまたは更新された公開メソッドだけでなく、Aspose.Cellsの背後にある動作に変更がある場合についても説明しています。

{{% /alert %}} 
## **ShapeクラスにTextDirectionプロパティを追加しました**
Shapeクラスには、テキスト流の方向を取得または設定するために使用できるTextDirectionプロパティが公開されています。TextDirectionプロパティは、スプレッドシート内のコメントの望ましいテキスト方向を設定するためにも使用できます。

**Java**

{{< highlight csharp >}}

 //Instantiate a new Workbook

Workbook book = new Workbook();

//Get the first worksheet

Worksheet sheet = book.getWorksheets().get(0);

//Adding a comment to "F5" cell

int commentIndex = sheet.getComments().add("F5");

Comment comment = sheet.getComments().get(commentIndex);

//Set its vertical alignment setting            

comment.getCommentShape().setTextVerticalAlignment(TextAlignmentType.CENTER);

//Set its horizontal alignment setting

comment.getCommentShape().setTextHorizontalAlignment(TextAlignmentType.RIGHT);

//Set the Text Direction - Right-to-Left

comment.getCommentShape().setTextDirection(TextDirectionType.RIGHT_TO_LEFT);

//Set the Comment note

comment.setNote("This is my Comment Text. This is test");

//Save the Excel file

book.save(myDir + "output.xlsx");

{{< /highlight >}}
## **HTMLLoadOptionsクラスにConvertFormulasDataプロパティを追加しました**
ConvertFormulasDataプロパティがHTMLLoadOptionsクラスに追加され、開発者がHTMLファイルからExcelの数式を読み込むために利用できるようになりました。boolean型のConvertFormulasDataプロパティは、文字列の値が'='で始まる場合に式に変換するかどうかを示します。

**Java**

{{< highlight csharp >}}

 //Create an instance of HTMLLoadOptions

HTMLLoadOptions loadOptions = new HTMLLoadOptions();

//Set ConvertFormulasData to true

loadOptions.setConvertFormulasData(true);

//Create an instance of Workbook and load an HTML based spreadsheet 

//while passing the instance of HTMLLoadOptions

Workbook workbook = new Workbook(myDir + "spreadsheet.html", loadOptions);

{{< /highlight >}}

{{% alert color="primary" %}} 

ConvertFormulasDataプロパティのデフォルト値はfalseです。

{{% /alert %}}
## **HtmlSaveOptionsクラスにImageOptionsプロパティを追加しました**
ImageOptionsプロパティがHtmlSaveOptionsクラスに追加されました。ImageOptionsプロパティを公開することで、スプレッドシートをエクスポートする際にHTMLに埋め込まれる画像の設定を行うことができるようになりました。 
## **HtmlSaveOptions.ExportChartImageFormatプロパティの廃止**
HtmlSaveOptions.ExportChartImageFormat はバージョン Aspose.Cells for .NET 8.0.2 から非推奨となりました。スプレッドシートをHTML形式にエクスポートする際に画像の形式設定はHtmlSaveOptions.ImageOptionsを使用することが推奨されています。
{{< app/cells/assistant language="java" >}}

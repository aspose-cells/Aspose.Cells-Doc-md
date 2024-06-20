---
title: Aspose.Cells 8.0.2での公開API変更
type: docs
weight: 30
url: /ja/net/public-api-changes-in-aspose-cells-8-0-2/
---

{{% alert color="primary" %}} 

このドキュメントは、Aspose.Cellsのバージョン8.0.1から8.0.2への変更点を記載しており、モジュール/アプリケーション開発者に興味を持たれる可能性があるものです。新しいまたは更新された公開メソッドだけでなく、Aspose.Cellsの背後にある動作に変更がある場合についても説明しています。

{{% /alert %}} 
## **ShapeクラスにTextDirectionプロパティを追加しました**
Shapeクラスには、テキスト流の方向を取得または設定するために使用できるTextDirectionプロパティが公開されています。TextDirectionプロパティは、スプレッドシート内のコメントの望ましいテキスト方向を設定するためにも使用できます。

**C#**

{{< highlight csharp >}}

 //Instantiate a new Workbook

var book = new Workbook();

//Get the first worksheet

var sheet = book.Worksheets[0];

//Add a comment to A1 cell

var comment = sheet.Comments[sheet.Comments.Add("A1")];

//Set its vertical alignment setting            

comment.CommentShape.TextVerticalAlignment  = TextAlignmentType.Center;

//Set its horizontal alignment setting

comment.CommentShape.TextHorizontalAlignment = TextAlignmentType.Right;

//Set the Text Direction - Right-to-Left

comment.CommentShape.TextDirection = TextDirectionType.RightToLeft;

//Set the Comment note

comment.Note = "This is my Comment Text. This is test";

//Save the Excel file

book.Save(myDir + "output.xlsx");

{{< /highlight >}}

{{% alert color="primary" %}} 

[コメントの文字方向を変更する](/cells/ja/net/change-text-direction-of-the-comment/)詳細な記事をご覧ください。

{{% /alert %}}
## **HTMLLoadOptionsクラスにConvertFormulasDataプロパティを追加しました**
ConvertFormulasDataプロパティがHTMLLoadOptionsクラスに追加され、開発者がHTMLファイルからExcelの数式を読み込むために利用できるようになりました。boolean型のConvertFormulasDataプロパティは、文字列の値が'='で始まる場合に式に変換するかどうかを示します。

**C#**

{{< highlight csharp >}}

 //Create an instance of HTMLLoadOptions

HTMLLoadOptions loadOptions = new HTMLLoadOptions();

//Set ConvertFormulasData to true

loadOptions.ConvertFormulasData = true;

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

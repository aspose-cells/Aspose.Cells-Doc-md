---
title: パブリック API Aspose.Cells 8.0.2 の変更点
type: docs
weight: 30
url: /ja/net/public-api-changes-in-aspose-cells-8-0-2/
---
{{% alert color="primary" %}} 

このドキュメントでは、バージョン 8.0.1 から 8.0.2 への Aspose.Cells API の変更点について説明します。これは、モジュール/アプリケーション開発者にとって興味深いものです。これには、新規および更新されたパブリック メソッドだけでなく、Aspose.Cells の舞台裏での動作の変更の説明も含まれています。

{{% /alert %}} 
## **Shape クラスに TextDirection プロパティを追加**
Shape クラスには、Shape オブジェクトのテキスト フローの方向を取得または設定するために使用できる TextDirection プロパティが公開されています。以下に示すように、TextDirection プロパティを使用して、スプレッドシート内のコメントの目的のテキスト方向を設定することもできます。

**C#**

{{< highlight "csharp" >}}

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

の詳細記事をご確認ください[コメントの文字方向の変更](/cells/ja/net/change-text-direction-of-the-comment/)

{{% /alert %}}
## **ConvertFormulasData プロパティを HTMLLoadOptions クラスに追加**
ConvertFormulasData プロパティが HTMLLoadOptions クラスに追加され、開発者が HTML ファイルから Excel 式を簡単にロードできるようになりました。ブール値の ConvertFormulasData プロパティは、文字列値が文字 '=' で始まる場合に、文字列を数式に変換するかどうかを示します。

**C#**

{{< highlight "csharp" >}}

 //Create an instance of HTMLLoadOptions

HTMLLoadOptions loadOptions = new HTMLLoadOptions();

//Set ConvertFormulasData to true

loadOptions.ConvertFormulasData = true;

//Create an instance of Workbook and load an HTML based spreadsheet 

//while passing the instance of HTMLLoadOptions

Workbook workbook = new Workbook(myDir + "spreadsheet.html", loadOptions);

{{< /highlight >}}

{{% alert color="primary" %}} 

ConvertFormulasData プロパティのデフォルト値は false です。

{{% /alert %}}
## **ImageOptions プロパティを HtmlSaveOptions クラスに追加**
ImageOptions プロパティが HtmlSaveOptions クラスに追加されました。 ImageOptions プロパティを公開することで、開発者はスプレッドシートのエクスポート中に HTML に埋め込まれた画像の設定を行うことができます。
## **廃止された HtmlSaveOptions.ExportChartImageFormat プロパティ**
HtmlSaveOptions.ExportChartImageFormat は、Aspose.Cells for .NET 8.0.2 から廃止されました。スプレッドシートを HTML 形式にエクスポートする際は、代わりに HtmlSaveOptions.ImageOptions を画像形式の設定に使用することをお勧めします。

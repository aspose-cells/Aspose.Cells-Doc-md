---
title: パブリック API Aspose.Cells 8.0.2 の変更点
type: docs
weight: 40
url: /ja/java/public-api-changes-in-aspose-cells-8-0-2/
---
{{% alert color="primary" %}} 

このドキュメントでは、バージョン 8.0.1 から 8.0.2 への Aspose.Cells API の変更点について説明します。これは、モジュール/アプリケーション開発者にとって興味深いものです。これには、新規および更新されたパブリック メソッドだけでなく、Aspose.Cells の舞台裏での動作の変更の説明も含まれています。

{{% /alert %}} 
## **Shape クラスに TextDirection プロパティを追加**
Shape クラスには、Shape オブジェクトのテキスト フローの方向を取得または設定するために使用できる TextDirection プロパティが公開されています。以下に示すように、TextDirection プロパティを使用して、スプレッドシート内のコメントの目的のテキスト方向を設定することもできます。

**Java**

{{< highlight "csharp" >}}

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
## **ConvertFormulasData プロパティを HTMLLoadOptions クラスに追加**
ConvertFormulasData プロパティが HTMLLoadOptions クラスに追加され、開発者が HTML ファイルから Excel 式を簡単にロードできるようになりました。ブール値の ConvertFormulasData プロパティは、文字列値が文字 '=' で始まる場合に、文字列を数式に変換するかどうかを示します。

**Java**

{{< highlight "csharp" >}}

 //Create an instance of HTMLLoadOptions

HTMLLoadOptions loadOptions = new HTMLLoadOptions();

//Set ConvertFormulasData to true

loadOptions.setConvertFormulasData(true);

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

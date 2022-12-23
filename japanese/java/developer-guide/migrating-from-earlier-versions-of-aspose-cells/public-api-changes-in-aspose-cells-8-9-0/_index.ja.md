---
title: パブリック API Aspose.Cells 8.9.0 の変更点
type: docs
weight: 310
url: /ja/java/public-api-changes-in-aspose-cells-8-9-0/
---
{{% alert color="primary" %}} 

このドキュメントでは、モジュール/アプリケーション開発者にとって興味深い、バージョン 8.8.3 から 8.9.0 への Aspose.Cells API への変更について説明します。新規および更新されたパブリック メソッド、追加および削除されたクラスなどだけでなく、Aspose.Cells の舞台裏での動作の変更の説明も含まれています。

{{% /alert %}} 
## **追加された API**
### **HtmlSaveOptions.DefaultFontName プロパティを追加**
Aspose.Cells for Java 8.9.0 では、HtmlSaveOptions クラスの DefaultFontName プロパティが公開され、スプレッドシートを HTML 形式でレンダリングする際にデフォルトのフォント名を指定できるようになりました。デフォルトのフォントは、スタイルのフォントが存在しない場合にのみ使用されます。 HtmlSaveOptions.DefaultFontName プロパティのデフォルト値は null です。つまり、Aspose.Cells for Java API は、元のフォントと同じファミリを持つユニバーサル フォントを使用します。

{{% alert color="primary" %}} 

この機能の詳細については、次の記事を参照してください。[スプレッドシートをレンダリングするためのデフォルト フォントを HTML 形式に設定する](/cells/ja/java/set-default-font-while-rendering-spreadsheet-to/).

{{% /alert %}} 

以下は、簡単な使用シナリオです。

**Java**

{{< highlight "csharp" >}}

 //Create an instance of HtmlSaveOptions

HtmlSaveOptions options = new HtmlSaveOptions();

//Set default font name for Html rendering

options.setDefaultFontName("Arial");

//Load a spreadsheet in an instance of Workbook

Workbook book = new Workbook(dir + "sample.xlsx");

//Save the spreadsheet in Html format while passing instance of HtmlSaveOptions

book.save(dir + "output.html", options);

{{< /highlight >}}
### **ImageOrPrintOptions.DefaultFont プロパティを追加**
Aspose.Cells for Java 8.9.0 では、DefaultFont プロパティを公開することにより、ImageOrPrintOptions クラスのデフォルトのフォント名を設定できます。上記のプロパティは、スプレッドシート内の Unicode 文字がセル スタイルの正しいフォントで設定されていない場合に使用できます。そのため、そのような文字は、結果の画像でブロックとして表示される場合があります。

{{% alert color="primary" %}} 

 Unicode 文字を表示するには、DefaultFont プロパティを MingLiu または MS Gothic に設定します。上記のプロパティが設定されていない場合、Aspose.Cells はシステムのデフォルト フォントを使用して Unicode 文字を表示します。

{{% /alert %}} {{% alert color="primary" %}} 

この機能の詳細については、次の記事を参照してください。[画像形式でスプレッドシートをレンダリングするためのデフォルト フォントの設定](/cells/ja/java/set-default-font-while-rendering-spreadsheet-to-images/).

{{% /alert %}} 

以下は、簡単な使用シナリオです。

**Java**

{{< highlight "csharp" >}}

 //Create an instance of ImageOrPrintOptions

ImageOrPrintOptions options = new ImageOrPrintOptions();

//Set default font name for image rendering

options.setDefaultFont("Arial");

//Load a spreadsheet in an instance of Workbook

Workbook book = new Workbook(dir + "sample.xlsx");

//Access the worksheet to be rendered

Worksheet sheet = book.getWorksheets().get(0);

//Create an instance of SheetRender

SheetRender render = new SheetRender(sheet, options);

//Save spreadsheet to image

render.toImage(0, dir + "output.png");

{{< /highlight >}}
### **PivotTable.Excel2003Compatible プロパティを追加**
Aspose.Cells for Java API は、PivotTable クラスのブール型 Excel2003Compatible プロパティを公開しました。これにより、ピボットテーブルが更新目的で Excel 2003 と互換性があるかどうかを指定できます。 Excel2003Compatible プロパティのデフォルト値は true です。これは、文字列が 255 文字以下でなければならないことを意味します。文字列が 255 文字を超える場合、切り捨てられます。 false の場合、前述の制限は適用されません。

{{% alert color="primary" %}} 

この機能の詳細については、次の記事を参照してください。[ピボット テーブルを更新するための Excel 2003 の互換性](/cells/ja/java/specify-whether-the-pivottable-is-compatible-for-excel2003-while-refreshing-pivottable/).

{{% /alert %}} 

以下は、簡単な使用シナリオです。

**Java**

{{< highlight "csharp" >}}

 //Load a spreadsheet in an instance of Workbook

Workbook book = new Workbook(dir + "sample.xlsx");

//Access the desired Pivot Table from the spreadsheet

PivotTable pivot = book.getWorksheets().get(0).getPivotTables().get(0);

//Set Excel 2003 compatibility to false

pivot.setExcel2003Compatible(false);

//Refresh & recalculate Pivot Table

pivot.refreshData();

pivot.calculateData();

{{< /highlight >}}

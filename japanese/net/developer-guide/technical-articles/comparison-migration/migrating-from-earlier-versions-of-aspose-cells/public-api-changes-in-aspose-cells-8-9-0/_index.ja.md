---
title: Aspose.Cells 8.9.0 での公開 API 変更
type: docs
weight: 300
url: /ja/net/public-api-changes-in-aspose-cells-8-9-0/
---

{{% alert color="primary" %}} 

このドキュメントは、Aspose.Cells API の変更点を説明し、モジュール/アプリケーション開発者の関心を引く可能性がある、バージョン 8.8.3 から 8.9.0 への変更点を含んでいます。新しいおよび更新された公開メソッド、追加および削除されたクラスなどだけでなく、Aspose.Cells の内部の挙動の変更についても説明しています。

{{% /alert %}} 
## **APIの追加**
### **HtmlSaveOptions.DefaultFontName プロパティが追加されました**
Aspose.Cells for .NET 8.9.0 では、HtmlSaveOptions クラスの DefaultFontName プロパティを公開し、スプレッドシートを HTML 形式にレンダリングする際にデフォルトのフォント名を指定できるようになりました。デフォルトのフォントは、スタイルのフォントが存在しない場合のみ使用されます。HtmlSaveOptions.DefaultFontName プロパティのデフォルト値は null で、元のフォントと同じファミリーを持つユニバーサルフォントが使用されます。

{{% alert color="primary" %}} 

この機能の詳細については、[Setting Default Font for Rendering Spreadsheets to HTML Format](/cells/ja/net/set-default-font-while-rendering-spreadsheet-to/)の記事を参照してください。

{{% /alert %}} 

以下はシンプルな使用シナリオです。

**C#**

{{< highlight csharp >}}

 // Create an instance of HtmlSaveOptions

var options = new HtmlSaveOptions();

// Set default font name for Html rendering

options.DefaultFontName = "Arial";

// Load a spreadsheet in an instance of Workbook

var book = new Workbook(dir + "sample.xlsx");

// Save the spreadsheet in Html format while passing instance of HtmlSaveOptions

book.Save(dir + "output.html", options);

{{< /highlight >}}


### **ImageOrPrintOptions.DefaultFont プロパティが追加されました**
Aspose.Cells for .NET 8.9.0 では、ImageOrPrintOptions クラスの DefaultFont プロパティを公開し、スプレッドシートで Unicode 文字がセルスタイルで正しく設定されていない場合に使用されるデフォルトのフォント名を設定できるようになりました。

{{% alert color="primary" %}} 

Unicode 文字を正しくフォントで設定されていない場合、MingLiu または MS Gothic に DefaultFont プロパティを設定してください。前述のプロパティが設定されていない場合、Aspose.Cells はUnicode 文字を表示するためにシステムのデフォルトフォントを使用します。

{{% /alert %}} {{% alert color="primary" %}} 

この機能の詳細については、[Setting Default Font for Rendering Spreadsheets in Image Formats](/cells/ja/net/set-default-font-while-rendering-spreadsheet-to-images/)の記事を参照してください。

{{% /alert %}} 

以下はシンプルな使用シナリオです。

**C#**

{{< highlight csharp >}}

 // Create an instance of ImageOrPrintOptions

var options = new ImageOrPrintOptions();

// Set default font name for image rendering

options.DefaultFont = "Arial";

// Load a spreadsheet in an instance of Workbook

var book = new Workbook(dir + "sample.xlsx");

// Access the worksheet to be rendered

var sheet = book.Worksheets[0];

// Create an instance of SheetRender

var render = new SheetRender(sheet, options);

// Save spreadsheet to image

render.ToImage(0, dir + "output.png");

{{< /highlight >}}


### **PivotTable.IsExcel2003Compatible プロパティが追加されました**
Aspose.Cells for .NET API は PivotTable クラスのために Excel 2003 互換のリフレッシュを指定する IsExcel2003Compatible プロパティを公開しました。IsExcel2003Compatible プロパティのデフォルト値は true であり、文字列は 255 文字以下である必要があります。文字列が 255 文字を超える場合、切り捨てられます。false の場合、前述の制限は課されません。

{{% alert color="primary" %}} 

この機能の詳細については、[Compatibility for Excel 2003 for Refreshing Pivot Tables](https://docs.aspose.com/cells/net/specify-whether-the-pivottable-is-compatible-for-excel2003-while-refreshing-pivottable/)の記事を参照してください。

{{% /alert %}} 

以下はシンプルな使用シナリオです。

**C#**

{{< highlight csharp >}}

 // Load a spreadsheet in an instance of Workbook

var book = new Workbook(dir + "sample.xlsx");

// Access the desired Pivot Table from the spreadsheet

var pivot = book.Worksheets[0].PivotTables[0];

// Set Excel 2003 compatibility to false

pivot.IsExcel2003Compatible = false;

// Refresh & recalculate Pivot Table

pivot.RefreshData();

pivot.CalculateData();

{{< /highlight >}}


### **GridWeb.GetVersion メソッドが追加されました**
Aspose.Cells.GridWeb for .NET 8.9.0 で、GridWeb コンポーネントのリリース版を返す {GetVersion}} ファクトリメソッドを公開しました。
{{< app/cells/assistant language="csharp" >}}

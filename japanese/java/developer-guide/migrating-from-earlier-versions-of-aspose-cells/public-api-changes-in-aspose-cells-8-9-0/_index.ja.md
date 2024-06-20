---
title: Aspose.Cells 8.9.0 での公開 API 変更
type: docs
weight: 310
url: /ja/java/public-api-changes-in-aspose-cells-8-9-0/
---

{{% alert color="primary" %}} 

このドキュメントは、Aspose.Cells API の変更点を説明し、モジュール/アプリケーション開発者の関心を引く可能性がある、バージョン 8.8.3 から 8.9.0 への変更点を含んでいます。新しいおよび更新された公開メソッド、追加および削除されたクラスなどだけでなく、Aspose.Cells の内部の挙動の変更についても説明しています。

{{% /alert %}} 
## **APIの追加**
### **HtmlSaveOptions.DefaultFontName プロパティが追加されました**
Aspose.Cells for Java 8.9.0 では、HtmlSaveOptions クラスの DefaultFontName プロパティが公開され、スプレッドシートを HTML 形式にレンダリングする際にデフォルトのフォント名を指定することが可能となりました。デフォルトのフォントは、スタイルのフォントが存在しない場合にのみ使用されます。HtmlSaveOptions.DefaultFontName プロパティのデフォルト値は null です。つまり、Aspose.Cells for Java API は元のフォントと同じファミリーを持つユニバーサルフォントを使用します。

{{% alert color="primary" %}} 

この機能の詳細については、[Setting Default Font for Rendering Spreadsheets to HTML Format](/cells/ja/java/set-default-font-while-rendering-spreadsheet-to/) の詳細な記事を参照してください。

{{% /alert %}} 

以下はシンプルな使用シナリオです。

**Java**

{{< highlight csharp >}}

 //Create an instance of HtmlSaveOptions

HtmlSaveOptions options = new HtmlSaveOptions();

//Set default font name for Html rendering

options.setDefaultFontName("Arial");

//Load a spreadsheet in an instance of Workbook

Workbook book = new Workbook(dir + "sample.xlsx");

//Save the spreadsheet in Html format while passing instance of HtmlSaveOptions

book.save(dir + "output.html", options);

{{< /highlight >}}
### **ImageOrPrintOptions.DefaultFont プロパティが追加されました**
Aspose.Cells for Java 8.9.0 では、ImageOrPrintOptions クラスの DefaultFont プロパティを公開し、スプレッドシートのセルスタイルで適切なフォントが設定されていない場合に、デフォルトのフォント名を設定することが可能となりました。このような文字は、結果の画像でブロックとして表示される可能性があります。 

{{% alert color="primary" %}} 

Unicode 文字を正しくフォントで設定されていない場合、MingLiu または MS Gothic に DefaultFont プロパティを設定してください。前述のプロパティが設定されていない場合、Aspose.Cells はUnicode 文字を表示するためにシステムのデフォルトフォントを使用します。 

{{% /alert %}} {{% alert color="primary" %}} 

この機能の詳細については、[Setting Default Font for Rendering Spreadsheets in Image Formats](/cells/ja/java/set-default-font-while-rendering-spreadsheet-to-images/) の詳細な記事を参照してください。

{{% /alert %}} 

以下はシンプルな使用シナリオです。

**Java**

{{< highlight csharp >}}

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
### **PivotTable.Excel2003Compatible プロパティが追加されました**
Aspose.Cells for Java APIは、PivotTableクラスのExcel2003CompatibleプロパティのBoolean型を公開し、PivotTableの更新目的でPivotTableがExcel 2003互換であるかどうかを指定することができます。Excel2003Compatibleプロパティのデフォルト値はtrueで、これは文字列が255文字以下である必要があることを意味します。文字列が255文字を超える場合、切り捨てられます。falseの場合、前述の制限は課されません。

{{% alert color="primary" %}} 

この機能の詳細については、[Excel 2003のPivotテーブルの更新のための互換性](/cells/ja/java/specify-whether-the-pivottable-is-compatible-for-excel2003-while-refreshing-pivottable/)の記事をご覧ください。

{{% /alert %}} 

以下はシンプルな使用シナリオです。

**Java**

{{< highlight csharp >}}

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

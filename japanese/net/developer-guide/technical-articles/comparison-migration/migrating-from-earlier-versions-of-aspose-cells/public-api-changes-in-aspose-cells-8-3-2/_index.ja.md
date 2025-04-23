---
title: Aspose.Cells 8.3.2でのパブリックAPI変更
type: docs
weight: 120
url: /ja/net/public-api-changes-in-aspose-cells-8-3-2/
---

{{% alert color="primary" %}} 

この文書では、Aspose.Cells APIの8.3.1から8.3.2への変更について、モジュール/アプリケーション開発者に興味を持たれる可能性がある変更について記載しています。 新しいおよび更新されたパブリックメソッド、[追加されたクラスなど](/cells/ja/net/public-api-changes-in-aspose-cells-8-3-2/)や[削除されたクラスなど](/cells/ja/net/public-api-changes-in-aspose-cells-8-3-2/)だけでなく、Aspose.Cellsの裏側の動作に変更がある場合についても説明しています。

{{% /alert %}} 
## **APIの追加**
### **PivotItemの絶対位置を設定する仕組み**
Aspose.Cells for .NET 8.3.2では、PivotItemの絶対位置指定機能が提供されており、以下のプロパティおよび補助メソッドが公開されています。

- PivotItem.Positionプロパティは、親ノードに関係なくすべてのPivotItemsで位置インデックスを指定するために使用できます。
- PivotItem.PositionInSameParentNodeプロパティは、同じ親ノードのPivotItemsで位置インデックスを指定するために使用できます。
- PivotItem.Move(int count, bool isSameParent)メソッドは、countの値に基づいてアイテムを上または下に移動するために使用できます。countはPivotItemを上または下に移動する位置の数を示し、countの値がゼロより小さい場合、アイテムは上に移動し、countの値がゼロより大きい場合、PivotItemは下に移動します。Boolean型のisSameParentパラメータは、移動操作を同じ親ノード内で実行するかどうかを指定します。

{{% alert color="primary" %}} 

PivotItem.Position、PivotItem.PositionInSameParentNodeプロパティおよびPivotItem.Move(int count, bool isSameParent)メソッドを使用する前に、PivotTable.RefreshDataとPivotTable.CalculateDataメソッドを呼び出す必要があります。

{{% /alert %}} 
### **SignatureLineクラスが追加されました**
Aspose.Cells for .NET 8.3.2では、MS Excelと同等の機能であるSignature Lineを模倣するためのサポートが提供されています。このリリースでは、SignatureLineクラスとPicture.SignatureLineプロパティが公開されています。

以下のサンプルコードでは、Picture.SignatureLineプロパティを使用してワークブックに署名行を追加しています。

**C#**

{{< highlight csharp >}}

 //Create workbook object

Workbook workbook = new Workbook();

//Insert picture of your choice

int index = workbook.Worksheets[0].Pictures.Add(0, 0, "signature.jpg");

//Access picture and add signature line inside it

Picture pic = workbook.Worksheets[0].Pictures[index];

//Create signature line object

SignatureLine s = new SignatureLine();

s.Signer = "John Doe";

s.Title = "Development Lead";

s.Email = "john.doe@aspose.com";

//Assign the signature line object to Picture.SignatureLine property

pic.SignatureLine = s;

{{< /highlight >}}


### **Chart.HasAxisメソッドが追加されました**
v8.3.2のリリースにより、Aspose.Cells APIはChart.HasAxis(AxisType axisType, bool isPrimary)メソッドを提供し、特定の軸がチャートにあるかどうかを判断することができます。

次のサンプルコードは、Chart.HasAxisメソッドの使用方法を示しており、サンプルチャートにプライマリ、セカンダリ、値の軸があるかどうかを判断します。

**C#**

{{< highlight csharp >}}

 //Create workbook object

Workbook workbook = new Workbook("source.xlsx");

//Access the first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Access the chart

Chart chart = worksheet.Charts[0];

//Determine which axis exists in chart

bool ret = chart.HasAxis(AxisType.Category, true);

Console.WriteLine("Has Primary Category Axis: " + ret);

ret = chart.HasAxis(AxisType.Category, false);

Console.WriteLine("Has Secondary Category Axis: " + ret);

ret = chart.HasAxis(AxisType.Value, true);

Console.WriteLine("Has Primary Value Axis: " + ret);

ret = chart.HasAxis(AxisType.Value, false);

Console.WriteLine("Has Secondary Value Axis: " + ret);

{{< /highlight >}}


### **WorkbookSettings.CheckWriteProtectedPasswordメソッドが追加されました**
メソッドWorkbookSettings.CheckWriteProtectedPasswordを使用すると、表計算を変更するための指定したパスワードが正しいかどうかを開発者が確認できます。

**C#**

{{< highlight csharp >}}

 //Specify password to open inside the load options

LoadOptions opts = new LoadOptions();

opts.Password = "1234";

//Open the source Excel file with load options

Workbook workbook = new Workbook("Book1.xlsx", opts);

//Check if 567 is Password to modify

bool ret = workbook.CheckWriteProtectedPassword("567");

Console.WriteLine("Is 567 correct Password to modify: " + ret);

{{< /highlight >}}


### **オーバーロードされたWorkbookRender.ToPrinterおよびSheetRender.ToPrinterメソッドが追加されました**
Aspose.Cells for .NET 8.3.2では、WorkbookRender.ToPrinter(string PrinterName, int PrintPageIndex, int PrintPageCount)およびSheetRender.ToPrinter(string PrinterName, int PrintPageIndex, int PrintPageCount)メソッドが提供され、ワークブックやワークシートのページの範囲を印刷することができます。

以下のサンプルコードは、前述のメソッドを使用して、ワークブックとワークシートのページ 2 から 5 を印刷する方法を示しています。

**C#**

{{< highlight csharp >}}

 //Create workbook from source Excel file

Workbook workbook = new Workbook("source.xlsx");

//Print the workbook specifying the range of pages

//Here we are printing pages 2-5

WorkbookRender wr = new WorkbookRender(workbook, new ImageOrPrintOptions());

wr.ToPrinter(printerName, 1, 4);

//Access first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Print the worksheet specifying the range of pages

//Here we are printing pages 2-5

SheetRender sr = new SheetRender(worksheet, new ImageOrPrintOptions());

sr.ToPrinter(printerName, 1, 4);

{{< /highlight >}}


### **Worksheet.RefreshPivotTablesメソッドが追加されました**
新しく追加されたWorksheet.RefreshPivotTablesメソッドを使用すると、指定されたスプレッドシート内のすべてのピボットテーブルを一括更新することができます。

**C#**

{{< highlight csharp >}}

 worksheet.RefreshPivotTables();

{{< /highlight >}}


### **Workbook.GetNamedStyleメソッドが追加されました**
Aspose.Cells for .NET APIは、文字列をパラメータとして受け取り、そのパラメータに基づいてスタイルオブジェクトを取得するWorkbook.GetNamedStyleメソッドを公開しました。
### **Cells.ImportTwoDimensionArrayメソッドが追加されました**
Aspose.Cells for .NET APIは、TxtLoadOptionsを定義したもとでCells.ImportTwoDimensionArray(object[,], object[,], int, int, TxtLoadOptions)メソッドを公開し、二次元配列をワークシートにインポートすることができるようになりました。
### **OnePagePerSheet、PageIndex、PageCount プロパティが追加されました**
Aspose.Cells for .NET 8.3.2では、XpsSaveOptionsクラスにOnePagePerSheet、PageIndexおよびPageCountプロパティが公開されました。OnePagePerSheetプロパティを使用してスプレッドシートのコンテンツを1ページに収めることができ、PageCountプロパティを使用して印刷するページ数を取得したり設定したりすることができます。PageIndexプロパティは、保存する最初のページの0から始まるインデックスを取得/設定します。
### **NumberDecimalSeparator、NumberGroupSeparator プロパティが追加されました**
Aspose.Cells for .NET 8.3.2 では、NumberDecimalSeparator および NumberGroupSeparator プロパティが導入され、スプレッドシートの数値のフォーマットおよび解析に使用されるカスタムセパレータを取得および設定できます。

以下のサンプルコードは、Aspose.Cells API を使用してカスタムセパレータを指定する方法を示しています。次のコードでは、デシマルセパレータおよびグループのセパレータをそれぞれドットとスペースに指定しています。

**C#**

{{< highlight csharp >}}

 Workbook workbook = new Workbook();

//Specify custom separators

workbook.Settings.NumberDecimalSeparator = '.';

workbook.Settings.NumberGroupSeparator = ' ';

{{< /highlight >}}


### **PdfSaveOptions.IsFontSubstitutionCharGranularity プロパティを追加**
Aspose.Cells for .NET 8.3.2 では、PdfSaveOptions.IsFontSubstitutionCharGranularity プロパティが公開され、特定のフォントファミリを使用して表示できない場合に発生する問題を解決するために使用されます。PdfSaveOptions.IsFontSubstitutionCharGranularity プロパティが true に設定されている場合、表示できない特定の文字のフォントのみが表示可能なフォントに変更され、単語や文の残りは元のフォントのままとなります。

**C#**

{{< highlight csharp >}}

 //Save to Pdf after setting PdfSaveOptions.IsFontSubstitutionCharGranularity to true

PdfSaveOptions opts = new PdfSaveOptions();

opts.IsFontSubstitutionCharGranularity = true;

{{< /highlight >}}


## **API が削除されました**
### **削除された廃止されたメソッド**
公開APIから以下のメソッドが削除されました。

- Workbook.Open および Workbook.Save メソッド。
- Workbook.SetOleSize メソッド。
- Workbook.LoadData メソッド。
- WorkbookDesigner.Open および WorkbookDesigner.Save メソッド。
- WorksheetCollection.DeleteName メソッド。
### **削除された廃止されたプロパティ**
公開APIから以下のプロパティが削除されました。

- Workbook.IsProtected プロパティ。
- Workbook.Language プロパティ。
- Workbook.Region プロパティ。
- WorkbookSettings.ReCalcOnOpen プロパティ。
- WorkbookSettings.Language property.
- WorkbookSettings.Encoding property.
- WorkbookSettings.ConvertNumericData property.
- WorksheetCollection.HidePivotFieldList property.
- WorksheetCollection.EnableHTTPCompression property.
- WorksheetCollection.IsMinimized プロパティ。
- WorksheetCollection.IsHidden プロパティ。
- WorksheetCollection.SheetTabBarWidth property.
- WorksheetCollection.WindowLeft property.
- WorksheetCollection.WindowLeftInch property.
- WorksheetCollection.WindowLeftCM property.
- WorksheetCollection.WindowTop property.
- WorksheetCollection.WindowTopInch property.
- WorksheetCollection.WindowTopCM property.
- WorksheetCollection.WindowWidth property.
- WorksheetCollection.WindowWidthInch property.
- WorksheetCollection.WindowWidthCM property.
- WorksheetCollection.WindowHeight property.
- WorksheetCollection.WindowHeightInch property.
- WorksheetCollection.WindowHeightCM property.
- Worksheet.HPageBreaks property.
- Worksheet.VPageBreaks property.
- HtmlSaveOptions.DisplayHTMLCrossString property.
- HtmlSaveOptions.ExportChartImageFormat property.
- SaveOptions.ExpCellNameToXLSX property.
- SaveOptions.DefaultFont property.
- SaveOptions.Compliance property.
- SaveOptions.PdfBookmark property.
- SaveOptions.PdfImageCompression property.
- TxtSaveOptions.AlwaysQuoted property.
## **非推奨のAPI**
### **非推奨のWorkbook.SaveOptions プロパティ**
適切なSaveOptionsプロパティを設定した後に、SaveOptionsのオブジェクトをWorkbook.Saveメソッドに渡す必要があります。
### **非推奨のWorkbook.Styles プロパティおよびClass StyleCollection**
WorksheetインスタンスのためのWorkbook.CreateStyleメソッドを使用してスタイルを作成・操作することを推奨します。また、Workbook.GetNamedStyle(string)メソッドを使用して名前付きスタイルを取得することができます。
### **非推奨のPivotItem.Move(int count) メソッド**
Aspose.Cells 8.3.2のリリースに伴い、PivotItem.Moveメソッドには、親ノード内のPivotItemを移動する整数パラメータとブールパラメータを受け取る別のオーバーロードが導入されました。
{{< app/cells/assistant language="csharp" >}}

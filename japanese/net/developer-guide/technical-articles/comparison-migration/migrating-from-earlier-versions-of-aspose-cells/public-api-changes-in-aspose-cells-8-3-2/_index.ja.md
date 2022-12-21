---
title: パブリック API Aspose.Cells の変更点 8.3.2
type: docs
weight: 120
url: /ja/net/public-api-changes-in-aspose-cells-8-3-2/
---
{{% alert color="primary" %}} 

このドキュメントでは、モジュール/アプリケーション開発者にとって興味深い、バージョン 8.3.1 から 8.3.2 への Aspose.Cells API への変更について説明します。新規および更新された public メソッドだけでなく、[クラス追加など](/cells/ja/net/public-api-changes-in-aspose-cells-8-3-2/)と[削除されたクラスなど](/cells/ja/net/public-api-changes-in-aspose-cells-8-3-2/)だけでなく、Aspose.Cells の舞台裏での動作の変更についても説明します。

{{% /alert %}} 
## **追加された API**
### **PivotItem の絶対位置を設定する仕組み**
機能を提供するために[PivotItem の絶対配置](/cells/ja/net/specifying-the-absolute-position-of-the-pivot-item/)、Aspose.Cells for .NET 8.3.2 は、以下にリストされている一連のプロパティと支援メソッドを公開しています。

- PivotItem.Position プロパティを使用して、親ノードに関係なく、すべての PivotItems の位置インデックスを指定できます。
- PivotItem.PositionInSameParentNode プロパティを使用して、同じ親ノードの下にある PivotItems の位置インデックスを指定できます。
- PivotItem.Move(int count, bool isSameParent) メソッドを使用して、カウント値に基づいてアイテムを上下に移動できます。カウントは、PivotItem を上下に移動する位置の数です。カウント値がゼロより小さい場合、アイテムは上に移動し、カウント値がゼロより大きい場合、PivotItem は下に移動します。ブール型の isSameParent パラメータは、移動操作を同じ親ノードで実行する必要があるかどうかを指定しますか否か。

{{% alert color="primary" %}} 

PivotItem.Position、PivotItem.PositionInSameParentNode プロパティ、および PivotItem.Move(int count, bool isSameParent) メソッドを使用する前に、PivotTable.RefreshData および PivotTable.CalculateData メソッドを呼び出す必要があることに注意してください。

{{% /alert %}} 
### **クラス SignatureLine が追加されました**
Aspose.Cells for .NET 8.3.2 は、MS Excel の同等の機能を模倣する署名欄のサポートを提供します。 Aspose.Cells for .NET のこのリリースでは、この目的のために SignatureLine クラスと Picture.SignatureLine プロパティが公開されています。

次のサンプル コードは、Picture.SignatureLine プロパティを使用して署名欄をブックに追加します。

**C#**

{{< highlight "csharp" >}}

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


### **メソッド Chart.HasAxis が追加されました**
v8.3.2 のリリースにより、Aspose.Cells API は Chart.HasAxis(AxisType axisType, bool isPrimary) メソッドを提供して、グラフに特定の軸があるかどうかを判断します。

次のサンプル コードは、Chart.HasAxis メソッドを使用して、サンプル グラフに第 1 軸、第 2 軸、および数値軸があるかどうかを判断する方法を示しています。

**C#**

{{< highlight "csharp" >}}

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


### **メソッド WorkbookSettings.CheckWriteProtectedPassword が追加されました**
メソッド WorkbookSettings.CheckWriteProtectedPassword を使用すると、開発者は、スプレッドシートを変更するための特定のパスワードが正しいかどうかを確認できます。

**C#**

{{< highlight "csharp" >}}

 //Specify password to open inside the load options

LoadOptions opts = new LoadOptions();

opts.Password = "1234";

//Open the source Excel file with load options

Workbook workbook = new Workbook("Book1.xlsx", opts);

//Check if 567 is Password to modify

bool ret = workbook.CheckWriteProtectedPassword("567");

Console.WriteLine("Is 567 correct Password to modify: " + ret);

{{< /highlight >}}


### **オーバーロード メソッド WorkbookRender.ToPrinter および SheetRender.ToPrinter が追加されました**
Aspose.Cells for .NET 8.3.2 では、WorkbookRender.ToPrinter(string PrinterName, int PrintPageIndex, int PrintPageCount) メソッドと SheetRender.ToPrinter(string PrinterName, int PrintPageIndex, int PrintPageCount) メソッドが提供され、ワークブックとワークシートのページ範囲をそれぞれ印刷します。

次のサンプル コードは、前述のメソッドを使用してブックとワークシートの 2 ～ 5 ページを印刷する方法を示しています。

**C#**

{{< highlight "csharp" >}}

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


### **メソッド Worksheet.RefreshPivotTables が追加されました**
新しく追加されたメソッド Worksheet.RefreshPivotTables を使用すると、特定のスプレッドシートのすべてのピボット テーブルを 1 回の呼び出しで更新できます。

**C#**

{{< highlight "csharp" >}}

 worksheet.RefreshPivotTables();

{{< /highlight >}}


### **メソッド Workbook.GetNamedStyle が追加されました**
Aspose.Cells for .NET API は、文字列をパラメーターとして受け取り、渡されたパラメーターに基づいて Style オブジェクトを取得する Workbook.GetNamedStyle メソッドを公開しました。
### **メソッド Cells.ImportTwoDimensionArray が追加されました**
Aspose.Cells for .NET API は、Cells.ImportTwoDimensionArray(object[,], object[,], int, int, TxtLoadOptions) メソッドを公開することで、2 次元配列をスプレッドシートのセルにインポートできるようにしました。上記のメソッドは、TxtLoadOptions で定義されたより柔軟なオプションを使用して、データの 2 次元配列をワークシートにインポートします。
### **プロパティ OnePagePerSheet、PageIndex、PageCount を追加**
Aspose.Cells for .NET 8.3.2 は、XpsSaveOptions クラスの OnePagePerSheet、PageIndex、および PageCount プロパティを公開しました。ユーザーは、OnePagePerSheet プロパティを使用してスプレッドシートのすべてのコンテンツを XPS の 1 ページに収めたり、PageCount プロパティを使用して印刷するページ数を取得したりできます。 PageIndex プロパティは、保存する最初のページの 0 から始まるインデックスを取得または設定します。
### **プロパティ NumberDecimalSeparator および NumberGroupSeparator が追加されました**
Aspose.Cells for .NET 8.3.2 では NumberDecimalSeparator および NumberGroupSeparator プロパティが導入され、スプレッドシートの数値の書式設定と解析に使用されるカスタム セパレータを取得/設定できます。

次のサンプル コードは、Aspose.Cells API を使用してカスタム セパレータを指定する方法を示しています。

**C#**

{{< highlight "csharp" >}}

 Workbook workbook = new Workbook();

//Specify custom separators

workbook.Settings.NumberDecimalSeparator = '.';

workbook.Settings.NumberGroupSeparator = ' ';

{{< /highlight >}}


### **プロパティ PdfSaveOptions.IsFontSubstitutionCharGranularity が追加されました**
Aspose.Cells for .NET 8.3.2 は、特定のフォント ファミリを使用して一部の Unicode 文字を表示できないという問題を克服するために、PdfSaveOptions.IsFontSubstitutionCharGranularity プロパティを公開しました。 PdfSaveOptions.IsFontSubstitutionCharGranularity プロパティが true に設定されている場合、表示できない特定の文字のフォントのみが表示可能なフォントに変更され、残りの単語または文は元のフォントのままになります。

**C#**

{{< highlight "csharp" >}}

 //Save to Pdf after setting PdfSaveOptions.IsFontSubstitutionCharGranularity to true

PdfSaveOptions opts = new PdfSaveOptions();

opts.IsFontSubstitutionCharGranularity = true;

{{< /highlight >}}


## **削除された API**
### **廃止されたメソッドの削除**
以下のメソッドは Public API から削除されました。

- Workbook.Open および Workbook.Save メソッド。
- Workbook.SetOleSize メソッド。
- Workbook.LoadData メソッド。
- WorkbookDesigner.Open および WorkbookDesigner.Save メソッド。
- WorksheetCollection.DeleteName メソッド。
### **廃止されたプロパティの削除**
次のプロパティは、Public API から削除されました。

- Workbook.IsProtected プロパティ。
- Workbook.Language プロパティ。
- Workbook.Region プロパティ。
- WorkbookSettings.ReCalcOnOpen プロパティ。
- WorkbookSettings.Language プロパティ。
- WorkbookSettings.Encoding プロパティ。
- WorkbookSettings.ConvertNumericData プロパティ。
- WorksheetCollection.HidePivotFieldList プロパティ。
- WorksheetCollection.EnableHTTPCompression プロパティ。
- WorksheetCollection.IsMinimized プロパティ。
- WorksheetCollection.IsHidden プロパティ。
- WorksheetCollection.SheetTabBarWidth プロパティ。
- WorksheetCollection.WindowLeft プロパティ。
- WorksheetCollection.WindowLeftInch プロパティ。
- WorksheetCollection.WindowLeftCM プロパティ。
- WorksheetCollection.WindowTop プロパティ。
- WorksheetCollection.WindowTopInch プロパティ。
- WorksheetCollection.WindowTopCM プロパティ。
- WorksheetCollection.WindowWidth プロパティ。
- WorksheetCollection.WindowWidthInch プロパティ。
- WorksheetCollection.WindowWidthCM プロパティ。
- WorksheetCollection.WindowHeight プロパティ。
- WorksheetCollection.WindowHeightInch プロパティ。
- WorksheetCollection.WindowHeightCM プロパティ。
- Worksheet.HPageBreaks プロパティ。
- Worksheet.VPageBreaks プロパティ。
- HtmlSaveOptions.DisplayHTMLCrossString プロパティ。
- HtmlSaveOptions.ExportChartImageFormat プロパティ。
- SaveOptions.ExpCellNameToXLSX プロパティ。
- SaveOptions.DefaultFont プロパティ。
- SaveOptions.Compliance プロパティ。
- SaveOptions.PdfBookmark プロパティ。
- SaveOptions.PdfImageCompression プロパティ。
- TxtSaveOptions.AlwaysQuoted プロパティ。
## **廃止された API**
### **プロパティ Workbook.SaveOptions 廃止**
適切な SaveOptions プロパティを設定した後、SaveOptions のオブジェクトを Workbook.Save メソッドに渡す必要があります。
### **プロパティ Workbook.Styles & クラス StyleCollection 廃止**
StyleCollection.Add メソッドでスタイルを作成する代わりに、Workbook.CreateStyle メソッドを使用して Workbook インスタンスのスタイルを作成および操作することをお勧めします。さらに、Workbook.GetNamedStyle(string) メソッドを使用して、StyleCollection[string] の代わりに名前付きスタイルを取得できます。
### **メソッド PivotItem.Move(int count) 廃止されました**
Aspose.Cells 8.3.2 のリリースにより、API は PivotItem.Move メソッドの別のオーバーロードを導入しました。このメソッドは、親ノード内で PivotItem を移動するためのカウントおよびブール値パラメーターの整数パラメーターを受け入れます。

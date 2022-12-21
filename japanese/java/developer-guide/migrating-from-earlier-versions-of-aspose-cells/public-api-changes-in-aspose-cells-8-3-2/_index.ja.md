---
title: パブリック API Aspose.Cells の変更点 8.3.2
type: docs
weight: 130
url: /ja/java/public-api-changes-in-aspose-cells-8-3-2/
---
{{% alert color="primary" %}} 

このドキュメントでは、モジュール/アプリケーション開発者にとって興味深い、バージョン 8.3.1 から 8.3.2 への Aspose.Cells API への変更について説明します。新規および更新された public メソッドだけでなく、[クラス追加など](/cells/ja/java/public-api-changes-in-aspose-cells-8-3-2/)と[削除されたクラスなど](/cells/ja/java/public-api-changes-in-aspose-cells-8-3-2/)だけでなく、Aspose.Cells の舞台裏での動作の変更についても説明します。

{{% /alert %}} 
## **追加された API**
### **PivotItem の絶対位置を設定する仕組み**
機能を提供するために[PivotItem の絶対配置](/cells/ja/java/specifying-the-absolute-position-of-the-pivot-item/)、Aspose.Cells for Java 8.3.2 は、以下にリストされている一連のプロパティとメソッドを公開しています。

- PivotItem.setPosition を使用して、親ノードに関係なく、すべての PivotItems の位置インデックスを設定できます。
- PivotItem.setPositionInSameParentNode を使用して、同じ親ノードの下の PivotItems に位置インデックスを設定できます。
- PivotItem.move(int count, bool isSameParent) メソッドを使用して、count 値に基づいて項目を上下に移動できます。count は、PivotItem を上下に移動する位置の数です。カウント値がゼロより小さい場合、アイテムは上に移動し、カウント値がゼロより大きい場合、PivotItem は下に移動します。ブール型の isSameParent パラメータは、移動操作を同じ親ノードで実行する必要があるかどうかを指定しますか否か。

{{% alert color="primary" %}} 

PivotItem.setPosition、PivotItem.setPositionInSameParentNode プロパティ、および PivotItem.move(int count, bool isSameParent) メソッドを使用する前に、PivotTable.refreshData および PivotTable.calculateData メソッドを呼び出す必要があることに注意してください。

{{% /alert %}} 
### **クラス SignatureLine が追加されました**
Aspose.Cells 8.3.2 は、MS Excel の同等の機能を模倣する署名欄のサポートを提供します。このリリースでは、この目的のために SignatureLine クラスと Picture.SignatureLine プロパティが公開されています。

次のサンプル コードは、Picture.SignatureLine プロパティを使用して署名欄をブックに追加します。

**Java**

{{< highlight "csharp" >}}

 //Create workbook object

Workbook workbook = new Workbook();

//Insert picture of your choice

int index = workbook.getWorksheets().get(0).getPictures().add(0, 0, "signature.jpg");

//Access picture and add signature line inside it

Picture pic = workbook.getWorksheets().get(0).getPictures().get(index);

//Create signature line object

SignatureLine s = new SignatureLine();

s.setSigner("John Doe");

s.setTitle("Development Lead");

s.setEmail("john.doe@aspose.com");

//Assign the signature line object to Picture.SignatureLine property

pic.setSignatureLine(s);

{{< /highlight >}}
### **メソッド Chart.hasAxis が追加されました**
v8.3.2 のリリースにより、Aspose.Cells API は Chart.hasAxis(AxisType axisType, bool isPrimary) メソッドを提供して、グラフに特定の軸があるかどうかを判断します。

次のサンプル コードは、Chart.hasAxis メソッドを使用して、サンプル グラフに主軸、副軸、値軸があるかどうかを判断する方法を示しています。

**Java**

{{< highlight "csharp" >}}

 //Create workbook object

Workbook workbook = new Workbook("source.xlsx");

//Access the first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Access the chart

Chart chart = worksheet.getCharts().get(0);

//Determine which axis exists in chart

boolean ret = chart.hasAxis(AxisType.CATEGORY, true);

System.out.println("Has Primary Category Axis: " + ret);

ret = chart.hasAxis(AxisType.CATEGORY, false);

System.out.println("Has Secondary Category Axis: " + ret);

ret = chart.hasAxis(AxisType.VALUE, true);

System.out.println("Has Primary Value Axis: " + ret);

ret = chart.hasAxis(AxisType.VALUE, false);

System.out.println("Has Seconary Value Axis: " + ret);

{{< /highlight >}}
### **メソッド WorkbookSettings.checkWriteProtectedPassword が追加されました**
メソッド WorkbookSettings.checkWriteProtectedPassword を使用すると、開発者は、スプレッドシートを変更するための特定のパスワードが正しいかどうかを確認できます。

**Java**

{{< highlight "csharp" >}}

 //Specify password to open inside the load options

LoadOptions opts = new LoadOptions();

opts.setPassword("1234");

//Open the source Excel file with load options

Workbook workbook = new Workbook("Book1.xlsx", opts);

//Check if 567 is Password to modify

boolean ret = workbook.checkWriteProtectedPassword("567");

System.out.println("Is 567 correct Password to modify: " + ret);

{{< /highlight >}}
### **オーバーロード メソッド WorkbookRender.toPrinter および SheetRender.toPrinter が追加されました**
Aspose.Cells 8.3.2 は WorkbookRender.toPrinter(string printerName, int printPageIndex, int printPageCount) メソッドと SheetRender.toPrinter(string printerName, int printPageIndex, int printPageCount) メソッドを提供して、ワークブックとワークシートのページ範囲をそれぞれ印刷します。

次のサンプル コードは、前述のメソッドを使用してブックとワークシートの 2 ～ 5 ページを印刷する方法を示しています。

**Java**

{{< highlight "csharp" >}}

 //Create workbook from source Excel file

Workbook workbook = new Workbook("source.xlsx");

//Print the workbook specifying the range of pages

//Here we are printing pages 2-5

WorkbookRender wr = new WorkbookRender(workbook, new ImageOrPrintOptions());

wr.toPrinter(printerName, 1, 4);

//Access first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Print the worksheet specifying the range of pages

//Here we are printing pages 2-5

SheetRender sr = new SheetRender(worksheet, new ImageOrPrintOptions());

sr.toPrinter(printerName, 1, 4);

{{< /highlight >}}
### **メソッド Worksheet.refreshPivotTables が追加されました**
新しく追加されたメソッド Worksheet.refreshPivotTables を使用すると、特定のスプレッドシート内のすべてのピボット テーブルを 1 回の呼び出しで更新できます。

**Java**

{{< highlight "csharp" >}}

 worksheet.refreshPivotTables();

{{< /highlight >}}
### **メソッド Workbook.getNamedStyle が追加されました**
Aspose.Cells 8.3.2 は Workbook.getNamedStyle メソッドを公開しました。このメソッドは、文字列をパラメーターとして受け取り、渡されたパラメーターに基づいて Style オブジェクトを取得します。
### **メソッド Cells.importTwoDimensionArray が追加されました**
Aspose.Cells API は、Cells.importTwoDimensionArray(object[,], object[,], int, int, TxtLoadOptions) メソッドを公開することで、2 次元配列をスプレッドシートのセルにインポートできるようにしました。上記のメソッドは、TxtLoadOptions で定義されたより柔軟なオプションを使用して、データの 2 次元配列をワークシートにインポートします。
### **プロパティ OnePagePerSheet、PageIndex、PageCount を追加**
Aspose.Cells for Java 8.3.2 は、XpsSaveOptions クラスの OnePagePerSheet、PageIndex、および PageCount プロパティを公開しました。ユーザーは、OnePagePerSheet プロパティを使用してスプレッドシートのすべてのコンテンツを XPS の 1 ページに収めたり、PageCount プロパティを使用して印刷するページ数を取得したりできます。 PageIndex プロパティは、保存する最初のページの 0 から始まるインデックスを取得または設定します。
### **プロパティ NumberDecimalSeparator および NumberGroupSeparator が追加されました**
Aspose.Cells for Java 8.3.2 では NumberDecimalSeparator および NumberGroupSeparator プロパティが導入され、スプレッドシートの数値の書式設定と解析に使用されるカスタム セパレータを取得/設定できます。

次のサンプル コードは、Aspose.Cells API を使用してカスタム セパレータを指定する方法を示しています。次のコードでは、カスタムの Decimal および Group セパレータをそれぞれドットとスペースとして指定しています。

**Java**

{{< highlight "csharp" >}}

 Workbook workbook = new Workbook();

//Specify custom separators

workbook.getSettings().setNumberDecimalSeparator('.');

workbook.getSettings().setNumberGroupSeparator(' ');

{{< /highlight >}}
### **プロパティ PdfSaveOptions.setFontSubstitutionCharGranularity が追加されました**
Aspose.Cells for Java 8.3.2 は、特定のフォント ファミリを使用して一部の Unicode 文字を表示できないという問題を解決するために、PdfSaveOptions.setFontSubstitutionCharGranularity プロパティを公開しました。 PdfSaveOptions.setFontSubstitutionCharGranularity プロパティが true に設定されている場合、表示できない特定の文字のフォントのみが表示可能なフォントに変更され、残りの単語または文は元のフォントのままになります。

**Java**

{{< highlight "csharp" >}}

 //Save to PDF after setting PdfSaveOptions.setFontSubstitutionCharGranularity

PdfSaveOptions opts = new PdfSaveOptions();

opts.setFontSubstitutionCharGranularity(true);

{{< /highlight >}}
## **削除された API**
### **廃止されたメソッドの削除**
以下のメソッドは Public API から削除されました。

- Workbook.open および Workbook.save メソッド。
- Workbook.setOleSize メソッド。
- Workbook.loadData メソッド。
- WorkbookDesigner.open および WorkbookDesigner.save メソッド。
- WorksheetCollection.deleteName メソッド。
### **廃止されたプロパティの削除**
次のプロパティは、Public API から削除されました。

- Workbook.isProtected プロパティ。
- Workbook.Language プロパティ。
- Workbook.Region プロパティ。
- WorkbookSettings.ReCalcOnOpen プロパティ。
- WorkbookSettings.Language プロパティ。
- WorkbookSettings.Encoding プロパティ。
- WorkbookSettings.ConvertNumericData プロパティ。
- WorksheetCollection.HidePivotFieldList プロパティ。
- WorksheetCollection.EnableHTTPCompression プロパティ。
- WorksheetCollection.isMinimized プロパティ。
- WorksheetCollection.isHidden プロパティ。
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
### **プロパティ Workbook.saveOptions 廃止**
適切な SaveOptions プロパティを設定した後、SaveOptions のオブジェクトを Workbook.Save メソッドに渡す必要があります。
### **プロパティ Workbook.Styles & クラス StyleCollection 廃止**
StyleCollection.add メソッドでスタイルを作成する代わりに、Workbook.createStyle メソッドを使用して Workbook インスタンスのスタイルを作成および操作することをお勧めします。さらに、StyleCollection.get(string) の代わりに Workbook.getNamedStyle(string) メソッドを使用して名前付きスタイルを取得できます。
### **メソッド PivotItem.move(int count) 廃止されました**
Aspose.Cells 8.3.2 のリリースにより、API は PivotItem.move メソッドの別のオーバーロードを導入しました。このメソッドは、親ノード内で PivotItem を移動するためのカウントおよびブール値パラメーターの整数パラメーターを受け入れます。

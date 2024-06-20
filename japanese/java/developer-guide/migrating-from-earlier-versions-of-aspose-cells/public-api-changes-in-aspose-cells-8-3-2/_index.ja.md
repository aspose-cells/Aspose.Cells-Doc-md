---
title: Aspose.Cells 8.3.2でのパブリックAPI変更
type: docs
weight: 130
url: /ja/java/public-api-changes-in-aspose-cells-8-3-2/
---

{{% alert color="primary" %}} 

このドキュメントでは、8.3.1から8.3.2へのAspose.Cells APIの変更について、モジュール/アプリケーション開発者に興味を持つ可能性がある事項について説明しています。新しいおよび更新されたパブリックメソッド、[追加されたクラスなど](/cells/ja/java/public-api-changes-in-aspose-cells-8-3-2/)および[削除されたクラスなど](/cells/ja/java/public-api-changes-in-aspose-cells-8-3-2/)だけでなく、Aspose.Cellsの背後にある動作に関する変更の説明も含まれます。

{{% /alert %}} 
## **APIの追加**
### **PivotItemの絶対位置を設定する仕組み**
PivotItemの絶対位置指定の機能を提供するために、Aspose.Cells for Java 8.3.2では、以下にリストされている一連のプロパティとメソッドが公開されました。

- PivotItem.setPositionを使用して、親ノードに関係なくすべてのPivotItemの位置インデックスを設定できます。
- PivotItem.setPositionInSameParentNodeを使用して、同じ親ノード内のPivotItemの位置インデックスを設定できます。
- PivotItem.move(int count, bool isSameParent)メソッドを使用して、count値に基づいてアイテムを上下に移動できます。countはPivotItemを上または下に移動する位置の数を指定し、count値が負の場合、アイテムは上に移動し、count値が正の場合、PivotItemは下に移動します。Boolean型のisSameParentパラメータは、移動操作を同じ親ノードで実行するかどうかを指定します。

{{% alert color="primary" %}} 

PivotItem.setPosition、PivotItem.setPositionInSameParentNodeプロパティおよびPivotItem.move(int count, bool isSameParent)メソッドを使用する前に、PivotTable.refreshDataおよびPivotTable.calculateDataメソッドを呼び出す必要があります。

{{% /alert %}} 
### **SignatureLineクラスが追加されました**
Aspose.Cells 8.3.2では、MS Excelの同等機能であるSignature Lineをエミュレートするためのサポートが提供されます。このリリースでは、目的のためにSignatureLineクラスとPicture.SignatureLineプロパティが公開されました。

以下のサンプルコードでは、Picture.SignatureLineプロパティを使用してワークブックに署名行を追加しています。

**Java**

{{< highlight csharp >}}

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
### **Chart.hasAxisメソッドを追加しました**
v8.3.2のリリースに伴い、Aspose.Cells APIはChart.hasAxis(AxisType axisType, bool isPrimary)メソッドを提供し、特定の軸がチャートに存在するかどうかを判断できるようにしました。

次のサンプルコードは、Chart.hasAxisメソッドを使用して、サンプルのチャートにプライマリ、セカンダリ、値の軸があるかどうかを判断する方法を示しています。

**Java**

{{< highlight csharp >}}

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
### **WorkbookSettings.checkWriteProtectedPasswordメソッドを追加しました**
WorkbookSettings.checkWriteProtectedPassword メソッドは、スプレッドシートを変更するためのパスワードが正しいかどうかを開発者が確認することを可能にします。

**Java**

{{< highlight csharp >}}

 //Specify password to open inside the load options

LoadOptions opts = new LoadOptions();

opts.setPassword("1234");

//Open the source Excel file with load options

Workbook workbook = new Workbook("Book1.xlsx", opts);

//Check if 567 is Password to modify

boolean ret = workbook.checkWriteProtectedPassword("567");

System.out.println("Is 567 correct Password to modify: " + ret);

{{< /highlight >}}
### **Overload Methods WorkbookRender.toPrinter & SheetRender.toPrinter Added**
Aspose.Cells 8.3.2 では、WorkbookRender.toPrinter(string printerName, int printPageIndex, int printPageCount) および SheetRender.toPrinter(string printerName, int printPageIndex, int printPageCount) メソッドを提供しています。これらのメソッドはそれぞれワークブックとワークシートのページの範囲を印刷するために使用されます。

以下のサンプルコードは、前述のメソッドを使用して、ワークブックとワークシートのページ 2 から 5 を印刷する方法を示しています。

**Java**

{{< highlight csharp >}}

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
### **Worksheet.refreshPivotTables メソッドが追加されました**
新たに追加された Worksheet.refreshPivotTables メソッドは、指定されたスプレッドシート内のすべてのピボットテーブルを一括で更新することを可能にします。

**Java**

{{< highlight csharp >}}

 worksheet.refreshPivotTables();

{{< /highlight >}}
### **Workbook.getNamedStyle メソッドが追加されました**
Aspose.Cells 8.3.2 で新たに公開された Workbook.getNamedStyle メソッドは、パラメータとして文字列を受け取り、そのパラメータに基づいてスタイルオブジェクトを取得します。
### **Cells.importTwoDimensionArray メソッドが追加されました**
Aspose.Cells API は、Cells.importTwoDimensionArray(object[,], object[,], int, int, TxtLoadOptions) メソッドを公開することで、スプレッドシートのセルに二次元配列をインポートできるようにしました。このメソッドは、TxtLoadOptions で定義されたより柔軟なオプションを使用して、データの二次元配列をワークシートにインポートします。
### **OnePagePerSheet、PageIndex、PageCount プロパティが追加されました**
Aspose.Cells for Java 8.3.2 では、OnePagePerSheet、PageIndex、PageCount プロパティが XpsSaveOptions クラスに公開されています。OnePagePerSheet プロパティを使用すると、1 ページにスプレッドシートのすべてのコンテンツを収めることができます。また、PageCount プロパティを使用すると、印刷するページ数を取得できます。PageIndex プロパティは、保存する最初のページの 0 から始まるインデックスを取得/設定します。
### **NumberDecimalSeparator、NumberGroupSeparator プロパティが追加されました**
Aspose.Cells for Java 8.3.2 で、NumberDecimalSeparator、NumberGroupSeparator プロパティが導入され、スプレッドシートで数値のフォーマットとパースに使用されるカスタムセパレータを取得/設定できます。

以下のサンプルコードは、Aspose.Cells API を使用してカスタムセパレータを指定する方法を示しています。以下のコードは、カスタムの小数点とグループセパレータをそれぞれドットとスペースに指定しています。

**Java**

{{< highlight csharp >}}

 Workbook workbook = new Workbook();

//Specify custom separators

workbook.getSettings().setNumberDecimalSeparator('.');

workbook.getSettings().setNumberGroupSeparator(' ');

{{< /highlight >}}
### **PdfSaveOptions.setFontSubstitutionCharGranularity プロパティが追加されました**
Aspose.Cells for Java 8.3.2 では、PdfSaveOptions.setFontSubstitutionCharGranularity プロパティを公開し、特定のフォントファミリーを使用して表示できない一部の Unicode 文字を表示可能なフォントに変更することが可能となります。PdfSaveOptions.setFontSubstitutionCharGranularity プロパティが true に設定されている場合、表示不可能な特定の文字のみが表示可能なフォントに変更され、それ以外の単語や文章は元のフォントのままとなります。

**Java**

{{< highlight csharp >}}

 //Save to PDF after setting PdfSaveOptions.setFontSubstitutionCharGranularity

PdfSaveOptions opts = new PdfSaveOptions();

opts.setFontSubstitutionCharGranularity(true);

{{< /highlight >}}
## **API が削除されました**
### **削除された廃止されたメソッド**
公開APIから以下のメソッドが削除されました。

- Workbook.open および Workbook.save メソッド。
- Workbook.setOleSize メソッド。
- Workbook.loadData メソッド。
- WorkbookDesigner.open および WorkbookDesigner.save メソッド。
- WorksheetCollection.deleteName メソッド。
### **削除された廃止されたプロパティ**
公開APIから以下のプロパティが削除されました。

- Workbook.isProtected プロパティ。
- Workbook.Language プロパティ。
- Workbook.Region プロパティ。
- WorkbookSettings.ReCalcOnOpen プロパティ。
- WorkbookSettings.Language property.
- WorkbookSettings.Encoding property.
- WorkbookSettings.ConvertNumericData property.
- WorksheetCollection.HidePivotFieldList property.
- WorksheetCollection.EnableHTTPCompression property.
- WorksheetCollection.isMinimized property.
- WorksheetCollection.isHidden property.
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
### **廃止されたWorkbook.saveOptionsプロパティ**
適切なSaveOptionsプロパティを設定した後に、SaveOptionsのオブジェクトをWorkbook.Saveメソッドに渡す必要があります。 
### **廃止されたWorkbook.StylesおよびClass StyleCollectionプロパティ**
Workbook.createStyleメソッドを使用してWorkbookインスタンスのスタイルを作成および操作することを推奨します。また、StyleCollection.addメソッドでスタイルを作成する代わりに、Workbook.getNamedStyle(string)メソッドを使用して名前付きスタイルを取得できます。
### **廃止されたPivotItem.move(int count)メソッド**
Aspose.Cells 8.3.2以降、APIにはPivotItem.moveメソッドの別のオーバーロードが導入され、親ノード内でPivotItemを移動するための整数パラメータとブールパラメータを受け入れます。 

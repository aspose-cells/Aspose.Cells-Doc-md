---
title: Aspose.Cells 8.6.2の公開API変更
type: docs
weight: 220
url: /ja/java/public-api-changes-in-aspose-cells-8-6-2/
---

{{% alert color="primary" %}} 

このドキュメントでは、Aspose.Cells APIの8.6.1から8.6.2への変更について記載されています。これはモジュール/アプリケーション開発者に関心がある可能性のある新しいおよび更新された公開メソッド、追加されたクラスだけでなく、Aspose.Cellsの内部の動作に関する変更の説明も含まれています。

{{% /alert %}} 
## **APIの追加**
### **Smart Markersのコールバックのサポート**
このリリースのAspose.Cells for Java APIでは、WorkbookDesigner.CallBackフィールドとISmartMarkerCallBackインタフェースが公開され、それらを共に使用して、セル参照や/または処理されているスマートマーカーに関する通知を取得できます。 

**Java**

{{< highlight csharp >}}

 public class SmartMarkerCallBack implements ISmartMarkerCallBack 

{

	Workbook workbook;

	SmartMarkerCallBack(Workbook workbook)

	{

	    this.workbook = workbook;

	}



	@Override

	public void process(int sheetIndex, int rowIndex, int colIndex, String tableName, String columnName)

	{

	    System.out.println("Processing Cell : " + workbook.getWorksheets().get(sheetIndex).getName() + "!" + CellsHelper.cellIndexToName(rowIndex, colIndex));

	    System.out.println("Processing Marker : " + tableName + "." + columnName);

	}

}

{{< /highlight >}}

プロセスの残りは、デザイナースプレッドシートのロード（WorkbookDesignerを使用）またはゼロから作成し、データソースを設定して処理することが含まれます。ただし、通知を有効にするには、WorkbookDesigner.processメソッドを呼び出す前にWorkbookDesigner.CallBackプロパティを設定する必要があります。

**Java**

{{< highlight csharp >}}

 //Instantiate a new Workbook designer

WorkbookDesigner report = new WorkbookDesigner();

//Get the first worksheet of the workbook

Worksheet sheet = report.getWorkbook().getWorksheets().get(0);

//Set the Variable Array marker to a cell

//You may also place this Smart Marker into a template file manually using Excel and then open this file via WorkbookDesigner 

sheet.getCells().get("A1").putValue("&=$VariableArray");

//Set the data source for the marker(s)

report.setDataSource("VariableArray", new String[] { "English", "Arabic", "Hindi", "Urdu", "French" });

//Set the CallBack property

report.setCallBack(new SmartMarkerCallBack(report.getWorkbook()));

//Process the markers

report.process(false);

{{< /highlight >}}
### **Chart.toPdfメソッドの追加**
Aspose.Cells for Java 8.6.2では、Chart.toPdfメソッドが公開され、Chartの形状を直接PDF形式にレンダリングするために使用できます。このメソッドは現在、ファイルの保存先としてString型のパラメータを受け入れます。

以下はシンプルな使用シナリオです。

**Java**

{{< highlight csharp >}}

 //Load spreadsheet containing charts

Workbook workbook = new Workbook(inputFilePath);

//Access first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Access first chart inside the worksheet

Chart chart = worksheet.getCharts().get(0);

//Save the chart in PDF format

chart.toPdf(outputFilePath);

{{< /highlight >}}
### **Workbook.removeUnusedStylesメソッドの追加**
Aspose.Cells for Java 8.6.2では、Workbook.removeUnusedStylesメソッドが公開され、ブック内の未使用のスタイルオブジェクトをすべて削除できます。 

以下はシンプルな使用シナリオです。

**Java**

{{< highlight csharp >}}

 //Load spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Remove all unused styles from the template

workbook.removeUnusedStyles();

{{< /highlight >}}
### **Cells.Styleプロパティの追加**
Cells.Styleプロパティは、デフォルトのスタイルを示すワークシートのスタイルにアクセスするために使用できます。

以下はシンプルな使用シナリオです。

**Java**

{{< highlight csharp >}}

 //Load a spreadsheet

Workbook book = new Workbook(inputFilePath);

//Access the default style of worksheet

Style style = book.getWorksheets().get(0).getCells().getStyle();

{{< /highlight >}}
### **GridWebのためのイベントの追加**
Aspose.Cells.GridWeb for Java 8.6.2では、次の2つの新しいイベントが公開されています。

1. AjaxCallFinished：コントロールのAjax更新が終了したときに発生します。（EnableAJAXはtrueに設定する必要があります）。
1. CellModifiedOnAjax: セルがAJAX呼び出しで変更されたときに発生します。

---
title: パブリック API Aspose.Cells の変更点 8.6.2
type: docs
weight: 220
url: /ja/java/public-api-changes-in-aspose-cells-8-6-2/
---
{{% alert color="primary" %}} 

このドキュメントでは、モジュール/アプリケーション開発者にとって興味深い、バージョン 8.6.1 から 8.6.2 への Aspose.Cells API への変更について説明します。新規および更新されたパブリック メソッド、追加されたクラスだけでなく、Aspose.Cells の舞台裏での動作の変更の説明も含まれています。

{{% /alert %}} 
## **追加された API**
### **スマートマーカーによるコールバックのサポート**
Aspose.Cells for Java API のこのリリースでは、WorkbookDesigner.CallBack フィールドと ISmartMarkerCallBack インターフェイスが公開されました。[処理中のセル参照および/またはスマート マーカーに関する通知を取得する](/cells/ja/java/getting-notifications-while-merging-data-with-smart-markers/).次のコードは、 ISmartMarkerCallBack インターフェイスを使用して WorkbookDesigner.process メソッドのコールバックを処理する新しいクラスを定義する方法を示しています。

**Java**

{{< highlight "csharp" >}}

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

プロセスの残りの部分には、スマート マーカーを含むデザイナー スプレッドシートを WorkbookDesigner でロードするか、ゼロから作成してデータ ソースを設定して処理することが含まれます。ただし、通知を有効にするには、以下に示すように WorkbookDesigner.process メソッドを呼び出す前に WorkbookDesigner.CallBack プロパティを設定する必要があります。

**Java**

{{< highlight "csharp" >}}

 //Instantiate a new Workbook designer

WorkbookDesigner report = new WorkbookDesigner();

//Get the first worksheet of the workbook

Worksheet sheet = report.getWorkbook().getWorksheets().get(0);

//Set the Variable Array marker to a cell

//You may also place this Smart Marker into a template file manually using Excel and then open this file via WorkbookDesigner 

sheet.getCells().get("A1").putValue("&=$VariableArray");

//Set the data source for the marker(s)

report.setDataSource("VariableArray", new String[]{ "English", "Arabic", "Hindi", "Urdu", "French" });

//Set the CallBack property

report.setCallBack(new SmartMarkerCallBack(report.getWorkbook()));

//Process the markers

report.process(false);

{{< /highlight >}}
### **メソッド Chart.toPdf が追加されました**
Aspose.Cells for Java 8.6.2 では、Chart シェイプを PDF 形式に直接レンダリングするために使用できる Chart.toPdf メソッドが公開されています。上記のメソッドは現在、結果のファイルをディスクに保存するためのファイル パスの場所として String 型のパラメーターを受け入れます。

以下は、簡単な使用シナリオです。

**Java**

{{< highlight "csharp" >}}

 //Load spreadsheet containing charts

Workbook workbook = new Workbook(inputFilePath);

//Access first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Access first chart inside the worksheet

Chart chart = worksheet.getCharts().get(0);

//Save the chart in PDF format

chart.toPdf(outputFilePath);

{{< /highlight >}}
### **メソッド Workbook.removeUnusedStyles が追加されました**
Aspose.Cells for Java 8.6.2 は Workbook.removeUnusedStyles メソッドを公開しました。[スタイルのプールからすべての未使用の Style オブジェクトを削除します](/cells/ja/java/remove-unused-styles-inside-the-workbook/). 

以下は、簡単な使用シナリオです。

**Java**

{{< highlight "csharp" >}}

 //Load spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Remove all unused styles from the template

workbook.removeUnusedStyles();

{{< /highlight >}}
### **プロパティ Cells.スタイルが追加されました**
Cells.Style プロパティを使用して、デフォルト スタイルを表すワークシートのスタイルにアクセスできます。

以下は、簡単な使用シナリオです。

**Java**

{{< highlight "csharp" >}}

 //Load a spreadsheet

Workbook book = new Workbook(inputFilePath);

//Access the default style of worksheet

Style style = book.getWorksheets().get(0).getCells().getStyle();

{{< /highlight >}}
### **GridWeb に追加されたイベント**
Aspose.Cells.GridWeb for Java 8.6.2 では、次の 2 つの新しいイベントが公開されました。

1. AjaxCallFinished: コントロールの AJAX 更新が完了したときに発生します。 (EnableAJAX を true に設定する必要があります)。
1. CellModifiedOnAjax: AJAX 呼び出しでセルが変更されたときに発生します。

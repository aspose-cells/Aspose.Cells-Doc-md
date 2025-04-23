---
title: Aspose.Cells 8.6.2の公開API変更
type: docs
weight: 210
url: /ja/net/public-api-changes-in-aspose-cells-8-6-2/
---

{{% alert color="primary" %}} 

このドキュメントでは、Aspose.Cells APIの8.6.1から8.6.2への変更について記載されています。これはモジュール/アプリケーション開発者に関心がある可能性のある新しいおよび更新された公開メソッド、追加されたクラスだけでなく、Aspose.Cellsの内部の動作に関する変更の説明も含まれています。

{{% /alert %}} 
## **APIの追加**
### **Smart Markersのコールバックのサポート**
このリリースのAspose.Cells for .NET APIは、WorkbookDesigner.CallBackプロパティとISmartMarkerCallBackインタフェースを公開し、セルの参照やスマートマーカーの処理に関する通知を取得できるようにします。次のコード例は、ISmartMarkerCallBackインタフェースを使用して、新しいクラスを定義し、WorkbookDesigner.Processメソッドのコールバックを処理する方法を示しています。

**C#**

{{< highlight csharp >}}

 class SmartMarkerCallBack : ISmartMarkerCallBack

{

    Workbook workbook;

    internal SmartMarkerCallBack(Workbook workbook)

    {

        this.workbook = workbook;

    }

    public void Process(int sheetIndex, int rowIndex, int colIndex, string tableName, string columnName)

    {

        Console.WriteLine("Processing Cell : " + workbook.Worksheets[sheetIndex].Name + "!" + CellsHelper.CellIndexToName(rowIndex, colIndex));

        Console.WriteLine("Processing Marker : " + tableName + "." + columnName);

    }

}

{{< /highlight >}}



プロセスの残りの部分には、WorkbookDesigner を使用してスマートマーカーを含むデザイナースプレッドシートをロードし、データソースを設定して処理するという操作が含まれます。ただし、通知を有効にするためには、WorkbookDesigner.Process メソッドを呼び出す前に WorkbookDesigner.CallBack プロパティを設定する必要があります。

**C#**

{{< highlight csharp >}}

 //Loading the designer spreadsheet in an instance of Workbook

Workbook workbook = new Workbook(inputFilePath);

//Loading the instance of Workbook in an instance of WorkbookDesigner

WorkbookDesigner designer = new WorkbookDesigner(workbook);

//Set the WorkbookDesigner.CallBack property to an instance of newly created class

designer.CallBack = new SmartMarkerCallBack(workbook);

//Set the data source 

designer.SetDataSource(table);

//Process the Smart Markers in the designer spreadsheet

designer.Process(false);

{{< /highlight >}}


### **Chart.ToPdf メソッドを追加**
Aspose.Cells for .NET 8.6.2ではChart.ToPdfメソッドが公開され、[Chart形式を直接PDF形式に変換する](/cells/ja/net/convert-an-excel-chart-to-image/)ことができます。このメソッドは現在、結果のファイルをディスク上に保存するためのファイルパスの文字列型のパラメータを受け入れます。

以下はシンプルな使用シナリオです。

**C#**

{{< highlight csharp >}}

 //Load spreadsheet containing charts

Workbook workbook = new Workbook(inputFilePath);

//Access first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Access first chart inside the worksheet

Chart chart = worksheet.Charts[0];

//Save the chart in PDF format

chart.ToPdf(outputFilePath);

{{< /highlight >}}


### **Workbook.RemoveUnusedStyles メソッドを追加**
Aspose.Cells for .NET 8.6.2ではWorkbook.RemoveUnusedStylesメソッドが公開され、[使用されていないスタイルオブジェクトをワークブック内から削除する](/cells/ja/net/remove-unused-styles-inside-the-workbook/)ことができます。

以下はシンプルな使用シナリオです。

**C#**

{{< highlight csharp >}}

 //Load spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Remove all unused styles from the template

workbook.RemoveUnusedStyles();

{{< /highlight >}}


### **Cells.Styleプロパティの追加**
Cells.Styleプロパティは、デフォルトのスタイルを示すワークシートのスタイルにアクセスするために使用できます。

以下はシンプルな使用シナリオです。

**C#**

{{< highlight csharp >}}

 //Load a spreadsheet

Workbook book = new Workbook(inputFilePath);

//Access the default style of worksheet

Style style = book.Worksheets[0].Cells.Style;

{{< /highlight >}}


### **GridWebのためのイベントの追加**
Aspose.Cells.GridWeb for .NET 8.6.2 で次の 2 つの新しいイベントを公開しました。

1. AjaxCallFinished: コントロールの AJAX 更新が完了したときに発生します。（EnableAJAX は true に設定されている必要があります）。
1. CellModifiedOnAjax: セルがAJAX呼び出しで変更されたときに発生します。
{{< app/cells/assistant language="csharp" >}}

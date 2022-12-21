---
title: パブリック API Aspose.Cells の変更点 8.6.2
type: docs
weight: 210
url: /ja/net/public-api-changes-in-aspose-cells-8-6-2/
---
{{% alert color="primary" %}} 

このドキュメントでは、モジュール/アプリケーション開発者にとって興味深い、バージョン 8.6.1 から 8.6.2 への Aspose.Cells API への変更について説明します。新規および更新されたパブリック メソッド、追加されたクラスだけでなく、Aspose.Cells の舞台裏での動作の変更の説明も含まれています。

{{% /alert %}} 
## **追加された API**
### **スマートマーカーによるコールバックのサポート**
 Aspose.Cells for .NET API のこのリリースでは、WorkbookDesigner.CallBack プロパティと ISmartMarkerCallBack インターフェイスが公開されました。[処理中のセル参照および/またはスマート マーカーに関する通知を取得する](/cells/ja/net/getting-notifications-while-merging-data-with-smart-markers/).次のコードは、 ISmartMarkerCallBack インターフェイスを使用して WorkbookDesigner.Process メソッドのコールバックを処理する新しいクラスを定義する方法を示しています。

**C#**

{{< highlight "csharp" >}}

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



プロセスの残りの部分には、スマート マーカーを含むデザイナー スプレッドシートを WorkbookDesigner でロードし、データ ソースを設定して処理することが含まれます。ただし、通知を有効にするには、以下に示すように WorkbookDesigner.Process メソッドを呼び出す前に WorkbookDesigner.CallBack プロパティを設定する必要があります。

**C#**

{{< highlight "csharp" >}}

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


### **メソッド Chart.ToPdf が追加されました**
Aspose.Cells for .NET 8.6.2 は Chart.ToPdf メソッドを公開しました。[Chart シェイプを PDF 形式に直接レンダリングする](/cells/ja/net/convert-an-excel-chart-to-image/).上記のメソッドは現在、文字列型のパラメータをファイル パスの場所として受け入れ、結果のファイルをディスクに保存します。

以下は、簡単な使用シナリオです。

**C#**

{{< highlight "csharp" >}}

 //Load spreadsheet containing charts

Workbook workbook = new Workbook(inputFilePath);

//Access first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Access first chart inside the worksheet

Chart chart = worksheet.Charts[0];

//Save the chart in PDF format

chart.ToPdf(outputFilePath);

{{< /highlight >}}


### **メソッド Workbook.RemoveUnusedStyles が追加されました**
Aspose.Cells for .NET 8.6.2 は Workbook.RemoveUnusedStyles メソッドを公開しました。[スタイルのプールからすべての未使用の Style オブジェクトを削除します](/cells/ja/net/remove-unused-styles-inside-the-workbook/).

以下は、簡単な使用シナリオです。

**C#**

{{< highlight "csharp" >}}

 //Load spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Remove all unused styles from the template

workbook.RemoveUnusedStyles();

{{< /highlight >}}


### **プロパティ Cells.スタイルが追加されました**
Cells.Style プロパティを使用して、デフォルト スタイルを表すワークシートのスタイルにアクセスできます。

以下は、簡単な使用シナリオです。

**C#**

{{< highlight "csharp" >}}

 //Load a spreadsheet

Workbook book = new Workbook(inputFilePath);

//Access the default style of worksheet

Style style = book.Worksheets[0].Cells.Style;

{{< /highlight >}}


### **GridWeb に追加されたイベント**
Aspose.Cells.GridWeb for .NET 8.6.2 では、次の 2 つの新しいイベントが公開されました。

1. AjaxCallFinished: コントロールの AJAX 更新が完了したときに発生します。 (EnableAJAX は true に設定されます)。
1. CellModifiedOnAjax: AJAX 呼び出しでセルが変更されたときに発生します。

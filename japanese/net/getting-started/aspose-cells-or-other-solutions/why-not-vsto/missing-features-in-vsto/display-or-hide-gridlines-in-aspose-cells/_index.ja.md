---
title: Aspose.Cellsでグリッド線を表示または非表示にする
type: docs
weight: 50
url: /ja/net/display-or-hide-gridlines-in-aspose-cells/
---

{{% alert color="primary" %}}

すべてのExcelワークシートにはデフォルトでグリッド線があります。それらはセルを区別しやすくするために役立ちます。グリッド線によって、各セルが簡単に識別できるワークシートとして確認できます。

{{% /alert %}}

## **グリッド線の表示の制御**

Aspose.CellsはMicrosoft Excelファイルを表す[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)クラスを提供します。[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)クラスには[**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)コレクションが含まれており、Excelファイルの各ワークシートにアクセスできます。

ワークシートは[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラスで表されます。[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラスには、ワークシートを管理するための様々なプロパティとメソッドが提供されています。グリッド線の表示を制御するには、[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラスの[**IsGridlinesVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isgridlinesvisible)プロパティを使用します。[**IsGridlinesVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isgridlinesvisible)は**true**または**false**の値のみを格納できるブール値プロパティです。

下記は、Excelファイルの最初のワークシートのグリッド線を非表示にする[**IsGridlinesVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isgridlinesvisible)プロパティの使用を示す完全な例です。

以下のスクリーンショットでは、Book1.xlsファイルにはSheet1、Sheet2、Sheet3の3つのワークシートが含まれています。すべてのワークシートにはグリッド線があります。

**Book1.xls: 修正前のワークシートビュー** 

![todo:image_alt_text](display-or-hide-gridlines-in-aspose-cells_1.png)

Workbookクラスを使用してBook1.xlsファイルを開き、最初のワークシートのグリッド線を非表示にします。修正されたファイルはoutput.xlsとして保存されます。

**Output.xls: モディファイ後のワークシート** 

![todo:image_alt_text](display-or-hide-gridlines-in-aspose-cells_2.png)

**C#**

{{< highlight csharp >}}

 //Creating a file stream containing the Excel file to be opened

FileStream fstream = new FileStream("book1.xls", FileMode.Open);

//Instantiating a Workbook object

//Opening the Excel file through the file stream

Workbook workbook = new Workbook(fstream);

//Accessing the first worksheet in the Excel file

Worksheet worksheet = workbook.Worksheets[0];

//Hiding the gridlines of the first worksheet of the Excel file

worksheet.IsGridlinesVisible = false;

//Saving the modified Excel file

workbook.Save("output.xls");

//Closing the file stream to free all resources

fstream.Close();

{{< /highlight >}}

## **ランニングコードのダウンロード**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20VSTO%20Spreadsheets/Aspose.Cells%20Features%20missing%20in%20VSTO/Display%20or%20Hide%20Gridlines)

## **サンプルコードをダウンロード**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesAsposeCellsForVSTO1.1)
{{< app/cells/assistant language="csharp" >}}

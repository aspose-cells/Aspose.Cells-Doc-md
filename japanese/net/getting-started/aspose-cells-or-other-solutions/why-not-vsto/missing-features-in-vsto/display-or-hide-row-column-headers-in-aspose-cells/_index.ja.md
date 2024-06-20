---
title: Aspose.Cellsで行列ヘッダーの表示または非表示を制御する
type: docs
weight: 60
url: /ja/net/display-or-hide-row-column-headers-in-aspose-cells/
---

{{% alert color="primary" %}}

Excelファイルのすべてのワークシートは、行と列に配置されたセルで構成されています。すべての行と列には、それぞれ固有の値があり、それを使用して識別し、個々のセルを識別します。たとえば、行は1、2、3、4などと番号がつけられ、列はA、B、C、Dなどとアルファベット順に並べられます。行と列の値はヘッダーに表示されます。Aspose.Cellsを使用すると、開発者はこれらの行と列のヘッダーの表示を制御できます。

{{% /alert %}}

## **ワークシートの表示を制御する**

Aspose.Cellsは、Microsoft Excelファイルを表す[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)クラスを提供します。[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)クラスには、Excelファイルの各ワークシートへのアクセスを可能にする[**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)コレクションが含まれています。

ワークシートは[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラスによって表されます。[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラスは、ワークシートの管理に幅広いプロパティとメソッドを提供します。行と列のヘッダーの表示を制御するには、[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)クラスの[**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isrowcolumnheadersvisible)プロパティを使用します。[**IsRowColumnHeadersVisible**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/isrowcolumnheadersvisible)はブール値のプロパティであり、**true**または**false**の値のみを格納できます。

以下に示す完全な例は、ファイルの最初のワークシートで行と列のヘッダーを非表示にする方法を示しています。

スクリーンショットはBook1.xls、入力ファイルを示しています。Sheet1、Sheet2、Sheet3の3つのワークシートが含まれています。それぞれのワークシートには、行と列のヘッダーが表示されています。

**Book1.xls: 修正前のワークシート**

![todo:image_alt_text](display-or-hide-row-column-headers-in-aspose-cells_1.png)

Book1.xlsはWorkbookクラスのOpenメソッドを呼び出すことで開かれ、最初のワークシートの行と列のヘッダーが非表示になります。変更されたファイルはoutput.xlsとして保存されます。

**Output.xls: モディファイ後のワークシート** 

![todo:image_alt_text](display-or-hide-row-column-headers-in-aspose-cells_2.png)

**C#**

{{< highlight csharp >}}

 //Creating a file stream containing the Excel file to be opened

FileStream fstream = new FileStream("book1.xls", FileMode.Open);

//Instantiating a Workbook object

//Opening the Excel file through the file stream

Workbook workbook = new Workbook(fstream);

//Accessing the first worksheet in the Excel file

Worksheet worksheet = workbook.Worksheets[0];

//Hiding the headers of rows and columns

worksheet.IsRowColumnHeadersVisible = false;

//Saving the modified Excel file

workbook.Save("output.xls");

//Closing the file stream to free all resources

fstream.Close();

{{< /highlight >}}

## **ランニングコードのダウンロード**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20VSTO%20Spreadsheets/Aspose.Cells%20Features%20missing%20in%20VSTO/Display%20or%20Hide%20Row%20Column%20Headers)

## **サンプルコードをダウンロード**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesAsposeCellsForVSTO1.1)

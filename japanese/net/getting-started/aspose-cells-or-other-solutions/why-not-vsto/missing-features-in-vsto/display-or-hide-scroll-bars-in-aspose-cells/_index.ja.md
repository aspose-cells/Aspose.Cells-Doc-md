---
title: Aspose.Cellsでのスクロールバーの表示または非表示
type: docs
weight: 70
url: /ja/net/display-or-hide-scroll-bars-in-aspose-cells/
---

{{% alert color="primary" %}}

スクロールバーは、ファイルの内容を移動するために非常によく使用されます。通常、次の2種類のスクロールバーがあります。

- 垂直スクロールバー
- 水平スクロールバー

Microsoft Excelは、ユーザーがワークシートの内容をスクロールできるように、水平および垂直のスクロールバーを提供しています。Aspose.Cellsを使用すると、Excelファイルの両方のタイプのスクロールバーの表示/非表示を制御することができます。

{{% /alert %}}

Aspose.Cellsは、Excelファイルを表す[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)クラスを提供します。[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)クラスは、Excelファイルの管理に幅広いプロパティとメソッドを提供します。スクロールバーの表示を制御するには、[**WorkbookSettings**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings)クラスの[**IsVScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/isvscrollbarvisible)および[**IsHScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/ishscrollbarvisible)プロパティを使用します。[**IsVScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/isvscrollbarvisible)と[**IsHScrollBarVisible**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/ishscrollbarvisible)はブール値のプロパティであり、これらのプロパティは**true**または**false**の値のみを格納できます。

以下は、Excelファイル（book1.xls）を開き、両方のスクロールバーを非表示にして変更したファイルをoutput.xlsとして保存する完全なコードです。

下のスクリーンショットは、スクロールバーが含まれているBook1.xlsファイルを示しています。変更されたファイルはoutput.xlsファイルとして保存され、下にも表示されています。

**Book1.xls: 修正前のExcelファイル**

![todo:image_alt_text](display-or-hide-scroll-bars-in-aspose-cells_1.png)

**output.xls: 修正後のExcelファイル**

![todo:image_alt_text](display-or-hide-scroll-bars-in-aspose-cells_2.png)

**C#**

{{< highlight csharp >}}

 //Creating a file stream containing the Excel file to be opened

FileStream fstream = new FileStream("book1.xls", FileMode.Open);

//Instantiating a Workbook object

//Opening the Excel file through the file stream

Workbook workbook = new Workbook(fstream);

//Hiding the vertical scroll bar of the Excel file

workbook.Settings.IsVScrollBarVisible = false;

//Hiding the horizontal scroll bar of the Excel file

workbook.Settings.IsHScrollBarVisible = false;

//Saving the modified Excel file

workbook.Save("output.xls");

//Closing the file stream to free all resources

fstream.Close();

{{< /highlight >}}

## **ランニングコードのダウンロード**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20VSTO%20Spreadsheets/Aspose.Cells%20Features%20missing%20in%20VSTO/Display%20or%20Hide%20Scroll%20Bars)

## **サンプルコードをダウンロード**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesAsposeCellsForVSTO1.1)
{{< app/cells/assistant language="csharp" >}}

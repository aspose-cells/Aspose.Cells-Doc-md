---
title: xlsx4jでのワークブックのスクロールバーの表示および非表示
type: docs
weight: 30
url: /ja/java/display-and-hide-scrollbars-of-workbooks-in-xlsx4j/
---

## **Aspose.Cells - ワークブックのスクロールバーの表示および非表示**
Aspose.Cellsでは、Excelファイルを表す **Workbook** クラスが提供されています。 **Workbook** クラスには、Excelファイルを管理するためのさまざまなプロパティとメソッドが提供されています。ただし、Excelファイル内のスクロールバーの表示を制御するには、 **Workbook** クラスの **setVScrollBarVisible** および **setHScrollBarVisible** メソッドを使用することができます。

**Java**

{{< highlight java >}}

 //Instantiating a Excel object by excel file path

Workbook workbook = new Workbook(dataDir + "book1.xls");

//Hiding the vertical scroll bar of the Excel file

workbook.getSettings().setVScrollBarVisible(false);

//Hiding the horizontal scroll bar of the Excel file

workbook.getSettings().setHScrollBarVisible(false);

//Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(dataDir + "AsposeSrollbarsHide.xls");

// ===============================================================

//Displaying the vertical scroll bar of the Excel file

workbook.getSettings().setVScrollBarVisible(true);

//Displaying the horizontal scroll bar of the Excel file

workbook.getSettings().setHScrollBarVisible(true);

//Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(dataDir + "AsposeDisplaySrollbars.xls");


{{< /highlight >}}
## **ランニングコードのダウンロード**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Xlsx4j-v1.0.0)
## **サンプルコードをダウンロード**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/asposefeatures/worksheets/displayandhidescrollbars/AsposeDisplayAndHideScrollbars.java)

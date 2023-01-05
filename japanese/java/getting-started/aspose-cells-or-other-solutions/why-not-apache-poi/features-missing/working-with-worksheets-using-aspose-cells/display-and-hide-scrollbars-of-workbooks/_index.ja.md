---
title: ワークブックのスクロールバーの表示と非表示
type: docs
weight: 40
url: /ja/java/display-and-hide-scrollbars-of-workbooks/
---
## **Aspose.Cells - ワークブックのスクロールバーの表示と非表示**
Aspose.Cells はクラスを提供し、**ワークブック**これは Excel ファイルを表します。**ワークブック**クラスには、Excel ファイルを管理するためのさまざまなプロパティとメソッドが用意されています。ただし、Excel ファイルのスクロール バーの表示を制御するために、開発者は**setVScrollBarVisible** & **setHScrollBarVisible**のメソッド**ワークブック**クラス。

**Java**

{{< highlight "java" >}}

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
## **実行中のコードをダウンロード**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **サンプルコードをダウンロード**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/worksheets/AsposeDisplayAndHideScrollbars.java)

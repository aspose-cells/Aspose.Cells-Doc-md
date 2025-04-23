---
title: Aspose.Cells を使用してワークブックのタブの表示および非表示を制御
type: docs
weight: 50
url: /ja/java/display-and-hide-tabs-of-workbook-using-aspose-cells/
---

## **Aspose.Cells - ワークブックのタブの表示および非表示**
Aspose.Cellsでは、Microsoft Excelファイルを表す **Workbook** クラスが提供されています。 **Workbook** クラスには、Excelファイルを管理するためのさまざまなプロパティとメソッドが提供されています。Excelファイル内のタブの表示を制御するために、開発者は **Workbook** クラスの **setShowTabs** メソッドを使用することができます。

**Java**

{{< highlight java >}}

 //Instantiating a Workbook object by excel file path

Workbook workbook = new Workbook(dataDir + "book1.xls");

//Hiding the tabs of the Excel file

workbook.getSettings().setShowTabs(false);

//Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(dataDir + "AsposeHideTabs.xls");

// ===============================================================

//Displaying the tabs of the Excel file

workbook.getSettings().setShowTabs(true);

//Saving the modified Excel file in default (that is Excel 2003) format

workbook.save(dataDir + "AsposeDisplayTabs.xls");

{{< /highlight >}}
## **ランニングコードのダウンロード**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **サンプルコードをダウンロード**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/worksheets/AsposeDisplayAndHideTabs.java)

{{< app/cells/assistant language="java" >}}

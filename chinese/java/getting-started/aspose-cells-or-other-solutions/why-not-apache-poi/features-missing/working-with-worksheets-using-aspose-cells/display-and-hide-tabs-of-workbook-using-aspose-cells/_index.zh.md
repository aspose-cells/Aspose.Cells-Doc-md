---
title: 显示和隐藏工作簿的选项卡
type: docs
weight: 50
url: /zh/java/display-and-hide-tabs-of-workbook-using-aspose-cells/
---

## **Aspose.Cells - 显示和隐藏工作簿的选项卡**
Aspose.Cells提供了一个代表Microsoft Excel文件的Workbook类。Workbook类提供了广泛的属性和方法来管理Excel文件。为了控制Excel文件中选项卡的可见性，开发人员可以使用Workbook类的**setShowTabs**方法。

Java

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
## **下载运行代码**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **下载示例代码**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/worksheets/AsposeDisplayAndHideTabs.java)


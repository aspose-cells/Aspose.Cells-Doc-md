---
title: 在 xlsx4j 中显示和隐藏工作簿的选项卡
type: docs
weight: 40
url: /zh/java/display-and-hide-tabs-of-workbook-in-xlsx4j/
---
## **Aspose.Cells - 工作簿的显示和隐藏选项卡**
Aspose.Cells 提供了一个类 Workbook，它表示一个 Microsoft Excel 文件。 Workbook 类提供了广泛的属性和方法来管理 Excel 文件。要控制 Excel 文件中选项卡的可见性，开发人员可以使用 Workbook 类的 setShowTabs 方法。

**Java**

{{< highlight "java" >}}

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
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Xlsx4j-v1.0.0)
## **下载示例代码**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/asposefeatures/worksheets/displayandhidetabs/AsposeDisplayAndHideTabs.java)

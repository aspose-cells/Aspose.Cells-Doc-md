---
title: 在 Apache POI 和 Aspose.Cells 中冻结窗格
type: docs
weight: 80
url: /zh/java/freeze-panes-in-apache-poi-and-aspose-cells/
---
## **Aspose.Cells - 冻结窗格**
Aspose.Cells提供了一个类，[工作簿](http://docs.aspose.com:8082/docs/display/cellsjava/Workbook)表示 Microsoft Excel 文件。 Workbook 类包含一个 WorksheetCollection，它允许访问 Excel 文件中的每个工作表。

工作表由[工作表](http://docs.aspose.com:8082/docs/display/cellsjava/Worksheet)班级。 Worksheet 类提供了广泛的属性和方法来管理工作表。要配置冻结窗格，请调用 Worksheet 类的 freezePanes 方法。 FreezePanes 方法采用以下参数：

- **排**，冻结将从其开始的单元格的行索引。
- **柱子**，冻结将从其开始的单元格的列索引。
- **冻结行**，顶部窗格中可见行的数量。
- **冻结列**左窗格中可见列的数量

**Java**

{{< highlight "java" >}}

 worksheet1.freezePanes(0,2,0,2); // Freezing Columns

worksheet2.freezePanes(2,0,2,0); // Freezing Rows

{{< /highlight >}}
## **Apache POI SS - HSSF XSSF - 冻结窗格**
sheet.createFreezePane 可用于在使用 Apache POI SS - HSSF 和 XSSF 时实现 FreezePane 功能

**Java**

{{< highlight "java" >}}

 // Freeze just one row

sheet1.createFreezePane( 0, 2, 0, 2 );

// Freeze just one column

sheet2.createFreezePane( 2, 0, 2, 0 );

// Freeze the columns and rows (forget about scrolling position of the lower right quadrant).

sheet3.createFreezePane( 2, 2 );

{{< /highlight >}}
## **下载运行代码**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **下载示例代码**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/cellsrowscolumns/freezepanes)

{{% alert color="primary" %}} 

欲了解更多详情，请访问[冻结窗格](http://docs.aspose.com:8082/docs/display/cellsjava/Freeze+Panes).

{{% /alert %}}

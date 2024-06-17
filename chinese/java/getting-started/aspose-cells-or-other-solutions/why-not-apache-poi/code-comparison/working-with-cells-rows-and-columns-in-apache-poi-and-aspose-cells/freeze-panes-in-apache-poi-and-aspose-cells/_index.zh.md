---
title: Apache POI和Aspose.Cells中的冻结窗格
type: docs
weight: 80
url: /zh/java/freeze-panes-in-apache-poi-and-aspose-cells/
---

## **Aspose.Cells - 冻结窗格**
Aspose.Cells提供了一个代表Microsoft Excel文件的类[Workbook](http://docs.aspose.com:8082/docs/display/cellsjava/Workbook)，Workbook类包含一个WorksheetCollection，允许访问Excel文件中的每个工作表。

工作表由[Worksheet](http://docs.aspose.com:8082/docs/display/cellsjava/Worksheet)类表示。Worksheet类提供了广泛的属性和方法来管理工作表。要配置冻结窗格，请调用Worksheet类的freezePanes方法。因此，FreezePanes方法接受以下参数：

- **行**，冻结将从该行开始。
- **列**，冻结将从该列开始。
- **冻结行**，顶部窗格中可见的行数。
- **冻结列**，左侧窗格中可见的列数

**Java**

{{< highlight java >}}

 worksheet1.freezePanes(0,2,0,2); // Freezing Columns

worksheet2.freezePanes(2,0,2,0); // Freezing Rows

{{< /highlight >}}
## **Apache POI SS - HSSF XSSF - 冻结窗格**
sheet.createFreezePane可实现使用Apache POI SS - HSSF和XSSF时的冻结窗格功能

**Java**

{{< highlight java >}}

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

查看更多详情，请访问[冻结窗格](http://docs.aspose.com:8082/docs/display/cellsjava/Freeze+Panes)

{{% /alert %}}

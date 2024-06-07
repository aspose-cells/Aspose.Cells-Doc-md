---
title: 在 Apache POI 和 Aspose.Cells 中冻结窗格
type: docs
weight: 80
url: /zh/java/freeze-panes-in-apache-poi-and-aspose-cells/
---

## **Aspose.Cells - 冻结窗格**
Aspose.Cells提供了一个名为 [Workbook](http://docs.aspose.com:8082/docs/display/cellsjava/Workbook) 的类，代表Microsoft Excel文件。Workbook 类包含一个WorksheetCollection，允许访问Excel文件中的每个工作表。

工作表由 [Worksheet](http://docs.aspose.com:8082/docs/display/cellsjava/Worksheet) 类表示。Worksheet 类提供了广泛的属性和方法来管理工作表。要配置冻结窗格，请调用Worksheet 类的 freezePanes 方法。 FreePanes 方法接受以下参数:

- **行**，冻结将从该行开始的单元格的行索引。
- **列**，冻结将从该列开始的单元格的列索引。
- **冻结行**，顶部窗格中可见行数。
- **冻结列**，左侧窗格中可见列数

**Java**

{{< highlight java >}}

 worksheet1.freezePanes(0,2,0,2); // Freezing Columns

worksheet2.freezePanes(2,0,2,0); // Freezing Rows

{{< /highlight >}}
## **Apache POI SS - HSSF XSSF - 冻结窗格**
sheet.createFreezePane 可用于在使用 Apache POI SS - HSSF 和 XSSF 时实现冻结窗格功能

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

要了解更多详细信息，请访问[冻结窗格](http://docs.aspose.com:8082/docs/display/cellsjava/Freeze+Panes)。

{{% /alert %}}

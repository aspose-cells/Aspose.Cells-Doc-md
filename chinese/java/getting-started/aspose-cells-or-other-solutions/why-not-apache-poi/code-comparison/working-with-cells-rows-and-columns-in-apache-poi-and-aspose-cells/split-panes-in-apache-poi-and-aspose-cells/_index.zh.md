---
title: Apache POI 和 Aspose.Cells 中的拆分窗格
type: docs
weight: 70
url: /zh/java/split-panes-in-apache-poi-and-aspose-cells/
---
## **Aspose.Cells - 拆分窗格**
Aspose.Cells 提供了一个类 Workbook，代表一个 Microsoft Excel 文件。 Workbook 类提供了广泛的属性和方法来管理 Excel 文件。要实现拆分视图，请使用 Worksheet 类的拆分方法。要删除拆分窗格，请使用 removeSplit 方法。

**Java**

{{< highlight "java" >}}

 //Instantiate a new workbook / Open a template file

Workbook book = new Workbook(dataDir + "workbook.xls");

//Set the active cell

book.getWorksheets().get(0).setActiveCell("A20");

//Split the worksheet window

book.getWorksheets().get(0).split();

{{< /highlight >}}
## **Apache POI SS - HSSF 和 XSSF - 拆分窗格**
使用 Apache POI SS（HSSF 和 XSSF）时，可以通过 createSplitPane 方法实现拆分窗格功能 API

**Java**

{{< highlight "java" >}}

 Workbook wb = new XSSFWorkbook();

Sheet sheet = wb.createSheet("new sheet");

// Create a split with the lower left side being the active quadrant

sheet.createSplitPane(2000, 2000, 0, 0, Sheet.PANE_LOWER_LEFT);

{{< /highlight >}}
## **下载运行代码**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **下载示例代码**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/cellsrowscolumns/splitpanes)

{{% alert color="primary" %}} 

欲了解更多详情，请访问[拆分窗格](http://docs.aspose.com:8082/docs/display/cellsjava/Split+Panes).

{{% /alert %}}

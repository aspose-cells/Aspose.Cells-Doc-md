---
title: 在Apache POI和Aspose.Cells中分割窗格
type: docs
weight: 70
url: /zh/java/split-panes-in-apache-poi-and-aspose-cells/
---

## **Aspose.Cells - 分割窗格**
Aspose.Cells提供了一个表示Microsoft Excel文件的Workbook类。Workbook类提供了许多用于管理Excel文件的属性和方法。要实现分割视图，请使用Worksheet类的split方法。要删除分割窗格，请使用removeSplit方法。

**Java**

{{< highlight java >}}

 //Instantiate a new workbook / Open a template file

Workbook book = new Workbook(dataDir + "workbook.xls");

//Set the active cell

book.getWorksheets().get(0).setActiveCell("A20");

//Split the worksheet window

book.getWorksheets().get(0).split();

{{< /highlight >}}
## **Apache POI SS - HSSF和XSSF - 分割窗格**
在使用Apache POI SS（HSSF和XSSF）API时，可以通过createSplitPane方法实现分割窗格功能

**Java**

{{< highlight java >}}

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

有关更多详细信息，请访问[Split Panes](http://docs.aspose.com:8082/docs/display/cellsjava/Split+Panes)。

{{% /alert %}}

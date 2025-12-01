---
title: Split Panes in Apache POI and Aspose.Cells
type: docs
weight: 70
url: /java/split-panes-in-apache-poi-and-aspose-cells/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Aspose.Cells - Split Panes**
Aspose.Cells provides a class, Workbook that represents a Microsoft Excel file. The Workbook class provides a wide range of properties and methods for managing Excel files. To implement split views, use the Worksheet class' split method. To remove split panes, use the removeSplit method.

**Java**

{{< highlight java >}}

 //Instantiate a new workbook / Open a template file

Workbook book = new Workbook(dataDir + "workbook.xls");

//Set the active cell

book.getWorksheets().get(0).setActiveCell("A20");

//Split the worksheet window

book.getWorksheets().get(0).split();

{{< /highlight >}}
## **Apache POI SS - HSSF & XSSF - Split Panes**
Split Panes functionality can be achieved by createSplitPane method while using Apache POI SS (HSSF & XSSF) API

**Java**

{{< highlight java >}}

 Workbook wb = new XSSFWorkbook();

Sheet sheet = wb.createSheet("new sheet");

// Create a split with the lower left side being the active quadrant

sheet.createSplitPane(2000, 2000, 0, 0, Sheet.PANE_LOWER_LEFT);

{{< /highlight >}}
## **Download Running Code**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Download Sample Code**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/cellsrowscolumns/splitpanes)

{{% alert color="primary" %}} 

For more details, visit [Split Panes](http://docs.aspose.com:8082/docs/display/cellsjava/Split+Panes).

{{% /alert %}}

---
title: 在工作簿中复制工作表
type: docs
weight: 40
url: /zh/java/copy-sheet-within-workbook/
---
## **Microsoft Excel - 在工作簿中移动或复制工作表**
以下是在工作簿内或工作簿之间复制和移动工作表所涉及的步骤。

1. 要在工作簿内或工作簿之间移动或复制工作表，请打开将接收工作表的工作簿。
1. 切换到包含要移动或复制的工作表的工作簿，然后选择工作表。
1. 在**编辑**菜单，点击**移动或复制工作表**.
1. 在“到书”框中，单击要接收工作表的工作簿。
1. 要将所选工作表移动或复制到新工作簿，请单击**新书**.
1. 在里面**片前**框，单击要在其前插入移动或复制的工作表的工作表。
1. 要复制工作表而不是移动它们，请选择**创建副本**复选框。
## **Aspose.Cells - 在工作簿中复制工作表**
{{% alert color="primary" %}} 

Aspose.Cells 提供了一个重载方法，WorksheetCollection.addCopy()，用于将工作表添加到集合并从现有工作表复制数据。该方法的一个版本将源工作表的索引作为参数。另一个版本采用源工作表的名称。

以下示例显示如何复制工作簿中的现有工作表。

{{% /alert %}} 

使用 Aspose.Cells 复制工作表

**Java**

{{< highlight "java" >}}

 //Create a new Workbook by excel file path

Workbook wb = new Workbook(dataDir + "workbook.xls");

//Create a Worksheets object with reference to the sheets of the Workbook.

WorksheetCollection sheets = wb.getWorksheets();

//Copy data to a new sheet from an existing sheet within the Workbook.

sheets.addCopy("Sheet1");

{{< /highlight >}}
## **Apache POI SS - 工作簿中的复制表**
{{% alert color="primary" %}} 

Workbook.cloneSheet() 用于复制带有工作簿的工作表。

{{% /alert %}} 

使用 Apache POI SS 复制表格

**Java**

{{< highlight "java" >}}

 Workbook wb = new HSSFWorkbook();

wb.createSheet("new sheet");

wb.createSheet("second sheet");

Sheet cloneSheet = wb.cloneSheet(0);

{{< /highlight >}}
## **下载运行代码**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **下载示例代码**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/worksheets/copysheetwithinworkbook)

{{% alert color="primary" %}} 

欲了解更多详情，请访问[复制和移动工作表](/cells/zh/java/copying-and-moving-worksheets).

{{% /alert %}}

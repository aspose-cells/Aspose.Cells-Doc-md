---
title: 在工作簿内复制工作表
type: docs
weight: 40
url: /zh/java/copy-sheet-within-workbook/
---

## **Microsoft Excel - 在工作簿内移动或复制工作表**
以下是在工作簿内或在工作簿之间复制和移动工作表的步骤

1. 要在工作簿内或在工作簿之间移动或复制工作表，请打开将接收工作表的工作簿
1. 切换到包含要移动或复制的工作表的工作簿，然后选择这些工作表。
1. 在**编辑**菜单上，单击**移动或复制工作表**。
1. 在目标工作簿框中，单击要接收工作表的工作簿
1. 要将选定的工作表移动或复制到新工作簿，请单击 **新建工作簿**
1. 在**工作表之前**框中，单击要插入已移动或复制的工作表之前的工作表。
1. 要复制工作表而不是移动它们，请选中 **创建副本** 复选框
## **Aspose.Cells - 在工作簿内复制工作表**
{{% alert color="primary" %}} 

Aspose.Cells提供了一种重载的方法，WorksheetCollection.addCopy()，用于将工作表添加到集合中并从现有工作表复制数据。该方法的一个版本将源工作表的索引作为参数。另一个版本将源工作表的名称作为参数。

以下示例显示如何在工作簿内复制现有工作表。

{{% /alert %}} 

使用Aspose.Cells复制工作表

**Java**

{{< highlight java >}}

 //Create a new Workbook by excel file path

Workbook wb = new Workbook(dataDir + "workbook.xls");

//Create a Worksheets object with reference to the sheets of the Workbook.

WorksheetCollection sheets = wb.getWorksheets();

//Copy data to a new sheet from an existing sheet within the Workbook.

sheets.addCopy("Sheet1");

{{< /highlight >}}
## **Apache POI SS - 复制工作簿内工作表**
{{% alert color="primary" %}} 

Workbook.cloneSheet() 用于在工作簿内复制工作表。

{{% /alert %}} 

使用 Apache POI SS 复制工作表

**Java**

{{< highlight java >}}

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

有关更多详细信息，请访问[复制和移动工作表](/cells/zh/java/copying-and-moving-worksheets)。

{{% /alert %}}

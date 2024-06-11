---
title: 设置打印标题
type: docs
weight: 30
url: /zh/net/set-print-titles/
---

## **Aspose.Cells - 设置打印标题**
Aspose.Cells允许您指定要在打印的工作表的所有页面上重复显示的行和列标题。要这样做，使用 [PageSetup](https://reference.aspose.com/cells/net/aspose.cells/pagesetup) 类的PrintTitleColumns和PrintTitleRows属性。

要重复显示的行或列是通过传递它们的行号或列号来定义的。例如，行被定义为 $1:$2，列被定义为 $A:$B。

**C#**

{{< highlight cs >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook("../../data/test.xlsx");

//Obtaining the reference of the PageSetup of the worksheet

PageSetup pageSetup = workbook.Worksheets[0].PageSetup;

//Defining column numbers A & B as title columns

pageSetup.PrintTitleColumns = "$A:$B";

//Defining row numbers 1 & 2 as title rows

pageSetup.PrintTitleRows= "$1:$2";

{{< /highlight >}}
## **下载运行代码**
从以下所列的社交编码站点下载**设置打印标题** 表单:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/AsposeCellsFeaturesMissinginNPOI_v1.0/Set.Print.Titles.Aspose.Cells.zip)

{{% alert color="primary" %}} 

要了解更多详细信息，请访问[设置打印选项](/cells/zh/net/setting-print-options/)。

{{% /alert %}}

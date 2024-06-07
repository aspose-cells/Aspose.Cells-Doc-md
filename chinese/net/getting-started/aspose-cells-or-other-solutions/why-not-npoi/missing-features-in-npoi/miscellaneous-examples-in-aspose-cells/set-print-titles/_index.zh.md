---
title: 设置打印标题
type: docs
weight: 30
url: /zh/net/set-print-titles/
---

## **Aspose.Cells - 设置打印标题**
Aspose.Cells允许您指定行和列标题以在打印的工作表的所有页面上重复。要这样做，请使用 [PageSetup](https://reference.aspose.com/cells/net/aspose.cells/pagesetup) 类的PrintTitleColumns 和PrintTitleRows 属性。

将重复的行或列由其行号或列号传递定义。例如，行定义为$1:$2，列定义为$A:$B。

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
从以下提到的任何社交编码网站下载**设置打印标题**：

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/AsposeCellsFeaturesMissinginNPOI_v1.0/Set.Print.Titles.Aspose.Cells.zip)

{{% alert color="primary" %}} 

有关更多详细信息，请访问[设置打印选项](/cells/zh/net/setting-print-options/)。

{{% /alert %}}

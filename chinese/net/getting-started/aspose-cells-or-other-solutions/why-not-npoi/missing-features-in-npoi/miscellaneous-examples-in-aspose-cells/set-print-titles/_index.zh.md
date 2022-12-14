---
title: 设置打印标题
type: docs
weight: 30
url: /zh/net/set-print-titles/
---
## **Aspose.Cells - 设置打印标题**
Aspose.Cells 允许您指定行和列标题以在打印的工作表的所有页面上重复。为此，请使用[页面设置](https://reference.aspose.com/cells/net/aspose.cells/pagesetup)类 PrintTitleColumns 和 PrintTitleRows 属性。

将重复的行或列通过传递它们的行号或列号来定义。例如，行定义为 $1:$2，列定义为 $A:$B。

**C#**

{{< highlight "cs" >}}

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
下载**设置打印标题**形成以下任何一个社交编码网站：

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/AsposeCellsFeaturesMissinginNPOI_v1.0/Set.Print.Titles.Aspose.Cells.zip)

{{% alert color="primary" %}} 

欲了解更多详情，请访问[设置打印选项](/cells/zh/net/setting-print-options/).

{{% /alert %}}

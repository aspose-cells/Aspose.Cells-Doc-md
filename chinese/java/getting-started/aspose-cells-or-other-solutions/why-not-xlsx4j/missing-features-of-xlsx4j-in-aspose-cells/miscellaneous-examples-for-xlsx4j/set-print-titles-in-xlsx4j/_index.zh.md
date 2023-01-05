---
title: 在 xlsx4j 中设置打印标题
type: docs
weight: 40
url: /zh/java/set-print-titles-in-xlsx4j/
---
## **Aspose.Cells - 设置打印标题**
Aspose.Cells 允许您指定行和列标题以在打印的工作表的所有页面上重复。为此，请使用[页面设置](/java/PageSetup)类的 setPrintTitleColumns 和 setPrintTitleRows 属性。

将重复的行或列通过传递它们的行号或列号来定义。例如，行定义为 $1:$2，列定义为 $A:$B。

**Java**

{{< highlight "java" >}}

 //Obtaining the reference of the PageSetup of the worksheet

PageSetup pageSetup = sheet.getPageSetup();

//Defining column numbers A & B as title columns

pageSetup.setPrintTitleColumns("$A:$B");

//Defining row numbers 1 & 2 as title rows

pageSetup.setPrintTitleRows("$1:$2");

{{< /highlight >}}
## **下载运行代码**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Xlsx4j-v1.0.0)
## **下载示例代码**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/asposefeatures/print/setprinttitles/AsposeSetPrintTitles.java)

{{% alert color="primary" %}} 

欲了解更多详情，请访问[设置打印选项](/cells/zh/java/page-setup-features/#setting-print-options).

{{% /alert %}}

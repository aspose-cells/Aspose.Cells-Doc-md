---
title: 设置打印标题
type: docs
weight: 10
url: /zh/java/set-print-titles/
---

## **Aspose.Cells - 设置打印标题**
Aspose.Cells允许您指定要在打印的工作表的所有页面上重复的行和列标题。为此，使用 [PageSetup](/java/pagesetup) 类的 setPrintTitleColumns 和 setPrintTitleRows 属性。

要重复显示的行或列是通过传递它们的行号或列号来定义的。例如，行被定义为 $1:$2，列被定义为 $A:$B。

Java

{{< highlight java >}}

 //Obtaining the reference of the PageSetup of the worksheet

PageSetup pageSetup = sheet.getPageSetup();

//Defining column numbers A & B as title columns

pageSetup.setPrintTitleColumns("$A:$B");

//Defining row numbers 1 & 2 as title rows

pageSetup.setPrintTitleRows("$1:$2");

{{< /highlight >}}
## **下载运行代码**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **下载示例代码**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/print/AsposePrintTitles.java)

{{% alert color="primary" %}} 

要了解更多详情，请访问[设置打印选项](/cells/zh/java/page-setup-features/#setting-print-options)。

{{% /alert %}}

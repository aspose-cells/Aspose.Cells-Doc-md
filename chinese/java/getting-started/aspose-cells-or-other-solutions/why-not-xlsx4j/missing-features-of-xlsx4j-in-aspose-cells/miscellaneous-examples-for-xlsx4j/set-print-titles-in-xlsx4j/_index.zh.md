---
title: 在xlsx4j中设置打印标题
type: docs
weight: 40
url: /zh/java/set-print-titles-in-xlsx4j/
---

## **Aspose.Cells - 设置打印标题**
Aspose.Cells允许您指定要在打印的工作表的所有页面上重复的行和列标题。为此，请使用[PageSetup](/java/PageSetup)类的setPrintTitleColumns和setPrintTitleRows属性。

要重复显示的行或列是通过传递它们的行号或列号来定义的。例如，行被定义为 $1:$2，列被定义为 $A:$B。

**Java**

{{< highlight java >}}

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

要了解更多详情，请访问[设置打印选项](/cells/zh/java/page-setup-features/#setting-print-options)。

{{% /alert %}}
{{< app/cells/assistant language="java" >}}

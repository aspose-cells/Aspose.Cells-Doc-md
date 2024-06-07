---
title: 设置打印标题
type: docs
weight: 10
url: /zh/java/set-print-titles/
---

## **Aspose.Cells - 设置打印标题**
Aspose.Cells允许您指定在打印工作表的所有页面上重复的行和列标题。要实现此目的，请使用[PageSetup](/java/pagesetup)类的setPrintTitleColumns和setPrintTitleRows属性。

将重复的行或列由其行号或列号传递定义。例如，行定义为$1:$2，列定义为$A:$B。

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

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **下载示例代码**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/print/AsposePrintTitles.java)

{{% alert color="primary" %}} 

如需更多详情，请访问[设置打印选项](/cells/zh/java/page-setup-features/#setting-print-options)。

{{% /alert %}}

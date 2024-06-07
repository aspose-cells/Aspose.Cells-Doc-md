---
title: 使用 Aspose.Cells for Java 与 ColdFusion
type: docs
weight: 40
url: /zh/java/using-aspose-cells-for-java-with-coldfusion/
---

{{% alert color="primary" %}}

本文提供了 ColdFusion 开发人员在其 ColdFusion 应用程序中使用 Aspose.Cells for Java 所需的基本信息和代码段。

本文展示了如何使用 ColdFusion 创建简单的网页，并使用 Aspose.Cells for Java 生成一个简单的 Excel 文件。

{{% /alert %}}

## **Aspose.Cells：真正的产品**

使用 Aspose.Cells，开发人员可以导出数据，以每个细节和每个级别格式化电子表格，导入图像、导入图表、创建图表、操作图表、流式传输 Microsoft Excel 数据，以 XLS、CSV、SpreadsheetML、TabDelimited、TXT、XML（[Aspose.Pdf](https://products.aspose.com/pdf/java/) 集成）等多种格式进行保存。

要了解更多产品信息、功能和程序员指南，请参阅 Aspose.Cells 文档和在线特色 [演示](https://github.com/aspose-cells/Aspose.Cells-for-Java)。您可以 [下载](https://downloads.aspose.com/cells/java) 并免费评估。

### **先决条件**

要在 ColdFusion 应用程序中使用 Aspose.Cells for Java，请将 Aspose.Cells.jar 文件复制到 {InstallationFolder\\}\wwwroot\WEB-INF\lib 文件夹中。

别忘了在 lib 文件夹中放入新的 JAR 文件后重新启动 ColdFusion 应用程序服务器。

### **使用 Aspose.Cells for Java 和 ColdFusion 创建 Excel 文件**

以下，我们创建一个生成空的 Microsoft Excel 文件，插入一些内容并将其保存为 XLS 文件的简单应用程序。

以下是实际代码（ColdFusion & Aspose.Cells for Java）。执行代码后，将生成一个名为 output.xls 的 Excel 文件。

**生成的 output.xls**

![todo:image_alt_text](using-aspose-cells-for-java-with-coldfusion_1.png)

**Java**

{{< highlight java >}}

 <html>

<head><title>Hello World!</title></head>

<body>

    <b>This example shows how to create a simple MS Excel Workbook using Aspose.Cells</b>

    <cfset workbook=CreateObject("java", "com.aspose.cells.Workbook").init()>

    <cfset worksheets = workbook.getWorksheets()>

    <cfset sheet= worksheets.get("Sheet1")>

    <cfset cells= sheet.getCells()>

    <cfset cell= cells.getCell(0,0)>

    <cfset cell.setValue("Hello World!")>

    <cfset workbook.save("C:\output.xls")>

</body>

</html>

{{< /highlight >}}

## **摘要**

{{% alert color="primary" %}}

本文介绍了如何在 ColdFusion 中使用 Aspose.Cells for Java。

Aspose.Cells 提供了极大的灵活性，提供出色的速度、效率和可靠性。Aspose.Cells 从多年的研究、设计和精心调整中受益。

欢迎在 [Aspose.Cells 论坛](https://forum.aspose.com/c/cells/9) 提出查询、评论和建议。

{{% /alert %}}

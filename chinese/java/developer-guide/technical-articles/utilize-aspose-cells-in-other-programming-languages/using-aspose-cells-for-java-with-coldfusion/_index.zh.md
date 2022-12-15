---
title: 将 Aspose.Cells for Java 与 ColdFusion 一起使用
type: docs
weight: 40
url: /zh/java/using-aspose-cells-for-java-with-coldfusion/
---
{{% alert color="primary" %}}

本文给出了 ColdFusion 开发者在 ColdFusion 应用程序中使用 Aspose.Cells for Java 所需的基本信息和代码段。

本文介绍如何使用 ColdFusion 创建一个简单的网页，并使用 Aspose.Cells for Java 生成一个简单的 Excel 文件。

{{% /alert %}}

## **Aspose.Cells：真正的产品**

使用 Aspose.Cells 开发人员可以导出数据、在每个细节和每个级别格式化电子表格、导入图像、导入图表、创建图表、操作图表、流式传输 Microsoft Excel 数据，以各种格式保存，包括 XLS、CSV、SpreadsheetML、TabDelimited、TXT、XML ([Aspose.Pdf](https://products.aspose.com/pdf/java/)集成）等等。

要了解有关产品信息、功能和程序员指南的更多信息，请参阅 Aspose.Cells 文档和在线精选[演示](https://github.com/aspose-cells/Aspose.Cells-for-Java).你可以[下载](https://downloads.aspose.com/cells/java)并免费评估。

### **先决条件**

要在 ColdFusion 应用程序中使用 Aspose.Cells for Java，请将 Aspose.Cells.jar 文件复制到 {InstallationFolder\\}\wwwroot\WEB-INF\lib 文件夹。

将新的 JAR 文件放入 lib 文件夹后，不要忘记重新启动 ColdFusion 应用程序服务器。

### **使用 Aspose.Cells for Java & ColdFusion 创建 Excel 文件**

下面，我们创建一个简单的应用程序，生成一个空的 Microsoft Excel 文件，插入一些内容并将其另存为 XLS 文件。

以下是实际代码（ColdFusion & Aspose.Cells for Java）。执行代码后，将生成一个 Excel 文件 output.xls。

**生成的输出.xls**

![待办事项：图像_替代_文本](using-aspose-cells-for-java-with-coldfusion_1.png)

**Java**

{{< highlight "java" >}}

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

## **概括**

{{% alert color="primary" %}}

本文介绍如何将 Aspose.Cells for Java 与 ColdFusion 一起使用。

Aspose.Cells 提供了极大的灵活性，并提供了出色的速度、效率和可靠性。 Aspose.Cells 得益于多年的研究、设计和精心调整。

我们欢迎在[Aspose.Cells论坛](https://forum.aspose.com/c/cells/9).

{{% /alert %}}

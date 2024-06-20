---
title: 您的第一个 Aspose.Cells 应用程序  Hello World
type: docs
weight: 30
url: /zh/java/your-first-aspose-cells-application-hello-world/
---

{{% alert color="primary" %}}

这个初学者主题展示了开发人员如何使用 Aspose.Cells 的简单 API 创建一个简单的第一个应用程序（Hello World）。该应用程序在工作表的指定单元格中创建了一个包含 Hello World 文字的 Microsoft Excel 文件。

{{% /alert %}}

### **创建Hello World应用程序**

使用 Aspose.Cells API 创建 Hello World 应用程序：

1. 创建 [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) 类的一个实例。
1. 应用许可证：
   1. 如果您已购买许可证，请在应用程序中使用该许可证以获得对 Aspose.Cells 全部功能的访问。
   1. 如果您正在使用组件的评估版本 （如果您在没有许可证的情况下使用 Aspose.Cells），请跳过此步骤。
1. 创建一个新的 Microsoft Excel 文件，或者打开现有文件，在其中您想要添加/更新一些文本。
1. 访问 Microsoft Excel 文件中的工作表的任何单元格。
1. 在访问的单元格中插入单词**Hello World!**。
1. 生成修改后的Microsoft Excel文件。

下面的示例演示了上述步骤。

#### **创建一个工作簿**

以下示例从头开始创建一个新的工作簿，在第一个工作表的单元格A1中写入单词"Hello World!"，然后保存文件。

**生成的电子表格** 

![todo:image_alt_text](your-first-aspose-cells-application-hello-world_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-introduction-CreatingWorkbook-1.java" >}}

#### **打开现有文件**

以下示例打开名为**book1.xls**的现有Microsoft Excel模板文件，在第一个工作表的单元格A1中写入单词"Hello World!"，然后将工作簿保存为新文件。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-introduction-OpeningExistingFile-1.java" >}}

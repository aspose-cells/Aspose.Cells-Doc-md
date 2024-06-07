---
title: Aspose.Cells Java 用于 xlsx4j
linktitle: 为什么不使用xlsx4j
type: docs
weight: 100
url: /zh/java/aspose-cells-java-for-xlsx4j/
description: 本节介绍了我们为什么不选择 xlsx4j 来解析 Excel。
---

{{% alert color="primary" %}}
有时我们会遇到以下问题：为什么我们应该使用 Aspose 产品而不是 xlsx4j？这个问题很容易回答：功能和功能。
{{% /alert %}}


## **xlsx4j**
xlsx4j 是一个用于创建和操作 Microsoft Open XML Excel xlsx 文件的开源（ASLv2）Java库，类似于用于操作 Microsoft Open XML Word docx 文件的 docx4j。
它类似于 Microsoft 的 OpenXML SDK，但适用于 Java。docx4j 使用 JAXB 创建内存中的对象表示。
您需要花时间去了解 JAXB 和 Open XML 文件结构。

更多信息请访问 [docx4java.org](https://www.docx4java.org/trac/docx4j)
## **Java的Aspose.Cells**
Aspose.Cells for Java 是一款屡获殊荣的Excel电子表格组件，允许Java开发人员嵌入读取、写入和操作Excel®电子表格（XLS、XLSX、XLSM、XLSB、XLTX、SpreadsheetML、CSV、ODS）、HTML、MHTML、PDF和图像文件格式的能力到他们自己的Java应用程序中，而无需依赖Microsoft Excel®。

Aspose.Cells for Java是一个成熟、可伸缩、功能丰富的组件，提供许多功能，远远超出其他供应商简单数据导出功能的范围。使用Aspose.Cells for Java，开发人员可以导出数据，以最精细的级别格式化电子表格，导入图像，创建图表，应用和计算复杂公式，流式传输Excel®数据，保存为各种格式等等-所有这些都无需使用Microsoft Excel®或Microsoft Office Automation。

更多信息请访问 [aspose.com](https://products.aspose.com/cells/java/)

## **为什么不选择 xlsx4j**
xlsx4j 只能解析和保存 Microsoft Open XML Excel xlsx 文件，而 Aspose.Cells for Java 可以处理所有 Excel 文件格式（XLS、XLSX、XLSM、XLSB、XLTX、SpreadsheetML、CSV、ODS），支持各种文件格式转换。

## **Aspose.Cells Java 用于 xlsx4j**
Aspose.Cells for xlsx4j 项目展示了使用 Aspose.Cells Java APIs 相比 xlsx4j 可以执行不同任务的方式。该项目还涵盖了仅在 Aspose.Cells APIs 中可用而不在 xlsx4j 中用于处理电子表格的功能。

该项目对于希望比较 xlsx4j 与 Aspose.Cells 或从 xlsx4j 迁移到 Aspose.Cells 的开发人员很有帮助。
## **系统要求和支持的平台**
### **系统要求**
下面是执行 Aspose.Cells Java 用于 xlsx4j 的系统要求:

- 安装 Java 1.4 或以上版本。
- 下载Aspose.Cells组件。
- 下载 docx4j 库。
### **支持的平台**
以下是支持的平台:

- Aspose.Cells 8.3.0 或以上版本。
- docx4j 3.1.0 或以上版本库。
- Java IDE（Eclipse、NetBeans、IntelliJ等）。
## **下载中**
以下运行示例的发行版可在以下所有社交编码站点上下载:

### **GitHub**
- [Aspose.Cells Java 用于 Xlsx4j - v 1.0](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Xlsx4j-v1.0.0)

要配置 **Aspose.Cells for Java API**，请在您的 **pom.xml** 中包含 Aspose 仓库 URL 和 Aspose.Cells for Java API Maven 依赖项如下:
### **Aspose Maven 仓库**
{{< highlight java >}}

 <repositories>

    <repository>

        <id>aspose-maven-repository</id>

        <name>Aspose Maven Repository</name>

        <url>http://repository.aspose.com/repo/</url>

    </repository>

</repositories>

{{< /highlight >}}
### **Aspose.Cells for Java Maven 依赖项**
{{< highlight java >}}

 <dependencies>

    <dependency>

        <groupId>com.aspose</groupId>

        <artifactId>aspose-cells</artifactId>

        <version>8.6.0</version>

    </dependency>

</dependencies>

{{< /highlight >}}

**注意:** 请使用可用的最新版本的 Aspose API。
## **支持、扩展和贡献**
### **支持**
自 Aspose 成立的第一天起，我们就知道仅仅提供优质的产品给我们的客户是不够的。我们还需要提供优质的服务。我们自己也是开发人员，了解遇到技术问题或软件中的一些怪癖会让您无法完成工作是多么令人沮丧。我们的目标是解决问题，而不是制造问题。

这就是为什么我们提供免费支持的原因。无论是谁使用我们的产品，不论是购买还是试用，都值得我们的全力关注和尊重。

您可以使用以下任一平台记录与 Aspose.Cells Java 用于 xlsx4j 相关的任何问题或建议:

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-Java/issues)
### **扩展和贡献**
Aspose.Cells Java for xlsx4j 是开源的，其源代码可在下面列出的主要社交编码网站上获得。鼓励开发人员下载源代码，并通过建议或添加新功能或改进现有功能来做出贡献，以使其他人也能从中受益。
### **源代码**
您可以从以下位置获取最新的源代码

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_Java_for_Xlsx4j)
## **示例代码**
本节包括以下主题

- [Aspose.Cells 和 xlsx4j 中常见特性的代码比较](/cells/zh/java/code-comparison-for-common-features-in-aspose-cells-and-xlsx4j/)
  - [使用 xlsx4j 处理电子表格](/cells/zh/java/working-with-spreadsheet-in-xlsx4j/)
    - [在xlsx4j的电子表格中添加注释](/cells/zh/java/add-comments-in-spreadsheet-in-xlsx4j/)
    - [在 xlsx4j 中的电子表格中添加图片](/cells/zh/java/add-images-in-spreadsheet-in-xlsx4j/)
    - [在 xlsx4j 中创建新的电子表格](/cells/zh/java/create-new-spreadsheet-in-xlsx4j/)
    - [在 xlsx4j 中打开和保存电子表格](/cells/zh/java/open-and-save-spreadsheet-in-xlsx4j/)
    - [在 xlsx4j 中调整行列高度](/cells/zh/java/row-column-height-adjustment-in-xlsx4j/)
- [Aspose.Cells 中 xlsx4j的缺失功能](/cells/zh/java/missing-features-of-xlsx4j-in-aspose-cells/)
  - [xlsx4j 中的数据处理特性](/cells/zh/java/data-handling-features-in-xlsx4j/)
    - [在 xlsx4j 中计算小计](/cells/zh/java/calculate-sub-totals-in-xlsx4j/)
    - [从 xlsx4j 中的工作表导出数据](/cells/zh/java/export-data-from-worksheets-in-xlsx4j/)
    - [在 xlsx4j 中查找单元格中的值](/cells/zh/java/find-value-in-cells-in-xlsx4j/)
    - [在 xlsx4j 中的公式计算引擎](/cells/zh/java/formula-calculation-engine-in-xlsx4j/)
    - [将数据导入到 xlsx4j 中的工作表](/cells/zh/java/import-data-to-worksheets-in-xlsx4j/)
    - [在 xlsx4j 中排序数据](/cells/zh/java/sort-data-in-xlsx4j/)
    - [在 xlsx4j 中进行先例和从属跟踪](/cells/zh/java/tracing-precedents-and-dependents-in-xlsx4j/)
  - [xlsx4j 的杂项示例](/cells/zh/java/miscellaneous-examples-for-xlsx4j/)
    - [将电子表格转换为 PDF 在 xlsx4j 中](/cells/zh/java/convert-spreadsheet-to-pdf-in-xlsx4j/)
    - [在 xlsx4j 中创建数据透视表](/cells/zh/java/create-pivot-table-in-xlsx4j/)
    - [在 xlsx4j 中打印工作簿](/cells/zh/java/printing-workbooks-in-xlsx4j/)
    - [在 xlsx4j 中设置打印标题](/cells/zh/java/set-print-titles-in-xlsx4j/)
  - [在 xlsx4j 中处理图表](/cells/zh/java/working-with-charts-in-xlsx4j/)
    - [在 xlsx4j 中将图表转换为图像](/cells/zh/java/convert-chart-to-image-in-xlsx4j/)
    - [在 xlsx4j 中创建图表](/cells/zh/java/create-charts-in-xlsx4j/)
    - [在 xlsx4j 中创建数据透视图表](/cells/zh/java/create-pivot-charts-in-xlsx4j/)
  - [在 xlsx4j 中处理工作表](/cells/zh/java/working-with-worksheets-in-xlsx4j/)
    - [在 xlsx4j 中将工作簿转换为 HTML](/cells/zh/java/convert-workbook-to-html-in-xlsx4j/)
    - [在 xlsx4j 中检测合并的单元格](/cells/zh/java/detect-merged-cells-in-xlsx4j/)
    - [在 xlsx4j 中显示和隐藏工作簿的滚动条](/cells/zh/java/display-and-hide-scrollbars-of-workbooks-in-xlsx4j/)
    - [在xlsx4j中显示和隐藏工作簿的选项卡](/cells/zh/java/display-and-hide-tabs-of-workbook-in-xlsx4j/)
    - [在xlsx4j中将每个工作表保存为不同的PDF](/cells/zh/java/save-each-worksheet-to-different-pdf-in-xlsx4j/)
    - [在xlsx4j中设置工作表选项卡颜色](/cells/zh/java/set-worksheet-tab-color-in-xlsx4j/)

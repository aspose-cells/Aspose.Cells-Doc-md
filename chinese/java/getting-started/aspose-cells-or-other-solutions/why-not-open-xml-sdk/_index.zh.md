---
title: 为什么不打开 XML SDK
type: docs
weight: 20
url: /zh/java/why-not-open-xml-sdk/
---
{{% alert color="primary" %}} 

我们有时会听到这样的问题：

**为什么我们应该使用 Aspose 产品而不是免费的 Open XML SDK？**

这个问题很容易回答：**特性和功能**.

{{% /alert %}} 
## **什么是 Open XML SDK？**
根据 MSDN 库，Open XML SDK 定义为：Open XML SDK 2.0 简化了操作 Open XML 包和包内的底层 Open XML 架构元素的任务。 Open XML SDK 2.0 封装了开发人员在 Open XML 包上执行的许多常见任务，因此您只需几行代码即可执行复杂的操作。OOXML 文档本质上是压缩的 XML 文件，而 Open XML SDK 是类的集合，允许您以强类型方式处理 OOXML 文档的内容。这不是解压缩文件以提取 XML、将 XML 加载到 DOM 树并直接使用 XML 元素和属性，而是 Open XML SDK 提供了类来执行此操作。
## **什么是 Aspose.Cells？**
Aspose.Cells 是一个类库，它允许您的应用程序执行以下电子表格处理任务： 所有流行的 Excel 格式之间的高质量转换，包括转换为 PDF、HTML、TIFF 和打印。使用工作簿对象模型进行编程。能够从一个或多个文档的片段构建文档，同时通过风格格式、图表和图形自动合并数据。高级功能，例如从不同数据源（包括 Array、ArrayList、DataTable / ResultSet）导入数据。强大的公式计算引擎，支持几乎所有标准和高级 Microsoft Excel 函数。

{{% alert color="primary" %}}
## **比较 Open XML SDK 和 Aspose.Cells**
下表比较了 Open XML SDK 和 Aspose.Cells 的功能。{{% /alert %}}

|**功能或功能类别**|**打开 XML SDK**|**Aspose.Cells**|
|:- |:- |:- |
|支持的 Excel 或其他格式|XLSX|XLS、CSV、SpreadsheetML 2003、XLSX、HTML、制表符分隔、ODS、纯文本 (TXT)、PDF、XPS|
|在 Excel 格式之间转换|不|是的|
|<p>使用工作簿对象模型的高级编程：</p><p>- 查找和替换。</p><p>- 组装电子表格。</p><p>- 在工作簿之间复制片段和工作表。</p>|不|是的|
|使用文档对象模型进行详细编程，访问所有电子表格元素的单个元素和格式属性。|是的|是的|
|对底层 XML 元素和属性（如关系标识符、OOXML 文档的列表标识符）的低级直接和完全访问。|是的|不|
|<p>生成报告，用数据填充文档：</p><p>- 导入/导出数据到/从*数据表 /*结果集。</p><p>- 智能标记功能。</p><p>- 插入/删除行/列/范围。</p><p>- 自定义数据源。</p>|不|是的|
|<p>渲染和打印：*将工作表页面呈现为光栅图像（TIFF、多页 TIFF、PNG、JPEG、BMP）。*将电子表格页面呈现为矢量图像 (EMF)。* 将图表转换为图像（TIFF、多页 TIFF、PNG、JPEG、BMP、EMF 等）</p><p>- 指定图像分辨率、质量、压缩和其他选项。 </p><p>- 使用 .NET 打印基础设施打印电子表格。该组件内置打印方法，打印工作表，如MS Excel打印预览所示。</p>|不|是的|
|动态计算/重新计算公式|不|是的|
|支持的平台|Windows, .NET|Windows, Linux, Java, .NET, Mono|
## **结论**
  {{% alert color="primary" %}}Open XML SDK 和 Aspose.Cells 并没有直接竞争，因为它们针对的是完全不同的需求和受众。 Open XML SDK 是一个类库，提供了一种处理 OOXML 文档的强类型方式。 Aspose.Cells是一个非常好用的电子表格处理库，对所有Microsoft Excel和其他文件格式提供了很好的支持。如果您需要做的只是对 XLSX 文档进行相当基本的编程操作，那么 Open XML SDK 可能是一个合适的选择。使用 Open XML SDK，您可以轻松完成简单的任务，例如生成简单的 XLSX 文档或删除注释、页眉/页脚、提取图像或其他。有些任务可以用Open XML SDK实现，但不能用Aspose.Cells实现。例如，如果你需要直接访问一个OOXML文档的XML元素和属性，那么你应该使用Open XML SDK。但是，如果你需要对文档执行复杂的操作，例如下面的一些任务，那么使用 Aspose.Cells 是你最好的选择：支持除 XLSX 之外的其他文件格式。在工作簿之间复制片段和工作表，或以适当方式组合对象、样式和其他格式的方式连接工作簿。替换格式化或未格式化的文本。高级功能，例如从不同数据源（包括 Array、ArrayList、DataTable / ResultSet）导入数据。生成业务文档，例如来自数据源的带有订单详细信息的订单。将文档转换为 PDF 或 XPS，使其看起来与 Microsoft Excel 转换后的文档完全一样。开发 .NET 或 Java 应用程序。{{% /alert %}}

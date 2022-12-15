---
title: 在工作表中应用条件格式
type: docs
weight: 40
url: /zh/java/apply-conditional-formatting-in-worksheets/
---
{{% alert color="primary" %}}

本文旨在详细介绍如何将条件格式添加到工作表中的一系列单元格。

条件格式是 Microsoft Excel 中的一项高级功能，它允许您将格式应用于一系列单元格，并根据单元格的值或公式的值更改格式。例如，单元格的背景可能是红色以突出负值，或者文本颜色可能是绿色以突出正值。当单元格的值满足格式条件时，应用格式。如果单元格的值不满足格式条件，则使用单元格的默认格式。

可以使用 Microsoft Office Automation 应用条件格式，但这有其缺点。涉及的原因和问题有几个：例如，安全性、稳定性、可扩展性和速度。寻找其他解决方案的主要原因是 Microsoft 本身强烈建议不要使用 Office Automation 进行软件解决方案。

本文展示了如何使用 Aspose.Cells API 使用几行最简单的代码创建控制台应用程序，在单元格上添加条件格式。

{{% /alert %}}

## **使用条件格式**

本文完成以下任务：

1. [使用 Aspose.Cells 根据单元格值应用条件格式](/cells/zh/java/apply-conditional-formatting-in-worksheets/#task-1-using-asposecells-to-apply-conditional-formatting-based-on-cell-value).
1. [使用 Aspose.Cells 应用基于公式的条件格式](/cells/zh/java/apply-conditional-formatting-in-worksheets/#task-2-using-asposecells-to-apply-conditional-formatting-based-on-a-formula).

### **任务 1：使用 Aspose.Cells 应用基于 Cell 值的条件格式**

1. **下载并安装 Aspose.Cells.zip**:
   1. [下载](https://downloads.aspose.com/cells/java) Aspose.Cells for Java.
1. 在您的开发计算机上解压它。
所有 Aspose 组件在安装后都在评估模式下工作。评估模式没有时间限制，只在生成的文档中注入水印。
1. **创建项目**.
使用 Java 编辑器（例如 Eclipse）创建一个项目，或者使用文本编辑器创建一个简单的程序。
1. **添加类路径**.
要使用 Eclipse 设置类路径，请执行以下步骤：
1. 从 Aspose.Cells.zip 中提取 Aspose.Cells.jar 和 dom4j_1.6.1.jar。
 1、在Eclipse中设置项目的类路径：
 1.在Eclipse中选择你的项目然后选择**特性**来自**项目**菜单。
1. 选择对话框左侧的“Java Build Path”。
 1. 在**图书馆**选项卡，选择**添加 JAR**或者**添加外部 JAR**选择 Aspose.Cells.jar 和 dom4j_1.6.1.jar 并将它们添加到构建路径中。
 1.编写应用调用Aspose的组件API。
或者您可以在运行时在 Windows 中的 DOS 提示符下设置路径。

{{< highlight "java" >}}

  javac -classpath %classpath%;e:\Aspose.Cells.jar;  ClassName .javajava -classpath %classpath%;e:\Aspose.Cells.jar;  ClassName  

{{< /highlight >}}

1. **根据单元格值应用条件格式**.
下面是组件用来完成任务的代码。它在单元格上应用条件格式。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ConditionalFormattingOnCellValue-ApplyConditionalFormattingOnCellValue.java" >}}

执行上述代码时，条件格式将应用于输出文件 (output.xls) 第一个工作表中的单元格“A1”。应用于 A1 的条件格式取决于单元格值。如果 A1 的单元格值介于 50 和 100 之间，则由于应用了条件格式，背景颜色为红色。请查看生成的 XLS 文件的以下屏幕截图。

**输出A1值小于50的Excel文件**

![待办事项：图像_替代_文本](apply-conditional-formatting-in-worksheets_1.png)

**输出 A1 在 50 到 100 之间的 Excel 文件**

![待办事项：图像_替代_文本](apply-conditional-formatting-in-worksheets_2.png)

### **任务 2：使用 Aspose.Cells 应用基于公式的条件格式**

1. **根据公式应用条件格式**.
下面是组件用于完成任务的实际代码。它在“B3”上应用条件格式。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ConditionalFormattingBasedOnFormula-ConditionalFormattingBasedOnFormula.java" >}}

执行上述代码时，条件格式将应用于输出文件 (output.xls) 第一个工作表中的单元格“B3”。应用的条件格式取决于将“B3”的值计算为 B1 和 B2 之和的公式。请查看生成的 XLS 文件的以下屏幕截图。

**输出B3值小于100的Excel文件**

![待办事项：图像_替代_文本](apply-conditional-formatting-in-worksheets_3.png)

**输出B3大于100的Excel文件**

![待办事项：图像_替代_文本](apply-conditional-formatting-in-worksheets_4.png)

### **结论**

{{% alert color="primary" %}}

本文介绍如何使用 Aspose.Cells API 将条件格式应用于工作表中的单元格。希望它能为您提供一些见解，以便您可以在自己的方案中使用这些选项。

Aspose.Cells 为解决方案提供了极大的灵活性，并提供了出色的速度、效率和可靠性，以满足特定的业务应用程序要求。 Aspose.Cells 受益于多年的研究、设计和精心调整。

我们欢迎您在[Aspose.Cells论坛](https://forum.aspose.com/c/cells/9).我们保证及时回复。

{{% /alert %}}

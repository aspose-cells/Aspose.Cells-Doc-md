---
title: 在工作表中应用条件格式
type: docs
weight: 40
url: /zh/java/apply-conditional-formatting-in-worksheets/
---

{{% alert color="primary" %}}

本文旨在提供如何在工作表的一系列单元格中添加条件格式的详细理解。

条件格式是Microsoft Excel中的高级功能，允许您为一系列单元格应用格式，并根据单元格的值或公式的值更改格式。例如，单元格的背景可能是红色以突出显示负值，或正值可能为绿色的文本颜色。当单元格的值符合格式条件时，将应用该格式。如果单元格的值不符合格式条件，则使用单元格的默认格式。

通过Microsoft Office Automation 可以应用条件格式，但这样做存在其缺点。涉及了几个原因和问题：例如，安全性，稳定性，可伸缩性和速度。寻找另一种解决方案的主要原因是Microsoft自己强烈建议不要在软件解决方案中使用Office Automation。

本文展示如何创建一个控制台应用程序，并在几行最简单的代码中使用Aspose.Cells API在单元格上添加条件格式。

{{% /alert %}}

## **使用条件格式**

本文介绍以下任务：

1. [使用 Aspose.Cells 根据单元格值应用条件格式](/cells/zh/java/apply-conditional-formatting-in-worksheets/#task-1-using-asposecells-to-apply-conditional-formatting-based-on-cell-value)。
2. [使用 Aspose.Cells 根据公式应用条件格式](/cells/zh/java/apply-conditional-formatting-in-worksheets/#task-2-using-asposecells-to-apply-conditional-formatting-based-on-a-formula)。

### **任务1：使用 Aspose.Cells 根据单元格值应用条件格式**

1. **下载并安装 Aspose.Cells.zip**：
   1. [下载](https://downloads.aspose.com/cells/java) Aspose.Cells for Java。
   1. 在开发计算机上解压缩。
      安装任何 Aspose 组件时都是以评估模式运行。评估模式没有时间限制，并且只向生成的文档中注入水印。
1. **创建一个项目**。
   创建使用 Java 编辑器（例如 Eclipse）的项目或使用文本编辑器创建简单程序。
3. **添加类路径**。
   要在 Eclipse 中设置类路径，请执行以下步骤：
   1. 从Aspose.Cells.zip中提取Aspose.Cells.jar和dom4j_1.6.1.jar。
   1. 在Eclipse中设置项目的类路径:
      3. 在 Eclipse 中选择您的项目，然后从“项目”菜单中选择 **属性**。
      4. 在对话框的左侧选择“Java 构建路径”。
      5. 在 **库** 选项卡上，选择 **添加 JAR** 或 **添加外部 JAR** 来选择 Aspose.Cells.jar 和 dom4j_1.6.1.jar 并将它们添加到构建路径中。
   1. 编写应用程序以调用Aspose组件的API。
      或者您可以在 Windows 的 DOS 提示符下在运行时设置路径。

{{< highlight java >}}

  javac -classpath %classpath%;e:\Aspose.Cells.jar;  ClassName .javajava -classpath %classpath%;e:\Aspose.Cells.jar;  ClassName  

{{< /highlight >}}

1. **根据单元格值应用条件格式**。
   以下是组件用于完成任务的代码。它会在单元格上应用条件格式。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ConditionalFormattingOnCellValue-ApplyConditionalFormattingOnCellValue.java" >}}

当执行上述代码时，在输出文件（output.xls）的第一个工作表的单元格“A1”上应用了条件格式。A1 的条件格式取决于单元格的值。如果 A1 的单元格值在 50 到 100 之间，则由于应用了条件格式，背景颜色为红色。请参阅生成的 XLS 文件的以下屏幕截图。

**A1 值小于 50 的输出 Excel 文件**

![todo:image_alt_text](apply-conditional-formatting-in-worksheets_1.png)

**A1 值在 50 到 100 之间的输出 Excel 文件**

![todo:image_alt_text](apply-conditional-formatting-in-worksheets_2.png)

### **任务2：使用 Aspose.Cells 根据公式应用条件格式**

1. **根据公式应用条件格式**。
   以下是组件用于完成任务的实际代码。它会在“B3”上应用条件格式。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ConditionalFormattingBasedOnFormula-ConditionalFormattingBasedOnFormula.java" >}}

执行上述代码时，会将条件格式应用于输出文件（output.xls）的第一个工作表中的“B3”单元格。所应用的条件格式取决于计算“B3”值的公式，该公式将“B1”和“B2”的值相加。请参阅生成的XLS文件的以下截图。

**B3值小于100的输出Excel文件**

![todo:image_alt_text](apply-conditional-formatting-in-worksheets_3.png)

**B3值大于100的输出Excel文件**

![todo:image_alt_text](apply-conditional-formatting-in-worksheets_4.png)

### **结论**

{{% alert color="primary" %}}

本文展示了如何使用Aspose.Cells API对工作表中的单元格应用条件格式。希望这将为您提供一些见解，以便您可以在自己的场景中使用这些选项。

Aspose.Cells为解决方案提供了极大的灵活性，并提供了出色的速度、效率和可靠性，以满足特定的业务应用需求。Aspose.Cells受益于多年的研究、设计和精心调整。

我们欢迎您在[Aspose.Cells论坛](https://forum.aspose.com/c/cells/9)中提出您的问题、评论和建议。我们将及时回复。

{{% /alert %}}

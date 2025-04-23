---
title: 在工作表中应用条件格式
type: docs
weight: 40
url: /zh/java/apply-conditional-formatting-in-worksheets/
---

{{% alert color="primary" %}}

本文旨在详细介绍如何向工作表的一系列单元格添加条件格式。

条件格式是Microsoft Excel中的一个高级功能，允许您对一系列单元格应用格式，并且根据单元格的值或公式的值进行格式更改。例如，单元格的背景可能显示为红色以突出显示负值，或者正值的文字颜色可能为绿色。当单元格的值满足格式条件时，将应用格式。如果单元格的值不满足格式条件，则使用单元格的默认格式。

使用Microsoft Office Automation可以应用条件格式，但这有其缺点。涉及几个原因和问题：例如，安全性，稳定性，可扩展性和速度。寻找另一个解决方案的主要原因是，Microsoft本身强烈建议不要在软件解决方案中使用Office Automation。

本文展示了如何使用Aspose.Cells API在单元格上添加条件格式的几行简单的代码来创建一个控制台应用程序。

{{% /alert %}}

## **处理条件格式**

本文按照以下任务进行：

1. [使用Aspose.Cells根据单元格值应用条件格式](/cells/zh/java/apply-conditional-formatting-in-worksheets/#task-1-using-asposecells-to-apply-conditional-formatting-based-on-cell-value)。
1. [使用Aspose.Cells根据公式应用条件格式](/cells/zh/java/apply-conditional-formatting-in-worksheets/#task-2-using-asposecells-to-apply-conditional-formatting-based-on-a-formula)。

### **任务1：使用Aspose.Cells根据单元格值应用条件格式**

1. **下载并安装Aspose.Cells.zip**：
   1. [下载](https://downloads.aspose.com/cells/java) Aspose.Cells for Java。
   1. 在开发计算机上解压缩。
      所有Aspose组件在安装时都以评估模式运行。评估模式没有时间限制，只会在生成的文档中添加水印。
1. **创建一个项目**。
   可以使用诸如Eclipse之类的Java编辑器创建项目，也可以使用文本编辑器创建一个简单的程序。
1. **添加类路径**。
   要在Eclipse中设置类路径，请执行以下步骤：
   1. 从 Aspose.Cells.zip 中提取 Aspose.Cells.jar 和 dom4j_1.6.1.jar。
   1. 在 Eclipse 的项目中设置类路径：
      1. 在Eclipse中选择您的项目，然后从“项目”菜单中选择**属性**。
      1. 在对话框的左侧选择“Java构建路径”。
      1. 在**库**选项卡上，选择**添加JAR**或**添加外部JAR**以选择Aspose.Cells.jar和dom4j_1.6.1.jar并将它们添加到构建路径中。
   1. 编写调用Aspose组件API的应用程序。
      或者，您可以在Windows的DOS提示符下运行时设置路径。

{{< highlight java >}}

  javac -classpath %classpath%;e:\Aspose.Cells.jar;  ClassName .javajava -classpath %classpath%;e:\Aspose.Cells.jar;  ClassName  

{{< /highlight >}}

1. **根据单元格值应用条件格式**。
   以下是组件用于完成任务的代码。它在一个单元格上应用了条件格式。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ConditionalFormattingOnCellValue-ApplyConditionalFormattingOnCellValue.java" >}}

执行上述代码时，条件格式被应用于输出文件（output.xls）的第一个工作表中的单元格“A1”。A1的条件格式是根据单元格值而定的。如果A1的值在50到100之间，则由于应用了条件格式，背景颜色为红色。请参阅所生成的XLS文件的以下屏幕截图。

**A1值小于50的输出Excel文件**

![todo:image_alt_text](apply-conditional-formatting-in-worksheets_1.png)

**A1值在50到100之间的输出Excel文件**

![todo:image_alt_text](apply-conditional-formatting-in-worksheets_2.png)

### **任务2：使用Aspose.Cells根据公式应用条件格式**

1. **根据公式应用条件格式**。
   以下是组件用于完成任务的实际代码。它在“B3”上应用了条件格式。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ConditionalFormattingBasedOnFormula-ConditionalFormattingBasedOnFormula.java" >}}

执行上述代码时，条件格式被应用于输出文件（output.xls）的第一个工作表中的单元格“B3”。应用的条件格式取决于计算“B3”值的公式，该公式将B1和B2的和作为“B3”的值。请参阅所生成的XLS文件的以下屏幕截图。

**B3值小于100的输出Excel文件**

![todo:image_alt_text](apply-conditional-formatting-in-worksheets_3.png)

**B3值大于100的输出Excel文件**

![todo:image_alt_text](apply-conditional-formatting-in-worksheets_4.png)

### **结论**

{{% alert color="primary" %}}

本文介绍了如何使用Aspose.Cells API在工作表中对单元格应用条件格式。希望这能为您提供洞察力，以便在自己的场景中使用这些选项。

Aspose.Cells为解决方案提供了极大的灵活性，并且在满足特定业务应用需求方面提供了出色的速度、效率和可靠性。Aspose.Cells经过多年的研究、设计和精心调整。

我们欢迎您在[Aspose.Cells论坛](https://forum.aspose.com/c/cells/9)中提出您的问题、评论和建议。我们保证会迅速回复。

{{% /alert %}}
{{< app/cells/assistant language="java" >}}

---
title: 在工作表之间复制形状
type: docs
weight: 250
url: /zh/java/copy-shapes-between-worksheets/
---
{{% alert color="primary" %}}

有时，您确实需要根据需要将不同的图片、图表和其他绘图对象复制到不同的工作表中。 Aspose.Cells 支持在工作表之间复制形状。图表、图像和其他对象以最高的精度复制。

您可以尝试 Office Automation，但这有其自身的缺点。涉及多个原因和问题：例如安全性、稳定性、可扩展性、速度、价格和功能。简而言之，有很多原因，其中最重要的一个是 Microsoft 自己强烈建议不要通过软件解决方案实现 Office 自动化。

在本文中，我们创建了一个控制台应用程序，使用 Aspose.Cells 使用几行最简单的代码在工作簿的工作表之间执行图片、图表和其他绘图对象的复制。

本文档旨在让开发人员详细了解如何在工作表之间复制形状（图片、图表、控件和其他绘图对象）。

{{% /alert %}}

## **复制形状**

本文介绍了如何：

- [将一张工作表中的图片复制到另一张工作表](/cells/zh/java/copy-shapes-between-worksheets/#copying-a-picture-from-one-worksheet-to-another).
- [将图表从一个工作表复制到另一个](/cells/zh/java/copy-shapes-between-worksheets/#task-2-copying-a-chart-from-one-worksheet-to-another).
- [将控件和其他绘图对象从一个工作表复制到另一个工作表](/cells/zh/java/copy-shapes-between-worksheets/#task-3-copying-controls-and-other-drawing-objects-from-one-worksheet-to-another).

### **将图片从一个工作表复制到另一个**

#### **步骤1：在Microsoft Excel中创建带有图片和图表的工作簿**

1. 在 Microsoft Excel 中创建了一个新工作簿。
1. 在第一个工作表上添加图片，在第二个工作表上添加图表。

以下屏幕截图显示了在 Microsoft Excel 中创建的两个模板工作表。

   **带有图表的工作表“图表”**

![待办事项：图像_替代_文本](copy-shapes-between-worksheets_1.png)

**带有图片的工作表“图片”**

![待办事项：图像_替代_文本](copy-shapes-between-worksheets_2.png)

现在，将名为“Picture”的工作表中的图片复制到最后一个工作表“Result”中。

#### **第 2 步：下载 Aspose.Cells.Zip**

1. [下载 Aspose.Cells for Java](https://downloads.aspose.com/cells/java).
1. 在您的开发计算机上将其解压缩。

全部[Aspose](http://www.aspose.com/)组件在安装后以评估模式工作。评估模式没有时间限制，它只在生成的文档中注入水印。

#### **第 3 步：创建项目**

您可以使用某些 Java 编辑器（例如 Eclipse）创建一个项目，或者使用记事本创建一个简单的程序。

#### **第 4 步：添加类路径**

要使用 Eclipse 设置类路径，请执行以下步骤：

1. 从 Aspose.Cells.zip 中提取 Aspose.Cells.jar 和 dom4j_1.6.1.jar。
1. 在 Eclipse 中设置项目的类路径：
1. 在 Eclipse 中选择您的项目，然后单击菜单 Project-Properties。
1. 在弹出窗口的左侧选择“Java Build Path”，然后选择“Libraries”选项卡，点击“Add JARs”或“Add External JARs”选择Aspose.Cells.jar和dom4j_1.6.1.jar并添加到build中路径。
1. 编写应用程序调用 Aspose 组件的 API。

或者您可以在运行时在 DOS 提示符下在 Windows 中设置它。例如：

javac -classpath %classpath%;e:\Aspose.Cells.jar;类名.javajava -classpath %classpath%;e:\Aspose.Cells.jar;班级名称

#### **步骤 5：将图片从一个工作表复制到另一个工作表**

以下是完成任务的代码。它将名为“Picture”的工作表中的图片复制到工作表“Result”中。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CopyPicturefromOneWorksheetToAnother-CopyPicturefromOneWorksheetToAnother.java" >}}

#### **结果任务 1：**

执行上述代码后，工作表“Picture”中的图片现在被复制到最后一个工作表“Result”

**带有复制图片的工作表“结果”**

![待办事项：图像_替代_文本](copy-shapes-between-worksheets_3.png)

### **任务 2：将图表从一个工作表复制到另一个工作表**

#### **步骤 1：将图表从一个工作表复制到另一个工作表**

以下是组件用于完成任务的实际代码。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CopyChartFromOneWorksheetToAnother-CopyChartFromOneWorksheetToAnother.java" >}}

#### **结果任务 2**

执行上述代码后，工作表“Chart”中的图表被复制到工作表“Result”中。请查看生成的工作表的以下快照。

**带有复制图片和图表的工作表“结果”**

![待办事项：图像_替代_文本](copy-shapes-between-worksheets_4.png)

### **任务 3：将控件和其他绘图对象从一个工作表复制到另一个工作表**

**带有文本框和椭圆形的“控制”工作表**

![待办事项：图像_替代_文本](copy-shapes-between-worksheets_5.png)

请参阅以下简单步骤，您需要执行这些步骤才能获得所需的结果。

#### **步骤 1：在工作簿之间复制工作表**

以下是组件用来完成任务的代码。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CopyWorksheetBetweenWorkbooks-CopyWorksheetBetweenWorkbooks.java" >}}

#### **结果任务 3**

执行上述代码后，工作表“Control”中的控件现在被复制到工作表“Result”中。请参阅以下“结果”快照。

**带有复制的文本框和椭圆形的工作表“结果”**

![待办事项：图像_替代_文本](copy-shapes-between-worksheets_6.png)

## **结论**

本文展示了如何在使用 Aspose.Cells 之间复制不同的形状，如图片、图表和其他绘图对象。希望它能给您一些启发，并且您将能够根据不同的场景使用这些选项。

Aspose.Cells 可以为解决方案提供比其他解决方案更大的灵活性，并提供出色的速度、效率和可靠性来满足特定的业务应用程序要求。结果确实表明 Aspose.Cells 受益于多年的研究、设计和精心调整。

我们热忱欢迎您在[Aspose.Cells论坛](https://forum.aspose.com/c/cells/9).

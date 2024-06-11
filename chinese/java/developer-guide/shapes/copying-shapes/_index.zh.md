---
title: 在工作表之间复制形状
type: docs
weight: 250
url: /zh/java/copy-shapes-between-worksheets/
---

{{% alert color="primary" %}}

有时，您需要根据要求将不同图片、图表和其他绘图对象复制到不同的工作表中。Aspose.Cells支持在工作表之间复制形状。图表、图片和其他对象都可以以最高精度进行复制。

您可能会尝试Office自动化，但这会有其自身的缺点。有多个原因和问题涉及其中：例如安全性、稳定性、可扩展性、速度、价格和功能。总之，有许多理由，其中最重要的是微软强烈建议不要使用软件解决方案中的Office自动化。

在本文中，我们创建一个控制台应用程序，使用Aspose.Cells使用简单的几行代码在工作簿的工作表之间执行图片、图表和其他绘图对象的复制。

本文旨在为开发人员提供如何在工作表之间复制形状（图片、图表、控件和其他绘图对象）的详细理解。

{{% /alert %}}

## **复制形状**

本文解释了如何：

- [从一个工作表复制图片到另一个工作表](/cells/zh/java/copy-shapes-between-worksheets/#copying-a-picture-from-one-worksheet-to-another)。
- [从一个工作表复制图表到另一个工作表](/cells/zh/java/copy-shapes-between-worksheets/#task-2-copying-a-chart-from-one-worksheet-to-another)。
- [从一个工作表复制控件和其他绘图对象到另一个工作表](/cells/zh/java/copy-shapes-between-worksheets/#task-3-copying-controls-and-other-drawing-objects-from-one-worksheet-to-another)。

### **从一个工作表复制图片到另一个工作表**

#### **步骤1：在Microsoft Excel中创建带有图片和图表的工作簿**

1. 在Microsoft Excel中创建一个新工作簿。
2. 在第一个工作表上添加一张图片，并在第二个工作表上添加一个图表。

   以下截图显示在Microsoft Excel中创建的两个模板工作表。

   **名为“Chart”的工作表，带有图表**

![todo:image_alt_text](copy-shapes-between-worksheets_1.png)

**名为“Picture”的工作表，带有图片**

![todo:image_alt_text](copy-shapes-between-worksheets_2.png)

现在，将“Picture”工作表中的图片复制到最后一个名为“Result”的工作表。

#### **步骤2：下载Aspose.Cells.Zip**

1. [下载Aspose.Cells for Java](https://downloads.aspose.com/cells/java).
1. 在开发计算机上解压缩。

   所有 [Aspose](http://www.aspose.com/) 组件在安装后都是以评估模式运行。 评估模式没有时间限制，只会在生成的文档中添加水印。

#### **步骤3：创建一个项目**

您可以使用一些Java编辑器（例如Eclipse）创建一个项目，或者使用记事本创建一个简单的程序。

#### **步骤4：添加类路径**

要在Eclipse中设置类路径，请执行以下步骤：

1. 从 Aspose.Cells.zip 中提取 Aspose.Cells.jar 和 dom4j_1.6.1.jar。
1. 在 Eclipse 的项目中设置类路径：
1. 在Eclipse中选择您的项目，然后单击菜单 Project-Properties。
1. 在弹出窗口的左侧选择“Java Build Path”，然后选择“Libraries”选项卡，单击“Add JARs”或“Add External JARs”以选择Aspose.Cells.jar和dom4j_1.6.1.jar，并将它们添加到构建路径中。
1. 编写调用Aspose组件API的应用程序。

或者您可以在Windows的DOS提示符中在运行时进行设置，例如：

javac -classpath %classpath%;e:\Aspose.Cells.jar; ClassName .javajava -classpath %classpath%;e:\Aspose.Cells.jar; ClassName

#### **步骤5：从一个工作表中复制图片到另一个工作表**

以下是完成该任务的代码。它将从名为“Picture”的工作表复制一张图片到名为“Result”的工作表。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CopyPicturefromOneWorksheetToAnother-CopyPicturefromOneWorksheetToAnother.java" >}}

#### **任务1的结果：**

执行上述代码后，来自工作表“Picture”的图片现在已被复制到最后一个工作表“Result”中

**名为“Result”的工作表，带有复制的图片**

![todo:image_alt_text](copy-shapes-between-worksheets_3.png)

### **任务2：从一个工作表中复制图表到另一个工作表**

#### **步骤1：将一个工作表中的图表复制到另一个工作表**

以下是组件用于完成任务的实际代码。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CopyChartFromOneWorksheetToAnother-CopyChartFromOneWorksheetToAnother.java" >}}

#### **结果任务2**

执行上述代码后，名为“Chart”的工作表中的图表被复制到名为“Result”的工作表。请查看以下结果工作表的快照。

带有复制图片和图表的“Result”工作表

![todo:image_alt_text](copy-shapes-between-worksheets_4.png)

### **任务3：在一个工作表和另一个中复制控件和其他绘图对象**

带有文本框和椭圆的“Control”工作表

![todo:image_alt_text](copy-shapes-between-worksheets_5.png)

请查看以下简单步骤，您需要执行这些步骤以获得您想要的结果。

#### **步骤1：在工作簿之间复制工作表**

以下是组件用于完成任务的代码。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CopyWorksheetBetweenWorkbooks-CopyWorksheetBetweenWorkbooks.java" >}}

#### **结果任务3**

执行上述代码后，“Control”工作表中的控件现在被复制到“Result”工作表。请查看“Result”的快照。

带有复制文本框和椭圆的“Result”工作表

![todo:image_alt_text](copy-shapes-between-worksheets_6.png)

## **结论**

本文介绍了如何在Aspose.Cells中复制不同形状，如图片、图表和其他绘图对象。希望它能给您一些见解，并且您将能够根据不同的情景利用这些选项。

Aspose.Cells可以为解决方案提供比其他更灵活的选项，同时提供出色的速度、效率和可靠性，以满足特定的商业应用需求。结果确实表明Aspose.Cells受益于多年的研究、设计和精心调整。

我们诚挚地欢迎您在[Aspose.Cells论坛](https://forum.aspose.com/c/cells/9)上提出您的疑问、评论和建议。

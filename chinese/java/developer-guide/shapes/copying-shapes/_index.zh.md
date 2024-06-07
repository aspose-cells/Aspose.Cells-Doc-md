---
title: 在工作表之间复制形状
type: docs
weight: 250
url: /zh/java/copy-shapes-between-worksheets/
---

{{% alert color="primary" %}}

有时，您确实需要根据需求将不同的图片、图表和其他绘图对象复制到不同的工作表中。Aspose.Cells支持在工作表之间复制形状。图表、图像和其他对象将以最高程度的精度复制。

您可能会尝试使用Office Automation，但这有其自身的缺点。涉及到一些原因和问题：例如安全性、稳定性、扩展性、速度、价格和功能。简而言之，有很多原因，最重要的一个原因是Microsoft强烈建议不要从软件解决方案中使用Office自动化。

在本文中，我们将使用几行最简单的代码使用Aspose.Cells在工作簿的工作表之间执行图片、图表和其他绘图对象的复制。

本文旨在为开发人员提供如何在工作表之间复制形状（图片、图表、控件和其他绘图对象）的详细理解。

{{% /alert %}}

## **复制形状**

本文解释了如何：

- [从一个工作表复制图片到另一个工作表](/cells/zh/java/copy-shapes-between-worksheets/#copying-a-picture-from-one-worksheet-to-another)。
- [从一个工作表复制图表到另一个工作表](/cells/zh/java/copy-shapes-between-worksheets/#task-2-copying-a-chart-from-one-worksheet-to-another)。
- [从一个工作表到另一个工作表复制控件和其他绘图对象](/cells/zh/java/copy-shapes-between-worksheets/#task-3-copying-controls-and-other-drawing-objects-from-one-worksheet-to-another)。

### **从一个工作表复制图片到另一个工作表**

#### **步骤1：在Microsoft Excel中创建带有图片和图表的工作簿**

1. 在Microsoft Excel中创建一个新工作簿。
1. 在第一个工作表上添加一张图片，在第二个工作表上添加一个图表。

   以下截图展示了在Microsoft Excel中创建的两个模板工作表。

   **带有图表的工作表“Chart”**

![todo:image_alt_text](copy-shapes-between-worksheets_1.png)

**带有图片的工作表“Picture”**

![todo:image_alt_text](copy-shapes-between-worksheets_2.png)

现在，将“Picture”工作表中的图片复制到最后一个工作表“Result”中。

#### **步骤2：下载Aspose.Cells.Zip**

1. [下载Aspose.Cells for Java](https://downloads.aspose.com/cells/java)。
1. 在开发计算机上解压缩。

   所有[Aspose](http://www.aspose.com/)组件在安装后均以评估模式运行。评估模式没有时间限制，只会将水印注入生成的文档中。

#### **步骤3：创建一个项目**

您可以使用一些Java编辑器，如Eclipse，创建项目，或者使用NotePad创建一个简单的程序。

#### **步骤4：添加类路径**

要在 Eclipse 中设置类路径，请执行以下步骤：

1. 从Aspose.Cells.zip中提取Aspose.Cells.jar和dom4j_1.6.1.jar。
1. 在Eclipse中设置项目的类路径:
1. 在Eclipse中选择您的项目，然后单击菜单项Project-Properties。
1. 在弹出窗口的左侧选择“Java构建路径”，然后选择“库”选项卡，单击“添加JAR”或“添加外部JAR”以选择Aspose.Cells.jar和dom4j_1.6.1.jar，并将其添加到构建路径中。
1. 编写应用程序以调用Aspose组件的API。

或者您可以在Windows的DOS提示下设置运行时。例如：

javac -classpath %classpath%;e:\Aspose.Cells.jar; ClassName .javajava -classpath %classpath%;e:\Aspose.Cells.jar; ClassName

#### **步骤5：从一个工作表复制图片到另一个工作表**

下面是完成任务的代码。它将一个图片从名为“Picture”的工作表复制到工作表“Result”。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CopyPicturefromOneWorksheetToAnother-CopyPicturefromOneWorksheetToAnother.java" >}}

#### **结果任务1：**

执行以上代码后，来自工作表“Picture”的图片已复制到最后一个工作表“Result”中

**复制图片后的“Result”工作表**

![todo:image_alt_text](copy-shapes-between-worksheets_3.png)

### **任务2：将图表从一个工作表复制到另一个工作表**

#### **步骤1：将图表从一个工作表复制到另一个工作表**

以下是组件用于完成任务的实际代码。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CopyChartFromOneWorksheetToAnother-CopyChartFromOneWorksheetToAnother.java" >}}

#### **结果任务2**

执行以上代码后，来自工作表“Chart”的图表已复制到工作表“Result”。请参阅以下结果工作表的快照。

**复制图片和图表后的“Result”工作表**

![todo:image_alt_text](copy-shapes-between-worksheets_4.png)

### **任务3：将控件和其他绘图对象从一个工作表复制到另一个工作表**

**具有文本框和椭圆的“Control”工作表**

![todo:image_alt_text](copy-shapes-between-worksheets_5.png)

请参阅以下简单的步骤以获得所需的结果。

#### **步骤1：在工作簿之间复制工作表**

以下是组件用于完成任务的代码。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CopyWorksheetBetweenWorkbooks-CopyWorksheetBetweenWorkbooks.java" >}}

#### **结果任务3**

执行以上代码后，来自工作表“Control”的控件现已复制到工作表“Result”。请参见“Result”工作表的以下快照。

**复制文本框和椭圆后的“Result”工作表**

![todo:image_alt_text](copy-shapes-between-worksheets_6.png)

## **结论**

本文介绍了如何使用Aspose.Cells在不同的工作表之间复制不同的形状，如图片、图表和其他绘图对象。希望能为您提供一些见解，并能根据您的不同场景利用这些选项。

Aspose.Cells对于解决方案提供了比其他解决方案更灵活的选择，并提供了卓越的速度、效率和可靠性，以满足特定的业务应用需求。结果表明，Aspose.Cells受益于多年的研究、设计和精心调优。

我们热烈欢迎您在[Aspose.Cells论坛](https://forum.aspose.com/c/cells/9)中提出问题、评论和建议。

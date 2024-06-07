---
title: 在工作簿内部和之间复制和移动工作表
type: docs
weight: 20
url: /zh/java/copy-and-move-worksheets-within-and-between-workbooks/
---

{{% alert color="primary" %}}

有时，您需要具有相同格式和数据输入的几个工作表。例如，如果您使用季度预算，可能希望创建一个包含带有相同列标题、行标题和公式的工作表的工作簿。有一种方法可以做到这一点：通过创建一个表然后复制它三次。

Aspose.Cells支持在工作簿内部或之间复制或移动工作表。工作表包括数据、格式、表、矩阵、图表、图像和其他对象，以最高精度复制。

{{% /alert %}}

## **复制和移动工作表**

本文解释了如何使用 Aspose.Cells 来：

- [在工作簿内复制工作表](/cells/zh/java/copy-and-move-worksheets-within-and-between-workbooks/#copying-a-worksheet-within-a-workbook)。
- [在工作簿内移动工作表](/cells/zh/java/copy-and-move-worksheets-within-and-between-workbooks/#moving-a-worksheet-with-in-a-workbook)。
- [在工作簿之间复制工作表](/cells/zh/java/copy-and-move-worksheets-within-and-between-workbooks/#copying-a-worksheet-between-workbooks)。
- [在工作簿之间移动工作表](/cells/zh/java/copy-and-move-worksheets-within-and-between-workbooks/#moving-a-worksheet-between-workbooks)。

### **在工作簿内复制工作表**

所有示例的初始步骤都是相同的。

1. 在Microsoft Excel中创建两个带有一些数据的工作簿。在此示例中，我们在Microsoft Excel中创建了两个新工作簿，并在工作表中输入了一些数据。

- FirstWorkbook.xls（3 个工作表）
- SecondWorkbook.xls（1 个工作表）

  **FirstWorkbook.xls**

![todo:image_alt_text](copy-and-move-worksheets-within-and-between-workbooks_1.png)

**SecondWorkbook.xls**

![todo:image_alt_text](copy-and-move-worksheets-within-and-between-workbooks_2.png)

1. 下载并安装Aspose.Cells:
   1. [下载Aspose.Cells for Java](https://downloads.aspose.com/cells/java)。
   1. 在开发计算机上解压缩。
      所有[Aspose](http://www.aspose.com/)组件在安装后均以评估模式运行。评估模式没有时间限制，只会将水印注入生成的文档中。
1. 创建一个项目:
   1. 使用诸如 Eclipse 之类的 Java 编辑器创建项目，或使用文本编辑器创建一个简单的程序。
1. 添加类路径：
   1. 从Aspose.Cells.zip中提取Aspose.Cells.jar和dom4j_1.6.1.jar。
   1. 在Eclipse中设置项目的类路径:
      1. 在 Eclipse 中选择您的项目，然后点击 **项目**，再点击 **属性**。
      1. 在对话框左侧选择 **Java 构建路径**，然后选择“库”选项卡，
      1. 点击 **添加 JAR** 或 **添加外部 JAR** 选择 Aspose.Cells.jar 和 dom4j_1.6.1.jar，然后将它们添加到构建路径中。

{{% alert color="primary" %}}

或者您可以在Windows的DOS提示符中在运行时设置类路径。
例如:

{{< highlight java >}}

javac -classpath %classpath%;e:\Aspose.Cells.jar; ClassName .javajava -classpath %classpath%;e:\Aspose.Cells.jar; ClassName

{{< /highlight >}}

{{% /alert %}}

1. 在工作簿内复制工作表：
   以下是用于完成任务的代码。它复制了第一个工作簿中的工作表复制。

执行此代码将移动名为复制的工作表，使其在第一个工作簿中以新名称“最后一张纸”显示。

**输出文件**

![todo:image_alt_text](copy-and-move-worksheets-within-and-between-workbooks_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-Value-CopyWithinWorkbook-1.java" >}}

### **移动工作簿中的工作表**

以下是用于完成任务的代码。

执行此代码会将索引1处的工作表从FirstWorkbook.xls中移动到索引2处。

**输出文件**

![todo:image_alt_text](copy-and-move-worksheets-within-and-between-workbooks_4.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-Value-MoveWorksheet-1.java" >}}

### **在工作簿之间复制工作表**

执行此代码将工作表复制到SecondWorkbook.xls，并将其命名为Sheet2。

**输出文件**

![todo:image_alt_text](copy-and-move-worksheets-within-and-between-workbooks_5.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-Value-CopyWorksheetsBetweenWorkbooks-1.java" >}}

### **在工作簿之间移动工作表**

执行此代码将从FirstWorkbook.xls中将工作表移动到SecondWorkbook.xls，并将其命名为Sheet3。

**输出 FirstWorkbook.xls**

![todo:image_alt_text](copy-and-move-worksheets-within-and-between-workbooks_6.png)

**输出 SecondWorkbook.xls**

![todo:image_alt_text](copy-and-move-worksheets-within-and-between-workbooks_7.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-Value-MoveWorksheet-1.java" >}}

## **结论**

{{% alert color="primary" %}}

本文介绍如何使用Aspose.Cells在工作簿内和工作簿之间复制和移动工作表。

Aspose.Cells经过多年的研究、设计和精心调优。我们欢迎您在[Aspose.Cells论坛](https://forum.aspose.com/c/cells/9)提出查询、评论和建议。我们保证会及时回复。

{{% /alert %}}

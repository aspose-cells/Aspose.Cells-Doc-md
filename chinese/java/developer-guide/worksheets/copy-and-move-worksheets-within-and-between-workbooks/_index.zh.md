---
title: 复制和移动工作表在工作簿内和工作簿之间
type: docs
weight: 20
url: /zh/java/copy-and-move-worksheets-within-and-between-workbooks/
---

{{% alert color="primary" %}}

有时，您可能需要具有相同格式和数据输入的许多工作表。例如，如果您使用季度预算，可能希望创建一个包含具有相同列标题、行标题和公式的工作表的工作簿。有一种方法可以做到这一点：先创建一个工作表，然后将其复制三次。

Aspose.Cells支持在工作簿内或工作簿之间复制或移动工作表。包括数据、格式、表、矩阵、图表、图像和其他对象的工作表都可以以最高精度复制。

{{% /alert %}}

## **复制和移动工作表**

本文介绍如何使用Aspose.Cells：

- [在工作簿内复制工作表](/cells/zh/java/copy-and-move-worksheets-within-and-between-workbooks/#copying-a-worksheet-within-a-workbook)。
- [在工作簿内移动工作表](/cells/zh/java/copy-and-move-worksheets-within-and-between-workbooks/#moving-a-worksheet-with-in-a-workbook)。
- [在工作簿之间复制工作表](/cells/zh/java/copy-and-move-worksheets-within-and-between-workbooks/#copying-a-worksheet-between-workbooks)。
- [在工作簿之间移动工作表](/cells/zh/java/copy-and-move-worksheets-within-and-between-workbooks/#moving-a-worksheet-between-workbooks)。

### **在工作簿内复制工作表**

所有示例的初始步骤都是相同的。

1. 在Microsoft Excel中创建两个带有一些数据的工作簿。对于本示例，我们在Microsoft Excel中创建了两个新工作簿，并为工作表输入了一些数据。

- FirstWorkbook.xls（3个工作表）
- SecondWorkbook.xls（1个工作表）。

  **FirstWorkbook.xls**

![todo:image_alt_text](copy-and-move-worksheets-within-and-between-workbooks_1.png)

**SecondWorkbook.xls**

![todo:image_alt_text](copy-and-move-worksheets-within-and-between-workbooks_2.png)

1. 下载并安装 Aspose.Cells：
   1. [下载Aspose.Cells for Java](https://downloads.aspose.com/cells/java).
   1. 在开发计算机上解压缩。
      所有 [Aspose](http://www.aspose.com/) 组件在安装后都是以评估模式运行。 评估模式没有时间限制，只会在生成的文档中添加水印。
1. 创建一个项目：
   1. 使用Java编辑器（如Eclipse）创建项目或使用文本编辑器创建简单程序。
1. 添加类路径:
   1. 从 Aspose.Cells.zip 中提取 Aspose.Cells.jar 和 dom4j_1.6.1.jar。
   1. 在 Eclipse 的项目中设置类路径：
      1. 在Eclipse中选择您的项目，单击“项目”，然后选择“属性”菜单。
      1. 在对话框左侧选择“Java构建路径”，然后选择“库”选项卡。
      1. 单击“添加JAR”或“添加外部JAR”来选择Aspose.Cells.jar和dom4j_1.6.1.jar并将它们添加到构建路径中。

{{% alert color="primary" %}}

或者可以在Windows的DOS提示符或者Linux的终端窗口中在运行时设置类路径。
例如:

{{< highlight java >}}

javac -classpath %classpath%;e:\Aspose.Cells.jar; ClassName .javajava -classpath %classpath%;e:\Aspose.Cells.jar; ClassName

{{< /highlight >}}

{{% /alert %}}

1. 在一个工作簿内复制工作表:
   以下是用于完成该任务的代码。它复制了FirstWorkbook.xls中的工作表Copy。

执行代码将名为移动表的工作表从 FirstWorkbook.xls 移动到名为最后工作表的新位置。

**输出文件**

![todo:image_alt_text](copy-and-move-worksheets-within-and-between-workbooks_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-Value-CopyWithinWorkbook-1.java" >}}

### **在工作簿中移动工作表**

以下是用来完成任务的代码。

执行代码将从 FirstWorkbook.xls 中的索引1移动工作表移动到索引2。

**输出文件**

![todo:image_alt_text](copy-and-move-worksheets-within-and-between-workbooks_4.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-Value-MoveWorksheet-1.java" >}}

### **在工作簿之间复制工作表**

执行代码将工作表复制到 SecondWorkbook.xls，并将其命名为Sheet2。

**输出文件**

![todo:image_alt_text](copy-and-move-worksheets-within-and-between-workbooks_5.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-Value-CopyWorksheetsBetweenWorkbooks-1.java" >}}

### **在工作簿之间移动工作表**

执行代码将从 FirstWorkbook.xls 移动工作表移到 SecondWorkbook.xls，并将其命名为Sheet3。

**输出 FirstWorkbook.xls 文件**

![todo:image_alt_text](copy-and-move-worksheets-within-and-between-workbooks_6.png)

**输出 SecondWorkbook.xls 文件**

![todo:image_alt_text](copy-and-move-worksheets-within-and-between-workbooks_7.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-Value-MoveWorksheet-1.java" >}}

## **结论**

{{% alert color="primary" %}}

本文详细介绍了如何使用 Aspose.Cells 在工作簿内部以及工作簿之间复制和移动工作表。

Aspose.Cells 经过多年的研究、设计和精心调整。我们欢迎您在 [Aspose.Cells 论坛](https://forum.aspose.com/c/cells/9) 上提出您的疑问、评论和建议。我们保证会及时回复。

{{% /alert %}}

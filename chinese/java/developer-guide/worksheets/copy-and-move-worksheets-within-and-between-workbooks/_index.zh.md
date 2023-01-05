---
title: 在工作簿内和工作簿之间复制和移动工作表
type: docs
weight: 20
url: /zh/java/copy-and-move-worksheets-within-and-between-workbooks/
---
{{% alert color="primary" %}}

有时，您确实需要许多具有通用格式和数据输入的工作表。例如，如果您处理季度预算，您可能希望创建一个工作簿，其中的工作表包含相同的列标题、行标题和公式。有一种方法可以做到这一点：创建一张纸，然后将其复制三次。

Aspose.Cells 支持在工作簿内或工作簿之间复制或移动工作表。包括数据、格式、表格、矩阵、图表、图像和其他对象在内的工作表以最高精度复制。

{{% /alert %}}

## **复制和移动工作表**

本文介绍了如何使用 Aspose.Cells 来：

- [在工作簿中复制工作表](/cells/zh/java/copy-and-move-worksheets-within-and-between-workbooks/#copying-a-worksheet-within-a-workbook).
- [在工作簿中移动工作表](/cells/zh/java/copy-and-move-worksheets-within-and-between-workbooks/#moving-a-worksheet-with-in-a-workbook).
- [在工作簿之间复制工作表](/cells/zh/java/copy-and-move-worksheets-within-and-between-workbooks/#copying-a-worksheet-between-workbooks).
- [在工作簿之间移动工作表](/cells/zh/java/copy-and-move-worksheets-within-and-between-workbooks/#moving-a-worksheet-between-workbooks).

### **在工作簿中复制工作表**

所有示例的初始步骤都相同。

1. 在 Microsoft Excel 中使用一些数据创建两个工作簿。出于本示例的目的，我们在 Microsoft Excel 中创建了两个新工作簿，并将一些数据输入到工作表中。

- FirstWorkbook.xls（3 个工作表）
- SecondWorkbook.xls（1 个工作表）。

  **FirstWorkbook.xls**

![待办事项：图片_替代_文本](copy-and-move-worksheets-within-and-between-workbooks_1.png)

**第二工作簿.xls**

![待办事项：图片_替代_文本](copy-and-move-worksheets-within-and-between-workbooks_2.png)

1. 下载并安装 Aspose.Cells：
   1. [下载 Aspose.Cells for Java](https://downloads.aspose.com/cells/java).
1. 在您的开发计算机上解压它。
全部[Aspose](http://www.aspose.com/)组件在安装后以评估模式工作。评估模式没有时间限制，它只在生成的文档中注入水印。
1. 创建一个项目：
 1. 使用 Java 编辑器（如 Eclipse）创建项目或使用文本编辑器创建简单程序。
1. 添加类路径：
1. 从 Aspose.Cells.zip 中提取 Aspose.Cells.jar 和 dom4j_1.6.1.jar。
 1、在Eclipse中设置项目的类路径：
 1. 在 Eclipse 中选择您的项目并单击菜单**项目**， 然后**特性**.
1.选择**Java 构建路径**在对话框的左侧，然后选择库选项卡，
 1.点击**添加 JAR**要么**添加外部 JAR**选择 Aspose.Cells.jar 和 dom4j_1.6.1.jar 并将它们添加到构建路径中。

{{% alert color="primary" %}}

或者您可以在 Windows 上的 DOS 提示符下在运行时设置类路径。
例如：

{{< highlight "java" >}}

javac -classpath %classpath%;e:\Aspose.Cells.jar; ClassName .javajava -classpath %classpath%;e:\Aspose.Cells.jar; ClassName

{{< /highlight >}}

{{% /alert %}}

1. 在工作簿中复制工作表：
下面是用于完成任务的代码。它复制 FirstWorkbook.xls 中的工作表 Copy。

执行代码将 FirstWorkbook.xls 中名为 Copy 的工作表移动到新名称 Last Sheet。

**输出文件**

![待办事项：图片_替代_文本](copy-and-move-worksheets-within-and-between-workbooks_3.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-Value-CopyWithinWorkbook-1.java" >}}

### **在工作簿中移动工作表**

下面是用于完成任务的代码。

执行代码将工作表从索引 1 移动到 FirstWorkbook.xls 中的索引 2。

**输出文件**

![待办事项：图片_替代_文本](copy-and-move-worksheets-within-and-between-workbooks_4.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-Value-MoveWorksheet-1.java" >}}

### **在工作簿之间复制工作表**

执行代码将工作表 Copy 复制到 SecondWorkbook.xls 并使用新名称 Sheet2。

**输出文件**

![待办事项：图片_替代_文本](copy-and-move-worksheets-within-and-between-workbooks_5.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-Value-CopyWorksheetsBetweenWorkbooks-1.java" >}}

### **在工作簿之间移动工作表**

执行代码会将移动工作表从 FirstWorkbook.xls 移动到 SecondWorkbook.xls，新名称为 Sheet3。

**输出 FirstWorkbook.xls**

![待办事项：图片_替代_文本](copy-and-move-worksheets-within-and-between-workbooks_6.png)

**输出 SecondWorkbook.xls**

![待办事项：图片_替代_文本](copy-and-move-worksheets-within-and-between-workbooks_7.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-Value-MoveWorksheet-1.java" >}}

## **结论**

{{% alert color="primary" %}}

本文介绍如何使用 Aspose.Cells 在工作簿内和工作簿之间复制和移动工作表。

 Aspose.Cells 得益于多年的研究、设计和精心调整。我们欢迎您的查询、意见和建议[Aspose.Cells论坛](https://forum.aspose.com/c/cells/9).我们保证及时回复。

{{% /alert %}}

---
title: 复制和移动工作表在工作簿内和工作簿之间
type: docs
weight: 80
url: /zh/net/copy-and-move-worksheets-within-and-between-workbooks/
---

{{% alert color="primary" %}}

有时，您可能需要具有相同格式和数据输入的许多工作表。例如，如果您使用季度预算，可能希望创建一个包含具有相同列标题、行标题和公式的工作表的工作簿。有一种方法可以做到这一点：先创建一个工作表，然后将其复制三次。

Aspose.Cells支持在工作簿内或工作簿之间复制或移动工作表。包括数据、格式、表、矩阵、图表、图像和其他对象的工作表都可以以最高精度复制。

{{% /alert %}}

## **复制和移动工作表**

### **在工作簿内复制工作表**

所有示例的初始步骤都是相同的。

1. 在Microsoft Excel中创建两个带有一些数据的工作簿。对于本示例，我们在Microsoft Excel中创建了两个新工作簿，并为工作表输入了一些数据。

- FirstWorkbook.xlsx（3 个工作表）。
- SecondWorkbook.xlsx（1 个工作表）。

1. 下载并安装 Aspose.Cells：
   1. [下载 Aspose.Cells for .NET](https://downloads.aspose.com/cells/net)。
   1. 在您的开发计算机上安装它。
      所有 [Aspose](http://www.aspose.com/) 组件在安装后都是以评估模式运行。 评估模式没有时间限制，只会在生成的文档中添加水印。
1. 创建一个项目：
   1. 启动 Visual Studio.Net。
   1. 创建新的控制台应用程序。
1. 添加引用：
   1. 向项目添加对 Aspose.Cells 的引用。
      例如，向 ...\Program Files\Aspose\Aspose.Cells\Bin\Net1.0\Aspose.Cells.dll 添加引用。
1. 在工作簿内复制工作表
   第一个示例将 FirstWorkbook.xlsx 内的第一个工作表（Copy）复制。

执行代码后，名为 Copy 的工作表将在 FirstWorkbook.xlsx 中复制并命名为 Last Sheet。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-CopyMoveWorksheets-CopyWorksheets.cs" >}}

### **工作簿内移动工作表**

以下代码显示了如何将工作簿内的工作表从一个位置移动到另一个位置。执行代码后，Move 工作表从 FirstWorkbook.xlsx 的索引 1 移动到索引 2。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-CopyMoveWorksheets-MoveWorksheets.cs" >}}

### **在工作簿之间复制工作表**

执行代码后，工作表名为 Copy 被复制到 SecondWorkbook.xlsx，并命名为 Sheet2。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-CopyMoveWorksheets-CopyWorksheetsBetweenWorkbooks.cs" >}}

### **在工作簿之间移动工作表**

执行代码后，工作表名为 Move 从 FirstWorkbook.xlsx 移动到 SecondWorkbook.xlsx，并命名为 Sheet3。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-CopyMoveWorksheets-MoveWorksheetsBetweenWorkbooks.cs" >}}

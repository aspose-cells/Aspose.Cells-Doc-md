---
title: 在工作簿内和工作簿之间复制和移动工作表
type: docs
weight: 80
url: /zh/net/copy-and-move-worksheets-within-and-between-workbooks/
---
{{% alert color="primary" %}}

有时，您确实需要许多具有通用格式和数据输入的工作表。例如，如果您处理季度预算，您可能希望创建一个工作簿，其中的工作表包含相同的列标题、行标题和公式。有一种方法可以做到这一点：创建一张纸，然后将其复制三次。

Aspose.Cells 支持在工作簿内或工作簿之间复制或移动工作表。包括数据、格式、表格、矩阵、图表、图像和其他对象在内的工作表以最高精度复制。

{{% /alert %}}

## **复制和移动工作表**

### **在工作簿中复制工作表**

所有示例的初始步骤都相同。

1. 在 Microsoft Excel 中使用一些数据创建两个工作簿。出于本示例的目的，我们在 Microsoft Excel 中创建了两个新工作簿，并将一些数据输入到工作表中。

- FirstWorkbook.xlsx（3 个工作表）。
- SecondWorkbook.xlsx（1 个工作表）。

1. 下载并安装 Aspose.Cells：
   1. [下载 Aspose.Cells for .NET](https://downloads.aspose.com/cells/net).
 1. 在您的开发计算机上安装它。
全部[Aspose](http://www.aspose.com/)组件在安装后以评估模式工作。评估模式没有时间限制，它只在生成的文档中注入水印。
1. 创建一个项目：
 1. 启动 Visual Studio.Net。
 1. 创建一个新的控制台应用程序。
1. 添加参考资料：
 1.在项目中添加对Aspose.Cells的引用。
例如，添加对 ...\Program Files\Aspose\Aspose.Cells\Bin\Net1.0\Aspose.Cells.dll 的引用
1. 在工作簿中复制工作表
第一个示例复制 FirstWorkbook.xlsx 中的第一个工作表 (Copy)。

执行代码时，名为 Copy 的工作表被复制到 FirstWorkbook.xlsx 中，名称为 Last Sheet。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-CopyMoveWorksheets-CopyWorksheets.cs" >}}

### **在工作簿中移动工作表**

下面的代码显示了如何将工作表从工作簿中的一个位置移动到另一个位置。执行代码会将名为 Move 的工作表从索引 1 移动到 FirstWorkbook.xlsx 中的索引 2。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-CopyMoveWorksheets-MoveWorksheets.cs" >}}

### **在工作簿之间复制工作表**

执行代码会将名为 Copy 的工作表复制到名为 Sheet2 的 SecondWorkbook.xlsx。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-CopyMoveWorksheets-CopyWorksheetsBetweenWorkbooks.cs" >}}

### **在工作簿之间移动工作表**

执行代码会将名为 Move 的工作表从 FirstWorkbook.xlsx 移动到名为 Sheet3 的 SecondWorkbook.xlsx。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-CopyMoveWorksheets-MoveWorksheetsBetweenWorkbooks.cs" >}}

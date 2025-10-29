---
title: 在工作簿内外复制和移动工作表，使用Golang via C++
linktitle: 复制和移动工作表
type: docs
weight: 80
url: /zh/go-cpp/copy-and-move-worksheets-within-and-between-workbooks/
description: 学习如何使用Aspose.Cells for C++在Excel工作簿中复制和移动工作表。
---

{{% alert color="primary" %}}

有时，您需要多个具有相同格式和数据输入的工作表。例如，制作季度预算时，可能需要创建包含相同列标题、行标题和公式的工作簿。这可以通过创建一个工作表，然后多次复制实现。

Aspose.Cells支持在工作簿内或工作簿之间复制或移动工作表。包括数据、格式、表、矩阵、图表、图像和其他对象的工作表都可以以最高精度复制。

{{% /alert %}}

## **复制和移动工作表**

### **在工作簿内复制工作表**

所有示例的初始步骤相同：

1. 在Microsoft Excel中创建两个带有一些数据的工作簿。本示例中，我们创建了两个新工作簿并在工作表中输入了一些数据：
   - FirstWorkbook.xlsx（3个工作表）
   - SecondWorkbook.xlsx（1个工作表）

1. 下载并安装 Aspose.Cells：
    1. [下载 Aspose.Cells for C++](https://downloads.aspose.com/cells/go-cpp/)
   1. 在您的开发计算机上安装

1. 创建一个项目：
   1. 在你偏好的IDE中创建一个新的C++项目

1. 添加引用：
   1. 添加Aspose.Cells for C++库到你的项目

1. 在工作簿内复制工作表
   第一个示例将 FirstWorkbook.xlsx 内的第一个工作表（Copy）复制。

执行代码后，名为 Copy 的工作表将在 FirstWorkbook.xlsx 中复制并命名为 Last Sheet。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CopyAndMoveWorksheetsWithinAndBetweenWorkbooks.go" >}}
### **工作簿内移动工作表**

以下代码显示了如何将工作簿内的工作表从一个位置移动到另一个位置。执行代码后，Move 工作表从 FirstWorkbook.xlsx 的索引 1 移动到索引 2。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CopyAndMoveWorksheetsWithinAndBetweenWorkbooks-1.go" >}}
### **在工作簿之间复制工作表**

执行代码时，将名为Copy的工作表复制到SecondWorkbook.xlsx，并命名为Sheet2。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CopyAndMoveWorksheetsWithinAndBetweenWorkbooks-2.go" >}}
### **在工作簿之间移动工作表**

执行代码后，工作表名为 Move 从 FirstWorkbook.xlsx 移动到 SecondWorkbook.xlsx，并命名为 Sheet3。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CopyAndMoveWorksheetsWithinAndBetweenWorkbooks-3.go" >}}

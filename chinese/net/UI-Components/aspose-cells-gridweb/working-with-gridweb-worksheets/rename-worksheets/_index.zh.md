---
title: 重命名工作表
type: docs
weight: 40
url: /zh/net/rename-worksheets/
---
{{% alert color="primary" %}} 

在 Aspose.Cells.GridWeb 中处理许多工作表并决定更改它们的名称以使它们更有意义时，重命名工作表可能非常有用。例如，可以将包含发票的工作表重命名为 Invoice 而不是 Sheet1。本主题描述了这个简单但有用的功能。

{{% /alert %}} 
## **重命名工作表**
所有工作表都包含一个名称属性，允许开发人员访问或修改工作表的名称。要重命名工作表：

1. 从 GridWorksheetCollection 访问工作表。
1. 重命名选定的工作表。



{{% alert color="primary" %}} 

 Aspose.Cells.GridWeb中工作表的访问方法请参考[访问工作表](/cells/zh/net/access-worksheets/).

{{% /alert %}} 

在执行代码之前，工作表有一个默认名称，例如 Sheet1。

**输入文件：默认名称为 Sheet1 的工作表** 

![待办事项：图像_替代_文本](rename-worksheets_1.png)

运行代码后，工作表被重命名为 Students。

**输出：工作表重命名为 Students** 

![待办事项：图像_替代_文本](rename-worksheets_2.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-RenameWorksheets.aspx-RenameWorksheet.cs" >}}

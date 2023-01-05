---
title: 保存 Excel 文件
type: docs
weight: 20
url: /zh/net/saving-an-excel-file/
---
{{% alert color="primary" %}} 

使用 Aspose.Cells.GridDesktop 控件，用户不仅可以创建新的 Excel 文件，还可以管理现有的文件。但是，在这两种情况下，都需要保存 Aspose.Cells.GridDesktop 的内容。所以，这是我们现在讨论的主题，让我们的用户知道他们如何将他们的网格内容保存为 Excel 文件。

{{% /alert %}} 
## **介绍**
Aspose.Cells.GridDesktop控件的内容保存为Excel文件，Aspose.Cells.GridDesktop提供了以下方法。

1. **另存为文件**
1. **另存为流**
## **保存文件**
创建桌面应用程序并向窗体添加两个带有 GridControl 控件的按钮。将按钮的文本属性设置为**另存为文件**和**另存为流**分别。
### **另存为文件**
创建的点击事件**另存为文件**按钮并将以下代码粘贴到其中。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-SavingExcelFile-SavingAFile.cs" >}}

{{% alert color="primary" %}} 

重要提示：要讨论的重点是 Aspose.Cells.GridDesktop 控件还包含一个名为 SaveToExcel 的方法，该方法也用于将 Excel 文件的内容加载到网格中。但是，这种方法现在已经过时了。因此，建议所有开发人员使用比废弃方法更健壮和高效的 ExportExcelFile 方法。

{{% /alert %}} 
### **另存为流**
有时，开发人员可能需要将他们的 Grid 内容保存到流中（例如，MemoryStream）。为方便此任务，Aspose.Cells.GridDesktop 控件还支持将网格数据保存到流中。创建的点击事件**另存为流**按钮并将以下代码粘贴到其中。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-SavingExcelFile-SavingUsingStream.cs" >}}

{{% alert color="primary" %}} 

重要提示：Microsoft Excel 支持 Excel 工作表最多可包含 65,536 行和 256 列。 Aspose.Cells.GridDesktop 也遵循相同的标准。在 Aspose.Cells.GridDesktop 控件中，开发人员可以创建比标准限制更多的行和列，但在将网格数据保存到 Excel 文件时，将抛出异常。这意味着只有包含在 65,536 行和 256 列中的数据可以使用 Aspose.Cells.GridDesktop 保存到 Excel 文件中。

{{% /alert %}}

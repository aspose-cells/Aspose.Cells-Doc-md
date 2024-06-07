---
title: 保存Excel文件
type: docs
weight: 20
url: /zh/net/aspose-cells-griddesktop/save-an-excel-file/
keywords: GridDesktop,保存,文件
description: 本文介绍了如何在GridDesktop中保存文件。
---

{{% alert color="primary" %}} 

使用 Aspose.Cells.GridDesktop 控件，用户不仅可以创建新的 Excel 文件，还可以管理现有文件。但在这两种情况下，有必要保存 Aspose.Cells.GridDesktop 的内容。因此，我们现在讨论的主题是告知用户如何将其 Grid 内容保存为 Excel 文件。

{{% /alert %}} 
## **介绍**
要将 Aspose.Cells.GridDesktop 控件的内容保存为 Excel 文件，Aspose.Cells.GridDesktop 提供以下方法。

1. **保存为文件**
1. **保存为流**
## **保存文件**
创建一个桌面应用程序，并向表单添加两个按钮，同时使用 GridControl 控件。分别将按钮的文本属性设置为 **另存为文件** 和 **另存为流**。
### **保存为文件**
创建 **另存为文件** 按钮的 Click 事件，并粘贴以下代码至其中。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-SavingExcelFile-SavingAFile.cs" >}}

{{% alert color="primary" %}} 

重要提示：讨论的一个重要点是 Aspose.Cells.GridDesktop 控件还包含一个名为 SaveToExcel 的方法，它也用于将 Excel 文件的内容加载到 Grid 中。但是，此方法现在已经过时。所以，建议所有开发人员使用 ExportExcelFile 方法，该方法比过时的方法更健壮和高效。

{{% /alert %}} 
### **保存为流**
有时，开发人员可能需要将其 Grid 内容保存到流中（例如，MemoryStream）。为简化此任务，Aspose.Cells.GridDesktop 控件还支持将 Grid 数据保存到流中。创建 **另存为流** 按钮的 Click 事件，并粘贴以下代码至其中。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-SavingExcelFile-SavingUsingStream.cs" >}}

{{% alert color="primary" %}} 

重要提示：Microsoft Excel 支持 Excel 表可以包含最多 65,536 行和 256 列。Aspose.Cells.GridDesktop 也遵循相同的标准。在 Aspose.Cells.GridDesktop 控件中，开发人员可以创建比标准限制更多的行和列，但当将网格数据保存到 Excel 文件时，会引发异常。这意味着只能保存 65,536 行和 256 列中包含的数据到一个 Excel 文件中，使用 Aspose.Cells.GridDesktop。

{{% /alert %}}

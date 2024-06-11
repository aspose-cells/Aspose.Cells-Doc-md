---
title: 保存Excel文件
type: docs
weight: 20
url: /zh/net/aspose-cells-griddesktop/save-an-excel-file/
keywords: GridDesktop，保存，文件
description: 本文介绍如何在GridDesktop中保存文件。
---

{{% alert color="primary" %}} 

使用Aspose.Cells.GridDesktop控件，用户不仅可以创建新的Excel文件，还可以管理现有文件。但在这两种情况下，都需要保存Aspose.Cells.GridDesktop的内容。因此，我们现在的讨论主题是让用户了解他们如何将Grid内容保存为Excel文件。

{{% /alert %}} 
## **介绍**
要将Aspose.Cells.GridDesktop控件的内容保存为Excel文件，Aspose.Cells.GridDesktop提供了以下方法。

1. **保存为文件**
1. **保存为流**
## **保存文件**
创建一个桌面应用程序，并向窗体添加带有GridControl控件的两个按钮。将按钮的文本属性分别设置为**另存为文件**和**另存为流**。
### **另存为文件**
创建**另存为文件**按钮的单击事件，并在其中粘贴以下代码。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-SavingExcelFile-SavingAFile.cs" >}}

{{% alert color="primary" %}} 

重要提示：一个重要的讨论点是，Aspose.Cells.GridDesktop控件还包含一个名为SaveToExcel的方法，也用于将Excel文件的内容加载到Grid中。但是，这种方法现在已经过时。因此，建议所有开发人员使用更健壮和高效的ExportExcelFile方法，而不是过时的方法。

{{% /alert %}} 
### **保存为流**
有时，开发人员可能需要将Grid内容保存到流中（例如，MemoryStream）。为了简化这个任务，Aspose.Cells.GridDesktop控件也支持将Grid数据保存到流中。创建**另存为流**按钮的单击事件，并在其中粘贴以下代码。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-SavingExcelFile-SavingUsingStream.cs" >}}

{{% alert color="primary" %}} 

重要提示：Microsoft Excel支持Excel表最多包含65,536行和256列。Aspose.Cells.GridDesktop也遵循相同的标准。在Aspose.Cells.GridDesktop控件中，开发人员可以创建更多的行和列，而不受标准限制，但是保存网格数据到Excel文件时，会抛出异常。这意味着只有包含在65,536行和256列中的数据才能使用Aspose.Cells.GridDesktop保存到Excel文件。

{{% /alert %}}

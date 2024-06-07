---
title: 打开 Excel 文件
type: docs
weight: 10
url: /zh/net/aspose-cells-griddesktop/openg-an-excel-file/
keywords: GridDesktop，打开，文件
description: 本文介绍了如何在 GridDesktop 中打开文件。
---

{{% alert color="primary" %}} 

Aspose.Cells Grid Suite 的一个独特特性是与 Excel 文件的兼容性。在本主题中，我们将演示用户如何在其 Windows 应用程序中使用 Aspose.Cells.GridDesktop 控件打开 Excel 文件。

{{% /alert %}} 
## **介绍**
要使用 Aspose.Cells.GridDesktop 打开 Excel 文件，您必须创建一个包含 GridDesktop 控件的桌面应用程序。如果您不了解如何将 Aspose.Cells.GridDesktop 控件添加到 Windows 窗体中，则应参考[如何使用 Aspose.Cells.GridDesktop](/cells/zh/net/how-to-use-aspose-cells-griddesktop/)。

Aspose.Cells.GridDesktop 提供以下三种不同的打开 Excel 文件的方式。

1. **从文件中打开**
1. **打开 CSV 文件**
1. **从流中打开**
## **打开 Excel 文件**
在这个示例中创建一个桌面应用程序，并执行以下操作。

- 在表单中添加一个 GridControl 控件。
- 添加三个按钮，并将它们的文本属性设置如下：
  - **打开 Excel 文件**
  - **打开 CSV 文件**
  - **从流中打开**
### **从文件中打开**
要将 Excel 文件的内容加载到 Aspose.Cells.GridDesktop 控件中，您将需要调用控件的一个方法，以指定 Excel 文件的路径。之后，Aspose.Cells.GridDesktop 控件将自动从指定的路径找到文件并显示其内容。加载 Excel 文件内容的代码片段在下面的示例中提供。创建**打开 Excel 文件**按钮的 Click 事件，并将以下代码粘贴到其中。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-OpeningExcelFile-OpeningExcelFile.cs" >}}


上面的代码片段可以被开发者以任何他们想要的方式使用。例如，如果您想要在窗体加载时自动加载一个 Excel 文件，则可以在窗体的 Load 事件下添加此代码。
### **打开 CSV 文件**
Aspose.Cells.GridDesktop 控件还支持加载 CSV 文件。创建**打开 CSV 文件**按钮的 Click 事件，并将以下代码粘贴到其中。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-OpeningExcelFile-OpeningCSVFile.cs" >}}
### **从流中打开**
在上面的讨论中，我们已经讨论了如何通过使用文件路径加载 Excel 文件，但 Aspose.Cells.GridDesktop 控件还支持从流中加载 Excel 文件。创建**从流中打开**按钮的 Click 事件，并将以下代码粘贴到其中。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-OpeningExcelFile-OpeningFromStream.cs" >}}



使用文件流作为一个更好的方法来防止任何类型的文件访问或共享违规问题，因为这种方法通过关闭流来确保关闭到文件的所有连接。

{{% alert color="primary" %}} 

重要提示：讨论的一个重要点是 Aspose.Cells.GridDesktop 控件还包含一个名为 LoadFromExcel 的方法，它也用于将 Excel 文件的内容加载到 Grid 中。但是，此方法现在已经过时。所以，建议所有开发人员使用 ImportExcelFile 方法，该方法比过时的方法更健壮和高效。

{{% /alert %}}

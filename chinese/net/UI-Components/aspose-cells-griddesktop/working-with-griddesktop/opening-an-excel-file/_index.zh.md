---
title: 打开 Excel 文件
type: docs
weight: 10
url: /zh/net/opening-an-excel-file/
---
{{% alert color="primary" %}} 

Aspose.Cells Grid Suite 的一个独特功能是它与 Excel 文件的兼容性。在本主题中，我们将演示用户如何使用 Aspose.Cells.GridDesktop 控件在其 Windows 应用程序中打开 Excel 文件。

{{% /alert %}} 
## **介绍**
要使用 Aspose.Cells.GridDesktop 打开 Excel 文件，您必须创建一个包含 GridDesktop 控件的桌面应用程序。如果您不知道如何将 Aspose.Cells.GridDesktop 控件添加到您的 Windows 窗体，那么您应该参考[如何使用Aspose.Cells.GridDesktop](/cells/zh/net/how-to-use-aspose-cells-griddesktop/)

Aspose.Cells.GridDesktop提供以下三种不同的方式来打开Excel文件。

1. **从文件打开**
1. **打开一个 CSV 文件**
1. **从流中打开**
## **打开 Excel 文件**
在此示例中，创建一个桌面应用程序并执行以下操作。

- 向窗体中添加一个 GridControl 控件。
- 添加三个按钮，其文本属性设置如下：
  - **打开 Excel 文件**
  - **打开 CSV 文件**
  - **从流中打开**
### **从文件打开**
要将 Excel 文件的内容加载到 Aspose.Cells.GridDesktop 控件，您必须调用控件的方法来指定 Excel 文件的路径。之后，Aspose.Cells.GridDesktop 控件会自动从指定路径中查找文件并显示其内容。下面的示例提供了加载 Excel 文件内容的代码片段。创建的点击事件**打开 Excel 文件**按钮并将以下代码粘贴到其中。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-OpeningExcelFile-OpeningExcelFile.cs" >}}


开发人员可以按照他们想要的任何方式使用上面的代码片段。例如，如果您想在加载 Windows 窗体时自动加载 Excel 文件，则可以在窗体的 Load 事件下添加此代码。
### **打开一个 CSV 文件**
Aspose.Cells.GridDesktop控件也支持加载CSV文件。创建的点击事件**打开 CSV 文件**按钮并将以下代码粘贴到其中。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-OpeningExcelFile-OpeningCSVFile.cs" >}}
### **从流中打开**
在我们上面的讨论中，我们讨论了如何使用文件路径加载 Excel 文件，但是 Aspose.Cells.GridDesktop 控件还支持从流中加载 Excel 文件。创建的点击事件**从流中打开**按钮并将以下代码粘贴到其中。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-OpeningExcelFile-OpeningFromStream.cs" >}}



使用文件作为流是一种更好的方法来禁止任何类型的文件访问或共享冲突问题，因为这种方法确保通过关闭流来关闭与文件的所有连接。

{{% alert color="primary" %}} 

重要提示：要讨论的重点是 Aspose.Cells.GridDesktop 控件还包含一个名为 LoadFromExcel 的方法，该方法也用于将 Excel 文件的内容加载到网格中。但是，这种方法现在已经过时了。因此，建议所有开发人员使用比过时的方法更健壮和高效的 ImportExcelFile 方法。

{{% /alert %}}

---
title: 打开 Excel 文件
type: docs
weight: 10
url: /zh/net/aspose-cells-griddesktop/openg-an-excel-file/
keywords: GridDesktop, 打开, 文件
description: 本文介绍了如何在GridDesktop中打开文件。
---

{{% alert color="primary" %}} 

Aspose.Cells Grid Suite的一个独特功能是与Excel文件的兼容性。在这个主题中，我们将演示用户如何使用Aspose.Cells.GridDesktop控件在他们的Windows应用程序中打开Excel文件。

{{% /alert %}} 
## **介绍**
要使用Aspose.Cells.GridDesktop打开Excel文件，您必须在其中创建一个拥有GridDesktop控件的桌面应用程序。如果您不知道如何在您的Windows表单中添加Aspose.Cells.GridDesktop控件，则应参考《如何使用Aspose.Cells.GridDesktop》。

Aspose.Cells.GridDesktop提供了以下三种不同的打开Excel文件的方式。

1. **从文件中打开**
1. **打开CSV文件**
1. **从流中打开**
## **打开Excel文件**
在这个示例中，创建一个桌面应用程序并执行以下操作。

- 将一个GridControl控件添加到表单上。
- 添加三个按钮，并将它们的文本属性设置为以下内容：
  - **打开Excel文件**
  - **打开CSV文件**
  - **从流中打开**
### **从文件中打开**
要将Excel文件的内容加载到Aspose.Cells.GridDesktop控件中，您需要调用控件的一个方法来指定Excel文件的路径。此后，Aspose.Cells.GridDesktop控件将自动从指定的路径找到该文件并显示其内容。加载Excel文件内容的代码片段在下面的示例中提供。创建**打开Excel文件**按钮的Click事件，并粘贴以下代码。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-OpeningExcelFile-OpeningExcelFile.cs" >}}


上面的代码片段可以由开发人员以任何方式使用。例如，如果您希望在窗体加载时自动加载Excel文件，那么可以在窗体的Load事件下添加此代码。
### **打开CSV文件**
Aspose.Cells.GridDesktop控件还支持加载CSV文件。创建**打开CSV文件**按钮的Click事件，并粘贴以下代码。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-OpeningExcelFile-OpeningCSVFile.cs" >}}
### **从流中打开**
在我们上面的讨论中，我们已经讨论了使用文件路径加载Excel文件，但Aspose.Cells.GridDesktop控件也支持从流加载Excel文件。创建**从流打开**按钮的单击事件，并粘贴以下代码。



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-OpeningExcelFile-OpeningFromStream.cs" >}}



使用文件流作为一种更好的方法可以防止任何文件访问或共享违规问题，因为该方法确保通过关闭流来关闭与文件的所有连接。

{{% alert color="primary" %}} 

重要提示：一个重要的讨论点是，Aspose.Cells.GridDesktop控件还包含一个名为LoadFromExcel的方法，也用于将Excel文件的内容加载到Grid中。但是，这种方法现在已经过时。因此，建议所有开发人员使用更健壮和高效的ImportExcelFile方法，而不是过时的方法。

{{% /alert %}}

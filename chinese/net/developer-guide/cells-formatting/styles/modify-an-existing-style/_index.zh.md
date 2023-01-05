---
title: 修改现有样式
type: docs
weight: 90
url: /zh/net/modify-an-existing-style/
---
{{% alert color="primary" %}}

要将相同的格式选项应用于单元格，请创建一个新的格式样式对象。格式样式对象是字体、字号、缩进、数字、边框、样式等格式特征的组合，命名并存储为一个集合。应用时，将应用该样式中的所有格式。

您还可以使用现有样式，将其与工作簿一起保存并用于格式化具有相同属性的信息。

当单元格未明确格式化时，**普通的**样式（工作簿的默认样式）被应用。 Microsoft 除了普通样式外，Excel 还预定义了几种样式，包括逗号、货币和百分比。

Aspose.Cells 允许修改任何这些样式或您使用所需属性定义的任何其他样式。

{{% /alert %}}

## **使用 Microsoft Excel**

要更新 Microsoft Excel 97-2003 中的样式：

1. 在**格式**菜单，点击**风格**.
1. 从中选择要修改的样式**款式名称**列表。
1. 点击**调整**.
1. 使用格式 Cells 对话框中的选项卡选择所需的样式选项。
1. 点击**好的**.
1. 在下面**样式包括**指定你想要的样式特征。
1. 点击**好的**保存样式并将其应用于所选范围。

## **使用 Aspose.Cells**

下面的例子演示了如何使用[**风格.更新**](https://reference.aspose.com/cells/net/aspose.cells/style/methods/update)方法。

### **创建和修改样式**

这个例子创建了一个[**风格**](https://reference.aspose.com/cells/net/aspose.cells/style)对象，将其应用于一系列单元格并修改[**风格**](https://reference.aspose.com/cells/net/aspose.cells/style)目的。修改会自动应用于单元格和应用样式的范围。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ModifyExistingStyle-ModifyThroughStyleObject-1.cs" >}}

### **修改现有样式**

此示例使用一个简单的模板 Excel 文件，其中已将名为百分比的样式应用于范围。这个例子：

1. 获得风格，
1. 创建一个样式对象和
1. 修改样式格式。

修改会自动应用于应用样式的范围。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ModifyExistingStyle-ModifyThroughSampleExcelFile-1.cs" >}}

---
title: 保护工作表
type: docs
weight: 10
url: /zh/net/protecting-worksheets/
---

{{% alert color="primary" %}}

当工作表受保护时，用户可以采取的操作受到限制。例如，他们无法输入数据、插入或删除行或列等。

{{% /alert %}}

## **保护工作表**

### **介绍**

Microsoft Excel中的常规保护选项包括：

- 内容
- 对象
- 方案

受保护的工作表不会隐藏或保护敏感数据，因此它与文件加密不同。通常，工作表保护适用于展示目的。它防止最终用户修改工作表中的数据、内容和格式。

### **保护工作表**

Aspose.Cells提供了[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)类，表示Microsoft Excel文件。[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)类包含[**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)集合，允许访问Excel文件中的每个工作表。工作表由[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)类表示。

[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)类提供[**Protect**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/protect/index)方法，用于在工作表上应用保护。[**Protect**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/protect/methods/1)方法接受以下参数：

- 保护类型，工作表上应用的保护类型。 保护类型是用 [**ProtectionType**](https://reference.aspose.com/cells/net/aspose.cells/protectiontype) 枚举帮助应用的。
- 新密码，用于保护工作表的新密码。
- 旧密码，如果工作表已经受到密码保护，则传入旧密码。如果工作表尚未受到保护，则传递 null。

[**ProtectionType**](https://reference.aspose.com/cells/net/aspose.cells/protectiontype)枚举包含以下预定义的保护类型：

|**保护类型**|**描述**|
| :- | :- |
|All| 用户无法修改工作表中的任何内容
|Contents| 用户无法在工作表中输入数据
|Objects| 用户无法修改绘图对象
|Scenarios| 用户无法修改已保存的情景
|Structure| 用户无法修改结构
|Windows| 保护应用于窗口
|None| 不应用任何保护

下例显示如何使用密码保护工作表。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Security-Protecting-ProtectingWorksheet-1.cs" >}}

使用上述代码保护工作表后，打开工作表即可检查工作表的保护。一旦打开文件并尝试向工作表添加一些数据，您将会看到以下对话框：

|**警告对话框，提示用户无法修改工作表**|
| :- |
|![todo:image_alt_text](protecting-worksheets_1.png)|

要在工作表上操作，请选择 **保护**，然后在 **工具** 菜单项中选择 **取消保护工作表**。

选择取消保护工作表菜单项后，将会打开一个对话框，提示您输入密码，以便您可以在工作表上进行操作，如下所示：

|![todo:image_alt_text](protecting-worksheets_2.png)|

### **使用Microsoft Excel保护工作表的部分单元格**

可能会有某些场景需要仅锁定工作表中的一些单元格。如果要锁定工作表中的特定单元格，必须解锁工作表中的所有其他单元格。工作表中的所有单元格已初始化为锁定，您可以在 Microsoft Excel 中打开任何 Excel 文件并单击 **格式 | 单元格** 来显示 **单元格格式** 对话框，然后单击 **保护** 选项卡，查看一个复选框标记为“已锁定”默认为选中状态。

以下描述如何使用 MS Excel 锁定一些单元格。此方法适用于 Microsoft Office Excel 97、2000、2002、2003 及更高版本。

1. 点击**全选**按钮（位于行号1上方和列号A左侧的灰色矩形）来选择整个工作表。
1. 在**格式**菜单上点击**单元格**，点击**保护**选项卡，然后取消**锁定**复选框。
   这将解锁工作表上的所有单元格。
   如果**单元格**命令不可用，工作表的部分可能已被锁定。在**工具**菜单上，指向**保护**，然后点击**取消保护工作表**。
1. 仅选择您想要锁定的单元格，然后重复第2步，但这次选择**锁定**复选框。
1. 在**工具**菜单上，指向**保护**，点击**保护工作表**，然后点击**确定**。
1. 在**保护工作表**对话框中，您可以选择指定密码并选择要允许用户更改的元素。

### **使用Aspose Cells在工作表中保护一些单元格**

在这种方法中，我们只使用Aspose.Cells API来执行此任务。

示例：以下示例展示了如何在工作表中保护一些单元格。首先解锁工作表中的所有单元格，然后锁定其中的3个单元格（A1、B1、C1）。最后，保护工作表。[**Style**](https://reference.aspose.com/cells/net/aspose.cells/style) 对象包含一个布尔属性，[**IsLocked**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/islocked)。您可以将 [**IsLocked**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/islocked)属性设置为true或false，并应用*Column/Row.ApplyStyle()*方法来锁定或解锁带有所需属性的行/列。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Security-Protecting-ProtectingSpecificCellsinaWorksheet-1.cs" >}}

### **在工作表中保护一行**

Aspose.Cells允许您轻松锁定工作表中的任何行。在这里，我们可以利用[**Aspose.Cells.Row**](https://reference.aspose.com/cells/net/aspose.cells/row)类的[**ApplyStyle()**](https://reference.aspose.com/cells/net/aspose.cells/row/methods/applystyle)方法来对工作表中的特定行应用[**Style**](https://reference.aspose.com/cells/net/aspose.cells/style)。该方法接受两个参数：[**Style**](https://reference.aspose.com/cells/net/aspose.cells/style)对象和包含所有与应用格式相关的成员的[**StyleFlag**](https://reference.aspose.com/cells/net/aspose.cells/styleflag)对象。

下面的示例展示了如何在工作表中保护一行。首先解锁工作表中的所有单元格，然后锁定其中的第一行。最后，保护工作表。[**Style**](https://reference.aspose.com/cells/net/aspose.cells/style)对象包含一个布尔属性，[**IsLocked**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/islocked)。您可以将[**IsLocked**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/islocked)属性设置为true或false，以使用[**StyleFlag**](https://reference.aspose.com/cells/net/aspose.cells/styleflag)对象锁定或解锁行/列。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Security-Protecting-ProtectingSpecificRowInWorksheet-1.cs" >}}

### **在工作表中保护一列**

Aspose.Cells允许您轻松锁定工作表中的任何列。在这里，我们可以利用[**Aspose.Cells.Column**](https://reference.aspose.com/cells/net/aspose.cells/column)类的[**ApplyStyle()**](https://reference.aspose.com/cells/net/aspose.cells/column/methods/applystyle)方法来对工作表中的特定列应用[**Style**](https://reference.aspose.com/cells/net/aspose.cells/style)。该方法接受两个参数：[**Style**](https://reference.aspose.com/cells/net/aspose.cells/style)对象和包含所有与应用格式相关的成员的[**StyleFlag**](https://reference.aspose.com/cells/net/aspose.cells/styleflag)对象。

下面的示例展示了如何在工作表中保护一列。首先解锁工作表中的所有单元格，然后锁定其中的第一列。最后，保护工作表。[**Style**](https://reference.aspose.com/cells/net/aspose.cells/style)对象包含一个布尔属性，[**IsLocked**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/islocked)。您可以将[**IsLocked**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/islocked)属性设置为true或false，以使用[**StyleFlag**](https://reference.aspose.com/cells/net/aspose.cells/styleflag)对象锁定或解锁行/列。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Security-Protecting-ProtectColumnWorksheet-1.cs" >}}

### **允许用户编辑范围**

下面的示例展示了如何允许用户在受保护的工作表中编辑范围。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Security-Protecting-EditRangesWorksheet-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}

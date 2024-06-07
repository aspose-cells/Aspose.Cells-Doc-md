---
title: 保护工作表
type: docs
weight: 10
url: /zh/net/protecting-worksheets/
---

{{% alert color="primary" %}}

当工作表受保护时，用户能够执行的操作会受到限制。例如，他们不能输入数据，插入或删除行或列等。

{{% /alert %}}

## **保护工作表**

### **介绍**

Microsoft Excel中的常规保护选项包括：

- 内容
- 对象
- 方案

受保护的工作表不会隐藏或保护敏感数据，因此与文件加密不同。通常，工作表保护适用于演示目的。它防止最终用户在工作表中修改数据、内容和格式。

### **保护工作表**

Aspose.Cells提供一个代表Microsoft Excel文件的[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)类。[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)类包含了一个[**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)集合，允许访问Excel文件中的每个工作表。一个工作表由[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)类表示。

[**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)类提供了[**Protect**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/protect/index)方法，用于在工作表上应用保护。[**Protect**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/protect/methods/1)方法接受以下参数：

- 保护类型，要应用于工作表的保护类型。保护类型是通过[**ProtectionType**](https://reference.aspose.com/cells/net/aspose.cells/protectiontype)枚举帮助应用的。
- 新密码，用于保护工作表的新密码。
- 旧密码，如果工作表已受密码保护，则传递旧密码。如果工作表尚未受保护，则只需传递null。

[**ProtectionType**](https://reference.aspose.com/cells/net/aspose.cells/protectiontype)枚举包含以下预定义的保护类型:

|**保护类型**|**描述**|
| :- | :- |
|All|用户无法修改工作表上的任何内容|
|Contents|用户无法在工作表中输入数据|
|Objects|用户无法修改绘图对象|
|Scenarios|用户无法修改已保存的方案|
|Structure|用户无法修改结构|
|Windows|保护应用于窗口|
|None|未应用保护|

下面的示例展示了如何使用密码保护工作表。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Security-Protecting-ProtectingWorksheet-1.cs" >}}

在上述代码用于保护工作表后，您可以通过打开它来检查工作表上的保护。一旦您打开文件并尝试向工作表添加一些数据，您将看到以下对话框:

|**警告对话框，指出用户无法修改工作表**|
| :- |
|![todo:image_alt_text](protecting-worksheets_1.png)|

要在工作表上操作，请选择**保护**，然后从**工具**菜单项中选择**取消保护工作表**。

选择取消保护工作表菜单项后，会打开一个对话框，提示您输入密码，以便您可以在工作表上进行工作，如下所示:

|![todo:image_alt_text](protecting-worksheets_2.png)|

### **使用Microsoft Excel在工作表中保护几个单元格**

可能有某些情况需要仅锁定工作表中的几个单元格。如果要在工作表中锁定一些特定单元格，必须解锁工作表中的所有其他单元格。工作表中的所有单元格已初始化为锁定，您可以通过打开任何Excel文件到MS Excel并单击**格式 | 单元格...**以显示**格式单元格**对话框，然后单击**保护**标签，看到默认选中了名为“锁定”的复选框。

以下几点描述了如何使用MS Excel锁定几个单元格。该方法适用于Microsoft Office Excel 97, 2000, 2002, 2003及更高版本。

1. 单击**全选**按钮(直接位于第1行行号上方和列字母A的左侧的灰色矩形)选择整个工作表。
1. 单击**格式**菜单上的**单元格**，单击**保护**选项卡，然后取消**锁定**复选框。
   这将解锁工作表上的所有单元格。
   如果**单元格**命令不可用，则工作表的某些部分可能已锁定。在**工具**菜单上，指向**保护**，然后单击**取消保护工作表**。
1. 仅选择要锁定的单元格，然后重复步骤2，但这次选中**锁定**复选框。
1. 在**工具**菜单上，指向**保护**，单击**保护工作表**，然后单击**确定**。
1. 在**保护工作表**对话框中，您可以指定密码并选择要允许用户更改的元素。

### **使用Aspose Cells在工作表中保护几个单元格**

在此方法中，我们仅使用Aspose.Cells API来执行任务。

示例: 以下示例展示了如何在工作表中保护几个单元格。首先解锁工作表中的所有单元格，然后锁定其中的3个单元格(A1、B1、C1)。最后，保护工作表。[**Style**](https://reference.aspose.com/cells/net/aspose.cells/style)对象包含一个布尔属性，[**IsLocked**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/islocked)。您可以将[**IsLocked**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/islocked)的属性设置为true或false，并使用*Column/Row.ApplyStyle()*方法锁定或解锁具有所需属性的行/列。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Security-Protecting-ProtectingSpecificCellsinaWorksheet-1.cs" >}}

### **在工作表中保护一行**

Aspose.Cells允许您轻松锁定工作表中的任何行。在此，我们可以利用[**ApplyStyle()**](https://reference.aspose.com/cells/net/aspose.cells/row/methods/applystyle)类的[**Aspose.Cells.Row**](https://reference.aspose.com/cells/net/aspose.cells/row)方法来应用[**Style**](https://reference.aspose.com/cells/net/aspose.cells/style)到工作表中的特定行。此方法接受两个参数:一个[**Style**](https://reference.aspose.com/cells/net/aspose.cells/style)对象和一个具有所有与应用格式相关的成员的[**StyleFlag**](https://reference.aspose.com/cells/net/aspose.cells/styleflag)对象。

以下示例展示了如何在工作表中保护一行。首先解锁工作表中的所有单元格，然后锁定其中的第一行。最后，保护工作表。[**Style**](https://reference.aspose.com/cells/net/aspose.cells/style)对象包含一个布尔属性，[**IsLocked**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/islocked)。您可以设置[**IsLocked**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/islocked)的属性为true或false，使用[**StyleFlag**](https://reference.aspose.com/cells/net/aspose.cells/styleflag)对象锁定或解锁行/列。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Security-Protecting-ProtectingSpecificRowInWorksheet-1.cs" >}}

### **保护工作表中的列**

Aspose.Cells允许您轻松锁定工作表中的任何列。在这里，我们可以利用[**Aspose.Cells.Column**](https://reference.aspose.com/cells/net/aspose.cells/column)类的[**ApplyStyle()**](https://reference.aspose.com/cells/net/aspose.cells/column/methods/applystyle)方法来应用[**Style**](https://reference.aspose.com/cells/net/aspose.cells/style)到工作表中的特定列。该方法接受两个参数：一个[**Style**](https://reference.aspose.com/cells/net/aspose.cells/style)对象和一个包含所有与应用格式相关的成员的[**StyleFlag**](https://reference.aspose.com/cells/net/aspose.cells/styleflag)对象。

以下示例展示了如何保护工作表中的列。首先解锁工作表中的所有单元格，然后锁定其中的第一列。最后，保护工作表。[**Style**](https://reference.aspose.com/cells/net/aspose.cells/style)对象包含一个布尔属性，[**IsLocked**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/islocked)。您可以将[**IsLocked**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/islocked)属性设置为true或false，以使用[**StyleFlag**](https://reference.aspose.com/cells/net/aspose.cells/styleflag)对象锁定或解锁行/列。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Security-Protecting-ProtectColumnWorksheet-1.cs" >}}

### **允许用户编辑范围**

以下示例展示了如何允许用户编辑受保护工作表中的范围。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Security-Protecting-EditRangesWorksheet-1.cs" >}}

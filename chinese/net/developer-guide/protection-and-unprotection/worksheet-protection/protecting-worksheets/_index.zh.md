---
title: 保护工作表
type: docs
weight: 10
url: /zh/net/protecting-worksheets/
---
{{% alert color="primary" %}}

当工作表受到保护时，用户可以执行的操作将受到限制。例如，他们不能输入数据、插入或删除行或列等。

{{% /alert %}}

## **保护工作表**

### **介绍**

Microsoft Excel 中的常规保护选项是：

- 内容
- 对象
- 场景

受保护的工作表不会隐藏或保护敏感数据，因此它不同于文件加密。通常，工作表保护适用于演示目的。它可以防止最终用户修改工作表中的数据、内容和格式。

### **保护工作表**

Aspose.Cells提供了一个类，[**工作簿**](https://reference.aspose.com/cells/net/aspose.cells/workbook)表示 Microsoft Excel 文件。这[**工作簿**](https://reference.aspose.com/cells/net/aspose.cells/workbook)类包含一个[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)允许访问 Excel 文件中每个工作表的集合。工作表由[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)班级。

这[**工作表**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)类提供了[**保护**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/protect/index)用于在工作表上应用保护的方法。[**保护**](https://reference.aspose.com/cells/net/aspose.cells.worksheet/protect/methods/1)方法接受以下参数：

- 保护类型，要在工作表上应用的保护类型。保护类型是在[**保护类型**](https://reference.aspose.com/cells/net/aspose.cells/protectiontype)枚举。
- 新密码，用于保护工作表的新密码。
- Old Password，旧密码，如果工作表已经受密码保护。如果工作表尚未受到保护，则只需传递 null。

这[**保护类型**](https://reference.aspose.com/cells/net/aspose.cells/protectiontype)枚举包含以下预定义的保护类型：

|**保护类型**|**描述**|
|:- |:- |
|全部|用户不能修改此工作表上的任何内容|
|内容|用户不能在此工作表中输入数据|
|对象|用户不能修改绘图对象|
|场景|用户无法修改已保存的场景|
|结构|用户不能修改结构|
|Windows|保护适用于窗户|
|没有任何|没有应用保护|

下面的示例显示了如何使用密码保护工作表。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Security-Protecting-ProtectingWorksheet-1.cs" >}}

上面的代码对工作表进行了保护后，打开工作表就可以查看到保护情况了。打开文件并尝试向工作表中添加一些数据后，您将看到以下对话框：

|**警告用户无法修改工作表的对话框**|
|:- |
|![待办事项：图片_替代_文本](protecting-worksheets_1.png)|

要处理工作表，请通过选择取消保护工作表**保护**， 然后**取消保护工作表**来自**工具**菜单项。

选择取消保护工作表菜单项后，将打开一个对话框，提示您输入密码，以便您可以在工作表上工作，如下所示：

|![待办事项：图片_替代_文本](protecting-worksheets_2.png)|

### **使用Microsoft Excel保护工作表中的几个Cells**

在某些情况下，您可能只需要锁定工作表中的几个单元格。如果要锁定工作表中的某些特定单元格，则必须解锁工作表中的所有其他单元格。工作表中的所有单元格都已初始化为锁定，您可以检查此打开任何 excel 文件到 MS Excel 并单击**格式 | Cells...**以显示**格式 Cells**对话框，然后单击**保护**选项卡并看到标记为“已锁定”的复选框默认处于选中状态。

以下几点描述了如何使用 MS Excel 锁定几个单元格。此方法适用于Microsoft Office Excel 97、2000、2002、2003及以上版本。

1. 通过单击选择整个工作表**全选**按钮（第 1 行行号正上方和列字母 A 左侧的灰色矩形）。
1. 点击**Cells**在**格式**菜单，单击**保护**选项卡，然后清除**锁定**复选框。
这将解锁工作表上的所有单元格
如果**Cells**命令不可用，部分工作表可能已被锁定。在**工具**菜单，指向**保护** 然后点击**取消保护工作表**.
1. 只选择要锁定的单元格并重复步骤 2，但这次选择**锁定**复选框。
1. 在**工具**菜单，指向**保护** ， 点击**保护表**然后点击**好的**.
1. 在里面**保护表**对话框中，您可以选择指定密码并选择您希望用户能够更改的元素。

### **保护Worksheet中的几个Cells Using Aspose Cells**

在这个方法中，我们只使用 Aspose.Cells API 来完成任务。

示例：以下示例展示了如何保护工作表中的几个单元格。它首先解锁工作表中的所有单元格，然后锁定其中的 3 个单元格（A1、B1、C1）。最后，它保护工作表。这[**风格**](https://reference.aspose.com/cells/net/aspose.cells/style)对象包含一个布尔属性，[**被锁住了**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/islocked) .你可以设置[**被锁住了**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/islocked)属性为真或假并应用*列/行.ApplyStyle()*使用所需属性锁定或解锁行/列的方法。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Security-Protecting-ProtectingSpecificCellsinaWorksheet-1.cs" >}}

### **保护工作表中的一行**

Aspose.Cells 允许您轻松锁定工作表中的任何行。在这里，我们可以利用[**应用样式()**](https://reference.aspose.com/cells/net/aspose.cells/row/methods/applystyle)的方法[**Aspose.Cells.Row**](https://reference.aspose.com/cells/net/aspose.cells/row)类申请[**风格**](https://reference.aspose.com/cells/net/aspose.cells/style)到工作表中的特定行。这个方法有两个参数：一个[**风格**](https://reference.aspose.com/cells/net/aspose.cells/style)对象和[**风格旗帜**](https://reference.aspose.com/cells/net/aspose.cells/styleflag)具有与应用格式相关的所有成员的对象。

下面的示例演示如何保护工作表中的一行。它首先解锁工作表中的所有单元格，然后锁定其中的第一行。最后，它保护工作表。这[**风格**](https://reference.aspose.com/cells/net/aspose.cells/style)对象包含一个布尔属性，[**被锁住了**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/islocked) .你可以设置[**被锁住了**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/islocked)属性设置为 true 或 false 以使用[**风格旗帜**](https://reference.aspose.com/cells/net/aspose.cells/styleflag)目的。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Security-Protecting-ProtectingSpecificRowInWorksheet-1.cs" >}}

### **保护工作表中的列**

Aspose.Cells 允许您轻松锁定工作表中的任何列。在这里，我们可以利用[**应用样式()**](https://reference.aspose.com/cells/net/aspose.cells/column/methods/applystyle)的方法[**Aspose.Cells.Column**](https://reference.aspose.com/cells/net/aspose.cells/column)类申请[**风格**](https://reference.aspose.com/cells/net/aspose.cells/style)到工作表中的特定列。这个方法有两个参数：一个[**风格**](https://reference.aspose.com/cells/net/aspose.cells/style)对象和[**风格旗帜**](https://reference.aspose.com/cells/net/aspose.cells/styleflag)具有与应用格式相关的所有成员的对象。

以下示例显示如何保护工作表中的列。它首先解锁工作表中的所有单元格，然后锁定其中的第一列。最后，它保护工作表。这[**风格**](https://reference.aspose.com/cells/net/aspose.cells/style)对象包含一个布尔属性，[**被锁住了**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/islocked) .你可以设置[**被锁住了**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/islocked)属性设置为 true 或 false 以使用[**风格旗帜**](https://reference.aspose.com/cells/net/aspose.cells/styleflag)目的。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Security-Protecting-ProtectColumnWorksheet-1.cs" >}}

### **允许用户编辑范围**

以下示例显示如何允许用户编辑受保护工作表中的范围。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Security-Protecting-EditRangesWorksheet-1.cs" >}}

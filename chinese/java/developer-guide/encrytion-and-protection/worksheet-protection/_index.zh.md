---
title: 保护和取消保护工作表
type: docs
weight: 50
url: /zh/java/protect-and-unprotect-worksheet/
---

## **保护工作表**

当工作表受到保护时，用户可以执行的操作受到限制。例如，他们无法输入数据，插入或删除行或列等。 Microsoft Excel的一般保护选项包括：

- 内容
- 对象
- 方案

受保护的工作表不隐藏或保护敏感数据，因此与文件加密不同。一般来说，工作表保护适用于演示目的。它可以防止最终用户修改工作表中的数据、内容和格式。

### **添加或移除保护**

Aspose.Cells提供一个表示Microsoft Excel文件的[**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)类。 Workbook类包含一个WorksheetCollection，允许访问Excel文件中的每个工作表。工作表由[**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)类表示。

Worksheet类提供[**Protect**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#protect(int))方法，用于向工作表应用保护。Protect方法接受以下参数：

- 保护类型，要在工作表上应用的保护类型。保护类型是通过[**ProtectionType**](https://reference.aspose.com/cells/java/com.aspose.cells/ProtectionType)枚举来应用的。
- 新密码，用于保护工作表的新密码。
- 旧密码，如果工作表已受密码保护，则为旧密码。如果工作表尚未受保护，则只需传递null。

ProtectionType枚举包含以下预定义的保护类型：

|**保护类型**|**描述**|
| :- | :- |
|[**ALL**](https://reference.aspose.com/cells/java/com.aspose.cells/protectiontype#ALL)|用户无法修改此工作表中的任何内容|
|[**CONTENTS**](https://reference.aspose.com/cells/java/com.aspose.cells/protectiontype#CONTENTS)|用户无法在此工作表中输入数据|
|[**OBJECTS**](https://reference.aspose.com/cells/java/com.aspose.cells/protectiontype#OBJECTS)|用户无法修改绘图对象|
|[**SCENARIOS**](https://reference.aspose.com/cells/java/com.aspose.cells/protectiontype#SCENARIOS)|用户无法修改保存的方案|
|[**STRUCTURE**](https://reference.aspose.com/cells/java/com.aspose.cells/protectiontype#STRUCTURE)|用户无法修改保存的结构|
|[**WINDOWS**](https://reference.aspose.com/cells/java/com.aspose.cells/protectiontype#WINDOWS)|用户无法修改保存的窗口|
|[**NONE**](https://reference.aspose.com/cells/java/com.aspose.cells/protectiontype#NONE)|无保护|

下面的示例展示了如何使用密码保护工作表。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-ProtectingWorksheet-ProtectingWorksheet.java" >}}

在以上代码用于保护工作表后，通过打开它来检查工作表上的保护。一旦您打开文件并尝试向工作表添加一些数据，将显示以下对话框：

**警告对话框，用户无法修改工作表** 

![todo:image_alt_text](protect-and-unprotect-worksheet_1.png)

要处理工作表，需要选择**保护**，然后从**工具**菜单项中选择**取消工作表保护**。

**选择取消保护工作表菜单项** 

![todo:image_alt_text](protect-and-unprotect-worksheet_2.png)

弹出一个对话框提示输入密码。

**输入密码解除工作表保护** 

![todo:image_alt_text](protect-and-unprotect-worksheet_3.png)

### **保护少数单元格**

在工作表中可能需要锁定部分特定单元格的情况下，您必须解锁工作表中的所有其他单元格。工作表中的所有单元格已经初始化为锁定，您可以通过打开任何 Excel 文件到 MS Excel 并单击**格式 | 单元格...**来查看**格式单元格**对话框，然后单击保护选项卡，并查看一个名为“已锁定”的复选框默认会被选中。

以下是实现该任务的两种方法。

**方法1:**

以下几点描述了如何使用MS Excel锁定几个单元格。该方法适用于Microsoft Office Excel 97, 2000, 2002, 2003及更高版本。

1. 通过单击“全选”按钮（即位于行号为1的行号正上方和列号字母A左侧的灰色矩形）选择整个工作表。
1. 在“格式”菜单中点击单元格，点击保护选项卡，然后取消“锁定”复选框的选中状态。

   这将解锁工作表上的所有单元格。

{{% alert color="primary" %}}

如果“单元格”命令不可用，则工作表的部分可能已被锁定。在“工具”菜单上，指向“保护”，然后点击“取消工作表保护”。

{{% /alert %}}

1. 仅选择要锁定的单元格，然后重复步骤2，但这次选中“锁定”复选框。
1. 在**工具**菜单中，选择**保护**，单击**保护工作表**，然后单击**确定**。

{{% alert color="primary" %}}

在“保护工作表”对话框中，可以指定密码并选择要允许用户更改的元素。

{{% /alert %}}

**方法2:**

在此方法中，我们仅使用Aspose.Cells API来执行任务。

以下示例展示如何在工作表中保护少数单元格。首先解锁工作表中的所有单元格，然后锁定其中的3个单元格（A1、B1、C1）。最后，保护工作表。行/列有一个样式 API，其中进一步包含了一个设置锁定状态的方法。您可以使用这个方法来锁定或解锁行/列。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-ProtectingSpecificCellsinaWorksheet-ProtectingSpecificCellsinaWorksheet.java" >}}

### **在工作表中保护一行**

Aspose.Cells 允许您轻松锁定工作表中的任何行。在这里，我们可以使用[**applyStyle()**](https://reference.aspose.com/cells/java/com.aspose.cells/row#applyStyle(com.aspose.cells.Style,%20com.aspose.cells.StyleFlag)类的[**Row**](https://reference.aspose.com/cells/java/com.aspose.cells/Row)方法，应用样式到工作表中的特定行。该方法接受两个参数：一个[**Style**](https://reference.aspose.com/cells/java/com.aspose.cells/Style)对象和一个[**StyleFlag**](https://reference.aspose.com/cells/java/com.aspose.cells/StyleFlag)结构，其中包含了所有与应用格式相关的成员。

以下示例展示如何在工作表中保护一行。首先解锁工作表中的所有单元格，然后锁定其中的第一行。最后，保护工作表。行/列有一个样式 API，其中进一步包含了一个设置单元格锁定状态的方法。您可以使用样式标志结构来锁定或解锁行/列。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-ProtectRowWorksheet-ProtectRowWorksheet.java" >}}

### **保护工作表中的列**

Aspose.Cells 允许您轻松锁定工作表中的任何列。在这里，我们可以使用[**applyStyle()**](https://reference.aspose.com/cells/java/com.aspose.cells/column#applyStyle(com.aspose.cells.Style,%20com.aspose.cells.StyleFlag)类的[**Column**](https://reference.aspose.com/cells/java/com.aspose.cells/Column)方法，应用样式到工作表中的特定列。该方法接受两个参数：一个[**Style**](https://reference.aspose.com/cells/java/com.aspose.cells/Style)对象和一个[**StyleFlag**](https://reference.aspose.com/cells/java/com.aspose.cells/StyleFlag)结构，其中包含了所有与应用格式相关的成员。

以下示例展示如何在工作表中保护一列。首先解锁工作表中的所有单元格，然后锁定其中的第一列。最后，保护工作表。行/列有一个样式 API，其中进一步包含了一个设置锁定状态的方法。您可以使用样式标志结构来锁定或解锁行/列。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-ProtectColumnWorksheet-ProtectColumnWorksheet.java" >}}

## **取消保护工作表**

[保护工作表](/cells/zh/java/protect-and-unprotect-worksheet/#protect-worksheets) 和 [自 Excel XP 以来的高级保护设置](/cells/zh/java/protect-and-unprotect-worksheet/#advanced-protection-settings-since-excel-xp)讨论了保护工作表的不同方法。如果开发人员需要在运行时从受保护的工作表中移除保护以使对文件进行一些更改，那么 Aspose.Cells 可以轻松完成这一操作。

### **使用Microsoft Excel**

要从工作表中取消保护：

从**工具**菜单中选择**保护**，然后选择**取消工作表保护**。

**选择取消保护工作表** 

![todo:image_alt_text](protect-and-unprotect-worksheet_4.png)

保护已移除，除非工作表有密码保护。在这种情况下，会弹出一个对话框要求输入密码。

**输入密码解除工作表保护** 

![todo:image_alt_text](protect-and-unprotect-worksheet_5.png)

### **使用Aspose.Cells**

可以调用[**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)类的[**Unprotect**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#unprotect()方法来取消保护工作表。[**Unprotect**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#unprotect()方法可以以以下两种方式使用。

### **解除简单保护的工作表**

简单保护的工作表是不用密码保护的工作表。可以通过调用无需传递参数的取消保护方法来取消这些工作表的保护。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-UnprotectingSimplyProtectedWorksheet-UnprotectingSimplyProtectedWorksheet.java" >}}

### **解除密码保护的工作表**

受密码保护的工作表是使用密码保护的工作表。可以通过调用采用密码作为参数的Unprotect方法的重载版本来取消对这些工作表的保护。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-UnprotectProtectSheet-UnprotectProtectSheet.java" >}}

## **自Excel XP起的高级保护设置**

[保护工作表](/cells/zh/java/protect-and-unprotect-worksheet/#protect-worksheets)讨论了在 Microsoft Excel 97 和 2000 中保护工作表的方法。但自 Excel 2002 或 XP 发布以来，Microsoft 添加了许多高级保护设置。这些保护设置限制或允许用户执行以下操作：

- 删除行或列。
- 编辑内容、对象或场景。
- 格式化单元格、行或列。
- 插入行、列或超链接。
- 选择锁定或解锁的单元格。
- 使用数据透视表等等。

Aspose.Cells支持Excel XP和更高版本提供的所有高级保护设置。

### **使用Excel XP和更高版本的高级保护设置**

查看Excel XP中可用的保护设置:

1. 从**工具**菜单中选择**保护**，然后选择**保护工作表**。
   会显示一个对话框。

   **Excel XP中显示保护选项的对话框**

![todo:image_alt_text](protect-and-unprotect-worksheet_6.png)

1. 允许或限制工作表功能或应用密码。

### **使用Aspose.Cells进行高级保护设置**

Aspose.Cells支持所有高级保护设置。

Aspose.Cells提供一个类，[**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)，表示一个Microsoft Excel文件。Workbook类包含一个WorksheetCollection集合，允许访问Excel文件中的每个工作表。一个工作表由[**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)类表示。

Worksheet类提供了Protection属性，用于应用这些高级保护设置。Protection属性实际上是[**Protection**](https://reference.aspose.com/cells/java/com.aspose.cells/protection)类的对象，该对象封装了几个布尔属性，用于禁用或启用限制。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-AdvancedProtectionSettingsUsingAsposeCells-AdvancedProtectionSettingsUsingAsposeCells.java" >}}

以下是一个简单的示例应用程序。它打开一个Excel文件，并使用Excel XP及更高版本支持的大多数高级保护设置。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-AdvancedProtection-AdvancedProtection.java" >}}

{{% alert color="primary" %}}

将文件保存为EXCEL97TO2003或XLSX格式，因为这些高级保护设置仅受MS Excel XP和更高版本的支持。

{{% /alert %}}

### **单元格锁定问题**

如果您想要限制用户编辑单元格，必须在应用任何保护设置之前锁定单元格。否则，即使工作表受到保护，也可以编辑单元格。在 Microsoft Excel XP 中，可以通过以下对话框来锁定单元格：

**Excel XP中锁定单元格的对话框** 

![todo:image_alt_text](protect-and-unprotect-worksheet_7.png)

也可以使用Aspose.Cells API来锁定单元格。每个单元格都有一个Style API，它进一步包含一个setLocked方法。使用它来锁定或解锁单元格。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-LockCell-LockCell.java" >}}

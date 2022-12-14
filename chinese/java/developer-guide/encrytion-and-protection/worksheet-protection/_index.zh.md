---
title: 保护和取消保护工作表
type: docs
weight: 50
url: /zh/java/protect-and-unprotect-worksheet/
---
## **保护工作表**

当工作表受到保护时，用户可以执行的操作将受到限制。例如，他们不能输入数据，插入或删除行或列等。Microsoft Excel中的一般保护选项是：

- 内容
- 对象
- 场景

受保护的工作表不会隐藏或保护敏感数据，因此它不同于文件加密。通常，工作表保护适用于演示目的。它可以防止最终用户修改工作表中的数据、内容和格式。

### **添加或删除保护**

Aspose.Cells提供了一个类，[**工作簿**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)，代表一个 Microsoft Excel 文件。 Workbook 类包含一个 WorksheetCollection，它允许访问 Excel 文件中的每个工作表。工作表由[**工作表**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)班级。

Worksheet 类提供了[**保护**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#protect(int)用于对工作表应用保护的方法。 Protect 方法接受以下参数：

- 保护类型，要在工作表上应用的保护类型。保护类型是在[**保护类型**](https://reference.aspose.com/cells/java/com.aspose.cells/ProtectionType)枚举。
- 新密码，用于保护工作表的新密码。
- Old Password，旧密码，如果工作表已经受密码保护。如果工作表尚未受到保护，则只需传递一个空值。

ProtectionType 枚举包含以下预定义的保护类型：

|**保护类型**|**描述**|
|:- |:- |
|[**全部**](https://reference.aspose.com/cells/java/com.aspose.cells/protectiontype#ALL)|用户不能修改此工作表上的任何内容|
|[**内容**](https://reference.aspose.com/cells/java/com.aspose.cells/protectiontype#CONTENTS)|用户不能在此工作表中输入数据|
|[**对象**](https://reference.aspose.com/cells/java/com.aspose.cells/protectiontype#OBJECTS)|用户不能修改绘图对象|
|[**场景**](https://reference.aspose.com/cells/java/com.aspose.cells/protectiontype#SCENARIOS)|用户无法修改已保存的场景|
|[**结构体**](https://reference.aspose.com/cells/java/com.aspose.cells/protectiontype#STRUCTURE)|用户不能修改保存的结构|
|[**视窗**](https://reference.aspose.com/cells/java/com.aspose.cells/protectiontype#WINDOWS)|用户不能修改保存的窗口|
|[**没有任何**](https://reference.aspose.com/cells/java/com.aspose.cells/protectiontype#NONE)|无保护|

下面的示例显示了如何使用密码保护工作表。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-ProtectingWorksheet-ProtectingWorksheet.java" >}}

上面的代码对工作表进行保护后，打开工作表检查保护。打开文件并尝试向工作表添加一些数据后，将显示以下对话框：

**警告用户无法修改工作表的对话框** 

![待办事项：图片_替代_文本](protect-and-unprotect-worksheet_1.png)

要处理工作表，请通过选择取消保护工作表**保护**， 然后**取消保护工作表**来自**工具**菜单项如下图所示。

**选择取消保护工作表菜单项** 

![待办事项：图片_替代_文本](protect-and-unprotect-worksheet_2.png)

将打开一个对话框，提示输入密码。

**输入密码以取消保护工作表** 

![待办事项：图片_替代_文本](protect-and-unprotect-worksheet_3.png)

### **保护少数 Cells**

在某些情况下，您可能只需要锁定工作表中的几个单元格。如果要锁定工作表中的某些特定单元格，则必须解锁工作表中的所有其他单元格。工作表中的所有单元格都已初始化为锁定，您可以检查此打开任何 excel 文件到 MS Excel 并单击**格式 | Cells...**以显示**格式 Cells**对话框，然后单击“保护”选项卡，可以看到标记为“已锁定”的复选框默认处于选中状态。

以下是实现任务的两种方法。

**方法一：**

以下几点描述了如何使用 MS Excel 锁定几个单元格。此方法适用于Microsoft Office Excel 97、2000、2002、2003及以上版本。

1. 通过单击“全选”按钮（第 1 行行号正上方和列字母 A 左侧的灰色矩形）选择整个工作表。
1. 单击格式菜单上的 Cells，单击保护选项卡，然后清除锁定复选框。

这将解锁工作表上的所有单元格

{{% alert color="primary" %}}

如果单元格命令不可用，则部分工作表可能已被锁定。在工具菜单上，指向保护，然后单击取消保护工作表。

{{% /alert %}}

1. 仅选择要锁定的单元格并重复步骤 2，但这次选中“锁定”复选框。
1. 在**工具**菜单，选择**保护** ， 点击**保护表** 然后点击**好的**.

{{% alert color="primary" %}}

在“保护工作表”对话框中，您可以选择指定密码并选择您希望用户能够更改的元素。

{{% /alert %}}

**方法二：**

在这个方法中，我们只使用 Aspose.Cells API 来完成任务。

以下示例展示了如何保护工作表中的几个单元格。它首先解锁工作表中的所有单元格，然后锁定其中的 3 个单元格（A1、B1、C1）。最后，它保护工作表。行/列有一个 Style API，它进一步包含一个 set Locked 方法。您可以使用此方法锁定或解锁行/列。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-ProtectingSpecificCellsinaWorksheet-ProtectingSpecificCellsinaWorksheet.java" >}}

### **保护工作表中的一行**

Aspose.Cells 允许您轻松锁定工作表中的任何行。在这里，我们可以利用[**应用样式()**](https://reference.aspose.com/cells/java/com.aspose.cells/row#applyStyle(com.aspose.cells.Style,%20com.aspose.cells.StyleFlag) ） 的方法[**排**](https://reference.aspose.com/cells/java/com.aspose.cells/Row)类将 Style 应用于工作表中的特定行。这个方法有两个参数：一个[**风格**](https://reference.aspose.com/cells/java/com.aspose.cells/Style)对象和[**风格旗帜**](https://reference.aspose.com/cells/java/com.aspose.cells/StyleFlag)结构，其中包含与应用格式相关的所有成员。

下面的示例演示如何保护工作表中的一行。它首先解锁工作表中的所有单元格，然后锁定其中的第一行。最后，它保护工作表。行/列的样式 API 进一步包含 setCellLocked 方法。您可以使用 StyleFlag 结构锁定或解锁行/列。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-ProtectRowWorksheet-ProtectRowWorksheet.java" >}}

### **保护工作表中的列**

Aspose.Cells 允许您轻松锁定工作表中的任何列。在这里，我们可以利用[**应用样式()**](https://reference.aspose.com/cells/java/com.aspose.cells/column#applyStyle(com.aspose.cells.Style,%20com.aspose.cells.StyleFlag) ） 的方法[**柱子**](https://reference.aspose.com/cells/java/com.aspose.cells/Column)类将 Style 应用于工作表中的特定列。这个方法有两个参数：一个[**风格**](https://reference.aspose.com/cells/java/com.aspose.cells/Style)对象和[**风格旗帜**](https://reference.aspose.com/cells/java/com.aspose.cells/StyleFlag)结构，其中包含与应用格式相关的所有成员。

以下示例显示如何保护工作表中的列。它首先解锁工作表中的所有单元格，然后锁定其中的第一列。最后，它保护工作表。行/列有一个 Style API，它进一步包含一个 set Locked 方法。您可以使用 StyleFlag 结构锁定或解锁行/列。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-ProtectColumnWorksheet-ProtectColumnWorksheet.java" >}}

## **取消保护工作表**

[保护工作表](/cells/zh/java/protect-and-unprotect-worksheet/#protect-worksheets)和[自 Excel XP 以来的高级保护设置](/cells/zh/java/protect-and-unprotect-worksheet/#advanced-protection-settings-since-excel-xp)讨论了保护工作表的不同方法。如果开发人员需要在运行时从受保护的工作表中删除保护，以便可以对文件进行一些更改，该怎么办？使用 Aspose.Cells 可以轻松完成此操作。

### **使用 Microsoft Excel**

要取消对工作表的保护：

来自**工具**菜单，选择**保护**其次是**取消保护工作表**.

**选择取消保护工作表** 

![待办事项：图片_替代_文本](protect-and-unprotect-worksheet_4.png)

保护被移除，除非工作表受密码保护。在这种情况下，会出现一个对话框提示输入密码。

**输入密码以取消保护工作表** 

![待办事项：图片_替代_文本](protect-and-unprotect-worksheet_5.png)

### **使用 Aspose.Cells**

可以通过调用[**工作表**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)班级'[**取消保护**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#unprotect()） 方法。这[**取消保护**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#unprotect()方法可以以两种方式使用，如下所述。

### **取消保护简单保护的工作表**

简单保护的工作表是不受密码保护的工作表。可以通过调用 unprotect 方法而不传递参数来解除对此类工作表的保护。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-UnprotectingSimplyProtectedWorksheet-UnprotectingSimplyProtectedWorksheet.java" >}}

### **取消保护受密码保护的工作表**

受密码保护的工作表是受密码保护的工作表。通过调用将密码作为参数的 Unprotect 方法的重载版本，可以解除对此类工作表的保护。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-UnprotectProtectSheet-UnprotectProtectSheet.java" >}}

## **自 Excel XP 以来的高级保护设置**

[保护工作表](/cells/zh/java/protect-and-unprotect-worksheet/#protect-worksheets)在 Microsoft Excel 97 和 2000 中讨论了保护工作表。但是自从 Excel 2002 或 XP 发布以来，Microsoft 增加了许多高级保护设置。这些保护设置限制或允许用户：

- 删除行或列。
- 编辑内容、对象或场景。
- 格式化单元格、行或列。
- 插入行、列或超链接。
- 选择锁定或解锁的单元格。
- 使用数据透视表等等。

Aspose.Cells 支持 Excel XP 及更高版本提供的所有高级保护设置。

### **使用 Excel XP 及更高版本的高级保护设置**

查看 Excel XP 中可用的保护设置：

1. 来自**工具**菜单，选择**保护**其次是**保护表**.
显示一个对话框。

   **在 Excel XP 中显示保护选项的对话框**

![待办事项：图片_替代_文本](protect-and-unprotect-worksheet_6.png)

1. 允许或限制工作表功能或应用密码。

### **使用 Aspose.Cells 的高级保护设置**

Aspose.Cells 支持所有高级保护设置。

Aspose.Cells提供了一个类，[**工作簿**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) ，代表一个 Microsoft Excel 文件。 Workbook 类包含一个 WorksheetCollection 集合，它允许访问 Excel 文件中的每个工作表。工作表由[**工作表**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)班级。

Worksheet 类提供了用于应用这些高级保护设置的 Protection 属性。 Protection 属性实际上是[**保护**](https://reference.aspose.com/cells/java/com.aspose.cells/protection)封装了几个用于禁用或启用限制的布尔属性的类。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-AdvancedProtectionSettingsUsingAsposeCells-AdvancedProtectionSettingsUsingAsposeCells.java" >}}

下面是一个小的示例应用程序。它打开一个 Excel 文件并使用 Excel XP 和更高版本支持的大部分高级保护设置。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-AdvancedProtection-AdvancedProtection.java" >}}

{{% alert color="primary" %}}

将文件保存为 EXCEL97TO2003 或 XLSX 格式，因为这些高级保护设置只有 MS Excel XP 及更高版本才支持。

{{% /alert %}}

### **Cell 锁定问题**

如果要限制用户编辑单元格，则必须在应用任何保护设置之前锁定单元格。否则，即使工作表受到保护，也可以编辑单元格。在 Microsoft Excel XP 中，可以通过以下对话框锁定单元格：

**在 Excel XP 中锁定单元格的对话框** 

![待办事项：图片_替代_文本](protect-and-unprotect-worksheet_7.png)

也可以使用 Aspose.Cells API 锁定单元格。每个单元格都有一个 Style API，它还包含一个 setLocked 方法。使用它锁定或解锁单元格。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-LockCell-LockCell.java" >}}

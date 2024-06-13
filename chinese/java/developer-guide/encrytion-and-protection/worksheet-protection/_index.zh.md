---
title: 保护和取消保护工作表
type: docs
weight: 50
url: /zh/java/protect-and-unprotect-worksheet/
---

## **保护工作表**

当工作表受到保护时，用户可以执行的操作受到限制。例如，他们无法输入数据，插入或删除行或列等。Microsoft Excel中的一般保护选项为：

- 内容
- 对象
- 方案

受保护的工作表不隐藏或保护敏感数据，因此与文件加密不同。一般来说，工作表保护适用于展示目的。它阻止最终用户修改工作表中的数据、内容和格式。

### **添加或移除保护**

Aspose.Cells提供一个表示Microsoft Excel文件的类，[**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)。Workbook类包含一个WorksheetCollection，允许访问Excel文件中的每个工作表。工作表由[**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)类表示。

工作表类提供了[**Protect**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#protect(int))方法，用于对工作表应用保护。Protect方法接受以下参数：

- 保护类型，应用于工作表的保护类型。保护类型是使用[**ProtectionType**](https://reference.aspose.com/cells/java/com.aspose.cells/ProtectionType)枚举来应用的。
- 新密码，用于保护工作表的新密码。
- 旧密码，如果工作表已经受到密码保护。如果工作表尚未受保护，则只需传递null。

ProtectionType枚举包含以下预定义的保护类型：

|**保护类型**|**描述**|
| :- | :- |
|[**ALL**](https://reference.aspose.com/cells/java/com.aspose.cells/protectiontype#ALL)| 用户无法对工作表上的任何内容进行修改
|[**CONTENTS**](https://reference.aspose.com/cells/java/com.aspose.cells/protectiontype#CONTENTS)| 用户无法在工作表中输入数据
|[**OBJECTS**](https://reference.aspose.com/cells/java/com.aspose.cells/protectiontype#OBJECTS)| 用户无法修改绘图对象
|[**SCENARIOS**](https://reference.aspose.com/cells/java/com.aspose.cells/protectiontype#SCENARIOS)|用户无法修改保存的场景|
|[**STRUCTURE**](https://reference.aspose.com/cells/java/com.aspose.cells/protectiontype#STRUCTURE)|用户无法修改保存的结构|
|[**WINDOWS**](https://reference.aspose.com/cells/java/com.aspose.cells/protectiontype#WINDOWS)|用户无法修改保存的窗口|
|[**NONE**](https://reference.aspose.com/cells/java/com.aspose.cells/protectiontype#NONE)|无保护|

下例显示如何使用密码保护工作表。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-ProtectingWorksheet-ProtectingWorksheet.java" >}}

使用上述代码保护工作表后，通过打开文件检查工作表的保护。一旦打开文件并尝试向工作表添加一些数据，将显示以下对话框：

提示用户无法修改工作表的对话框警告 

![todo:image_alt_text](protect-and-unprotect-worksheet_1.png)

要在工作表上工作，选择“保护”，然后从“工具”菜单项中选择“取消保护工作表”，如下所示。

选择“取消保护工作表”菜单项 

![todo:image_alt_text](protect-and-unprotect-worksheet_2.png)

打开提示输入密码的对话框。

输入密码以取消保护工作表 

![todo:image_alt_text](protect-and-unprotect-worksheet_3.png)

### **保护少数单元格**

可能存在某些场景，您需要仅锁定工作表中的少数单元格。如果要锁定工作表中的某些特定单元格，您必须解锁工作表中的所有其他单元格。工作表中的所有单元格已初始化为锁定状态，您可以通过将任何 Excel 文件打开到 MS Excel 中并单击“格式|单元格...”来检查此情况，以显示“格式单元格”对话框然后单击“保护”选项卡，查看是否默认勾选了一个名为“锁定”的复选框。

以下是实现任务的两种方法。

方法1：

以下描述如何使用 MS Excel 锁定一些单元格。此方法适用于 Microsoft Office Excel 97、2000、2002、2003 及更高版本。

1. 通过点击“全选”按钮（位于行号 1 上方且列标 A 左侧的灰色矩形）选择整个工作表。
1. 在“格式”菜单中点击“单元格”，点击“保护”选项卡，然后清除“锁定”复选框。

   这将解锁工作表上的所有单元格。

{{% alert color="primary" %}}

如果“单元格”命令不可用，工作表的部分内容可能已被锁定。在“工具”菜单上，指向“保护”，然后单击“取消保护工作表”。

{{% /alert %}}

1. 仅选择要锁定的单元格，然后重复步骤2，但这次选择“锁定”复选框。
1. 在“工具”菜单上，选择“保护”，单击“保护工作表”，然后单击“确定”。

{{% alert color="primary" %}}

在“保护工作表”对话框中，您可以选择指定密码并选择要允许用户更改的元素。

{{% /alert %}}

方法2:

在这种方法中，我们只使用Aspose.Cells API来执行此任务。

下面的示例展示了如何在工作表中保护几个单元格。首先它解锁工作表中的所有单元格，然后锁定其中的3个单元格（A1，B1，C1）。最后，保护工作表。行/列有一个Style API，进一步包含了一个set Locked方法。您可以使用此方法来锁定或解锁行/列。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-ProtectingSpecificCellsinaWorksheet-ProtectingSpecificCellsinaWorksheet.java" >}}

### **在工作表中保护一行**

Aspose.Cells允许您轻松地锁定工作表中的任何行。在这里，我们可以利用[**Row**](https://reference.aspose.com/cells/java/com.aspose.cells/Row)类的[**applyStyle()**](https://reference.aspose.com/cells/java/com.aspose.cells/row#applyStyle(com.aspose.cells.Style,%20com.aspose.cells.StyleFlag))方法来将样式应用到工作表中的特定行。此方法接受两个参数：[**Style**](https://reference.aspose.com/cells/java/com.aspose.cells/Style)对象和[**StyleFlag**](https://reference.aspose.com/cells/java/com.aspose.cells/StyleFlag)结构，该结构具有所有与应用格式相关的成员。

下面的示例显示了如何在工作表中保护一行。首先它解锁工作表中的所有单元格，然后锁定其中的第一行。最后，保护工作表。行/列有一个Style API，进一步包含了一个setCellLocked方法。您可以使用StyleFlag结构来锁定或解锁行/列。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-ProtectRowWorksheet-ProtectRowWorksheet.java" >}}

### **在工作表中保护一列**

Aspose.Cells允许您轻松地锁定工作表中的任何列。在这里，我们可以利用[**Column**](https://reference.aspose.com/cells/java/com.aspose.cells/Column)类的[**applyStyle()**](https://reference.aspose.com/cells/java/com.aspose.cells/column#applyStyle(com.aspose.cells.Style,%20com.aspose.cells.StyleFlag))方法来将样式应用到工作表中的特定列。此方法接受两个参数：[**Style**](https://reference.aspose.com/cells/java/com.aspose.cells/Style)对象和[**StyleFlag**](https://reference.aspose.com/cells/java/com.aspose.cells/StyleFlag)结构，该结构具有所有与应用格式相关的成员。

下面的示例显示了如何在工作表中保护一列。首先它解锁工作表中的所有单元格，然后锁定其中的第一列。最后，保护工作表。行/列有一个Style API，进一步包含了一个set Locked方法。您可以使用StyleFlag结构来锁定或解锁行/列。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-ProtectColumnWorksheet-ProtectColumnWorksheet.java" >}}

## **取消保护工作表**

[保护工作表](/cells/zh/java/protect-and-unprotect-worksheet/#protect-worksheets)和[Excel XP以来的高级保护设置](/cells/zh/java/protect-and-unprotect-worksheet/#advanced-protection-settingssince-excel-xp)讨论了不同的保护工作表的方法。如果开发人员需要在运行时从受保护的工作表中移除保护，以便对文件进行一些更改，怎么办？Aspose.Cells可以轻松实现此目的。

### **使用Microsoft Excel**

要取消工作表的保护：

从“工具”菜单中，选择“保护”，然后选择“取消保护工作表”。

选择“取消保护工作表” 

![todo:image_alt_text](protect-and-unprotect-worksheet_4.png)

保护已被移除，除非工作表有密码保护。在这种情况下，会提示输入密码。

输入密码以取消保护工作表 

![todo:image_alt_text](protect-and-unprotect-worksheet_5.png)

### **使用Aspose.Cells**

可以通过调用[**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)类的[**Unprotect**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#unprotect--)方法来取消工作表的保护。 [**Unprotect**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#unprotect--)方法可以有两种用法，如下所述。

### **取消简单保护的工作表**

一个简单的受保护工作表是没有使用密码保护的工作表。这种工作表可以通过调用unprotect方法来取消保护，而无需传递参数。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-UnprotectingSimplyProtectedWorksheet-UnprotectingSimplyProtectedWorksheet.java" >}}

### **取消密码保护的工作表**

受密码保护的工作表是使用密码进行保护的工作表。这种工作表可以通过调用带有密码参数的Unprotect方法的重载版本来取消保护。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-UnprotectProtectSheet-UnprotectProtectSheet.java" >}}

## **自 Excel XP 以来的高级保护设置**

[保护工作表](/cells/zh/java/protect-and-unprotect-worksheet/#protect-worksheets)讨论了Microsoft Excel 97和2000中的工作表保护。但自Excel 2002或XP发布以来，Microsoft添加了许多高级保护设置。这些保护设置限制或允许用户：

- 删除行或列。
- 编辑内容、对象或方案。
- 格式化单元格、行或列。
- 插入行、列或超链接。
- 选择锁定或解锁的单元格。
- 使用数据透视表等功能。

Aspose.Cells支持Excel XP及更高版本提供的所有高级保护设置。

### **使用Excel XP和更高版本的高级保护设置**

要查看Excel XP中提供的保护设置：

1. 从**工具**菜单中选择**保护**，然后选择**保护工作表**。
   将显示对话框。

   **在Excel XP中显示保护选项的对话框**

![todo:image_alt_text](protect-and-unprotect-worksheet_6.png)

1. 允许或限制工作表功能或应用密码。

### **使用Aspose.Cells的高级保护设置**

Aspose.Cells支持所有高级保护设置。

Aspose.Cells 提供了一个表示 Microsoft Excel 文件的 Workbook 类。Workbook 类包含一个 WorksheetCollection 集合，允许访问 Excel 文件中的每个工作表。工作表由 Worksheet 类表示。

Worksheet 类提供了 Protection 属性，用于应用这些高级保护设置。Protection 属性实际上是 [**Protection**](https://reference.aspose.com/cells/java/com.aspose.cells/protection) 类的对象，封装了几个布尔属性，用于禁用或启用限制。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-AdvancedProtectionSettingsUsingAsposeCells-AdvancedProtectionSettingsUsingAsposeCells.java" >}}

下面是一个小例子应用程序。它打开一个 Excel 文件，并使用 Excel XP 及更新版本支持的大部分高级保护设置。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-AdvancedProtection-AdvancedProtection.java" >}}

{{% alert color="primary" %}}

将文件保存为 EXCEL97TO2003 或 XLSX 格式，因为这些高级保护设置仅受到 MS Excel XP 和更高版本的支持。

{{% /alert %}}

### **单元格锁定问题**

如果要限制用户编辑单元格，必须在应用任何保护设置之前锁定单元格。否则，即使工作表受到保护，也可以编辑单元格。在 Microsoft Excel XP 中，可以通过以下对话框锁定单元格：

**Excel XP 中锁定单元格的对话框** 

![todo:image_alt_text](protect-and-unprotect-worksheet_7.png)

还可以使用 Aspose.Cells API 锁定单元格。每个单元格都有一个 Style API，其中进一步包含了 setLocked 方法。使用它来锁定或解锁单元格。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-LockCell-LockCell.java" >}}

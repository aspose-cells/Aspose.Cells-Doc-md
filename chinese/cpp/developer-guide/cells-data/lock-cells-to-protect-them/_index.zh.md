---
title: 如何用C++锁定单元格以保护它们
linktitle: 如何锁定单元格以保护它们
type: docs
weight: 130
url: /zh/cpp/how-to-lock-cells-to-protect-them/
description: 本文为您展示使用C++ 和 Aspose.Cells库锁定单元格以保护它们的示例代码。
keywords: 用C++锁定单元格以保护它们，如何用C++锁定单元格以保护它们，在C++中锁定单元格以保护它们。
---

## **可能的使用场景**
锁定单元格以保护它们是在电子表格应用程序中常见的做法，原因包括：

1. 防止意外更改：锁定单元格可以防止用户无意中修改重要数据或公式。在复杂的电子表格中尤其有用，因为不小心的更改会导致重大错误。

1. 保持数据完整性：通过锁定单元格，可以确保关键数据保持一致和准确。这对于财务文件、报告以及任何需要数据完整性的文件来说都是至关重要的。

1. 受控访问：在协作环境中，锁定单元格允许你控制谁可以编辑电子表格的某些部分。例如，你可能只允许特定团队成员编辑特定单元格，而保持其他区域受保护。

1. 保护公式：公式常用于计算与数据分析。锁定包含公式的单元格可以确保这些公式不被意外更改或删除，从而保持整个工作表的功能。

1. 强制执行业务规则：在某些情况下，特定的业务规则或规定可能要求保护某些数据，防止修改。锁定单元格可以帮助满足这些要求。

1. 引导用户：通过锁定单元格并提供明确指示哪些单元格可以编辑，可以引导用户如何与电子表格交互，减少混淆和错误。

## **如何在Excel中锁定单元格以保护它们**
下面介绍在Microsoft Excel中锁定单元格的方法：

1. 选择要锁定的单元格：选择你想要锁定的单元格。如果要锁定整个工作表，可以跳过此步骤。
1. 打开“格式单元格”对话框：右键点击所选单元格，选择“设置单元格格式”，或按Ctrl+1。
<br>
<img src="1.png" width=60% />
1. 锁定单元格：在“设置单元格格式”对话框中，转到“保护”选项卡。勾选“锁定”复选框。点击“确定”。
1. 保护工作表：在功能区的“审阅”选项卡中，点击“保护工作表”。设置密码（可选）并选择你想允许的权限（例如选择锁定单元格、设置单元格格式等）。点击“确定”。
<br>
<img src="2.png" width=60% />

## **如何使用 C++ 锁定单元格以进行保护**

Aspose.Cells 是一个强大的库，用于以编程方式操作 Excel 文件。要使用 Aspose.Cells 锁定单元格，你需要按照以下步骤：加载[示例文件](sample.xlsx)，先解锁所有单元格（因为默认所有单元格都已锁定，但在未保护工作表前未生效），然后锁定你想保护的特定单元格，最后保护工作表以强制锁定效果。

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Load the Excel file
    Workbook workbook(u"sample.xlsx");

    // Access the first worksheet
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Unlock all cells first
    Style unlockStyle = workbook.CreateStyle();
    unlockStyle.SetIsLocked(false);

    StyleFlag styleFlag;
    styleFlag.SetLocked(true);
    sheet.GetCells().ApplyStyle(unlockStyle, styleFlag);

    // Lock specific cells (e.g., A1 and B2)
    Style lockStyle = workbook.CreateStyle();
    lockStyle.SetIsLocked(true);

    sheet.GetCells().Get(u"A1").SetStyle(lockStyle);
    sheet.GetCells().Get(u"B2").SetStyle(lockStyle);

    // Protect the worksheet to enforce the locking
    sheet.Protect(ProtectionType::All);

    // Save the modified workbook
    workbook.Save(u"output_locked.xlsx");

    std::cout << "Worksheet protection applied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **输出结果**
此代码确保只有指定的单元格（此例中的A1和B2）被锁定，并对工作表进行保护以强制执行这些设置。工作表中的其他单元格保持未锁定且可编辑。

<br>
<img src="3.png" width=60% />

{{< app/cells/assistant language="cpp" >}}

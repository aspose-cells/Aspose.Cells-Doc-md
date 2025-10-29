---
title: 使用 C++ 保护工作表
linktitle: 保护工作表
type: docs
weight: 10
url: /zh/cpp/protecting-worksheets/
description: 了解如何使用 Aspose.Cells 与 C++ 保护 Microsoft Excel 文件中的工作表、行、列和特定单元格。
---

{{% alert color="primary" %}}

 当工作表被保护时，用户可以执行的操作受到限制。例如，他们不能输入数据、插入或删除行列等。

{{% /alert %}}

## **保护工作表**

### **介绍**

Microsoft Excel中的常规保护选项包括：

- 内容
- 对象
- 方案

受保护的工作表不会隐藏或保护敏感数据，因此它与文件加密不同。通常，工作表保护适用于展示目的。它防止最终用户修改工作表中的数据、内容和格式。

### **保护工作表**

Aspose.Cells提供了[**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)类，表示Microsoft Excel文件。[**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)类包含[**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)集合，允许访问Excel文件中的每个工作表。工作表由[**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)类表示。

[**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)类提供[**Protect**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/protect/)方法，用于在工作表上应用保护。[**Protect**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/protect/)方法接受以下参数：

- 保护类型，工作表上应用的保护类型。 保护类型是用 [**ProtectionType**](https://reference.aspose.com/cells/cpp/aspose.cells/protectiontype/) 枚举帮助应用的。
- 新密码，用于保护工作表的新密码。
- 旧密码，如果工作表已经受到密码保护，则传入旧密码。如果工作表尚未受到保护，则传递 null。

[**ProtectionType**](https://reference.aspose.com/cells/cpp/aspose.cells/protectiontype/)枚举包含以下预定义的保护类型：

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

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"book1.xls";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"output.out.xls";

    // Create workbook from the input file
    Workbook excel(inputFilePath);

    // Accessing the first worksheet in the Excel file
    Worksheet worksheet = excel.GetWorksheets().Get(0);

    // Protecting the worksheet with a password
    worksheet.Protect(ProtectionType::All, u"aspose", nullptr);

    // Saving the modified Excel file in default format
    excel.Save(outputFilePath, SaveFormat::Excel97To2003);

    std::cout << "Worksheet protected and file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

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

示例：以下示例展示了如何在工作表中保护一些单元格。首先解锁工作表中的所有单元格，然后锁定其中的3个单元格（A1、B1、C1）。最后，保护工作表。[**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) 对象包含一个布尔属性，[**IsLocked**](https://reference.aspose.com/cells/cpp/aspose.cells/style/islocked/)。您可以将 [**IsLocked**](https://reference.aspose.com/cells/cpp/aspose.cells/style/islocked/)属性设置为true或false，并应用*Column/Row.ApplyStyle()*方法来锁定或解锁带有所需属性的行/列。

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String outDir(u"../Data/02_OutputDirectory/");

    Workbook wb;
    Worksheet sheet = wb.GetWorksheets().Get(0);

    for(int i = 0; i <= 255; ++i)
    {
        Style style = sheet.GetCells().GetColumns().Get(i).GetStyle();
        style.SetIsLocked(false);

        StyleFlag flag;
        flag.SetLocked(true);

        sheet.GetCells().ApplyColumnStyle(i, style, flag);
    }

    auto lockCell = [&](const U16String& cellRef)
    {
        Style style = sheet.GetCells().Get(cellRef).GetStyle();
        style.SetIsLocked(true);
        sheet.GetCells().Get(cellRef).SetStyle(style);
    };

    lockCell(u"A1");
    lockCell(u"B1");
    lockCell(u"C1");

    sheet.Protect(ProtectionType::All);

    U16String outputPath = outDir + u"output.out.xls";
    wb.Save(outputPath, SaveFormat::Excel97To2003);

    std::cout << "Protected workbook created successfully." << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

### **在工作表中保护一行**

Aspose.Cells允许您轻松锁定工作表中的任何行。在这里，我们可以利用[**Row**](https://reference.aspose.com/cells/cpp/aspose.cells/row/)类的[**ApplyStyle()**](https://reference.aspose.com/cells/cpp/aspose.cells/row/applystyle/)方法来对工作表中的特定行应用[**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/)。该方法接受两个参数：[**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/)对象和包含所有与应用格式相关的成员的[**StyleFlag**](https://reference.aspose.com/cells/cpp/aspose.cells/styleflag/)对象。

下面的示例展示了如何在工作表中保护一行。首先解锁工作表中的所有单元格，然后锁定其中的第一行。最后，保护工作表。[**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/)对象包含一个布尔属性，[**IsLocked**](https://reference.aspose.com/cells/cpp/aspose.cells/style/islocked/)。您可以将[**IsLocked**](https://reference.aspose.com/cells/cpp/aspose.cells/style/islocked/)属性设置为true或false，以使用[**StyleFlag**](https://reference.aspose.com/cells/cpp/aspose.cells/styleflag/)对象锁定或解锁行/列。

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook wb;
    Worksheet sheet = wb.GetWorksheets().Get(0);

    for (int i = 0; i <= 255; i++)
    {
        Column column = sheet.GetCells().GetColumns().Get(i);
        Style style = column.GetStyle();
        style.SetIsLocked(false);
        StyleFlag flag;
        flag.SetLocked(true);
        column.ApplyStyle(style, flag);
    }

    Row firstRow = sheet.GetCells().GetRows().Get(0);
    Style rowStyle = firstRow.GetStyle();
    rowStyle.SetIsLocked(true);

    StyleFlag rowFlag;
    rowFlag.SetLocked(true);
    sheet.GetCells().ApplyRowStyle(0, rowStyle, rowFlag);

    sheet.Protect(ProtectionType::All);
    wb.Save(outDir + u"output.out.xls", SaveFormat::Excel97To2003);

    std::cout << "File saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **在工作表中保护一列**

Aspose.Cells允许您轻松锁定工作表中的任何列。在这里，我们可以利用[**Column**](https://reference.aspose.com/cells/cpp/aspose.cells/column/)类的[**ApplyStyle()**](https://reference.aspose.com/cells/cpp/aspose.cells/column/applystyle/)方法来对工作表中的特定列应用[**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/)。该方法接受两个参数：[**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/)对象和包含所有与应用格式相关的成员的[**StyleFlag**](https://reference.aspose.com/cells/cpp/aspose.cells/styleflag/)对象。

下面的示例展示了如何在工作表中保护一列。首先解锁工作表中的所有单元格，然后锁定其中的第一列。最后，保护工作表。[**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/)对象包含一个布尔属性，[**IsLocked**](https://reference.aspose.com/cells/cpp/aspose.cells/style/islocked/)。您可以将[**IsLocked**](https://reference.aspose.com/cells/cpp/aspose.cells/style/islocked/)属性设置为true或false，以使用[**StyleFlag**](https://reference.aspose.com/cells/cpp/aspose.cells/styleflag/)对象锁定或解锁行/列。

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    Workbook wb;
    Worksheet sheet = wb.GetWorksheets().Get(0);

    for (int i = 0; i <= 255; i++)
    {
        Style style = sheet.GetCells().GetColumns().Get((uint8_t)i).GetStyle();
        style.SetIsLocked(false);
        StyleFlag flag;
        flag.SetLocked(true);
        sheet.GetCells().GetColumns().Get((uint8_t)i).ApplyStyle(style, flag);
    }

    Style style = sheet.GetCells().GetColumns().Get(0).GetStyle();
    style.SetIsLocked(true);

    StyleFlag flag;
    flag.SetLocked(true);
    sheet.GetCells().GetColumns().Get(0).ApplyStyle(style, flag);

    sheet.Protect(ProtectionType::All);
    wb.Save(outDir + u"output.out.xls", SaveFormat::Excel97To2003);

    std::cout << "File saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **允许用户编辑范围**

下面的示例展示了如何允许用户在受保护的工作表中编辑范围。

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Instantiate a new Workbook
    Workbook book;

    // Get the first (default) worksheet
    Worksheet sheet = book.GetWorksheets().Get(0);

    // Get the Allow Edit Ranges
    ProtectedRangeCollection allowRanges = sheet.GetAllowEditRanges();

    // Create the range and get the ProtectedRange
    int idx = allowRanges.Add(u"r2", 1, 1, 3, 3);
    ProtectedRange protectedRange = allowRanges.Get(idx);

    // Specify the password
    protectedRange.SetPassword(u"123");

    // Protect the sheet
    sheet.Protect(ProtectionType::All);

    // Save the Excel file
    book.Save(outDir + u"protectedrange.out.xls");

    std::cout << "Protected range created successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}

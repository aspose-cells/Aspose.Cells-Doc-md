---
title: Protecting Worksheets with C++
linktitle: Protecting Worksheets
type: docs
weight: 10
url: /cpp/protecting-worksheets/
description: Learn how to protect worksheets, rows, columns, and specific cells in Microsoft Excel files using Aspose.Cells with C++.
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

When a worksheet is protected, the actions a user can take are restricted. For example, they cannot input data, insert or delete rows or columns, etc.

{{% /alert %}}

## **Protect Worksheets**

### **Introduction**

The general protection options in Microsoft Excel are:

- Contents
- Objects
- Scenarios

Protected worksheets don't hide or protect sensitive data, so they're different from file encryption. Generally, worksheet protection is suitable for presentation purposes. It prevents the end user from modifying data, content, and formatting in the worksheet.

### **Protect a Worksheet**

Aspose.Cells provides a class, [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/), that represents a Microsoft Excel file. The [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) class contains a [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) collection that allows access to each worksheet in an Excel file. A worksheet is represented by the [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) class.

The [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) class provides the **Protect** method that is used to apply protection on the worksheet. The **Protect** method accepts the following parameters:

- **Protection Type** – the type of protection to apply on the worksheet. The protection type is applied with the help of the **ProtectionType** enumeration.
- **New Password** – the new password used to protect the worksheet.
- **Old Password** – the old password, if the worksheet is already password‑protected. If the worksheet is not already protected, then just pass `null`.

The **ProtectionType** enumeration contains the following pre‑defined protection types:

| **Protection Types** | **Description**                              |
| -------------------- | -------------------------------------------- |
| All                  | The user cannot modify anything on this worksheet |
| Contents             | The user cannot enter data in this worksheet |
| Objects              | The user cannot modify drawing objects       |
| Scenarios            | The user cannot modify saved scenarios       |
| Structure            | The user cannot modify the structure         |
| Windows              | Protection is applied to windows            |
| None                 | No protection is applied                    |

The example below shows how to protect a worksheet with a password.

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

    // Access the first worksheet in the Excel file
    Worksheet worksheet = excel.GetWorksheets().Get(0);

    // Protect the worksheet with a password
    worksheet.Protect(ProtectionType::All, u"aspose", nullptr);

    // Save the modified Excel file in default format
    excel.Save(outputFilePath, SaveFormat::Excel97To2003);

    std::cout << "Worksheet protected and file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

After using the above code to protect the worksheet, you can verify the protection by opening the file. Once you open the file and try to add data to the worksheet, you will see the following dialog:

| **A dialog warning that a user can't modify the worksheet** |
| ------------------------------------------------------------ |
| ![todo:image_alt_text](protecting-worksheets_1.png)          |

To work on the worksheet, unprotect it by selecting **Protection**, then **Unprotect Sheet** from the **Tools** menu.

After you select the **Unprotect Sheet** menu item, a dialog will open prompting you to enter the password so that you can work on the worksheet, as shown below:

| ![todo:image_alt_text](protecting-worksheets_2.png) |
| --------------------------------------------------- |

### **Protect a Few Cells in the Worksheet Using Microsoft Excel**

There are scenarios where you need to lock only a few cells in the worksheet. To lock specific cells, you must first unlock all the other cells. All cells in a worksheet are initially set to be locked; you can verify this by opening any Excel file, choosing **Format → Cells…**, and checking the **Protection** tab where the **Locked** checkbox is selected by default.

The following steps describe how to lock a few cells using Microsoft Excel. This method applies to Microsoft Office Excel 97, 2000, 2002, 2003, and later versions.

1. Select the entire worksheet by clicking the **Select All** button (the gray rectangle above row 1 and to the left of column A).  
2. Click **Cells** on the **Format** menu, then the **Protection** tab, and clear the **Locked** checkbox. This unlocks all the cells on the worksheet.  
   *If the **Cells** command is not available, parts of the worksheet may already be locked. In that case, go to **Tools → Protection → Unprotect Sheet**.*  
3. Select the cells you want to lock and repeat step 2, this time checking the **Locked** checkbox.  
4. On the **Tools** menu, point to **Protection**, click **Protect Sheet**, and then click **OK**.  
5. In the **Protect Sheet** dialog box, you can specify a password and select the elements that users are allowed to change.

### **Protect a Few Cells in the Worksheet Using Aspose.Cells**

In this method, we use only the Aspose.Cells API to perform the task.

Example: The following code shows how to protect a few cells in the worksheet. It first unlocks all cells, then locks three cells (A1, B1, C1), and finally protects the worksheet. The [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) object contains a boolean property, **IsLocked**. You can set **IsLocked** to `true` or `false` and apply the style with `Column::ApplyStyle()` or `Row::ApplyStyle()`.

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

    // Unlock all cells
    for (int i = 0; i <= 255; ++i)
    {
        Style style = sheet.GetCells().GetColumns().Get(i).GetStyle();
        style.SetIsLocked(false);
        StyleFlag flag;
        flag.SetLocked(true);
        sheet.GetCells().ApplyColumnStyle(i, style, flag);
    }

    // Lock specific cells
    auto lockCell = [&](const U16String& cellRef)
    {
        Style style = sheet.GetCells().Get(cellRef).GetStyle();
        style.SetIsLocked(true);
        sheet.GetCells().Get(cellRef).SetStyle(style);
    };

    lockCell(u"A1");
    lockCell(u"B1");
    lockCell(u"C1");

    // Protect the worksheet
    sheet.Protect(ProtectionType::All);

    U16String outputPath = outDir + u"output.out.xls";
    wb.Save(outputPath, SaveFormat::Excel97To2003);

    std::cout << "Protected workbook created successfully." << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

### **Protect a Row in the Worksheet**

Aspose.Cells allows you to easily lock any row in the worksheet. Use the **ApplyStyle()** method of the **Row** class to apply a [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) to a specific row. This method takes two arguments: a [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) object and a **StyleFlag** object that contains the formatting flags.

The example below unlocks all cells, then locks the first row, and finally protects the worksheet.

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

    // Unlock all cells
    for (int i = 0; i <= 255; ++i)
    {
        Column column = sheet.GetCells().GetColumns().Get(i);
        Style style = column.GetStyle();
        style.SetIsLocked(false);
        StyleFlag flag;
        flag.SetLocked(true);
        column.ApplyStyle(style, flag);
    }

    // Lock the first row
    Row firstRow = sheet.GetCells().GetRows().Get(0);
    Style rowStyle = firstRow.GetStyle();
    rowStyle.SetIsLocked(true);
    StyleFlag rowFlag;
    rowFlag.SetLocked(true);
    sheet.GetCells().ApplyRowStyle(0, rowStyle, rowFlag);

    // Protect the worksheet
    sheet.Protect(ProtectionType::All);
    wb.Save(outDir + u"output.out.xls", SaveFormat::Excel97To2003);

    std::cout << "File saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Protect a Column in the Worksheet**

Aspose.Cells also lets you lock any column. Use the **ApplyStyle()** method of the **Column** class to apply a [**Style**](https://reference.aspose.com/cells/cpp/aspose.cells/style/) to a specific column.

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

    // Unlock all cells
    for (int i = 0; i <= 255; ++i)
    {
        Style style = sheet.GetCells().GetColumns().Get((uint8_t)i).GetStyle();
        style.SetIsLocked(false);
        StyleFlag flag;
        flag.SetLocked(true);
        sheet.GetCells().GetColumns().Get((uint8_t)i).ApplyStyle(style, flag);
    }

    // Lock the first column
    Style style = sheet.GetCells().GetColumns().Get(0).GetStyle();
    style.SetIsLocked(true);
    StyleFlag flag;
    flag.SetLocked(true);
    sheet.GetCells().GetColumns().Get(0).ApplyStyle(style, flag);

    // Protect the worksheet
    sheet.Protect(ProtectionType::All);
    wb.Save(outDir + u"output.out.xls", SaveFormat::Excel97To2003);

    std::cout << "File saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Allow Users to Edit Ranges**

The following example shows how to allow users to edit a range in a protected worksheet.

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

    // Get the Allow Edit Ranges collection
    ProtectedRangeCollection allowRanges = sheet.GetAllowEditRanges();

    // Create the range and get the ProtectedRange object
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

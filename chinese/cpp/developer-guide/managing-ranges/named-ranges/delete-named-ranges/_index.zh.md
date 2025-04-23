---
title: 使用 C++ 删除命名范围
linktitle: 删除命名范围
type: docs
weight: 90
url: /zh/cpp/delete-named-ranges/
description: 学习如何使用 Aspose.Cells for C++ 从 Excel 或 OpenOffice 文件中删除定义的名称或命名范围。
---

## **介绍**
如果 Excel 文件中有太多的定义名称或命名范围，我们必须清除一些，因为它们再也不会被引用。

## **在MS Excel中删除命名区域**

要从Excel中删除命名区域，可以按照以下步骤进行：
1. 打开Microsoft Excel并打开包含命名区域的工作簿。
2. 转到Excel功能区中的“公式”选项卡。
3. 单击“已定义名称”组中的“名称管理器”按钮。这将打开名称管理器对话框。
4. 在名称管理器对话框中，选择要删除的命名区域。
5. 单击“删除”按钮。在提示时确认删除。
6. 单击“关闭”按钮关闭名称管理器对话框。
7. 保存工作簿以保留更改。

## **使用 Aspose.Cells for C++ 删除命名范围**
使用 Aspose.Cells for C++，您可以通过[文本](https://reference.aspose.com/cells/cpp/aspose.cells/namecollection/remove/)或[索引](https://reference.aspose.com/cells/cpp/aspose.cells/namecollection/removeat/)从列表中删除命名范围或定义的名称。

```c++
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
    U16String inputFilePath = srcDir + u"Book1.xlsx";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"Book2.xlsx";

    // Instantiate a new Workbook
    Workbook workbook(inputFilePath);

    // Get all the worksheets in the book
    WorksheetCollection worksheets = workbook.GetWorksheets();

    // Delete a named range by text
    worksheets.GetNames().Remove(u"NamedRange");

    // Delete a defined name by index
    worksheets.GetNames().RemoveAt(0);

    // Save the workbook to retain the changes
    workbook.Save(outputFilePath);

    std::cout << "Named ranges removed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

注意：如果定义的名称被公式引用，则无法删除。我们只能删除定义名称的公式。

## **删除一些已命名范围**
当我们删除已定义名称时，必须检查它是否被文件中的所有公式引用。
为了提高删除命名范围的性能，我们可以同时删除一些。

```c++
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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"Book1.xlsx";

    // Path of output excel file
    U16String outputFilePath = outDir + u"Book2.xlsx";

    // Instantiate a new Workbook
    Workbook workbook(inputFilePath);

    // Get all the worksheets in the book
    WorksheetCollection worksheets = workbook.GetWorksheets();

    // Delete some defined names
    Vector<U16String> namesToRemove = { u"NamedRange1", u"NamedRange2" };
    worksheets.GetNames().Remove(namesToRemove);

    // Save the workbook to retain the changes
    workbook.Save(outputFilePath);

    std::cout << "Named ranges removed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **删除重复的已定义名称**
有些 Excel 文件损坏是因为有些定义的名称重复。因此我们可以删除这些重复的名称以修复文件。

```c++
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
    U16String inputFilePath = srcDir + u"Book1.xlsx";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"Book2.xlsx";

    // Instantiate a new Workbook
    Workbook workbook(inputFilePath);

    // Get all the worksheets in the book
    WorksheetCollection worksheets = workbook.GetWorksheets();

    // Delete some defined names
    worksheets.GetNames().RemoveDuplicateNames();

    // Save the workbook to retain the changes
    workbook.Save(outputFilePath);

    std::cout << "Workbook saved successfully after removing duplicate names!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

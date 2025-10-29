--- 
title: 使用C++复制Excel中的范围 
linktitle: 复制范围 
type: docs 
weight: 105 
url: /zh/cpp/copy-ranges-of-excel/ 
description: 学习如何使用Aspose.Cells与C++复制Excel中的范围。 
--- 

## **介绍**

在Excel中，您可以选择一个范围，复制该范围，然后以特定选项粘贴到同一工作表、其他工作表或其他文件。

## **使用Aspose.Cells复制范围**

Aspose.Cells提供一些重载的[Range.Copy](https://reference.aspose.com/cells/cpp/aspose.cells/range/copy/)方法来复制范围，[Range.CopyStyle](https://reference.aspose.com/cells/cpp/aspose.cells/range/copystyle/)只复制范围的样式，[Range.CopyData](https://reference.aspose.com/cells/cpp/aspose.cells/range/copydata/)只复制范围的值。

## **复制范围**

创建两个范围：源范围、目标范围，然后使用Range.Copy方法将源范围复制到目标范围。

查看以下代码：

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Instantiate a new Workbook.
    Workbook workbook;

    // Get all the worksheets in the book.
    WorksheetCollection worksheets = workbook.GetWorksheets();

    // Get the first worksheet in the worksheets collection.
    Worksheet worksheet = worksheets.Get(0);

    // Create a range of cells.
    Range sourceRange = worksheet.GetCells().CreateRange(u"A1", u"A2");

    // Input some data with some formattings into
    // A few cells in the range.
    sourceRange.Get(0, 0).PutValue(u"Test");
    sourceRange.Get(1, 0).PutValue(u"123");

    // Create target range of cells.
    Range targetRange = worksheet.GetCells().CreateRange(u"B1", u"B2");

    // Copy source range to target range in the same worksheet 
    targetRange.Copy(sourceRange);

    // Create a new worksheet.
    worksheets.Add();
    worksheet = worksheets.Get(1);

    targetRange = worksheet.GetCells().CreateRange(u"A1", u"A2");
    // Copy source range to target range in another worksheet 
    targetRange.Copy(sourceRange);

    // Copy to another workbook
    Workbook anotherWorkbook;

    worksheet = workbook.GetWorksheets().Get(0);

    targetRange = worksheet.GetCells().CreateRange(u"A1", u"A2");
    // Copy source range to target range in another workbook 
    targetRange.Copy(sourceRange);

    std::cout << "Copy operations completed successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **使用选项粘贴范围**

Aspose.Cells支持使用特定类型粘贴范围。

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Instantiate a new Workbook.
    Workbook workbook;

    // Get all the worksheets in the book.
    WorksheetCollection worksheets = workbook.GetWorksheets();

    // Get the first worksheet in the worksheets collection.
    Worksheet worksheet = worksheets.Get(0);

    // Create a range of cells.
    Range sourceRange = worksheet.GetCells().CreateRange(u"A1", u"A2");

    // Input some data with some formattings into A few cells in the range.
    sourceRange.Get(0, 0).PutValue(u"Test");
    sourceRange.Get(1, 0).PutValue(u"123");

    // Create target range of cells.
    Range targetRange = worksheet.GetCells().CreateRange(u"B1", u"B2");

    // Init paste options.
    PasteOptions options;
    // Set paste type.
    options.SetPasteType(PasteType::ValuesAndFormats);
    options.SetSkipBlanks(true);

    // Copy source range to target range
    targetRange.Copy(sourceRange, options);

    std::cout << "Data copied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **仅复制数据的范围**
还可以使用Range.CopyData方法来复制数据，示例如下：

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Instantiate a new Workbook.
    Workbook workbook;

    // Get all the worksheets in the book.
    WorksheetCollection worksheets = workbook.GetWorksheets();

    // Get the first worksheet in the worksheets collection.
    Worksheet worksheet = worksheets.Get(0);

    // Create a range of cells.
    Range sourceRange = worksheet.GetCells().CreateRange(u"A1", u"A2");

    // Input some data with some formatting into
    // A few cells in the range.
    sourceRange.Get(0, 0).SetValue(u"Test");
    sourceRange.Get(1, 0).SetValue(123);

    // Create target range of cells.
    Range targetRange = worksheet.GetCells().CreateRange(u"B1", u"B2");

    // Copy the data of source range to target range
    targetRange.CopyData(sourceRange);

    std::cout << "Data copied successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **高级主题**
- [将源范围的行高复制到目标范围](/cells/zh/cpp/copy-row-heights-of-source-range-to-destination-range/)
{{< app/cells/assistant language="cpp" >}}

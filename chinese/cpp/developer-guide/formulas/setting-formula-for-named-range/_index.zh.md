---
title: 用 C++ 为命名范围设置公式
linktitle: 设置命名范围公式
type: docs
weight: 20
url: /zh/cpp/setting-formula-for-named-range/
description: 学习如何用 Aspose.Cells 在 Excel 文件中为命名范围设置公式，使用 C++。
---

## **为命名范围设置公式**
像 Excel 应用程序一样，Aspose.Cells API 提供在使用 [GetRefersTo()](https://reference.aspose.com/cells/cpp/aspose.cells/range/getrefersto/) 属性时为命名范围指定公式的能力。此功能在多种场景中都很有用，以下列出一些示例。

### **为命名范围设置简单公式**
简单公式可能是对同一（或不同）工作表中另一个单元格的引用。下面的示例创建一个新电子表格中的命名范围，并将其引用设置为另一个单元格。

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

    // Create an instance of Workbook
    Workbook book;

    // Get the WorksheetCollection
    WorksheetCollection worksheets = book.GetWorksheets();

    // Add a new Named Range with name "NewNamedRange"
    int index = worksheets.GetNames().Add(u"NewNamedRange");

    // Access the newly created Named Range
    Name name = worksheets.GetNames().Get(index);

    // Set RefersTo property of the Named Range to a formula. Formula references another cell in the same worksheet
    name.SetRefersTo(u"=Sheet1!$A$3");

    // Set the formula in the cell A1 to the newly created Named Range
    worksheets.Get(0).GetCells().Get(u"A1").SetFormula(u"NewNamedRange");

    // Insert the value in cell A3 which is being referenced in the Named Range
    worksheets.Get(0).GetCells().Get(u"A3").PutValue(u"This is the value of A3");

    // Calculate formulas
    book.CalculateFormula();

    // Save the result in XLSX format
    book.Save(outDir + u"output_out.xlsx");

    std::cout << "Named range created and formula calculated successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **为命名范围设置复杂公式**
复杂公式可以是任何内容，例如动态范围或跨不同工作表多个单元格的公式。下面的示例使用INDEX函数创建一个动态范围，根据其位置从列表中获取值。

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

    // Create an instance of Workbook
    Workbook book;

    // Get the WorksheetCollection
    WorksheetCollection worksheets = book.GetWorksheets();

    // Add a new Named Range with name "data"
    int index = worksheets.GetNames().Add(u"data");

    // Access the newly created Named Range from the collection
    Name data = worksheets.GetNames().Get(index);

    // Set RefersTo property of the Named Range to a cell range in same worksheet
    data.SetRefersTo(u"=Sheet1!$A$1:$A$10");

    // Add another Named Range with name "range"
    index = worksheets.GetNames().Add(u"range");

    // Access the newly created Named Range from the collection
    Name range = worksheets.GetNames().Get(index);

    // Set RefersTo property to a formula using the Named Range data
    range.SetRefersTo(u"=INDEX(data,Sheet1!$A$1,1):INDEX(data,Sheet1!$A$1,9)");

    // Save the workbook
    book.Save(outDir + u"output_out.xlsx");

    std::cout << "Named ranges created and workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

这是另一个示例，使用命名范围对不同工作表中的2个单元格的值进行求和。

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

    // Create an instance of Workbook
    Workbook book;

    // Get the WorksheetCollection
    WorksheetCollection worksheets = book.GetWorksheets();

    // Insert some data in cell A1 of Sheet1
    worksheets.Get(u"Sheet1").GetCells().Get(u"A1").PutValue(10);

    // Add a new Worksheet and insert a value to cell A1
    worksheets.Get(worksheets.Add()).GetCells().Get(u"A1").PutValue(10);

    // Add a new Named Range with name "range"
    int index = worksheets.GetNames().Add(u"range");

    // Access the newly created Named Range from the collection
    Name range = worksheets.GetNames().Get(index);

    // Set RefersTo property of the Named Range to a SUM function
    range.SetRefersTo(u"=SUM(Sheet1!$A$1,Sheet2!$A$1)");

    // Insert the Named Range as formula to 3rd worksheet
    worksheets.Get(worksheets.Add()).GetCells().Get(u"A1").SetFormula(u"range");

    // Calculate formulas
    book.CalculateFormula();

    // Save the result in XLSX format
    book.Save(outDir + u"output_out.xlsx");

    std::cout << "Output file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

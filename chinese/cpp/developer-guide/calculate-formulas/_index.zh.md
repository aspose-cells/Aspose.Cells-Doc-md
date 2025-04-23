---
title: 使用C++计算公式
linktitle: 计算公式
description: 本文介绍如何使用Aspose.Cells库结合C++计算Microsoft Excel中的公式。通过加载现有Excel文件或创建新Excel文件，我们可以使用Aspose.Cells提供的方法来计算公式并获取结果。最后，我们将修改后的Excel文件保存到磁盘。
keywords: Aspose.Cells、Excel、公式、计算、公式的直接计算、重复计算公式、添加公式。
type: docs
weight: 125
url: /zh/cpp/calculate-formulas/
---

## **添加公式及计算结果**

Aspose.Cells 有内嵌的公式计算引擎。它不仅可以重新计算导入设计模板中的公式，还支持计算在运行时添加的公式的结果。

Aspose.Cells支持大部分Microsoft Excel中的公式或函数（请参阅[支持的公式函数列表](/cells/zh/cpp/supported-formula-functions/)）。这些函数可以通过API或设计器电子表格使用。Aspose.Cells支持大量数学、字符串、布尔值、日期/时间、统计、数据库、查找和引用类的公式。

使用 [**GetFormula**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getformula/) 属性或 [**SetFormula(...)**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/setformula/) 方法将公式添加到单元格中。应用公式时，字符串前始终以等号（=）开始，就像在Microsoft Excel中创建公式一样，用逗号（,）分隔函数参数。

为了计算公式的结果，用户可以调用[**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)类的[**CalculateFormula**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/calculateformula/)方法，该方法处理Excel文件中所有嵌入的公式。或者，用户也可以调用[**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)类的[**CalculateFormula**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/calculateformula/)方法，处理工作表中所有嵌入的公式。或者，用户还可以调用[**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/)类的[**Calculate**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/calculate/)方法，处理单个单元格的公式。

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

    // Create a new workbook
    Workbook workbook;

    // Add a new worksheet to the workbook
    int sheetIndex = workbook.GetWorksheets().Add();

    // Get the reference of the newly added worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(sheetIndex);

    // Add values to cells
    worksheet.GetCells().Get(u"A1").PutValue(1);
    worksheet.GetCells().Get(u"A2").PutValue(2);
    worksheet.GetCells().Get(u"A3").PutValue(3);

    // Add a SUM formula to cell A4
    worksheet.GetCells().Get(u"A4").SetFormula(u"=SUM(A1:A3)");

    // Calculate the results of formulas
    workbook.CalculateFormula();

    // Get the calculated value of cell A4
    U16String value = worksheet.GetCells().Get(u"A4").GetStringValue();

    // Save the Excel file
    workbook.Save(outDir + u"output.xls");

    std::cout << "Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **公式重复计算的重要信息**

{{% alert color="primary" %}}

[**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/)类的**GetFormula**属性和**SetFormula(...)**方法的工作方式不同于[**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/)、[**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)和[**Cell**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/)类的**Calculate**方法。**GetFormula**属性和**SetFormula(...)**方法仅将公式添加到单元格，但不会在运行时计算结果。要获取公式的结果，请调用**Calculate**方法。

{{% /alert %}}

## **直接计算公式**

Aspose.Cells内置了一个公式计算引擎。除了计算从设计文件导入的公式外，Aspose.Cells还可以直接计算公式的结果。

有时，您需要在不将其添加到工作表的情况下直接计算公式结果。已在工作表中的单元格值已经存在，您只需根据某个Microsoft Excel公式计算这些值的结果，无需在工作表中添加公式。

您可以使用 Aspose.Cells 的公式计算引擎API [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) 来 [**calculate**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/calculateformula/) 这些公式的结果，而不必将它们添加到工作表中：

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

    // Create a workbook
    Workbook workbook;

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Put 20 in cell A1
    Cell cellA1 = worksheet.GetCells().Get(u"A1");
    cellA1.PutValue(20);

    // Put 30 in cell A2
    Cell cellA2 = worksheet.GetCells().Get(u"A2");
    cellA2.PutValue(30);

    // Calculate the Sum of A1 and A2
    Aspose::Cells::Object results = worksheet.CalculateFormula(u"=Sum(A1:A2)");

    // Print the output
    std::cout << "Value of A1: " << cellA1.GetStringValue().ToUtf8() << std::endl;
    std::cout << "Value of A2: " << cellA2.GetStringValue().ToUtf8() << std::endl;
    std::cout << "Result of Sum(A1:A2): " << results.ToString().ToUtf8() << std::endl;

    Aspose::Cells::Cleanup();
}
```

以上代码生成以下输出：
{{< highlight cpp >}}
Value of A1: 20
Value of A2: 30
Result of Sum(A1:A2): 50.0
{{< /highlight >}}

## **如何重复计算公式**

当工作簿中有大量公式，且用户需要多次计算它们，仅修改少部分内容时，启用公式计算链会有助于性能提升：[**FormulaSettings.GetEnableCalculationChain()**](https://reference.aspose.com/cells/cpp/aspose.cells/formulasettings/getenablecalculationchain/)。

```c++
#include <iostream>
#include <chrono>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Load the template workbook
    Workbook workbook(srcDir + u"book1.xls");

    // Print the time before formula calculation
    auto start = std::chrono::system_clock::now();
    std::time_t start_time = std::chrono::system_clock::to_time_t(start);
    std::cout << "Start time: " << std::ctime(&start_time);

    // Set the CreateCalcChain as true
    workbook.GetSettings().GetFormulaSettings().SetEnableCalculationChain(true);

    // Calculate the workbook formulas
    workbook.CalculateFormula();

    // Print the time after formula calculation
    auto end = std::chrono::system_clock::now();
    std::time_t end_time = std::chrono::system_clock::to_time_t(end);
    std::cout << "End time: " << std::ctime(&end_time);

    // Change the value of one cell
    workbook.GetWorksheets().Get(0).GetCells().Get(u"A1").PutValue(u"newvalue");

    // Re-calculate those formulas which depend on cell A1
    workbook.CalculateFormula();

    Aspose::Cells::Cleanup();
    return 0;
}
```

### **重要知识**

{{% alert color="primary" %}}

默认情况下，计算链是禁用的。因为创建计算链也需要额外时间，首次计算公式（[**Workbook.CalculateFormula(...)**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/calculateformula/)）可能会比不创建链的公式计算消耗更多的CPU处理时间和内存。如果用户不需要频繁计算公式，默认行为（直接计算公式，不创建计算链）可能是更好的选择。

{{% /alert %}}

## **高级主题**
- [将单元格添加到Microsoft Excel公式监视窗口](/cells/zh/cpp/add-cells-to-microsoft-excel-formula-watch-window/)
- [使用Aspose.Cells计算IFNA函数](/cells/zh/cpp/calculating-ifna-function-using-aspose-cells/)
- [计算数据表的数组公式](/cells/zh/cpp/calculation-of-array-formula-of-data-tables/)
- [计算Excel 2016的MINIFS和MAXIFS函数](/cells/zh/cpp/calculation-of-excel-2016-minifs-and-maxifs-functions/)
- [减少Cell.Calculate方法的计算时间](/cells/zh/cpp/decrease-the-calculation-time-of-cell-calculate-method/)
- [在不将其写入工作表的情况下直接计算自定义函数](/cells/zh/cpp/direct-calculation-of-custom-function-without-writing-it-in-a-worksheet/)
- [实现自定义计算引擎以扩展Aspose.Cells的默认计算引擎](/cells/zh/cpp/implement-custom-calculation-engine-to-extend-the-default-calculation-engine-of-aspose-cells/)
- [使用AbstractCalculationEngine返回一系列值](/cells/zh/cpp/returning-a-range-of-values-using-abstractcalculationengine/)
- [设置工作簿的公式计算模式](/cells/zh/cpp/setting-formula-calculation-mode-of-workbook/)
- [在 Aspose.Cells 中使用 FormulaText 函数](/cells/zh/cpp/using-formulatext-function-in-aspose-cells/)

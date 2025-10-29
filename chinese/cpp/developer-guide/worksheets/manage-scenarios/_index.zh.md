---
title: 使用C++创建、处理或删除工作表中的场景
linktitle: 管理场景
type: docs
weight: 190
url: /zh/cpp/create-manipulate-or-remove-scenarios-from-worksheets/
description: 在本文中，你将学习如何使用C++和Aspose.Cells API在Excel工作表中程序化创建、操作或删除场景。
keywords: 使用C++创建场景、删除场景、操作场景
---

{{% alert color="primary" %}}

有时，您需要在电子表格中创建、操作或删除方案。方案是一个命名的“假设”模型，其中包含由一个或多个公式链接的可变输入单元格。在创建方案之前，设计工作表，使其至少包含一个依赖于可以插入不同值的单元格的公式。以下示例演示了如何通过Aspose.Cells API在工作簿中的工作表中创建和删除方案。

{{% /alert %}}

 Aspose.Cells提供一些有用的类，例如[**ScenarioCollection**](https://reference.aspose.com/cells/cpp/aspose.cells/scenariocollection/)、[**Scenario**](https://reference.aspose.com/cells/cpp/aspose.cells/scenario/)、[**ScenarioInputCellCollection**](https://reference.aspose.com/cells/cpp/aspose.cells/scenarioinputcellcollection/)和[**ScenarioInputCell**](https://reference.aspose.com/cells/cpp/aspose.cells/scenarioinputcell/)类。还提供[**Worksheet.GetScenarios()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getscenarios/)属性。下面的示例代码打开一个包含一些场景的Excel文件（XLSX格式），删除一个现有的场景，并在保存前向工作表中添加一个新场景。示例使用非常简单的模板文件。

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source and output directories
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Load input Excel file
    Workbook workbook(srcDir + u"aspose-sample.xlsx");

    // Access first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access scenarios collection
    ScenarioCollection scenarios = worksheet.GetScenarios();
    if (scenarios.GetCount() > 0)
    {
        // Create new scenario and configure
        int32_t scenarioIndex = scenarios.Add(u"MyScenario");
        Scenario scenario = scenarios.Get(scenarioIndex);
        scenario.SetComment(u"Test scenario is created.");

        // Add input cell to scenario
        ScenarioInputCellCollection inputCells = scenario.GetInputCells();
        inputCells.Add(3, 1, u"1100000"); // Cell B4 (0-based)

        // Save modified workbook
        U16String outputPath = outDir + u"outBk_scenarios1.out.xlsx";
        workbook.Save(outputPath);

        std::cout << "\nProcess completed successfully.\nFile saved at " << outputPath.ToUtf8() << std::endl;
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}

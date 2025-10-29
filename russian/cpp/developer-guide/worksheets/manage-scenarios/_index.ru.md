---
title: Создавать, Манипулировать или Удалять сценарии из листов с помощью C++
linktitle: Управление сценариями
type: docs
weight: 190
url: /ru/cpp/create-manipulate-or-remove-scenarios-from-worksheets/
description: В этой статье вы научитесь создавать, управлять или удалять сценарии из Excel листов программным способом с помощью библиотеки C++ и API Aspose.Cells.
keywords: создать сценарий листа c++, удалить сценарий из листа Excel c++, управлять сценарием листа c++
---

{{% alert color="primary" %}}

Иногда вам может понадобиться создавать, изменять или удалять сценарии в электронных таблицах. Сценарий - это именованная модель «что если?», которая включает в себя переменные ввода, связанные одной или несколькими формулами. Перед созданием сценария разработайте лист книги так, чтобы в нем была по крайней мере одна формула, зависимая от ячеек, в которые можно вводить различные значения. В следующем примере показано, как создавать и удалять сценарии из листа книги в книге с помощью API Aspose.Cells.

{{% /alert %}}

Aspose.Cells предоставляет полезные классы, например, [**ScenarioCollection**](https://reference.aspose.com/cells/cpp/aspose.cells/scenariocollection/), [**Scenario**](https://reference.aspose.com/cells/cpp/aspose.cells/scenario/), [**ScenarioInputCellCollection**](https://reference.aspose.com/cells/cpp/aspose.cells/scenarioinputcellcollection/) и [**ScenarioInputCell**](https://reference.aspose.com/cells/cpp/aspose.cells/scenarioinputcell/). Также есть свойство [**Worksheet.GetScenarios()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getscenarios/). В примере кода ниже открывается файл XLSX, содержащий сценарии, и удаляется существующий сценарий. Также добавляется новый сценарий перед сохранением файла Excel. В качестве шаблона используется очень простой файл, содержащий сценарий.

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

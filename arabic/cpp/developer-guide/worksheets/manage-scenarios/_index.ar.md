---
title: إنشاء، تعديل أو إزالة السيناريوهات من أوراق العمل باستخدام C++
linktitle: إدارة السيناريوهات
type: docs
weight: 190
url: /ar/cpp/create-manipulate-or-remove-scenarios-from-worksheets/
description: في هذه المقالة، ستتعلم كيفية إنشاء، تعديل أو إزالة السيناريوهات من أوراق عمل إكسل برمجيًا باستخدام مكتبة C++ مع واجهة برمجة تطبيقات Aspose.Cells.
keywords: إنشاء سيناريو لورقة عمل C++، إزالة سيناريو لورقة عمل إكسل، تعديل سيناريو لورقة عمل C++
---

{{% alert color="primary" %}}

في بعض الأحيان، قد تحتاج إلى إنشاء، التلاعب أو حذف السيناريوهات في جداول البيانات. السيناريو هو نموذج 'ماذا لو؟' يتضمن خلايا إدخال متغيرة مرتبطة بواحد أو أكثر من الصيغ. قبل إنشاء سيناريو، صمم الورقة العمل بحيث تحتوي على صيغة واحدة على الأقل تعتمد على الخلايا التي يمكن إدراج قيم مختلفة فيها. يظهر المثال التالي كيفية إنشاء وإزالة السيناريوهات من ورقة عمل في مصنف باستخدام واجهات Aspose.Cells.

{{% /alert %}}

توفر Aspose.Cells بعض الفئات المفيدة، على سبيل المثال، الفئات [**ScenarioCollection**](https://reference.aspose.com/cells/cpp/aspose.cells/scenariocollection/)، [**Scenario**](https://reference.aspose.com/cells/cpp/aspose.cells/scenario/)، [**ScenarioInputCellCollection**](https://reference.aspose.com/cells/cpp/aspose.cells/scenarioinputcellcollection/)، و [**ScenarioInputCell**](https://reference.aspose.com/cells/cpp/aspose.cells/scenarioinputcell/). كما تقدم الخاصية [**Worksheet.GetScenarios()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getscenarios/). يفتح كود المثال أدناه ملف إكسل XLSX يحتوي على بعض السيناريوهات ويزيل سيناريو موجود، بالإضافة إلى إضافة سيناريو جديد إلى ورقة العمل قبل حفظ ملف الإكسل. يستخدم المثال ملف قالب بسيط جدًا يحتوي على سيناريو.

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

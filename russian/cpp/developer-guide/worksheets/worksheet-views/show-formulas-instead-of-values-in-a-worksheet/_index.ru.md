---
title: Показать формулы вместо значений в листе с помощью C++
linktitle: Показать формулы вместо значений
type: docs
weight: 20
url: /ru/cpp/show-formulas-instead-of-values-in-a-worksheet/
description: В этой статье приведен пример кода для использования API C++ для программного отображения формул вместо значений в листе Excel или электронной таблице.
---

{{% alert color="primary" %}}

Возможно показать формулы вместо вычисленных значений в Microsoft Excel, используя опцию **Показать формулы** из вкладки **Формулы**. Когда показаны формулы, Microsoft Excel отображает формулы в рабочем листе. То же самое можно сделать с помощью Aspose.Cells.

{{% /alert %}}

Aspose.Cells предоставляет свойство [**Worksheet.GetShowFormulas()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getshowformulas/). Установите его в **true** чтобы установить Microsoft Excel отображать формулы.

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

    // Path of input excel file
    U16String filePath = srcDir + u"source.xlsx";

    // Load the source workbook
    Workbook workbook(filePath);

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Show formulas of the worksheet
    worksheet.SetShowFormulas(true);

    // Save the workbook
    workbook.Save(outDir + u"out.xlsx");

    std::cout << "Formulas shown successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
